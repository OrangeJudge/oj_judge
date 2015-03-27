#!/bin/bash
SHARE_DIR=`pwd`"/share"
echo target: $SHARE_DIR
docker run --rm -v $SHARE_DIR:/oj oj bash -c "cd /oj && g++-4.8 main.cc -o main.out > std.out 2>std.err"\
