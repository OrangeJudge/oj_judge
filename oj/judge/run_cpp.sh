#!/bin/bash
to=$1

SHARE_DIR=`pwd`"/share"
echo target: $SHARE_DIR
cont=$(docker run -d -v $SHARE_DIR:/oj oj bash -c "cd /oj && { time ./main.out < std.in > std.out 2> std.err ; } 2> time.txt")
echo start run
code=$(timeout "$to" docker wait "$cont" || true)
docker kill $cont &> /dev/null
if [ -z "$code" ]; then
    echo timeout
else
    echo exited: $code
fi
docker rm $cont &> /dev/null
echo finish run
