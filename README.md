https://github.com/mustafaxt2/youtube_video_audio_downloader/assets/112318875/335bcfd3-de98-4b35-811f-f8baf5becef5

If you encounter a problem with regex, go into the C:\Users\yourUsername\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube folder, edit the cipher.py file and replace the line 30, which is:
var_regex = re.compile(r"^\w+\W")
With this line:
var_regex = re.compile(r"^\$*\w+\W")
