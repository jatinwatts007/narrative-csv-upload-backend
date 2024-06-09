import logging

from django.db.models import F

from UploadAPP.models import StudentProfile, SubjectProfile, SchoolProfile, CSVMetaData, StateProfile, CountryProfile

logging.basicConfig()
logger = logging.getLogger(__name__)


def get_country_profile_id(country_name, country_code):
    logger.info("Getting country profile")
    try:
        return CountryProfile.objects.get(country_name=country_name.lower(), country_code=country_code.upper())
    except CountryProfile.DoesNotExist:
        logger.info('country profile does not exist so creating a new one')
        return CountryProfile.objects.create(country_name=country_name.lower(), country_code=country_code.upper())


def get_state_profile_id(state_name, state_code, country_name, country_code):
    logger.info("Getting state profile")
    try:
        return StateProfile.objects.get(state_name=state_name.lower(), state_code=state_code.upper())
    except StateProfile.DoesNotExist:
        country_profile_id = get_country_profile_id(country_name, country_code)
        logger.info('state profile does not exist so creating a new one')
        return StateProfile.objects.create(state_name=state_name.lower(), state_code=state_code.upper(),
                                           country_id=country_profile_id)


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


def create_student_profile_row(name=None, subject=None, school=None, state_name=None, state_code=None,
                               country_name=None, country_code=None, csv_instance_id=None):
    logger.info('Creating student profile in database')

    subject_profile_id = get_subject_profile_id(subject_name=subject)
    school_profile_id = get_school_profile_id(school_name=school)
    state_profile_id = get_state_profile_id(state_name=state_name, state_code=state_code,
                                            country_name=country_name, country_code=country_code)
    StudentProfile.objects.create(name=name, subject_id=subject_profile_id, school_id=school_profile_id,
                                  state_id=state_profile_id, csv_id=csv_instance_id)
    logger.info('Student profile created in database')
    return


def get_csv_info_from_database(csv_instance_id):
    return (StudentProfile.objects.filter(csv_id=csv_instance_id.id)
            .annotate(school_name=F('school_id__school_name'), subject_name=F('subject_id__subject_name'),
                      state_name=F('state_id__state_code'), file_name=F('csv_id__file_name'))
            .values('name', 'school_name', 'state_name', 'subject_name', 'file_name').order_by('created_at'))
