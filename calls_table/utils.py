from datetime import datetime

import requests, csv
import time

from call.models import CallWindow, CallOkna, CallOkna, CallWindow

from client.models import Client, Number

from client.utils import create_calls_record
from calls_table.models import CallsTable

# from client.models import Client
from call.jobs.jobs import save_call_in_table
def save_call_in_table(client, call):
    # client.calls.add(call.pk)  # TODO fix

    calls = CallWindow.objects.filter(number=call.number).values('id').order_by('-id')
    ids_calls = calls.values_list('id', flat=True)

    for call_id in ids_calls:
        client.calls.add(call_id)

    calls_table = CallsTable.objects.create(client=client, call=call)
    calls_table.save()

def parse_csv_file():
    with open('call-history.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        i = 0
        for row in reader:
            i = i + 1
            id_call = i
            number_call = row[1]
            datetime_call = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            status = 2

            try:
                number = Number.objects.get(number=number_call)
                number_id = number.pk
            except Number.DoesNotExist:
                number = Number.objects.create(number=number_call, name='new client')
                number_id = number.pk
            try:
                client = Client.objects.get(numbers=number)
            except Client.DoesNotExist:
                client = Client.objects.create(author='system', name='new client')
                client.numbers.add(number_id)

            call = CallWindow.objects.create(id_call=id_call, number=number_call,
                                             datetime=datetime_call,
                                             call_type=status, client_id=client.pk)
            call.save()

            save_call_in_table(client=client, call=call)


def save_all_calls():
    pass
    # parse_csv_file()