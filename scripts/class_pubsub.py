#!/usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

class lidar:

    def __init__(self):

        self.nameTopicSub = "/scan"
        self.nameTopicPub = "/scan_mod"

        #Subscriptor

        rospy.Subscriber(self.nameTopicSub,LaserScan,self.lidar_callback,queue_size=10)

        #Publicador

        self.pub = rospy.Publisher(self.nameTopicPub,LaserScan,queue_size=10)

    def lidar_callback(self, lidar_scan):
        
        new_msg_laser_scan = lidar_scan #mensaje con info del callback
        new_msg_laser_scan.range_max = (10.0)
        new_msg_laser_scan.range_min = (0.0)
                    
        self.pub.publish(new_msg_laser_scan)
