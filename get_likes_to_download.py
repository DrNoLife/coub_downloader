import requests
import json


# Method used for writing our likes to the dll file.
def write_coubs_to_dll_file(coubs):
    for coub in coubs:
        coub_link = f"https://coub.com/view/{coub['permalink']}"
        (coub_link)

        with open("coubs_to_download.txt", 'a+') as f:
            f.write(coub_link+"\n")

# Get the header from text file.
def get_header_information():

    # Open text file.
    with open('my_liked_coubs_input.txt', 'r+') as f:
        header_content = f.read()

    # Make sure we remove any extra stuff.
    header_content = header_content.strip()

    return header_content

# Methods used for actually calling the API. Does stuff recursively.
def make_request_to_api(apiUrl, curr_page = 1, max_page = 1):
    try:
        # Try to read the local file that should contain cookie information that will be added to the header.
        try:
            header_content = get_header_information()
            token = f"remember_token={header_content}"
        except Exception as ex:
            print(str(ex))
            exit()

        # Make API call and get the json from the response.
        json_response = requests.get(f"{apiUrl}&page={curr_page}", headers={'Cookie':token}).text
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
    like_links_to_use = [
        'https://coub.com/api/v2/timeline/likes?all=true&order_by=likes_count',
        'https://coub.com/api/v2/timeline/likes?all=true&order_by=likes_count',
        'https://coub.com/api/v2/timeline/likes?all=true&order_by=date'
    ]

    # Loop through all links, and make API request.
    for link in like_links_to_use:
        print(f"Contacting API using link: {link}")

        make_request_to_api(apiUrl = link)

# Start the program.
loop_through_like_links()