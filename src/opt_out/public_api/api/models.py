from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models
from django.forms.models import ModelForm
from opt_out.public_api.api.enums import InteractionType, ReactionType, PerpetratorType


class Submission(models.Model):
    urls = ArrayField(models.CharField(max_length=256))
    self_submission = models.BooleanField()
    is_part_of_larger_attack = models.BooleanField()


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ["urls", "self_submission", "is_part_of_larger_attack"]

    def clean_urls(self):
        clean_url = self.data["urls"]
        if type(clean_url) != list:
            raise ValidationError("urls must be list")

        url_validator = URLValidator()
        for url in clean_url:
            url_validator(url)

        return clean_url

    def clean_self_submission(self):
        if "self_submission" not in self.data:
            raise ValidationError("missing self submission flag")

        clean_self_submission = self.data["self_submission"]
        if type(clean_self_submission) != bool:
            raise ValidationError("self submission flag must be a boolean value")

        return clean_self_submission

    def clean_is_part_of_larger_attack(self):
        if "is_part_of_larger_attack" not in self.data:
            raise ValidationError("missing is part of larger attack flag")

        clean_is_part_of_larger_attack = self.data["is_part_of_larger_attack"]
        if type(clean_is_part_of_larger_attack) != bool:
            raise ValidationError("is part of larger attack flag must be a boolean value")

        return clean_is_part_of_larger_attack


class SubmissionDetails(models.Model):
    identify = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    job = models.CharField(max_length=160)
    perpetrator = models.CharField(max_length=40, choices=[(tag.value, tag) for tag in PerpetratorType])
    interaction = models.CharField(max_length=40, choices=[(tag.value, tag) for tag in InteractionType])
    reaction_type = models.CharField(max_length=40, choices=[(tag.value, tag) for tag in ReactionType])
    experienced = ArrayField(models.CharField(max_length=300))
    feeling = models.CharField(max_length=300)

    submission = models.ForeignKey(Submission, on_delete=models.PROTECT)


class SubmissionDetailsForm(ModelForm):
    class Meta:
        model = SubmissionDetails
        fields = '__all__'

    def clean_identify(self):
        clean_identify = self.cleaned_data["identify"]

        if type(clean_identify) != str:
            raise ValidationError("identify must be string")

        if clean_identify is None:
            raise ValidationError("identify cannot be empty")

        return clean_identify


class Predictions(models.Model):
    texts = ArrayField(models.CharField(max_length=400))


class PredictionForm(ModelForm):
    class Meta:
        model = Predictions
        fields = '__all__'
