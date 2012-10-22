'''
Created on Sep 15, 2012

@author: Kyle
'''

import csv
from ATTparser.models import Bill_Object
from django.contrib.auth.models import User
from django.utils import timezone
import numberOperations
from django.core.files import File

#Parses the entire AT&T-generated CSV bill file and creates a database of calls
def read_in_bill(csvBill):
    #TMP hard-coding for testing purposes
    current_user = User.objects.get(username__exact='vince')
    
    phoneBillCSV = csv.reader(open(csvBill, 'r'))
    
    currentNumber = 0
    entryType = ''
    
    for row in phoneBillCSV:


        #blank row
        if len(row) < 1:
            continue        #blank row, ignore
        
        #valid data row
        elif numberOperations.stripWhitespace(row[0]).isdigit():
            entry = 3
            parseEntry(row, currentNumber, entryType, current_user)
            #self._billByNumbers.get(currentNumber).append(entry)
        
        #change of phone number
        elif row[0] == 'Data Detail' or row[0] == 'Call Detail':
            if row[0] == 'Data Detail': entryType = 'dt'
            elif row[0] == 'Call Detail': entryType = 'c'
        
            currentNumber = numberOperations.extractNumber(row[1])
            #if not currentNumber in self._billByNumbers.keys(): self._billByNumbers.update({currentNumber: []})

#Takes undecoded row of data, identifies entry type and returns the correct bill object
def parseEntry(row, current_number, entryType, current_user):
    date_time = numberOperations.extract_date(row[2], row[3])
    
    if entryType == 'c':
        if row[5] == 'INCOMING CL': incoming = True
        else: incoming = False
        current_user.phone_call_set.create(billed_number=str(current_number), 
                                           time_stamp=date_time, 
                                           upload_date=timezone.now(),
                                           incoming=incoming,
                                           duration=row[6],
                                           other_number=numberOperations.extractNumber(row[4]))
        
        #entry = BillObjects.Call(currentNumber, row[2], row[3], numberOperations.extractNumber(row[4]), row[6], incoming)
        
    elif row[5] == 'Data Transfer':
        current_user.data_transfer_set.create(billed_number=str(current_number), 
                                           time_stamp=date_time, 
                                           upload_date=timezone.now(),
                                           data=numberOperations.getKB(row))

        #entry = BillObjects.DataTransfer(currentNumber, row[2], row[3], numberOperations.getKB(row))
        pass

    elif row[10] == 'Sent' or row[10] == 'Rcvd':
        if row[5] == 'Text Message': multimedia = False
        else: multimedia = True
        if row[10] == 'Rcvd': incoming = True
        elif row[10] == 'Sent': incoming = False
        else: print "Bad row, text not sent/received", row
        
        current_user.text_message_set.create(billed_number=str(current_number), 
                                   time_stamp=date_time, 
                                   upload_date=timezone.now(),
                                   incoming=incoming,
                                   multimedia=multimedia,
                                   other_number=numberOperations.extractNumber(row[4]))

        #entry = BillObjects.Text(currentNumber, row[2], row[3], row[4], incoming, multimedia)
        
    else: #unknown data type, mark as such
        #entry = BillObjects.BillObject(currentNumber, row[2], row[3], 'o')
        pass
    #return entry

    

        
