#!/bin/bash
# set timeout to 600
FILE='./ondemand_confcall.py'

while true ; do

clear 
echo "### ask for 6 new rooms, should end with FULL: "
$FILE
$FILE
DATA=$FILE
echo $DATA
$FILE
$FILE
$FILE

echo "### ask for a new room, should be FULL: "
$FILE

echo "### room check, good pin, should be OK : "
$FILE $DATA

echo "### room check, wrong pin, should be NOK : "
$FILE 100 123456

echo "### room check, wrong room number, should be NOK : "
$FILE 999 123456

sleep 3
done




