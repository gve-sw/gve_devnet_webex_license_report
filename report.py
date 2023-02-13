"""
Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import json
import os
import pprint
from webex import AdminWebexRestAPI 
from dotenv import load_dotenv
load_dotenv()


def get_license_ids_for_name_list(LICENSE_NAME_LIST):
    
    org_licenses = webex_api.get_orga_licenses_list()
    
    licenses_ids = []
    
    for license_name in LICENSE_NAME_LIST:

        license_info = filter_license_details_by_name(org_licenses, license_name)
        license_id = license_info['id']
        licenses_ids.append(license_id)
        
        print(f"License Name: {license_name} - ID: {license_id}")

    return licenses_ids


def filter_license_details_by_name(org_licenses, license_name):

    for license in org_licenses['items']:
        if license['name'] == license_name:
            return license
        
    print(f"No associated license details for {license_name} found")


def get_people_with_license_ids(license_ids):
    
    org_people = webex_api.get_your_org_people()

    people_with_license_ids = []

    for person in org_people['items']:
        
        associated_person_licenses =  person['licenses']
        
        if is_id_list_subset_of_person_ids(license_ids, associated_person_licenses):
            people_with_license_ids.append(person)

    return people_with_license_ids


def is_id_list_subset_of_person_ids(filter_ids, overall_ids):

    return set(filter_ids).issubset(set(overall_ids))


if __name__ == "__main__":

    ADMIN_TOKEN = os.environ['ADMIN_TOKEN'] 
    LICENSE_NAME_LIST=json.loads(os.environ['LICENSE_NAME_LIST']) 

    webex_api = AdminWebexRestAPI(ADMIN_TOKEN)

    licenses_ids = get_license_ids_for_name_list(LICENSE_NAME_LIST)

    people_with_license_ids = get_people_with_license_ids(licenses_ids)

    print("User/s with this/these license/s:")
    for person in people_with_license_ids:
        print(f" * {person['displayName']} {person['emails'][0]}") 
    print(f"{len(people_with_license_ids)} user/s has/have the license/s.")

    #pprint(people_with_license_id)