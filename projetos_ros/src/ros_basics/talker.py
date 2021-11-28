#!/usr/bin/env python3
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist
import random


class Talker:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('coordinates', Twist, queue_size=10)
        self.lst = list(range(10))

    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            coordinates = Twist()

            coordinates.linear.x = random.choice(self.lst)
            coordinates.linear.y = random.choice(self.lst)
            coordinates.linear.z = random.choice(self.lst)

            coordinates.angular.x = random.choice(self.lst)
            coordinates.angular.y = random.choice(self.lst)
            coordinates.angular.z = random.choice(self.lst)

            self.pub.publish(coordinates)
            rate.sleep()

if __name__ == '__main__':
    try:
        t = Talker()
        t.start()
    except rospy.ROSInterruptException:
        pass
