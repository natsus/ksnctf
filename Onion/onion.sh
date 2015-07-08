#! /bin/bash
hash=`cat onion.txt`
a=0
while [ $a -ne 21 ]
do
  hash=`echo $hash | base64 -D`
  echo "-- $a try --"
  echo $hash
  a=`expr $a + 1`
done
