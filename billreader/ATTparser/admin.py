from django.contrib import admin
from ATTparser.models import Phone_Call, Text_Message, Data_Transfer

class Bill_Admin(admin.ModelAdmin):
    list_display = ('billed_user', 'billed_number', 'time_stamp')
    list_filter = ['billed_user','billed_number','time_stamp']

class Phone_Admin(admin.ModelAdmin):
    list_display = ('billed_user', 'billed_number', 'other_number', 'time_stamp', 'duration', 'incoming')
    list_filter = ['billed_user','billed_number']

class Text_Admin(admin.ModelAdmin):
    list_display = ('billed_user', 'billed_number', 'other_number', 'time_stamp', 'incoming', 'multimedia')
    list_filter = ['billed_user','billed_number']

class Data_Admin(admin.ModelAdmin):
    list_display = ('billed_user', 'billed_number', 'time_stamp', 'data')
    list_filter = ['billed_user','billed_number']



#admin.site.register(Bill_Object, Bill_Admin)
admin.site.register(Phone_Call, Phone_Admin)
admin.site.register(Text_Message, Text_Admin)
admin.site.register(Data_Transfer, Data_Admin)