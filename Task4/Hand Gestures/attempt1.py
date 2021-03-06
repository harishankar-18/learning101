#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np
import cv2
import math

def move(dir):
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist() 
    distance = 2
    speed = 5
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    if dir == 0:
        vel_msg.linear.x = speed
    elif dir == 1:
        vel_msg.linear.y = -1* speed
    elif dir == 2:
        vel_msg.linear.y = speed
    elif dir == 3:
        vel_msg.linear.x = -1* speed
    

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)
    
'''    
def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    # Imports

    distance = 5
    speed = 5

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    # Open Camera
                #all_image = np.hstack((drawing, crop_image))
        ##cv2.imshow('Contours', all_image)

        # Close the camera if 'q' is pressed


    #Checking if the movement is forward or backwards

    if(isForward == 'f'):
        vel_msg.linear.x = abs(speed)
    elif(isForward == 'b'):
        vel_msg.linear.x = -abs(speed)
    elif(isForward == 'r'):
        vel_msg.linear.y = -abs(speed)
    elif(isForward == 'l'):
        vel_msg.linear.y = -abs(speed)
    #Since we are moving just in x-axis

    while(1):
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        vel_msg.linear.x , vel_msg.linear.y  = get_dir()

        while not rospy.is_shutdown():

                    #Loop to move the turtle in an specified distance
            while(current_distance < distance):
                #Publish the velocity
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                t1=rospy.Time.now().to_sec()
                #Calculates distancePoseStamped
                current_distance= speed*(t1-t0)
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
 '''   

if __name__ == '__main__':
    while(True):

        try:
            #Testing our function
            capture = cv2.VideoCapture(0)
            while capture.isOpened():

                # Capture frames from the camera
                ret, frame = capture.read()

                # Get hand data from the rectangle sub window
                cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
                crop_image = frame[100:300, 100:300]
                
                # Apply Gaussian blur
                blur = cv2.GaussianBlur(crop_image, (3, 3), 0)

                # Change color-space from BGR -> HSV
                hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

                # Create a binary image with where white will be skin colors and rest is black
                mask2 = cv2.inRange(hsv, np.array([0, 48, 80]), np.array([20, 255, 255]))

                # Kernel for morphological transformation
                kernel = np.ones((5, 5))

                # Apply morphological transformations to filter out the background noise
                dilation = cv2.dilate(mask2, kernel, iterations=1)
                erosion = cv2.erode(dilation, kernel, iterations=1)

                # Apply Gaussian Blur and Threshold
                filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
                ret, thresh = cv2.threshold(filtered, 127, 255, 0)

                # Show threshold image
                cv2.imshow("Thresholded Hemal", thresh)

                # Find contours
                image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                
                try:
                
                    # Find contour with maximum area
                    contour = max(contours, key=lambda x: cv2.contourArea(x))

                    
                    # Create bounding rectangle around the contour
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

                    # Find convex hull
                    hull = cv2.convexHull(contour)

                    # Draw contour
                    drawing = np.zeros(crop_image.shape, np.uint8)
                    
                    cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
                    cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

                    # Find convexity defects
                    hull = cv2.convexHull(contour, returnPoints=False)
                    defects = cv2.convexityDefects(contour, hull)

                    # Use cosine rule to find angle of the far point from the start and end point i.e. the convex points (the finger
                    # tips) for all defects
                    count_defects = 0

                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(contour[s][0])
                        end = tuple(contour[e][0])
                        far = tuple(contour[f][0])

                        a = math.sqrt((end[0] - start[0]) * 2 + (end[1] - start[1]) * 2)
                        b = math.sqrt((far[0] - start[0]) * 2 + (far[1] - start[1]) * 2)
                        c = math.sqrt((end[0] - far[0]) * 2 + (end[1] - far[1]) * 2)
                        angle = (math.acos((b * 2 + c * 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

                        # if angle > 90 draw a circle at the far point
                        if angle <= 90:
                            count_defects += 1
                            cv2.circle(crop_image, far, 1, [0, 0, 255], -1)

                        cv2.line(crop_image, start, end, [0, 255, 0], 2)

                    # Print number of fingers
                    if count_defects == 0:
                        cv2.putText(frame, "ONE- Forward", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
                    elif count_defects == 1:
                        cv2.putText(frame, "TWO- Right turn", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
                    elif count_defects == 2:
                        cv2.putText(frame, "THREE- Left Turn", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
                    elif count_defects == 3:
                        cv2.putText(frame, "FOUR- Backwards", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
                    else:
                        pass
                    
                    move(count_defects)
                except:
                    pass
                
                # Show required images
                cv2.imshow("Gesture", frame)
                #all_image = np.hstack((drawing, crop_image))
                ##cv2.imshow('Contours', all_image)

                # Close the camera if 'q' is pressed
                if cv2.waitKey(1) == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()
            
        except rospy.ROSInterruptException: pass
