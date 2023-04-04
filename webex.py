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
import requests
from dotenv import load_dotenv
load_dotenv()

class AdminWebexRestAPI():

    def __init__(self, ADMIN_TOKEN):

        self.BASE_URL="https://webexapis.com/v1"
        self.ADMIN_TOKEN = ADMIN_TOKEN
        self.HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  self.ADMIN_TOKEN
                }


    def get_orga_licenses_list(self):
        """See: https://developer.webex.com/docs/api/v1/licenses/list-licenses"""

        url= f"{self.BASE_URL}/licenses"  
        method="GET"

        response = self.execute_rest_call(method, url, payload={})

        return response

    
    def get_your_org_people(self):
        """See: https://developer.webex.com/docs/api/v1/people/list-people"""
        
        url= f"{self.BASE_URL}/people"
        max=100 #response entries per request 

        people = self.request_data_via_pagination(url, max)
        
        return people


    def execute_rest_call(self, method, url, payload={}):
        """Execute a Rest API call based on the given method, url and payload. Return response json."""

        response = requests.request(method, url, headers=self.HEADERS, data=json.dumps(payload))

        if response.status_code != 200:
            raise Exception(response.json())
        else:
            return response.json()

    
    def request_data_via_pagination(self, REQUEST_URL, MAX):
        '''Retrieve a huge amount of data via API based on pagination
        See also: https://developer.webex.com/docs/basics#pagination'''
    
        complete_response_data = []
    
        initial_url = f'{REQUEST_URL}?max={str(MAX)}'
        payload = None
    
        #Initial request
        print(f'-----Initial request url: {initial_url}')
        response = requests.request("GET", initial_url, headers=self.HEADERS, data=payload)
        
        if 'items' in response.json():
            for entry in response.json()['items']:  
                complete_response_data.append(entry)
        
        #Concurrent requests
        while 'next' in response.links :

            next_link = response.links['next']['url'] 
            print(f'-----Next request for link: {next_link}')

            response = requests.get(next_link, headers=self.HEADERS, data=payload)

            if 'items' in response.json():
                for entry in response.json()['items']:  
                    complete_response_data.append(entry)

        return complete_response_data






