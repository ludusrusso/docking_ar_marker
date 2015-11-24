#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ar_pose.msg import ARMarker


pub_vel = None

def marker_cb(data):
    kx = -0.5
    kt = -0.5
    cmd_vel = Twist()
    cmd_vel.linear.x = -kx*data.pose.pose.position.z
    cmd_vel.angular.z = -kt*data.pose.pose.position.y

    pub_vel.publish(cmd_vel)



def listener():
    global pub_vel

    rospy.init_node('docker', anonymous=True)
    pub_vel = rospy.Publisher('/kobra/locomotion_cmd_vel', Twist, queue_size=10)

    rospy.Subscriber("/ar_pose_marker", ARMarker, marker_cb)

    rospy.spin()

if __name__ == '__main__':
    listener()
