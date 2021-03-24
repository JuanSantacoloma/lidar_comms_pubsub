#!/usr/bin/python

import rospy

from class_pubsub import lidar

# Inicializacion

if __name__ == '__main__':

    rospy.init_node('pubsub_node', anonymous=True)
    rospy.loginfo("Nodo inicializado")

    lidar()
    
    rospy.spin()

    

            