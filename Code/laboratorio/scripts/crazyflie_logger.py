import logging
import time
from threading import Event
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper
import rospy
from laboratorio.msg import Mellinguer


URI = uri_helper.uri_from_env(default='radio://0/110/2M/E7E7E7E708')
DEFAULT_HEIGHT = 0.1
position_estimate = [0, 0]
deck_attached_event = Event()
logging.basicConfig(level=logging.ERROR)

def move_linear_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(1)
        mc.forward(10)
        # time.sleep(1)
        # mc.turn_left(180)
        # time.sleep(1)
        # mc.forward(0.5)
        # time.sleep(1)

def log_pos_callback(timestamp, data, logconf):
    msg.roll = data['controller.cmd_roll']
    msg.pitch = data['controller.roll']
    msg.yaw = data['ctrlMel.i_err_z']

    pub.publish(msg)


def main():

    global pub,rate
    pub = rospy.Publisher('crazyflie', Mellinguer, queue_size=15)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(3000)

    global msg 
    msg = Mellinguer()


    
def take_off_simple(scf):
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(3)
        mc.stop()

if __name__ == '__main__':

    try:
        main()
    except rospy.ROSInterruptException:
        pass

    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        logconf = LogConfig(name='Position', period_in_ms=50)
        logconf.add_variable('controller.cmd_roll', 'float')
        logconf.add_variable('controller.roll', 'float')
        logconf.add_variable('ctrlMel.i_err_z', 'float')
        scf.cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_pos_callback)
        
        logconf.start()
        move_linear_simple(scf)
        logconf.stop()
