#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import control

class Sistema:
    
    xe = [3*(10**7),0,0]
    ue = [364.63]

    W = 8*(10**-5);

    time_step = 0.001
    T = np.arange(0,0.5,time_step)

        #A = [[0,1,0],[0,-0.3,-3.6*(10**-3)],[0,0,-0.1]]

        #B = [[0],[0],[0.333*(10**7)]]

        #C = [0,0,1]

        #D = [0] 


        #num = 100.7 s^3 + 63.55 s^2 + 10 s + 7.386e-07
        #den = 0.001204 s^5 + s^4 + 0.4 s^3 + 0.03 s^2 + 7.386e-10 s

    G=control.tf([3.33*(10**-8),10**-8,7.38*(10**-16)],[1,0.4,0.03,7.386*(10**-10)])
    R = control.tf([3.022*(10**9),10**9],[0.0012,1,0])


    F = control.feedback(G*R,1)

    int,y = control.step_response(F,T,ue+xe,W)

    plt.plot(int,y)
    plt.show()
