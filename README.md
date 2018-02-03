# google-cloud-vision-rapsi
Google cloud vision on raspberry pi

I'm not a developer, this was just trial and error until it worked.
I hope its useful to someone :)

This python file uses:
Raspistill to take a photo from a raspberry pi camera
The file is saved and sent to Google Cloud Vision api
(the google api piece follows this tutorial I think... it was a while ago I made this...
https://console.cloud.google.com/getting-started?project=smile-detector-astropi-smiley
)

The label returned from google cloud vision api is then sent to espeak via a commandline prompt which speaks the phrase of your choice including the returned label as a string.
