#!/usr/bin/env python3
# license removed for brevity

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class Listener:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('coordinates', Twist, self.callback)
        self.pub_linear = rospy.Publisher('Vel_linear', Float64, queue_size=10)
        self.pub_angular = rospy.Publisher('Vel_angular', Float64, queue_size=10)

    def callback(self, msg):
        xL , yL, zL = msg.linear.x, msg.linear.y, msg.linear.z
        result_linear = math.sqrt((xL**2) + (yL**2) + (zL**2))
        speed_linear = Float64()
        speed_linear.data = result_linear
        self.pub_linear.publish(speed_linear)

        xA , yA, zA = msg.angular.x, msg.angular.y, msg.angular.z
        result_angular = math.sqrt((xL**2) + (yL**2) + (zL**2))
        speed_angular = Float64()
        speed_angular.data = result_angular
        self.pub_angular.publish(speed_angular)


if __name__ == '__main__':
    l = Listener()
    rospy.spin()