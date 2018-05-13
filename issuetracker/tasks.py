from django.core.mail import send_mail
from issueTrackerREST.celery import app
from .models import Issue
from django.contrib.auth.models import User
from celery.decorators import periodic_task
from datetime import timedelta
from django.conf import settings

@app.task
def assigned_email(recipient, data):
	subject = "New Issue assigned"
	email_to_assignee(recipient, subject, data)

@periodic_task(run_every=settings.REPORT_SCHEDULE)
def despatch_issue_report():
	subject = "Issues assigned"
	users = User.objects.all()
	for user in users:
		issue_report = get_report_by_user(user)
		print issue_report,user.email
		if issue_report:
			recipient = user.email
			print issue_report
			email_to_assignee(recipient, subject, issue_report)

def email_to_assignee(recipient, subject, data):
	sender = 'nithinkvijayan@live.com'
	send_mail(subject, data, sender, [recipient])

def get_report_by_user(user):
	issues = Issue.objects.filter(assigned_to=user)
	issues_detail_list = []

	for issue in issues:
		issue_detail = "Issue Id - %s, Title - %s, Creator - %s, Description - %s, Status - %s" % (
			issue.id,
			issue.title,
			issue.created_by,
			issue.description,
			issue.status
			)
		issues_detail_list.append(issue_detail)
	issue_report = "\n".join(issues_detail_list)
	return issue_report

