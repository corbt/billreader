from ATTparser.models import Phone_Call, Text_Message


def get_full_history(user, billed_number, other_number):
    phone_calls=Phone_Call.objects.filter(billed_user=user
                  ).filter(billed_number=billed_number
                  ).filter(other_number=other_number)
    text_messages=Text_Message.objects.filter(billed_user=user
                  ).filter(billed_number=billed_number
                  ).filter(other_number=other_number)
    
    history = []
    for record in phone_calls:
        history.append({'time':record.time_stamp, 'incoming':record.incoming, 'type':'call'})
    for record in text_messages:
        if record.multimedia: type='multimedia'
        else: type='text'
        history.append({'time':record.time_stamp, 'incoming':record.incoming, 'type': type})

    return sorted(history, key=lambda k: k['time'], reverse=True)
