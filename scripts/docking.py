#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ar_pose.msg import ARMarker


pub_vel = None

vx = 0
vt = 0
mvt = 0
mvx = 0
l = 0.9


def marker_cb(data):
    kx = -0.05
    kt = -0.5
    mvx = kx*data.pose.pose.position.z
    mvt = kt*data.pose.pose.position.x



def listener():
    global pub_vel

    rospy.init_node('docker', anonymous=True)
    pub_vel = rospy.Publisher('/kobra/cmd_vel', Twist, queue_size=10)

    rospy.Subscriber("/ar_pose_marker", ARMarker, marker_cb)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        vx = l*vx + mvx
        vt = l*vt + mvt
        mvt = 0
        mvx = 0
        cmd_vel = Twist()
        cmd_vel.linear.x = vx
        cmd_vel.angular.z = vt

        rate.sleep()


if __name__ == '__main__':
    listener()
