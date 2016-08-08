#!/bin/bash
# set timeout to 600

while true ; do

clear 
echo "### ask for 6 new rooms, should end with FULL: "
./confcall_booking.py
./confcall_booking.py
DATA=$(./confcall_booking.py)
echo $DATA
./confcall_booking.py
./confcall_booking.py
./confcall_booking.py

echo "### ask for a new room, should be FULL: "
./confcall_booking.py

echo "### room check, good pin, should be OK : "
./confcall_booking.py $DATA

echo "### room check, wrong pin, should be NOK : "
./confcall_booking.py 100 123456

echo "### room check, wrong room number, should be NOK : "
./confcall_booking.py 999 123456

sleep 3
done
