#!/bin/bash
SHARE_DIR="$1"
TIME_LIMIT="$2"
MEMORY_LIMIT="$3"

echo "target: $SHARE_DIR"
echo "time limit: $TIME_LIMIT"
echo "memory limit: $MEMORY_LIMIT"
cont=$(docker run -d -v "$SHARE_DIR":/oj oj bash -c "cd /oj && { time ./main.out < std.in > std.out 2> std.err ; } 2> time.txt")
echo "start run $cont"
code=$(timeout "$TIME_LIMIT" docker wait "$cont" || true)
docker kill "$cont" &> /dev/null
if [ -z "$code" ]; then
    echo "timeout"
else
    echo "exited: $code"
fi
docker rm "$cont" &> /dev/null
echo finish run
