#!/usr/bin/env python3

import rospy
import matplotlib.animation as animation
import time
from geometry_msgs.msg import TransformStamped
from matplotlib import pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)

ax.autoscale(enable=None, axis="x", tight=True)

def getCords(data):

    x.append(data.transform.translation.x)
    y.append(data.transform.translation.y)
    z.append(data.transform.translation.z)

    if(len(x) > 2000):
        x.pop(0)
        y.pop(0)
        z.pop(0)

def animate(i,x, y, z):

    ax.clear()
    ax.plot3D(x, y, z, 'red')
    ax.legend(['pippo'])
    
def main():

    global x,y,z
    x = []
    y = []
    z = []

    rospy.init_node('plotter', anonymous=True)
    rospy.Subscriber("/vicon/pippo/pippo", TransformStamped, getCords)

    ani = animation.FuncAnimation(fig, animate, fargs=(x,y,z), interval=25)
    plt.show()

    rospy.spin()

if __name__ == '__main__':
    main()