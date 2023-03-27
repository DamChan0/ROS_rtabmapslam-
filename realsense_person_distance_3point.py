#real
import cv2
import imutils
import winsound
import threading
import pyrealsense2 as rs   
import numpy as np
from realsense_depth import*
####################################################################################################################################
################################################ 리얼센스 카메라 출력 + 거리정보 표시 ################################################
####################################################################################################################################
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def wearing():
       winsound.Beep(
           frequency= 360,
           duration= 50
       )   
       
def person_detection(send_distance):  
    cap = cv2.VideoCapture(1)
    while cap.isOpened():
            # Reading the video stream
            ret, aaaa = cap.read()
            if ret:
                aaaa = imutils.resize(aaaa, 
                                    width=min(600, aaaa.shape[1]))
        
                # Detecting all the regions 
                # in the aaaa that has a 
                # pedestrians inside it
                (regions, _) = hog.detectMultiScale(aaaa,
                                                    winStride=(4, 4),
                                                    padding=(8, 8),
                                                    scale=1.05)
        
                # Drawing the regions in the 
                # aaaa
                
                i=0
                for (x, y, w, h) in regions:
                    cv2.rectangle(aaaa, (x, y),
                                (x + w, y + h), 
                                (0, 0, 255), 2)
                    
                    distance = send_distance[i]
                    cv2.putText(aaaa,str(i),(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                    if (i>3 and distance < 1000) : {
                        
                    threading.Timer(0, wearing).start()
                    }
                    
                    i += 1

                ret, depth_fream, color_frame = dc.get_frame()    
                
                # Showing the output aaaa
                cv2.imshow("aaaa", aaaa)
            
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        
            cap.release()
            cv2.destroyAllWindows()
            dc = DepthCamera() 
            while True :
                
                ret, depth_fream, color_frame = dc.get_frame()
                
                point = (x/2 , y/2)      
                cv2.circle( color_frame , point , 4 , (0,0,225))
                distance = depth_fream[point[1], point[0]]
            
                
                cv2.putText(color_frame , "{}mm" .format(distance), (point[0], point[1] - 20) , cv2.FONT_HERSHEY_PLAIN , 1 ,(0,0,0,),2)
                        
                #         # 화면 출력 (사진으로
                #         # 화면 중앙을 지점으로 설정 (x 는 왼쪽부터 y는 위에서 아래로 길이 측정함)
                cv2.imshow("depth frame", depth_fream)
                cv2.imshow("Color frame", color_frame)
                key = cv2.waitKey(1)
                if key == 30:
                        break;  

def distance_show():
    dc = DepthCamera()
    # 화면 중앙을 지점으로 설정 (x 는 왼쪽부터 y는 위에서 아래로 길이 측정함)
    
    
    pointx = [320 , 640 ,960]
    pointy = [300, 300, 300]
    
    
    while True :
            
        ret, depth_fream, color_frame = dc.get_frame()
        
        for a ,b in zip(pointx ,pointy)  :      
            cv2.circle( color_frame , (a,b) , 2 , (0,0,225))
            distance = depth_fream[b, a]
           
        
            cv2.putText(color_frame , "{}mm" .format(distance), (a, b - 20) , cv2.FONT_HERSHEY_PLAIN , 1 ,(0,0,0,),2)
            
                
        #         # 화면 출력 (사진으로
        #         # 화면 중앙을 지점으로 설정 (x 는 왼쪽부터 y는 위에서 아래로 길이 측정함)
        cv2.imshow("depth frame", depth_fream)
        cv2.imshow("Color frame", color_frame)
        key = cv2.waitKey(1)
        if key == 30:
                break;  
        
        
        cap = cv2.VideoCapture(1)
        # Reading the video stream
        ret, aaaa = cap.read()
        if ret:
                aaaa = imutils.resize(aaaa, 
                                width=min(600, aaaa.shape[1]))
        
                # Detecting all the regions 
                # in the aaaa that has a 
                # pedestrians inside it
                (regions, _) = hog.detectMultiScale(aaaa,
                                                winStride=(4, 4),
                                                padding=(4, 4),
                                                scale=1.05)
        
                # Drawing the regions in the 
                # aaaa
                
                i=0
                for (x, y, w, h) in regions:
                        cv2.rectangle(aaaa, (x, y),
                                        (x + w, y + h), 
                                        (0, 0, 255), 2)
                        
                        
                        cv2.putText(aaaa,str(i),(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                        print(distance)
                        
                        if (i>0 and distance < 500) : {         ## i = 인식 개체수 distance 는 거리 mm
                        
                        threading.Timer(0, wearing).start()
                        }
                        
                        i += 1

                
        
                # Showing the output aaaa
                cv2.imshow("aaaa", aaaa)
        
                if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
        else:
                break
        
                
                

           
distance_show()

    
####################################################################################################################################################################################################################################################
    
    
    
    
    
    
    
    