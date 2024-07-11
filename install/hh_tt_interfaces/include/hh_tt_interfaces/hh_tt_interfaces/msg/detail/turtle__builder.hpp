// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hh_tt_interfaces:msg/Turtle.idl
// generated code does not contain a copyright notice

#ifndef HH_TT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
#define HH_TT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hh_tt_interfaces/msg/detail/turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hh_tt_interfaces
{

namespace msg
{

namespace builder
{

class Init_Turtle_theta
{
public:
  explicit Init_Turtle_theta(::hh_tt_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  ::hh_tt_interfaces::msg::Turtle theta(::hh_tt_interfaces::msg::Turtle::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hh_tt_interfaces::msg::Turtle msg_;
};

class Init_Turtle_y
{
public:
  explicit Init_Turtle_y(::hh_tt_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  Init_Turtle_theta y(::hh_tt_interfaces::msg::Turtle::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Turtle_theta(msg_);
  }

private:
  ::hh_tt_interfaces::msg::Turtle msg_;
};

class Init_Turtle_x
{
public:
  explicit Init_Turtle_x(::hh_tt_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  Init_Turtle_y x(::hh_tt_interfaces::msg::Turtle::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Turtle_y(msg_);
  }

private:
  ::hh_tt_interfaces::msg::Turtle msg_;
};

class Init_Turtle_name
{
public:
  Init_Turtle_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Turtle_x name(::hh_tt_interfaces::msg::Turtle::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Turtle_x(msg_);
  }

private:
  ::hh_tt_interfaces::msg::Turtle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::hh_tt_interfaces::msg::Turtle>()
{
  return hh_tt_interfaces::msg::builder::Init_Turtle_name();
}

}  // namespace hh_tt_interfaces

#endif  // HH_TT_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
