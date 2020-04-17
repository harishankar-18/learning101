#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np
PI = 3.1415926535897

def rotate():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Receiveing the user's input
    radius = input("Imput the radius of the circle:")
    speed = input("Speed:")

    angular_speed = np.radians(speed)

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0


    vel_msg.angular.z = abs(angular_speed)
    vel_msg.linear.x = abs(radius)
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < 2*PI):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*((t1-t0))


    #Forcing our robot to stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass
