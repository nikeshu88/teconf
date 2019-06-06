from django.urls import path
from .views import *

urlpatterns = [
    path('', submit_proposal, name='proposal_types'),
    path('<str:proposal_type>', ProposalView.as_view(), name='proposal_types'),
]
