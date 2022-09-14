#!/usr/bin/env python3

import rospy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from laboratorio.msg import Coordinates


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

y= []
t = []

# This function is called periodically from FuncAnimation
def animate(i,xs, ys):

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)



def getCords(data):

    y.append(data.y)
    t.append(data.x)

    
def main():

    global y
    y= []
    global t
    t = []

    rospy.init_node('plotter', anonymous=True)
    rospy.Subscriber("stepResponse", Coordinates, getCords)

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(t, y), interval=500)
    plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()