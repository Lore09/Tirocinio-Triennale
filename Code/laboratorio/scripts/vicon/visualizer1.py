#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped
from visualization_msgs.msg import Marker

def getCords(data):

    marker.header.frame_id = 'my_frame'
    marker.header.stamp = rospy.Time.now()

    marker.type = Marker.SPHERE

    marker.pose.position.x = data.transform.translation.x
    marker.pose.position.y = data.transform.translation.y
    marker.pose.position.z = data.transform.translation.z

    marker.action = Marker.ADD
    marker.ns = 'agents'

    marker.id = 32

    scale = 0.2
    marker.scale.x = scale
    marker.scale.y = scale
    marker.scale.z = scale

    color = [1.0, 0.0, 0.0, 1.0]

    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]
    marker.color.a = color[3]

    pub.publish(marker)


def main():

    global marker,pub

    marker = Marker()

    rospy.init_node('plotter', anonymous=True)

    rospy.Subscriber("/vicon/pippo/pippo", TransformStamped, getCords)
    pub = rospy.Publisher("/visualizer",Marker,queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    main()