import yt_dlp

url = input("Please enter your desired YouTube video URL: ")

yt_dlp.youtubeDL({ "format": "bestvideo + bestaudio/best" }).download([url])