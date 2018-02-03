import argparse
import base64
import httplib2
import os
import time
import picamera

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# The url template to retrieve the discovery document for trusted testers.
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

def main(photo_file):
    
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials,
                              discoveryServiceUrl=DISCOVERY_URL)

#Take a picture save it to disk and store it as photo_file variable

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.vflip = True
	camera.start_preview()
	time.sleep(2)
	camera.capture('1.jpg')

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        response = service_request.execute()
        label = response['responses'][0]['labelAnnotations'][0]['description']
        print('Found label: %s for %s' % (label, photo_file))
	os.system('espeak -ven+m2 -a 300 -s 130 "{0}"'.format("That is a " + str(label)))
        return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
