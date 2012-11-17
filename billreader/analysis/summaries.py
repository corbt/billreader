from ATTparser.models import Phone_Call, Text_Message, Data_Transfer

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
    