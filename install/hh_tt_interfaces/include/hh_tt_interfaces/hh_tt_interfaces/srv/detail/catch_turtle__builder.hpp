// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hh_tt_interfaces:srv/CatchTurtle.idl
// generated code does not contain a copyright notice

#ifndef HH_TT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_
#define HH_TT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hh_tt_interfaces/srv/detail/catch_turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hh_tt_interfaces
{

namespace srv
{

namespace builder
{

class Init_CatchTurtle_Request_name
{
public:
  Init_CatchTurtle_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hh_tt_interfaces::srv::CatchTurtle_Request name(::hh_tt_interfaces::srv::CatchTurtle_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hh_tt_interfaces::srv::CatchTurtle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hh_tt_interfaces::srv::CatchTurtle_Request>()
{
  return hh_tt_interfaces::srv::builder::Init_CatchTurtle_Request_name();
}

}  // namespace hh_tt_interfaces


namespace hh_tt_interfaces
{

namespace srv
{

namespace builder
{

class Init_CatchTurtle_Response_success
{
public:
  Init_CatchTurtle_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hh_tt_interfaces::srv::CatchTurtle_Response success(::hh_tt_interfaces::srv::CatchTurtle_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hh_tt_interfaces::srv::CatchTurtle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hh_tt_interfaces::srv::CatchTurtle_Response>()
{
  return hh_tt_interfaces::srv::builder::Init_CatchTurtle_Response_success();
}

}  // namespace hh_tt_interfaces

#endif  // HH_TT_INTERFACES__SRV__DETAIL__CATCH_TURTLE__BUILDER_HPP_
