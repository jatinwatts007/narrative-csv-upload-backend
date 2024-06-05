import csv
import logging

import googlemaps

from UploadAPP.data import create_student_profile_row, create_csv_file_meta_data

logging.basicConfig()
logger = logging.getLogger(__name__)


def decode_csv_file(csv_file):
    logger.info("Decoding csv file with utf-8-sig")
    decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
    logger.info("Decoded csv file with utf-8-sig")
    return decoded_file


def get_state_country_info_from_geocoding_api(address):
    logger.info("Calling geocoding api to get state and country")
    gmaps = googlemaps.Client(key='AIzaSyCb8mxdCWGQ7jt516EpK2DhpkqJrbXp1XA')
    state_name = None
    state_code = None
    country_name = None
    country_code = None

    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    if geocode_result is None:
        return state_name, state_code, country_name, country_code

    for geocode_details in geocode_result:
        for detail in geocode_details.get('address_components'):
            if detail.get('types')[0] == 'administrative_area_level_1':
                state_name = detail.get('long_name')
                state_code = detail.get('short_name')
            elif detail.get('types')[0] == 'country':
                country_name = detail.get('long_name')
                country_code = detail.get('short_name')
    return state_name, state_code, country_name, country_code



def create_student_info_row_db(subject_list, name, school, state, csv_instance_id):
    logger.info("Creating student info")
    state_name, state_code, country_name, country_code = get_state_country_info_from_geocoding_api(address=state)
    for subject in subject_list:
        create_student_profile_row(subject=subject, name=name, school=school,
                                   csv_instance_id=csv_instance_id, state_name=state_name, state_code=state_code,
                                   country_name=country_name, country_code=country_code)


def upload_file(csv_file):
    if csv_file is None:
        return None
    file_name = csv_file.name
    file_size = csv_file.size
    csv_instance_id = create_csv_file_meta_data(file_name=file_name, file_size=file_size)
    decoded_file = decode_csv_file(csv_file)
    reader = csv.DictReader(decoded_file)
    logger.info("Uploading csv file")
    for row in reader:
        print(row)
        subject_list = []
        name = None
        school = None
        state = None
        if any(map(bool, row.values())):
            for key in row.keys():
                remove_space = key.replace(" ", "").lower()
                if any(x in remove_space for x in ['class', 'subject']):
                    subject = row.get(key)
                    if subject:
                        subject_list.append(subject)
                elif 'name' in remove_space:
                    initial_name = row.get(key)
                    if name is None:
                        name = initial_name
                    else:
                        name += ' ' + initial_name
                elif any(x in remove_space for x in ['school', 'highschool', 'institute', 'collage']):
                    school = row.get(key)
                elif any(x in remove_space for x in ['location', 'place', 'state', 'address']):
                    address = row.get(key)
                    if state is None:
                        state = address
                    else:
                        state += ', ' + address
            create_student_info_row_db(subject_list=subject_list, name=name, school=school, state=state,
                                            csv_instance_id=csv_instance_id)
    logger.info("Uploaded csv file")
