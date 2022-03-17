# Shitty name lol, but whatever.
# This file is supposed to crawl / scan whatever community is supplied, and get AS MANY coub links as possible, and save these into the coubs_to_download.txt file.
# Then one can run the other program afterwards.

# Endpoints for the coub API
# https://github-wiki-see.page/m/HelpSeeker/CoubDownloader/wiki/Coub-API

import requests
import json

def get_community_from_file():
    try:
        with open("community_to_crawl.txt", 'r') as f:
            data = f.read()
            data = data.split('\n')
            community = data[0]
            ordering = data[1]
            ordering = ordering.split(':')[1]

            return [community, ordering]
    except:
        print("Error: community_to_crawl.txt not found.\nPlease create that file, and place a link to the community you want to crawl.")
        try:
            with open("community_to_crawl.txt", 'a') as f:
                f.write("https://coub.com/community/cars")
                f.write("order:views_count")
        except:
            print("Tried creating file for you: Failed. Sorry.")
        

# Handle the setup.
#community_link = "https://coub.com/community/cars"
from_local_file = get_community_from_file()
community_link = from_local_file[0]
community_order = from_local_file[1]
community_to_crawl = community_link.split('/')[2]
#url = f"https://coub.com/api/v2/timeline/community/{community_to_crawl}/fresh?order_by={community_order}"
url = f"https://coub.com/api/v2/timeline/community/{community_to_crawl}/quarter"


def make_request_to_api(apiurl, current_page = 1, max_page = 1):

    if current_page == 1:
        json_response = requests.get(apiurl).text
    else:
        json_response = requests.get(f"{apiurl}?page={current_page}").text
    
    community_overview = json.loads(json_response)

    if(max_page < community_overview['total_pages']):
        max_page = community_overview['total_pages']

    print(f"Community: {community_to_crawl}\n\tPage {current_page} / {max_page}")
    #print(f"url: {apiurl}?page={current_page}")

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