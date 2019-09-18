from django.contrib import admin
from opt_out.public_api.api.models import Submission

from opt_out.public_api.api.models import SubmissionDetails

admin.site.register(Submission)
admin.site.register(SubmissionDetails)
