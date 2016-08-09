# Asterisk OnDemand ConfCall Service

** Provides on demand conferences room number and pin to users. **

## Introduction 
This is done via 2 files :

- ondemand_confcall.py, the python script, in charge of :
	- generate, within a defined pool, room numbers and associted random pin code
	- keep track and cleaning of provided room number and pin
	- verify the correctness of room number and pin codes

- ondemand_confcall.conf, an asterisk dialplan exemple that containt 2 macros :
	- macro-ondemand_confcall_booking distribute room number and pin codes
	- macro-ondemand_confcall_access verify room number and pin code correcteness, then put callers in conference.

## Requirements :

- Asterisk, at least v1.6
- Python 

## Installation :

- put the python script in /var/lib/asterisk/agi-bin/
- adjust db_path, room_range, random_pin, and time_outdated to you convenience. (db file need to be writable by Asterisk)
- include the ondemand_conf_call.conf in your dial plan and give 2 extentions to both macro, for exemple :
	- exten = 666,1,Macro(ondemand_confcall_booking)
	- exten = +33123456789,1,Macro(ondemand_confcall_access)

### Use :

- call the ondemand_confcall_booking extension to get a room number and the corresponding pin number
- call the ondemand_confcall_access extension, give a valid room and pin number to access conference room

### Recommendations and tips :

- the booking macro should only be accessible via internal extention.
- the DB file is automaticaly created on the first launch of the script
- if the python script in initialy lanched in root, permitions on the DB file need to be adjusted (or remove the db file)
- adjust 'room_range' 


Enjoy
