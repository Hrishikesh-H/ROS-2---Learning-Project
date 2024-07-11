# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_hh_turtle_bringups_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED hh_turtle_bringups_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(hh_turtle_bringups_FOUND FALSE)
  elseif(NOT hh_turtle_bringups_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(hh_turtle_bringups_FOUND FALSE)
  endif()
  return()
endif()
set(_hh_turtle_bringups_CONFIG_INCLUDED TRUE)

# output package information
if(NOT hh_turtle_bringups_FIND_QUIETLY)
  message(STATUS "Found hh_turtle_bringups: 0.0.0 (${hh_turtle_bringups_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'hh_turtle_bringups' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${hh_turtle_bringups_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(hh_turtle_bringups_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${hh_turtle_bringups_DIR}/${_extra}")
endforeach()
