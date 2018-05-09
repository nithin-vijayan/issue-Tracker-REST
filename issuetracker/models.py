from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
	TICKET_STATUS = (
		('O', 'OPEN'),
		('C', 'CLOSE'),
		)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	assigned_to = models.ForeignKey(User, related_name='assigned_to')
	created_by = models.ForeignKey(User, related_name='created_by')
	status = models.CharField(max_length=1, choices=TICKET_STATUS)