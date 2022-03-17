# coub_downloader
The video sharing website Coub has announced it's closure. So I want a way to save all my liked coubs from the website.

Very rough and direct video showing how to use the program: https://www.youtube.com/watch?v=lZyFNhzX4Rg

Further guide on how to download all liked videos: https://www.youtube.com/watch?v=4JP9CT-RUng

**If you have the requirements installed, AND Git, you can use this video as a reference for how to use the program: ** <br />
https://www.youtube.com/watch?v=P5Pu1i0lGKk

## Extra notes

### New new new update.

Right so another update: 

**Community crawler now works** and it supports ordering. It will always sort by "most popular", but the user decides if it's by *views* or *likes*. 

After using the community crawler, the text document "coubs_to_download.txt" should be filled with many, many, hundreds of links.<br/>
If this is the case, then use the program *coub-dll.py*. This will go through that list, and download every single video.

Added progress bar, a better "completed" list and something else I forgot.

# How to use

Make sure you have Python installed.

Make sure you have the libraries required installed (check a bit further down to see which ones are needed).

After than, go ahead and download / clone the repo. <br />
After download, we need to fix a few things, so do the following:

1) Inside the repo, open the file *completed_coubs.txt*.
2) Delete all content within this file. After that, save it and close the file.
3) Create 2 folders inside the repo.
	* result
	* temp

After you've cleaned out the text file and added the two folders, we should be ready.

You can use the *coubs_to_download.txt* file to mention which coubs should be downloaded. <br />
Each line should represent a link to a coub, example: 

```
https://coub.com/view/31159x
https://coub.com/view/30ysj6
https://coub.com/view/3113aa
```

After this, you can save the file and close it. Now run the *coub-dll.py* file by using your Terminal / CMD / Powershell. <br />
The result of this will be saved in the, result folder.

If you want to mass download from communities, do the following:

1) Find the link to the community, example: coub.com/community/anime
2) Open the text file *community_to_crawl.txt* and replace the very first line with your link.
3) The second line can be used to change the ordering (views_count vs likes_count).
4) After this, save the file and close it.
5) Now run the python file *crawl_community_save_to_list.py*

After this is complete, just run the other program again, just like before. This will download all the videos found by the crawler.

## Requirements for the program

You need to have Python installed (I used the latest version). <br />
https://www.python.org/downloads/

The program needs the following libraries:
* ffmpeg
* ffmpeg-python
* requests
* json
* urllib.request
* subprocess
* os
* shutil

If you don't have them installed, use pip to install them:

```
pip install requests
```

### NOTICE REGARDING FFMPEG

You also need to add ffmpeg to your system environment path. If you don't know how to do this, Google for it. It's relatively straight forward.

## community_to_crawl.txt
This text file decides what community we'll look for coubs in. Only 2 lines should exist in this text document, and it should use this syntax:

```txt
https://coub.com/community/anime
order:views_count
```

The *"views_count"* can be exchanged for *"likes_count"*.

# Notes
This website was really good, for showing what API endspoints to use.
https://github-wiki-see.page/m/HelpSeeker/CoubDownloader/wiki/Coub-API

I realize the documentation is a bit wack right now, but honestly, it's a rushed job this project, and it works fine for me. <br />
I don't have the time to make it more user friendly, I'm sorry, but school is quite needy.

