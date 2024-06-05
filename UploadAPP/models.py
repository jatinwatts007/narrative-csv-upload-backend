import uuid

from django.db import models


# Create your models here.

class CSVMetaData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file_name = models.CharField(max_length=500)
    file_size = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'upload_csv_meta_data'


class CountryProfile(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=500, null=True, default=None)
    country_code = models.CharField(max_length=10, null=True, default=None)

    class Meta:
        db_table = 'country_profile'


class StateProfile(models.Model):
    id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=500, null=True, blank=False)
    state_code = models.CharField(max_length=10, null=True, default=None)
    country_id = models.ForeignKey(CountryProfile, on_delete=models.CASCADE, db_column='country_id', to_field='id',
                                   default=None, null=True)

    class Meta:
        db_table = 'state_profile_info'


class SubjectProfile(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        db_table = 'subject_profile_info'


class SchoolProfile(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=500, null=False, blank=False)
    school_address = models.CharField(max_length=500, null=True, default=None)

    class Meta:
        db_table = 'school_profile_info'


class StudentProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, null=True)
    subject_id = models.ForeignKey(SubjectProfile, on_delete=models.CASCADE, db_column='subject_id', to_field='id')
    school_id = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, db_column='school_id', to_field='id')
    state_id = models.ForeignKey(StateProfile, on_delete=models.CASCADE, db_column='state_id', to_field='id',
                                 default=None, null=True)
    csv_id = models.ForeignKey(CSVMetaData, on_delete=models.CASCADE, db_column='csv_id', to_field='id',
                               default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_profile_info'
