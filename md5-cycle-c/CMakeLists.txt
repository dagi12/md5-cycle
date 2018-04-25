# CMakeLists files in this project can
# refer to the root source directory of the project as ${HELLO_SOURCE_DIR} and
# to the root binary directory of the project as ${HELLO_BINARY_DIR}.
cmake_minimum_required(VERSION 2.8.11)
project(.)
add_executable(md5cycle main.c)
target_link_libraries(md5cycle -lcrypto)
target_link_libraries(md5cycle -lssl)