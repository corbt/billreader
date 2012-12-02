from ATTparser import __file__ as ATTdirectory
from ATTparser.parser import read_in_bill
from billreader.project_settings import USER_ROOT
import subprocess
import os
from datetime import datetime
from filecmp import cmp
import celery.task


#downloads the AT&T bill, makes sure that it isn't a duplicate, and then parses it
@celery.task(ignore_result=True)
def get_bill(user, debug=False):
    username=user.username
    att_number=user.att_user.att_number
    att_pw=user.att_user.att_pw
    
    #Bills stored in [data]/userdata/<username>/bills
    user_data=os.path.join(USER_ROOT, username, 'bills')
    if not os.path.exists(user_data):
        os.makedirs(user_data)
    
    #get old files to compare the new one to after download
    old_files=[os.path.join(user_data, d)
       for d in os.listdir(user_data) 
       if not os.path.isdir(os.path.join(user_data, d))]
    
    if debug:
        for file in old_files:
            os.remove(file)

    #give the file a timestamped name
    csv_path=os.path.join(user_data,datetime.now().strftime("%Y-%m-%d-%H:%M:%S")+".csv")
    
    #pull down the bill
    pull_script = os.path.join(os.path.dirname(ATTdirectory),'att_bill_retriever.sh')
    try: 
        subprocess.check_call([pull_script, att_number, att_pw, csv_path])
    except subprocess.CalledProcessError:
        return 1    #couldn't get file
    
    #check it against existing bills to see if we already scanned in a copy
    #list of all existing bills to compare against
    try:
        newest=max(old_files, key=os.path.getmtime)
    except: #No files in directory, so we're safe to process the bill
        read_in_bill(csv_path, user)
        return 0
        
    if cmp(csv_path, newest):
        #they're the same, so delete the new one and do nothing
        os.remove(csv_path)
    else:
        read_in_bill(csv_path, user)
        return 0