#!/usr/bin/env python3

import rospy
import tf2_ros
import random
from geometry_msgs.msg import TransformStamped
import math


class RandomTranform():
    def __init__(self, planet):
        rospy.init_node('random_transform', anonymous=True)

        self.tf = TransformStamped()
        self.tf.header.frame_id = 'centro_do_mundo'
        self.tf.child_frame_id = planet[0]
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.rotation.w = 1
        self.raio = planet[1]
        self.vel = planet[2]

        self.broadcaster = tf2_ros.TransformBroadcaster()

    def broadcast(self):
        #time = int(rospy.Time.now())
        #x = math.cos(1*time)
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.translation.x = math.sin(self.vel*base)*self.raio
        self.tf.transform.translation.y = math.cos(self.vel*base)*self.raio
        self.tf.transform.translation.z = 0

        self.broadcaster.sendTransform(self.tf)

if __name__ == '__main__':
    rndtf = [RandomTranform(planet) for planet in rospy.get_param('planets')]
    rate = rospy.Rate(60)
    base = 0
    while not rospy.is_shutdown():
        base += 0.05
        for rndtransform in rndtf:
            rndtransform.broadcast()

        rate.sleep()