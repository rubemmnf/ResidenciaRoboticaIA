#! /usr/bin/python3

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist


rospy.init_node('simple_publisher')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

cmd = Twist()

rate = rospy.Rate(1)

count = 0
while not rospy.is_shutdown():

    if count % 2 == 0:
        cmd.linear.x = 1
        cmd.angular.z = 0
    else:
        cmd.linear.x = 0
        cmd.angular.z = 1

    pub.publish(cmd)
    count += 1
    rate.sleep()


# twist.linear.x
# twist.linear.y
# twist.linear.z
# twist.angular.x
# twist.angular.y
# twist.angular.z
