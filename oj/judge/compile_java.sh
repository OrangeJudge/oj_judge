#!/bin/bash
SHARE_DIR="$1"
echo target: "$SHARE_DIR"
docker run --rm -v "$SHARE_DIR":/oj oj_java bash -c "cd /oj && javac Main.java > std.out 2>std.err"
