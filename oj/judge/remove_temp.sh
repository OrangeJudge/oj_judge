#!/bin/bash
function remove {
  local filename
  filename="$1"
  if [ -f "$filename" ]; then
    echo remove $filename
    rm "$filename"
  fi
}

cd share
remove std.out
remove std.err
remove main.out
remove time.txt
