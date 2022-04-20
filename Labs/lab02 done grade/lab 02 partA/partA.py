
import cv2 

import time 
import sys
import imutils 
from PIL import Image 

import os 


import tweepy


tokens = [] 
with open('Donglinkey.txt', 'r') as f:
  for line in f:
    tokens.append(line.strip()) 

consumer_key = tokens[0] 
consumer_secret = tokens[1] 
access_token = tokens[2] 
access_token_secret = tokens[3] 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


cam_port = 2 
video = cv2.VideoCapture(5) 

if (video.isOpened() == False):
  print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)


result = cv2.VideoWriter('vid/output.avi',
                         cv2.VideoWriter_fourcc('M','J','P','G'),
                         10, size)

while(video.isOpened()):
  res, frame = video.read()
  if res == True:
    result.write(frame)
    cv2.imshow('Frame', frame)
    cv2.imwrite('img/Frame.png', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      statusMessage = "Hi I am an image!"
      api.update_status_with_media(statusMessage,"img/Frame.png") 
      break
  else:
      break

video.release()
result.release()

cv2.destroyAllWindows()
print("yay")
text = 'yay'
print(".. ", text) 