#!/usr/bin/env python3

import rospy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from laboratorio.msg import Mellinguer

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def getCords(data):

    x.append(data.roll)
    y.append(data.pitch)
    z.append(data.yaw)

    timeline.append(time.time()-start_time)

    rospy.loginfo(data)

def animate(i,t, x, y, z):

    ax.clear()
    ax.plot(t, x,t,y)
    ax.legend(['cmd','desir'])

rosso - x
verde y 
blu z
    
def main():

    global x,y,z,start_time,timeline
    x = 
    y = []
    z = []
    timeline = []

    start_time = time.time()

    rospy.init_node('plotter', anonymous=True)
    rospy.Subscriber("crazyflie", Mellinguer, getCords)

    ani = animation.FuncAnimation(fig, animate, fargs=(timeline,x,y,z), interval=50)
    plt.show()

    rospy.spin()

if __name__ == '__main__':
    main()