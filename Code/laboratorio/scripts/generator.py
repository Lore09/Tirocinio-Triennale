#!/usr/bin/env python3

import rospy
import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import control

from laboratorio.msg import Coordinates

def get_step_response():

    xe = [3*(10**7),0,0]
    ue = [364.63]

    W = 8*(10**-5);
    
    start = float(rospy.get_param("start"))
    end = float(rospy.get_param("end"))

    T = np.arange(start,end,time_step)

    G=control.tf([3.33*(10**-8),10**-8,7.38*(10**-16)],[1,0.4,0.03,7.386*(10**-10)])
    R = control.tf([3.022*(10**9),10**9],[0.0012,1,0])

    F = control.feedback(G*R,1)

    int,y = control.step_response(F,T,ue+xe,W)

    return int,y


def main():

    pub = rospy.Publisher('stepResponse', Coordinates, queue_size=10)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(3000)

    # Ottengo la risposta al gradino del sistema
    global time_step
    time_step = 0.00001
    t,func = get_step_response()

    global msg 
    msg = Coordinates()
    
    save_data = bool(rospy.get_param("data"))

    if save_data:
        now = datetime.now()
        nomeFile = "data"+now.strftime("[%d-%m-%Y-%H:%M:%S]")+".csv"

        # Apertura csv
        file = open('/home/lore/catkin_ws/src/laboratorio/src/'+nomeFile,'w',encoding='UTF8')
        w = csv.writer(file)
        w.writerow(['t','step_response'])


    i = 0
    
    for value in func:

        i=i+time_step

        # Print to csv
        if save_data:
            w.writerow([i,value])

        if not rospy.is_shutdown():
            msg.x = i
            msg.y = value
            rospy.loginfo(msg)
            pub.publish(msg)

            rate.sleep()
            

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass