import datetime

import requests, csv
import time

from call.models import CallWindow, CallOkna, CallOkna, CallWindow

from client.models import Client, Number

from client.utils import create_calls_record

from calls_table.models import CallsTable
#
from client.models import Client

# API_URL = "https://86.57.178.104:4021"
API_URL = "https://192.168.1.209:4021"
MAIN_URL = API_URL + "/admin/api/jsonrpc/"
LOGIN = "Ilya"
PASSWORD = "bkmz1337"


def get_credentials():
    login_session = requests.Session()

    login_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
    }

    login_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Session.login",
        "params": {
            "userName": LOGIN,
            "password": PASSWORD,
            "application": {
                "name": "Test",
                "vendor": "Keiro",
                "version": "1.0",
                "remember": True
            }
        }
    }

    login_response = login_session.post(headers=login_headers,
                                        url=MAIN_URL, json=login_params, verify=False)

    token = login_response.json()["result"]["token"]
    kerio_cookies = login_session.cookies.get_dict()
    return {"token": token, "cookies": kerio_cookies}


def get_current_blacklist():
    credentials = get_credentials()

    get_current_blacklist_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    get_current_blacklist_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "CallerIdBlacklist.get",
    }

    get_current_blacklist_session = requests.Session()
    get_current_blacklist_response = get_current_blacklist_session.post(headers=get_current_blacklist_headers,
                                                                        url=MAIN_URL, json=get_current_blacklist_params,
                                                                        verify=False, cookies=credentials["cookies"])
    return get_current_blacklist_response.json()["result"]


def block_number(number):
    credentials = get_credentials()

    block_number_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    current_blacklist = get_current_blacklist()

    block_number_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "CallerIdBlacklist.set",
        "params": {
            "blockAnonymous": current_blacklist["blockAnonymous"],
            "blacklistItemList": current_blacklist["blacklistItemList"] + [
                {"expression": number, "enabled": True, "description": ""}]
        }
    }

    block_number_session = requests.Session()
    block_number_response = block_number_session.post(
        headers=block_number_headers, url=MAIN_URL, json=block_number_params, verify=False,
        cookies=credentials["cookies"])

    return block_number_response.json()


def hang_up(channel):
    credentials = get_credentials()

    hang_up_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    hang_up_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Server.hangupCall",
        "params": {
            "channels": [
                channel

            ]
        }
    }

    hang_up_session = requests.Session()
    hang_up_request = hang_up_session.post(
        headers=hang_up_headers, json=hang_up_params, url=MAIN_URL, verify=False, cookies=credentials["cookies"])

    print(hang_up_request.json())

    return hang_up_request.json()


def get_calls():
    credentials = get_credentials()
    get_calls_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
        "X-Token": credentials["token"]
    }

    get_calls_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Status.getCalls",
        "params": {
            "query": {
                "limit": -1,
                "start": 0,
                "orderBy": [
                    {
                        "columnName": "ANSWERED_DURATION",
                        "direction": "Asc"
                    }
                ]
            }
        }
    }

    get_calls_session = requests.Session()
    get_calls_request = get_calls_session.post(
        headers=get_calls_headers, json=get_calls_params, url=MAIN_URL, verify=False, cookies=credentials["cookies"])

    return get_calls_request.json()["result"]


def save_call_in_table(client, call):
    # client.calls.add(call.pk)  # TODO fix

    calls = CallWindow.objects.filter(number=call.number).values('id').order_by('-id')
    ids_calls = calls.values_list('id', flat=True)

    for call_id in ids_calls:
        client.calls.add(call_id)

    calls_table = CallsTable.objects.create(client=client, call=call)
    calls_table.save()


def parse_window24(data):
    # if not data['calls']:
    #     CallWindow.objects.filter(call_type='0').update(call_type='2')
    # else:
    #     for item in data['calls']:
    #         id_call = item["id"].split(".")[0]
    #         try:
    #             CallWindow.objects.get(id_call=id_call)
    #         except CallWindow.DoesNotExist:
    #             number_call = item["FROM"]["NUMBER"]
    #             if number_call in ('14', '15'):
    #                 continue
    #
    #             call = CallWindow.objects.create(
    #                 id_call=id_call,
    #                 number=number_call,
    #                 datetime=datetime.datetime.now(),
    #                 call_type=item["STATUS"]
    #             )
    #
    #             CallWindow.objects.filter(
    #                 id_call__in=CallWindow.objects.values('id_call').distinct()[1:]
    #             ).delete()
    #
    #             try:
    #                 number = Number.objects.get(number=number_call)
    #                 number_id = number.pk
    #             except Number.DoesNotExist:
    #                 number = Number.objects.create(number=number_call, name='new client')
    #                 number_id = number.pk
    #             try:
    #                 client = Client.objects.get(numbers=number)
    #                 client.calls.add(call)
    #             except Client.DoesNotExist:
    #                 client = Client.objects.create(author='system', name='new client')
    #                 client.numbers.add(number_id)
    #                 client.calls.add(call)
    #
    #             save_call_in_table(client=client, call=call)

    if not data['calls']:
        CallWindow.objects.filter(call_type='0').update(call_type='2')
    else:
        for item in data['calls']:
            id_call = item["id"].split(".")[0]  # add id only number and check record
            try:
                call = CallWindow.objects.get(id_call=id_call)  # if not record call id in db
            except CallWindow.DoesNotExist:
                number_call = item["FROM"]["NUMBER"]
                status = item["STATUS"]
                if not (number_call == '14') and not (number_call == '15'):
                    call = CallWindow.objects.create(id_call=id_call, number=number_call,
                                                     datetime=datetime.datetime.now(),
                                                     call_type=status)
                    call.save()
                    for id_call in CallWindow.objects.values_list('id_call', flat=True).distinct():
                        CallWindow.objects.filter(
                            pk__in=CallWindow.objects.filter(id_call=id_call).values_list('id', flat=True)[1:]).delete()
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

                    save_call_in_table(client=client, call=call)


# def parse_window24(data):
#     if not data["calls"]:
#         CallWindow.objects.filter(call_type='0').update(call_type='2')
#         print('ЗВОНКА НЕТ')
#     else:
#         print("ЗВОНОК ЕСТЬ")
#         for item in data["calls"]:
#             id_call = item["id"].split(".")[0]  # add id only number and check record
#             number_call = item["FROM"]["NUMBER"]
#             status = item["STATUS"]
#             check_call = Call.objects.filter(id_call=id_call)  # if not record call id in database
#             if not check_call:
#                 if not (number_call == '1') and not (number_call == '2'):
#                     # CallsTable.objects.get(client=client, call=call)
#                     try:
#                         number = Number.objects.get(number=number_call)
#                     except Number.DoesNotExist:
#                         number = Number.objects.create(number=number_call, name='new client')
#                     number_id = number.pk
#                     try:
#                         client = Client.objects.get(numbers=number)
#                         client_id = client.id
#                         # client_name = client.name
#                     except Client.DoesNotExist:
#                         client = Client.objects.create(author='system', name='new client')
#                         client.numbers.add(number_id)
#                         client_id = client.pk
#                         # client_name = 'new client'
#                     #
#                     call = Call.objects.create(id_call=id_call, number=number, datetime=datetime.datetime.now(),
#                                                call_type=status, client_id=client_id)
#                     client.calls.add(call.pk)  # TODO fix
#
#                     calls = Call.objects.filter(number=number_call).values('id').order_by('-id')
#                     ids_calls = calls.values_list('id', flat=True)
#
#                     for call_id in ids_calls:
#                         client.calls.add(call_id)
#
#                     calls_table = CallsTable.objects.create(client=client, call=call)
#                     calls_table.save()
#                     time.sleep(1)

# else:
#     Call.objects.filter(id_call=id_call).update(call_type=status)


def parse_okna360(data):
    if not data['calls']:
        pass
    else:
        for item in data['calls']:
            id_call = item["id"].split(".")[0]  # add id only number and check record
            check_call = CallOkna.objects.filter(id_call=id_call)  # if not record call id in db
            if not check_call:
                call = CallOkna(id_call=id_call)
                call.save()
                number = item["FROM"]["NUMBER"]
                if not (number == '1') and not (number == '2'):
                    response = requests.post(
                        f'https://okna360-crm.ru/ERPOKNA360/AddNewCalls.php?key=d41d8cd98f00b204e9800998ecf8427e&PhoneClient={number}')
                    # print(response)


def parse_active_calls():
    data = get_calls()
    parse_okna360(data)
    parse_window24(data)
