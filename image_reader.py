from __future__ import print_function
from google.cloud import vision

image_uri = 'https://thumbs.dreamstime.com/z/shopping-receipt-paper-sales-isolated-white-background-85651861.jpg'

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))
