# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from ATTparser import models, retriever, parser
#from ATTparser import tasks
import os

def loaddata(request, username):
    models.reset_db()
    
    try:
        current_user = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        return HttpResponse("Error: user \""+username+"\" not found in the database")

    
    retriever.get_bill(current_user, debug=True)
    #parser.read_in_bill.delay("/home/kyle/proj/bill_reader/web/billreader/"+username+".csv", current_user)

    '''
    if 'DOTCLOUD_ENVIRONMENT' in os.environ:
        retriever.get_bill(current_user)
        #parser.read_in_bill.delay("/home/dotcloud/current/billreader/"+username+".csv", current_user)
    else:
        #retriever.get_bill(current_user)
        #parser.read_in_bill.delay("/home/kyle/proj/bill_reader/web/billreader/"+username+".csv", current_user)
        pass
    '''

    return HttpResponse("Processing bill for "+username)
    

def index(request):
    return HttpResponse("No user specified, please try again.")