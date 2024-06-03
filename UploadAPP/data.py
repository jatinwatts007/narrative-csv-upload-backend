import logging

from UploadAPP.models import StudentProfile, SubjectProfile, SchoolProfile, CSVMetaData

logging.basicConfig()
logger = logging.getLogger(__name__)


def create_csv_file_meta_data(file_name, file_size):
    return CSVMetaData.objects.create(file_name=file_name, file_size=file_size)


def get_subject_profile_id(subject_name):
    logger.info("Getting subject profile")
    try:
        return SubjectProfile.objects.get(subject_name=subject_name.lower())
    except SubjectProfile.DoesNotExist:
        logger.info('subject profile does not exist so creating a new one')
        return SubjectProfile.objects.create(subject_name=subject_name.lower())


def get_school_profile_id(school_name):
    logger.info('Getting school profile')
    try:
        return SchoolProfile.objects.get(school_name=school_name.lower())
    except SchoolProfile.DoesNotExist:
        logger.info('school profile does not exist so creating a new')
        return SchoolProfile.objects.create(school_name=school_name.lower())


def create_student_profile_row(name=None, subject=None, school=None, state=None, csv_instance_id=None):
    logger.info('Creating student profile in database')
    subject_profile_id = get_subject_profile_id(subject_name=subject)
    school_profile_id = get_school_profile_id(school_name=school)
    StudentProfile.objects.create(name=name, subject_id=subject_profile_id, school_id=school_profile_id, state=state,
                                  csv_id=csv_instance_id)
    logger.info('Student profile created in database')
    return
