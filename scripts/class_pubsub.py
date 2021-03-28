# #!/usr/bin/python

import rospy
from sensor_msgs.msg import LaserScan

class lidar:

    def __init__(self):

        self.nameTopicSub = "/scan"
        self.nameTopicPub = "/scan_mod"

        # Subscriptor

        rospy.Subscriber(self.nameTopicSub, LaserScan, self.Lidar_Callback, queue_size=10)
        # Publicador

        self.pub = rospy.Publisher(self.nameTopicPub, LaserScan,queue_size=10)

    def Lidar_Callback(self, lidar_scan):
        new_msg_laser_scan = lidar_scan
        
        new_msg_laser_scan.range_max = 10.0
        new_msg_laser_scan.range_min = 0.7

        self.pub.publish(new_msg_laser_scan)