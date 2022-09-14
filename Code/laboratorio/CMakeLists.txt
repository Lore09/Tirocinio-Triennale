cmake_minimum_required(VERSION 3.0.2)
project(laboratorio)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  Coordinates.msg
  Mellinguer.msg
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
 )

include_directories(
  # include
  ${catkin_INCLUDE_DIRS}
  )
  
  
catkin_install_python(
    PROGRAMS scripts/generator.py scripts/plotter.py scripts/crazyflie_logger.py scripts/crazyflie_plotter.py scripts/vicon/3dplot.py scripts/vicon/visualizer1.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
    
    
catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)
