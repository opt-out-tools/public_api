from django.contrib import admin
from opt_out.public_api.api.models import Submission

from opt_out.public_api.api.models import FurtherDetails

admin.site.register(Submission)
admin.site.register(FurtherDetails)

