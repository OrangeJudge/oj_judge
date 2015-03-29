#!/bin/bash
SHARE_DIR="$1"
function remove {
  local filename
  filename="$SHARE_DIR/$1"
  if [ -f "$filename" ]; then
    rm "$filename"
  fi
}

remove std.in
remove std.out
remove std.err
remove time.txt
