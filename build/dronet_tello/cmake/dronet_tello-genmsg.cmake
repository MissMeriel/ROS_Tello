# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "dronet_tello: 2 messages, 0 services")

set(MSG_I_FLAGS "-Idronet_tello:/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Ivicon_bridge:/home/meriel/ros_workspace_clean.2018.09.24/src/vicon_bridge/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(dronet_tello_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_custom_target(_dronet_tello_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "dronet_tello" "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_custom_target(_dronet_tello_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "dronet_tello" "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dronet_tello
)
_generate_msg_cpp(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dronet_tello
)

### Generating Services

### Generating Module File
_generate_module_cpp(dronet_tello
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dronet_tello
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(dronet_tello_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(dronet_tello_generate_messages dronet_tello_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_cpp _dronet_tello_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_cpp _dronet_tello_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dronet_tello_gencpp)
add_dependencies(dronet_tello_gencpp dronet_tello_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dronet_tello_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dronet_tello
)
_generate_msg_eus(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dronet_tello
)

### Generating Services

### Generating Module File
_generate_module_eus(dronet_tello
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dronet_tello
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(dronet_tello_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(dronet_tello_generate_messages dronet_tello_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_eus _dronet_tello_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_eus _dronet_tello_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dronet_tello_geneus)
add_dependencies(dronet_tello_geneus dronet_tello_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dronet_tello_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dronet_tello
)
_generate_msg_lisp(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dronet_tello
)

### Generating Services

### Generating Module File
_generate_module_lisp(dronet_tello
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dronet_tello
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(dronet_tello_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(dronet_tello_generate_messages dronet_tello_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_lisp _dronet_tello_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_lisp _dronet_tello_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dronet_tello_genlisp)
add_dependencies(dronet_tello_genlisp dronet_tello_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dronet_tello_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dronet_tello
)
_generate_msg_nodejs(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dronet_tello
)

### Generating Services

### Generating Module File
_generate_module_nodejs(dronet_tello
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dronet_tello
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(dronet_tello_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(dronet_tello_generate_messages dronet_tello_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_nodejs _dronet_tello_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_nodejs _dronet_tello_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dronet_tello_gennodejs)
add_dependencies(dronet_tello_gennodejs dronet_tello_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dronet_tello_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello
)
_generate_msg_py(dronet_tello
  "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello
)

### Generating Services

### Generating Module File
_generate_module_py(dronet_tello
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(dronet_tello_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(dronet_tello_generate_messages dronet_tello_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/CNN_out.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_py _dronet_tello_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/meriel/ros_workspace_clean.2018.09.24/src/dronet_tello/msg/FlightData.msg" NAME_WE)
add_dependencies(dronet_tello_generate_messages_py _dronet_tello_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(dronet_tello_genpy)
add_dependencies(dronet_tello_genpy dronet_tello_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dronet_tello_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dronet_tello)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dronet_tello
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(dronet_tello_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET vicon_bridge_generate_messages_cpp)
  add_dependencies(dronet_tello_generate_messages_cpp vicon_bridge_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dronet_tello)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/dronet_tello
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(dronet_tello_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET vicon_bridge_generate_messages_eus)
  add_dependencies(dronet_tello_generate_messages_eus vicon_bridge_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dronet_tello)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dronet_tello
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(dronet_tello_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET vicon_bridge_generate_messages_lisp)
  add_dependencies(dronet_tello_generate_messages_lisp vicon_bridge_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dronet_tello)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/dronet_tello
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(dronet_tello_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET vicon_bridge_generate_messages_nodejs)
  add_dependencies(dronet_tello_generate_messages_nodejs vicon_bridge_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dronet_tello
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(dronet_tello_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET vicon_bridge_generate_messages_py)
  add_dependencies(dronet_tello_generate_messages_py vicon_bridge_generate_messages_py)
endif()
