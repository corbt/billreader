# Create your views here.
from django.http import HttpResponse
from ATTparser import parser, models

def test(request):
    #reset_db()
    parser.read_in_bill("/home/dotcloud/current/billreader/alli.csv")
    
    return HttpResponse("Finished")

def reset_db():
    models.Text_Message.objects.all().delete()
    models.Phone_Call.objects.all().delete()
    models.Data_Transfer.objects.all().delete()