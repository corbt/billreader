from ATTparser.models import Phone_Call, Text_Message, Data_Transfer
from django.db import models

def get_lines(user):
    phone_lines=Phone_Call.objects.filter(billed_user=user).values_list('billed_number', flat=True).distinct()
    text_lines=Text_Message.objects.filter(billed_user=user).values_list('billed_number', flat=True).distinct()
    data_lines=Data_Transfer.objects.filter(billed_user=user).values_list('billed_number', flat=True).distinct()
    
    lines=set()
    for item in phone_lines:
        lines.add(item)
    for item in text_lines:
        lines.add(item)
    for item in data_lines:
        lines.add(item)
        
    return list(lines)
    

def get_top_calls(user, billed_number):
    top_calls = Phone_Call.objects.filter(billed_user=user
      ).filter(billed_number=billed_number
      ).values('other_number').annotate(c=models.Count('other_number')
      ).order_by('-c')
      #TODO: filter by date as well
      
    return top_calls