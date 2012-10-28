from celery import task
from ATTparser import parser

@task()
def async_parse(bill_path, current_user):
    return parser.read_in_bill(bill_path, current_user)