from django.db import models
from django.contrib.auth.models import User

#virtual base class for all items
class Bill_Object(models.Model):
    billed_user = models.ForeignKey(User)
    billed_number = models.CharField(max_length=20)
    time_stamp = models.DateTimeField()
    upload_date = models.DateTimeField()
    
    class Meta:
        abstract = True
    def __unicode__(self):
        return "Calling number: %s Time: %s" % (self.billed_number, self.time_stamp)


class Text_Message(Bill_Object):
    incoming = models.BooleanField('Incoming Text')
    other_number = models.CharField('Number Texting', max_length=20)
    multimedia = models.BooleanField('Media Message')
 
class Phone_Call(Bill_Object):
    incoming = models.BooleanField('Incoming Call')
    duration = models.IntegerField('Call Duration (min)')
    other_number = models.CharField('Number Calling', max_length=20)


class Data_Transfer(Bill_Object):
    data = models.IntegerField('Data Transfered (KB)')
    
class ATT_user(models.Model):
    user=models.OneToOneField(User, primary_key=True)
    att_number=models.CharField('Account phone number', max_length=20)
    att_pw = models.CharField('Account password', max_length=20)
    
def reset_db():
    Text_Message.objects.all().delete()
    Phone_Call.objects.all().delete()
    Data_Transfer.objects.all().delete()