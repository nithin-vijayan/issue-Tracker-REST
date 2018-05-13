from django.db import models
from django.contrib.auth.models import User
from model_utils import FieldTracker


class Issue(models.Model):
	TICKET_STATUS = (
		('open', 'open'),
		('closed', 'closed'),
		)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	assigned_to = models.ForeignKey(User, related_name='assigned_to', to_field='username')
	created_by = models.ForeignKey(User, related_name='created_by', to_field='username')
	status = models.CharField(max_length=6, choices=TICKET_STATUS)

	#For tracking changes in assigned_to field while changing ticket assignee
	assign_tracker = FieldTracker(fields=['assigned_to'])

