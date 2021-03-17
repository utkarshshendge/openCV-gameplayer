    timer= cv2.getTickCount()
    success,img= cap.read()
    img = cv2.flip(img, 1)
    cv2.line(img,(0,160),(640,160),(0,224,19),2)
    cv2.line(img,(0,320),(640,320),(0,224,19),2)
    cv2.line(img,(290,0),(290,480),(0,224,19),2)
    cv2.line(img,(350,0),(350,480),(0,224,19),2)
    success,bbox= tracker.update(img)
    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"lost",(75,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(7,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    cv2.imshow("video",img)
    
    if cv2.waitKey(1) == 27 :break