// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hh_tt_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_
#define HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'turtles'
#include "hh_tt_interfaces/msg/detail/turtle__struct.h"

/// Struct defined in msg/TurtleArray in the package hh_tt_interfaces.
typedef struct hh_tt_interfaces__msg__TurtleArray
{
  hh_tt_interfaces__msg__Turtle__Sequence turtles;
} hh_tt_interfaces__msg__TurtleArray;

// Struct for a sequence of hh_tt_interfaces__msg__TurtleArray.
typedef struct hh_tt_interfaces__msg__TurtleArray__Sequence
{
  hh_tt_interfaces__msg__TurtleArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hh_tt_interfaces__msg__TurtleArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HH_TT_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__STRUCT_H_
