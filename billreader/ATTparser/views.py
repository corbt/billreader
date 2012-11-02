# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from ATTparser import parser, models
from ATTparser import tasks
import os

def loaddata(request, username):
    models.reset_db()
    try:
        current_user = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        return HttpResponse("Error: user \""+username+"\" not found in the database")

    
    if 'DOTCLOUD_ENVIRONMENT' in os.environ:
        parser.read_in_bill.delay("/home/dotcloud/current/billreader/"+username+".csv", current_user)
    else:
        parser.read_in_bill.delay(username+".csv", current_user)

    #tasks.async_parse.delay("vincebill.csv", current_user)

    return HttpResponse("Processing bill for "+username)
    

def index(request):
    return HttpResponse("No user specified, please try again.")