// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hh_tt_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
#define HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hh_tt_interfaces/msg/detail/turtle_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hh_tt_interfaces
{

namespace msg
{

namespace builder
{

class Init_TurtleArray_turtles
{
public:
  Init_TurtleArray_turtles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hh_tt_interfaces::msg::TurtleArray turtles(::hh_tt_interfaces::msg::TurtleArray::_turtles_type arg)
  {
    msg_.turtles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hh_tt_interfaces::msg::TurtleArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::hh_tt_interfaces::msg::TurtleArray>()
{
  return hh_tt_interfaces::msg::builder::Init_TurtleArray_turtles();
}

}  // namespace hh_tt_interfaces

#endif  // HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
