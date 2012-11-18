
def get_bill(user):
    username=user.username
    att_name=user.att_user.att_number
    att_pw=user.att_user.att_pw
    files=[os.path.join(MEDIA_ROOT, d) 
           for d in os.listdir(MEDIA_ROOT) 
           if not os.path.isdir(os.path.join(MEDIA_ROOT, d))]
    
    #here is where we would actually pull down the bill
    
    #check it against existing bills to see if we already scanned in a copy
    try:
        newest=max(files, key=os.path.getmtime)
    except ValueError: #No files in directory, so we're safe to process the bill
    