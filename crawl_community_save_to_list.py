# Shitty name lol, but whatever.
# This file is supposed to crawl / scan whatever community is supplied, and get AS MANY coub links as possible, and save these into the coubs_to_download.txt file.
# Then one can run the other program afterwards.

import requests
import json
import os

# To request page 2, one does /monthly?page=2


# Make a call.
# Get the data, and find out if there are more pages to go.
# If there are more pages, call the same method, but with changed url.
# Repeat.


# Handle the setup.
community_link = "https://coub.com/community/cars"
community_to_crawl = community_link.split('/')[4]
url = f"https://coub.com/api/v2/timeline/community/{community_to_crawl}/monthly"


def make_request_to_api(apiurl, current_page = 1, max_page = 1):
    json_response = requests.get(apiurl).text
    community_overview = json.loads(json_response)

    if(max_page < community_overview['total_pages']):
        max_page = community_overview['total_pages']

    print(f"Community: {community_to_crawl}\n\tPage {current_page} / {max_page}")

    coubs = community_overview['coubs']
    write_coubs_to_dll_file(coubs)

    if current_page <= max_page:
        current_page += 1
        make_request_to_api(apiurl, current_page, max_page)

def write_coubs_to_dll_file(coubs):
    for coub in coubs:
        coub_link = f"https://coub.com/view/{coub['permalink']}"
        (coub_link)

        with open("coubs_to_download.txt", 'a') as f:
            f.write(coub_link+"\n")

make_request_to_api(url)