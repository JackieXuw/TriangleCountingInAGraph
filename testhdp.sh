#!/bin/bash

HADOOP_HOME=/usr/hdp/2.4.2.0-258
HADOOP_MAPREDUCE=${HADOOP_HOME}/hadoop-mapreduce
HADOOP_STREAMER=${HADOOP_MAPREDUCE}/hadoop-streaming-2.7.1.2.4.2.0-258.jar
HDFS_DATA_HOME=/user/liuyangtest/wenjie
TRIANGLE_DATA_HOME=${HDFS_DATA_HOME}/triangle
 
# first remove existing output file
if $(hadoop dfs -test -d ${TRIANGLE_DATA_HOME}/triangle-output);
 then hadoop dfs -rm -r ${TRIANGLE_DATA_HOME}/triangle-output;
fi

hadoop jar ${HADOOP_STREAMER} \
-file mapper.py -mapper 'python mapper.py' \
-file reducer.py -reducer 'python reducer.py' \
-input ${TRIANGLE_DATA_HOME}/${testtriangle}.txt -output ${TRIANGLE_DATA_HOME}/triangle-output

# remove existing output file
if $(hadoop dfs -test -d ${TRIANGLE_DATA_HOME}/triangle-output2);
  then hadoop dfs -rm -r ${TRIANGLE_DATA_HOME}/triangle-output2;
fi

hadoop jar ${HADOOP_STREAMER} \
-file mapper2.py -mapper 'python mapper2.py' \
-file reducer2.py -reducer 'python reducer2.py' \
-input ${TRIANGLE_DATA_HOME}/triangle-output/part-00000 -output ${TRIANGLE_DATA_HOME}/triangle-output2
 
