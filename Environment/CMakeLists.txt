cmake_minimum_required(VERSION 3.23)
project(Environment)

# defines group of source files
file(GLOB src
        "src/*.h"
        "src/*.cpp"
        )

set(CMAKE_CXX_STANDARD 17)

add_executable(Environment main.cpp ${src})
