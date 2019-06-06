from django.db import models
# from conference import Conference

# Create your models here.

PROPOSAL_TYPES = [
    ('talk', 'Talk'),
    ('workshop', 'Workshop')
]


class Proposals(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1500)
    audience = models.CharField(max_length=1500)
    status = models.CharField(max_length=50)
    proposal_type = models.CharField(choices=PROPOSAL_TYPES, max_length=25)
    proposal_section = models.CharField(max_length=1500)
    pre_requisites = models.TextField(max_length=1500)
    current_urls = models.TextField(max_length=1500)
    speaker_info = models.TextField(max_length=1500)
    speaker_links = models.TextField(max_length=1500)
