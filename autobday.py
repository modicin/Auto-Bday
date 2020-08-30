from datetime import datetime
import csv
import os
from shutil import copy #modules to rename and delete files after changing values

#import messenger
import webbrowser as web
import pyautogui as pg
import time


def sendmsg(telno,msg = 'HAPPY BIRTHDAY!! Hope you have a great day!'):
    web.open('https://web.whatsapp.com/send?phone='+telno+'&text='+msg)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(10)
    pg.press('enter')
    return True

'''
def sendmsg(telno,timehr, timemin, msg = 'HAPPY BIRTHDAY!! Hope you have a great day!'):
    """
    Function to send the final message to specific number.
    :param telno: Telephone number to send the message to.
    :param timehr: The hour at which to send the message.
    :param timemin: The second at which to send the message
    :param msg: The Message to be sent to the person
    :return:
    """

    messenger.whatmsg(telno,msg)
    return True
'''

def timetosend():
    """
    Function that grabs the time and takes the integer for hour and minute, adds two to minute to ensure the message is
        sent in the near future and not the next day sort of future then returns a tuple of both of them.
    :return: tuple containing hour and minute to initiate send process
    """
    time = datetime.now()
    timehr = time.hour
    timemin = time.minute + 2
    return (timehr,timemin)


def birthdaycheck(date):
    """
    function to check for peoples birthdays today
    :param date: todays date which should be of the form 'dd-mm' and in string format
    :return: A list of peoples birthday today, their phone number and then there custom message if one exists
    """
    bdaystoday = []
    with open('birthdays.csv','r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ';') #creates a csv reader object
        i=0 #placeholder implemented in at later stage for the complete function.
        for row in csvreader:
            if row[0] == date:
                bdaystoday.append([row[2],row[1],row[3],i,row[4]]) #=(name,number,message,index,1 or 0 representing already sent today or not)
            i+=1

    return bdaystoday

def complete(indeces): #list of indexes of birthdays from that day.
    """
    This function does two things that are closely related:
        marks any messages that have been sent
    :param indeces: list containing all indeces refering to row number containing active birthdays that are yet to be sent a message.
    :return: returns nothing
    """

    with open('birthdays.csv','r') as csvin:
        csvreader = csv.reader(csvin,delimiter=';') #opening csvin file and reading it
        rows = [] #empty list to store all rows in.

        for row in csvreader: #creating a list of all rows
            rows.append(row)


        csvout = open('out.csv','w') #creating new writer object
        csvwriter = csv.writer(csvout,delimiter=';')

        for k in range(len(rows)):
#The first if statement cleverly (in my opinion) checks to see if a birthday message has been sent for prev days ...
#... and changes old value back to a 0.
            if rows[k][4] == '1':
                rows[k][4] = '0'

            if k in indeces:
                rows[k][4] = '1'
                csvwriter.writerow(rows[k])
            else:
                csvwriter.writerow(rows[k])

        csvout.close()
    return

def filedel():
    """
    Function that renames creates a backup birthday csv file then deletes the original and renames the out csv.
    """
    copy('/home/modicin/Documents/Python Projects/autobdaymessage/birthdays.csv', '/home/modicin/Documents/Python Projects/autobdaymessage/Backup/')
    os.remove('/home/modicin/Documents/Python Projects/autobdaymessage/birthdays.csv')
    os.rename(r'/home/modicin/Documents/Python Projects/autobdaymessage/out.csv',r'/home/modicin/Documents/Python Projects/autobdaymessage/birthdays.csv')
    return

def today():
    time = datetime.now()
    date = ("{:02}-{:02}".format(time.day,
                                 time.month))  # Creating date string ensuring it is in 2 digit format with leading zero.
    return date




