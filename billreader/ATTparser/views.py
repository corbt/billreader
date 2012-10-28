# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from ATTparser import parser, models
from ATTparser import tasks


def test(request):
    reset_db()
    current_user = User.objects.get(username__exact='alli')
    #parser.read_in_bill("/home/dotcloud/current/billreader/vincebill.csv")
    #parser.read_in_bill("vincebill.csv")

    #tasks.async_parse.delay("vincebill.csv", current_user)
    parser.read_in_bill.delay("/home/dotcloud/current/billreader/alli.csv", current_user)

    return HttpResponse("Processing bill")

def reset_db():
    models.Text_Message.objects.all().delete()
    models.Phone_Call.objects.all().delete()
    models.Data_Transfer.objects.all().delete()