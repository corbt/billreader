'''
Created on Sep 14, 2012

@author: Kyle
'''

import re
import datetime

#Removes dashes from phone number and returns a pure integer
def extractNumber(phoneString):
    if '@' in phoneString:  #email address, do no parsing
        return phoneString
    
    shortString = ''
    for s in phoneString:
        if s.isdigit():
            shortString = ''.join([shortString, s])
            
    if shortString != '': return shortString
    else: return phoneString #badly formatted, do nothing

#deals with poorly-formatted index column
def stripWhitespace(numString):
    return re.sub(r'\s', '', numString)

def getKB(row):
    if 'KB' in row[6]:
        return extractNumber(row[6])
    elif 'KB' in row[7]:
        return extractNumber(''.join([row[6], row[7]]))
    else:
        print "error, bad row: ", row
        
def extract_date(date, time):
    dateAndTime = ''.join([date, '|', time])
    timeStamp = datetime.datetime.strptime(dateAndTime, "%m/%d/%Y|%I:%M%p")
    return timeStamp
