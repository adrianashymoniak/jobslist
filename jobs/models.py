from django.db import models


class Job(models.Model):
    summary = models.CharField(max_length=150)
    description = models.TextField()
    language = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=4,
                              choices=(('Open', 'open'), ('Closed', 'closed')))
    urgency = models.CharField(max_length=5,
                               choices=(('Hot', 'hot'), ('Usual', 'usual')))
