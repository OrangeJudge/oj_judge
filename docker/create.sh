#!/usr/bin/env bash
cd cpp
docker build -t oj_cpp .
cd ..
cd java
docker build -t oj_java .
cd ..
