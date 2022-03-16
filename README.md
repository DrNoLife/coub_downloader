# coub_downloader
The video sharing website Coub has announced it's closure. So I want a way to save all my liked coubs from the website.

## Extra notes
Right so another update: 

**Community crawler now works** and it supports ordering. It will always sort by "most popular", but the user decides if it's by *views* or *likes*. 

After using the community crawler, the text document "coubs_to_download.txt" should be filled with many, many, hundreds of links.<br/>
If this is the case, then use the program *coub-dll.py*. This will go through that list, and download every single video.


# How to use
VERY VERY VERY EARLY STAGE!
You can see which libraries are being used, by taking a look at the coub-dll.py file.
So install those.

Other than that, do this:
1) Clone the repo.
2) Inside the repo, add 2 folders:
	* temp
	* result
3) Open coub-dll.py up in some sort of editor
4) Go down towards the button and the find line that says "coubs_to_download", and change the values to whatever coub you want to download.
5) Run the program.

This process will be made a lot easier in the future, but for now, it is what it is. As I said, still very early stage.

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

