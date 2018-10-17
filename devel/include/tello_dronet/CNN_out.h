// Generated by gencpp from file tello_dronet/CNN_out.msg
// DO NOT EDIT!


#ifndef TELLO_DRONET_MESSAGE_CNN_OUT_H
#define TELLO_DRONET_MESSAGE_CNN_OUT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace tello_dronet
{
template <class ContainerAllocator>
struct CNN_out_
{
  typedef CNN_out_<ContainerAllocator> Type;

  CNN_out_()
    : header()
    , steering_angle(0.0)
    , collision_prob(0.0)  {
    }
  CNN_out_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , steering_angle(0.0)
    , collision_prob(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _steering_angle_type;
  _steering_angle_type steering_angle;

   typedef float _collision_prob_type;
  _collision_prob_type collision_prob;





  typedef boost::shared_ptr< ::tello_dronet::CNN_out_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tello_dronet::CNN_out_<ContainerAllocator> const> ConstPtr;

}; // struct CNN_out_

typedef ::tello_dronet::CNN_out_<std::allocator<void> > CNN_out;

typedef boost::shared_ptr< ::tello_dronet::CNN_out > CNN_outPtr;
typedef boost::shared_ptr< ::tello_dronet::CNN_out const> CNN_outConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tello_dronet::CNN_out_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tello_dronet::CNN_out_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace tello_dronet

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'tello_dronet': ['/mnt/c/Users/jggrn/Documents/Projects/ros_workspace/src/tello_dronet/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::tello_dronet::CNN_out_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tello_dronet::CNN_out_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tello_dronet::CNN_out_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tello_dronet::CNN_out_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tello_dronet::CNN_out_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tello_dronet::CNN_out_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tello_dronet::CNN_out_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4a4cbb1fa95c6b93b88486210c46f9c1";
  }

  static const char* value(const ::tello_dronet::CNN_out_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4a4cbb1fa95c6b93ULL;
  static const uint64_t static_value2 = 0xb88486210c46f9c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::tello_dronet::CNN_out_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tello_dronet/CNN_out";
  }

  static const char* value(const ::tello_dronet::CNN_out_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tello_dronet::CNN_out_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 steering_angle\n\
float32 collision_prob\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::tello_dronet::CNN_out_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tello_dronet::CNN_out_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.steering_angle);
      stream.next(m.collision_prob);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CNN_out_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tello_dronet::CNN_out_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tello_dronet::CNN_out_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "steering_angle: ";
    Printer<float>::stream(s, indent + "  ", v.steering_angle);
    s << indent << "collision_prob: ";
    Printer<float>::stream(s, indent + "  ", v.collision_prob);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TELLO_DRONET_MESSAGE_CNN_OUT_H
