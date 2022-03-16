from __future__ import print_function
import requests
import json
import urllib.request
import subprocess
import os

def download_coub_content(coub_to_dll):
    coub_video = coub_to_dll['file_versions']['html5']['video']['higher']['url']
    coub_audio = coub_to_dll['file_versions']['html5']['audio']['high']['url']

    urllib.request.urlretrieve(coub_video, 'temp/coub_video.mp4')
    urllib.request.urlretrieve(coub_audio, 'temp/coub_audio.mp3')

def handle_coub_folder(path):
    path_exists = os.path.exists(path)
    if not path_exists:
        os.makedirs(path)

def handle_coub_name(name):
    return name.replace('|', ',').replace('/', '').replace('\\', '').replace(':', '').replace("http", '').replace("https", '')

def combine_video_and_audio(coub_id, coub_name, path = "default"):
    if path == "default":
        path = "temp/"

    # Let's test and sanitize some stuff.
    coub_name = handle_coub_name(coub_name)

    # Parameters for the command.
    input_video = path + "coub_video.mp4"
    input_audio = path + "coub_audio.mp3"
    save_path = "result/"
    extension = ".mp4"
    codec = "copy"

    # Equals: Name_Id
    coub_identification = f"\"{coub_name}\"_{coub_id}"

    # Equals: result/Name_Id
    coub_save_name = f"{save_path}{coub_identification}"

    # Checks if folder for this coub exists. Example: results/my coouuubbshere
    handle_coub_folder(f"{save_path}{coub_name}_{coub_id}")

    # Handles the "short" version of the coub. 
    # This gets placed in the main results folder.
    ffmpeg_command_short = f"ffmpeg -i {input_video} -i {input_audio} -shortest -map 0:v:0 -map 1:a:0 -loglevel quiet -c {codec} {coub_save_name}{extension}"

    # Handles the "long" version of the coub.
    # Gets placed inside the coubs own individual folder.
    ffmpeg_command_long = f"ffmpeg -stream_loop -1 -i {input_video} -i {input_audio} -shortest -map 0:v:0 -map 1:a:0 -loglevel quiet -c {codec} {coub_save_name}/{coub_identification}_long{extension}"

    # Output filepath should be something like: "result/Anime girl_2w6l6p.mp4"
    subprocess.run(ffmpeg_command_short)
    subprocess.run(ffmpeg_command_long)

    print(f"{coub_save_name}")

    return f"{save_path}{coub_name}_{coub_id}"

def get_metadata_for_coub(coub, path):

    # get data from coub object.
    title = coub['title']
    created_at = coub['created_at']
    updated_at = coub['updated_at']
    views_count = coub['views_count']
    age_restricted = coub['age_restricted']
    uploader_name = coub['channel']['title']
    uploader_description = coub['channel']['description']
    uploader_followers = coub['channel']['followers_count']
    category = coub['categories'][0]['title']
    community = coub['communities'][0]['title']
    likes_count = coub['likes_count']
    dislikes_count = coub['dislikes_count']
    recoubs_count = coub['recoubs_count']
    tags = ""
    for tag in coub['tags']:
        tags = tags + tag['title'] + ", "
    tags = tags.strip().rstrip(',') 

    # Format data in a "proper" way.
    output = f"title\t{title}"
    output = output + f"\ncreated_at\t{created_at}"
    output = output + f"\nupdated_at\t{updated_at}"
    output = output + f"\nviews_count\t{views_count}"
    output = output + f"\nage_restricted\t{age_restricted}"
    output = output + f"\nuploader_name\t{uploader_name}"
    output = output + f"\nuploader_description\t{uploader_description}"
    output = output + f"\nuploader_followers\t{uploader_followers}"
    output = output + f"\ncategory\t{category}"
    output = output + f"\ncommunity\t{community}"
    output = output + f"\nlikes_count\t{likes_count}"
    output = output + f"\ndislikes_count\t{dislikes_count}"
    output = output + f"\nrecoubs_count\t{recoubs_count}"
    output = output + f"\ntags\t{tags}"

    # Write the output to a file.
    with open(f"{path}/summary.txt", "w+") as outfile:
        outfile.write(output)

    # And just because why not, let's write all the json content to a file as well.
    with open(f"{path}/detailed.json", "w") as outfile:
        json.dump(coub, outfile)


def download_coub(coub):
    download_coub_content(coub)
    path = combine_video_and_audio(coub['permalink'], coub['title'])
    get_metadata_for_coub(coub, path)




# Go through a list of URL's.
coubs_to_download = [
    "https://coub.com/view/2ux3qe"
]


# Get the ID.
for c in coubs_to_download:
    id = c.split('/')[4]

    # Get coub info from API.
    url = "https://coub.com/api/v2/coubs/" + id
    coub_json = requests.get(url).text

    # Download and combine.
    coub = json.loads(coub_json)

    download_coub(coub)