from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Issue
from .tasks import assigned_email

@receiver(post_save, sender=Issue)
def post_save_issue(sender, instance, **kwargs):
	if instance.assign_tracker.has_changed('assigned_to'):
		assignee = instance.assigned_to
		ticket_number = instance.id
		ticket_title = instance.title
		message_body = "Ticket '%s - %s' is assigned to you" % (ticket_number, ticket_title)
		recipient = assignee.email
		assigned_email.apply_async((recipient, message_body), countdown=10)
