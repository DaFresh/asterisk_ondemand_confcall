# meetme-sefltservice


Asterisk OnDemand ConfCall Service


It provides on demand conferences room number and pin for users. The python script is in charge of :


- generate, within a defined pool, room numbers and associted random pin code
- keep track and cleaning of provided room number and pin
- verify the correctness of room number and pin codes

This is done via 2 files :

- ondemand_confcall.py : the python script
- ondemand_confcall.conf : an asterisk dialplan exemple that containt 2 macros for book and access conferenceis rooms.

Requirements :

- Asterisk, at least v1.6
- Python 

Installation :

- put the python script in /var/lib/asterisk/agi-bin/
- adjust db_path, room_range and random_pin to you convenience. (db file need to be writable by Asterisk)
- include the ondemand_conf_call.conf in your dial plan and point 2 extentions to both macro :
	- exten = 888,1,Macro(meetme_book)
	- exten = 888,1,Macro(meetme_book)

As a recommendation, the booking macro should only be accessible via internal extention.

Enjoy
