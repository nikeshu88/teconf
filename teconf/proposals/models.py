from django.db import models
from conference import Conference

# Create your models here.


class Proposals(models.Model):

    title = models.CharField(required=True)
    description = models.TextField()
    audience = models.CharField()
    status = models.CharField()
    proposal_type = models.CharField()
    proposal_section = models.CharField()
    pre_requisites = models.TextField()
    current_urls = models.TextField()
    speaker_info = models.TextField()
    speaker_links = models.TextField()
