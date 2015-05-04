#!/bin/bash
SHARE_DIR="$1"
echo target: "$SHARE_DIR"
docker run --rm -v "$SHARE_DIR":/oj oj bash -c "cd /oj && gcc-4.8 main.c -o main.out > std.out 2>std.err"
