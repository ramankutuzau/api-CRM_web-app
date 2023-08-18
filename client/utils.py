from call.models import CallWindow
from client.models import Client, Number, Address


def create_number_record(number,name):
    try:
        number_id = Number.objects.get(number=number).id
        return number_id
    except Number.DoesNotExist:
        num = Number.objects.create(number=number, name=name)
        num.save()
        return num.id


def create_calls_record(number_id):
    number = Number.objects.get(id=number_id)
    calls = CallWindow.objects.filter(number=number).values('id').order_by('-id')
    ids = calls.values_list('id', flat=True)
    return ids


def create_address_record(address):
    try:
        address_id = Address.objects.get(name=address).id
        return address_id
    except Address.DoesNotExist:
        address = Address.objects.create(name=address)
        address.save()
        return address.id


# def add_calls_to_client(Client):
#     id_client = Client.objects.filter(id='id')
