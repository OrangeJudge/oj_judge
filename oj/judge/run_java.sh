#!/bin/bash
SHARE_DIR="$1"
TIME_LIMIT="$2"
MEMORY_LIMIT="$3"

echo "target: $SHARE_DIR"
echo "time limit: $TIME_LIMIT"
echo "memory limit: $MEMORY_LIMIT"
cont=$(docker run -d -v "$SHARE_DIR":/oj oj_java bash -c "cd /oj && /usr/bin/time -o time.txt -f \"%U\\n%S\\n%M\" java Main < std.in > std.out 2> std.err")
echo "start run $cont"
code=$(timeout "$TIME_LIMIT" docker wait "$cont" || true)
docker kill "$cont" &> /dev/null
docker rm "$cont" &> /dev/null
echo "finish run $cont"
if [ -z "$code" ]; then
    echo "timeout"
    exit 1
else
    echo "exited: $code"
    exit 0
fi
