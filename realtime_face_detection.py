# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 01:11:21 2023

@author: abhij
"""

import cv2
import face_recognition

webcam_video_stream = cv2.VideoCapture(0)
all_face_locations = []

while True:
    ret,current_frame = webcam_video_stream.read()
    current_frame_small = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
    all_face_locations = face_recognition.face_locations(current_frame_small, number_of_times_to_upsample=2 ,model='hog')
    for index, current_face_location in enumerate(all_face_locations):
        top_pos,right_pos,bottom_pos,left_pos = current_face_location
        top_pos = top_pos*4
        right_pos = right_pos*4
        bottom_pos = bottom_pos*4
        left_pos = left_pos*4
        print('found face {} at top{},right{},bottom{},left{}'.format(index+1, top_pos,right_pos,bottom_pos,left_pos) )
        
        cv2.rectangle(current_frame,(left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),2 )
    cv2.imshow("webcam", current_frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    
webcam_video_stream.release()
cv2.destroyAllWindows()

    
        