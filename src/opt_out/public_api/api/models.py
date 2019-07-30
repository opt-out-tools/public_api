from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.forms.models import ModelForm

from src.opt_out.public_api.api.enums import Identify


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    urls = ArrayField(models.CharField(max_length=256))
    self_submission = models.BooleanField()
    is_part_of_larger_attack = models.BooleanField()

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ["urls", "self_submission", "is_part_of_larger_attack"]

    def clean_urls(self):
        clean_url = self.cleaned_data["urls"]
        if type(clean_url) != list:
            raise ValidationError("urls must be list")

        url_validator = URLValidator()
        for url in clean_url:
            url_validator(url)

class FurtherDetails(models.Model):
    identify = models.CharField(max_length=40, choices=[(tag, tag.value) for tag in Identify])

class FurtherDetailsForm(ModelForm):
    class Meta:
        model = FurtherDetails
        fields = ["identify"]

    def clean_identify(self):
        clean_identify = self.cleaned_data["identify"]
        if type(clean_identify) != str:
            raise ValidationError("identify must be string")

        if clean_identify is None:
            raise ValidationError("identify cannot be empty")
