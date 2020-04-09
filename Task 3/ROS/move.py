

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
     # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    direcction = input("Enter direcction: ")  #f, b, r, or l

    if(direction == 'f'):
        vel_msg.linear.x = abs(speed)
    elif(direction == 'b'):
        vel_msg.linear.x = -abs(speed)
    elif(direction == 'r'):
        vel_msg.linear.y = -abs(speed)
    elif(direction == 'l')
        vel_msg.linear.y = abs(speed)
        
        
       vel_msg.linear.z = 0
       vel_msg.angular.x = 0
       vel_msg.angular.y = 0
       vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
