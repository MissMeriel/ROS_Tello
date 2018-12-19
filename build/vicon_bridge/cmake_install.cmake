# Install script for directory: /home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/meriel/ros_workspace_clean.2018.09.24/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge/msg" TYPE FILE FILES
    "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/msg/Marker.msg"
    "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/msg/Markers.msg"
    "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/msg/TfDistortInfo.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge/srv" TYPE FILE FILES
    "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/srv/viconCalibrateSegment.srv"
    "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/srv/viconGrabPose.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge/cmake" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/build/vicon_bridge/catkin_generated/installspace/vicon_bridge-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/include/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/share/roseus/ros/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/share/common-lisp/ros/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/share/gennodejs/ros/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/meriel/ros_workspace_clean.2018.09.24/devel/lib/python2.7/dist-packages/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/lib/python2.7/dist-packages/vicon_bridge")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/vicon_bridge" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/include/vicon_bridge/tf_distortConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/vicon_bridge" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/lib/python2.7/dist-packages/vicon_bridge/__init__.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/meriel/ros_workspace_clean.2018.09.24/devel/lib/python2.7/dist-packages/vicon_bridge/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/vicon_bridge" TYPE DIRECTORY FILES "/home/meriel/ros_workspace_clean.2018.09.24/devel/lib/python2.7/dist-packages/vicon_bridge/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/build/vicon_bridge/catkin_generated/installspace/vicon_bridge.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge/cmake" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/build/vicon_bridge/catkin_generated/installspace/vicon_bridge-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge/cmake" TYPE FILE FILES
    "/home/meriel/ros_workspace_clean.2018.09.24/build/vicon_bridge/catkin_generated/installspace/vicon_bridgeConfig.cmake"
    "/home/meriel/ros_workspace_clean.2018.09.24/build/vicon_bridge/catkin_generated/installspace/vicon_bridgeConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/vicon_bridge" TYPE FILE FILES "/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/package.xml")
endif()

