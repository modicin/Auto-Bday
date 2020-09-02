# Auto-Bday
Send a birthday message via Whatsapp automatically to specified numbers with/without a custom message.

### [Releases](https://github.com/modicin/Auto-Bday/releases)

## Storing Birthdays
All birthday data is stored in a csv file names 'birthdays.csv' in the same directory as the python files.

|Variable|Descriptions|
| ----------- | ----------- |
|Birthday Date|Date of birthday in format dd-mm|
|Phone Number|Phone Number including country specific code e.g. +44 for UK|
|Name|Persons Name. Self explanatory|
|Message|Custom Message to send, if left blank, premade message will be sent(see below)|
|Sent this year?|Placeholder to prevent multiple sendings in a day, set as '0' when entering birthdays|

### Date format
Dates in the csv file should follow a day-month order as they do in the UK, first time setup for switching the two is coming in future releases.
The following separators between day and month are '-', '/', '.' and you can write dates with or without a preceding zero eg 2 or 02.

*This is not a very well written program and not ready to be easily imported into other programs, I will work very hard to to perfect it and suggestions or incredibly welcomed*
