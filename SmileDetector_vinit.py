#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# FACE CLASSIFIER

# In[2]:


face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector=cv2.CascadeClassifier('haarcascade_smile.xml')


# GRAB WEBCAM FEED

# In[3]:


#Grab web feed

webcam=cv2.VideoCapture(0)

#show Current Frame

while True:
    #Read current frame from wecam video steam
    successful_frame_read,frame=webcam.read()
    
    if not successful_frame_read:
        break
    
    #Change to Grayscale (only 1 channel instead of 4 which makes it run faster)
    frame_grayscale=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect Faces first
    faces=face_detector.detectMultiScale(frame_grayscale)
    #smiles=smile_detector.detectMultiScale(frame_grayscale, scaleFactor=1.7, minNeighbors=20)
    
    #print(faces)
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame, (x,y),(x+w,y+h),(100,200,50),4)
        
        the_face=frame[y:y+h,x:x+w]
        
        face_grayscale=cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        
        smiles=smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
        
        for (x_,y_,w_,h_) in smiles:
            cv2.rectangle(the_face, (x_,y_),(x_+w_,y_+h_),(50,50,255),6)
            
        
        #if len(smiles)>0:
            #cv2.putText(the_face,'smiling',(x,y+h+40),fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,50,50))
            
    
    #Showing the frame detected on webcam 
    cv2.imshow('Smile Detector',frame)
    
    #Display
    cv2.waitKey(1)

#Cleanup    
webcam.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




