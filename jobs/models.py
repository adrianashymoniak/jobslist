from django.db import models


class Job(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    summary = models.CharField(max_length=150)
    description = models.TextField()
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=4,
                              choices=(('Open', 'Open'), ('Closed', 'closed')))
    urgency = models.CharField(max_length=5,
                               choices=(('Hot', 'hot'), ('Usual', 'usual')))
