#!/usr/bin/env python

import rospy
import math
from basics.msg import Complex
from std_msgs.msg import Float32

def callback(msg):
	print 'Real:', msg.real
	print 'Imaginary:', msg.imaginary
	mag = Float32()
	mag.data = math.sqrt(msg.real * msg.real + msg.imaginary * msg.imaginary)
	print 'Mag:', mag.data
	pub.publish(mag)
	

rospy.init_node('message_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
pub = rospy.Publisher('mag', Float32, queue_size=10)
rospy.spin()

print 'done'

