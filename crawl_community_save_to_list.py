import requests
import json

# Get the community from the user.
def get_community_from_file():
    try:
        with open("community_to_crawl.txt", 'r') as f:
            data = f.read()
            data = data.split('/')[2]

            return data
    except:
        print("Error: community_to_crawl.txt not found.\nPlease create that file, and place a link to the community you want to crawl.")
        try:
            with open("community_to_crawl.txt", 'a') as f:
                f.write("coub.com/community/cars")
                #f.write("order:views_count")
        except:
            print("Tried creating file for you: Failed. Sorry.")

# Method used for writing our likes to the dll file.
def write_coubs_to_dll_file(coubs):
    for coub in coubs:
        coub_link = f"https://coub.com/view/{coub['permalink']}"
        (coub_link)

        with open("coubs_to_download.txt", 'a+') as f:
            f.write(coub_link+"\n")

# Methods used for actually calling the API. Does stuff recursively.
def make_request_to_api(apiUrl, curr_page = 1, max_page = 1):
    try:
        # Make API call and get the json from the response.
        json_response = requests.get(f"{apiUrl}&page={curr_page}").text
        json_overview = json.loads(json_response)
    except Exception as e:
        print(str(e))
        exit()

    # Update the max_page, so we resursively do stuff the correct amount of times.
    if max_page < json_overview['total_pages']:
        max_page = json_overview['total_pages']

    print(f"Page: {curr_page} / {max_page}")
    write_coubs_to_dll_file(json_overview['coubs'])

    # Check if we need to resursively do stuff.
    if curr_page <= max_page:
        curr_page += 1
        make_request_to_api(apiUrl, curr_page, max_page)

# The main functionality
def loop_through_like_links():
    print("Getting your likes.")

    community_from_user = get_community_from_file()

    api_links_to_use = [
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/fresh?getall=true&order_by=views_count',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/fresh?getall=true&order_by=likes_count',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/fresh?getall=true',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/rising?getall=true',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/monthly?getall=true',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/quarter?getall=true',
        f'http://coub.com/api/v2/timeline/community/{community_from_user}/half?getall=true'
    ]

    # Loop through all links, and make API request.
    for link in api_links_to_use:
        print(f"Contacting API using link: {link}")

        make_request_to_api(apiUrl = link)

# Start the program.
loop_through_like_links()