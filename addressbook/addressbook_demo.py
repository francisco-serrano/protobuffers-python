import addressbook.addressbook_pb2 as addressbook_pb2

from google.protobuf.json_format import MessageToJson


def new_phone_number(number, phone_type):
    return addressbook_pb2.Person.PhoneNumber(number=number, type=phone_type)


def new_person(name, person_id, email, phones):
    return addressbook_pb2.Person(name=name, id=person_id, email=email, phones=phones)


def new_address_book(people):
    return addressbook_pb2.AddressBook(people=people)


def write_address_book(address_book, filename):
    with open(filename, mode='wb') as f:
        bytes_as_string = address_book.SerializeToString()
        f.write(bytes_as_string)


def read_address_book(filename):
    with open(filename, mode='rb') as f:
        return addressbook_pb2.AddressBook().FromString(f.read())


def get_as_json(address_book):
    return MessageToJson(address_book)


my_address_book = new_address_book(people=[
    new_person('Tommy Vercetti', 1, 'tommy.vercetti@gmail.com', phones=[
        new_phone_number('123-456-7890', addressbook_pb2.Person.HOME),
        new_phone_number('098-765-4321', addressbook_pb2.Person.WORK)
    ]),
    new_person('Carl Johnson', 2, 'carl.johnson@gmail.com', phones=[
        new_phone_number('123-456-7890', addressbook_pb2.Person.HOME),
        new_phone_number('098-765-4321', addressbook_pb2.Person.WORK)
    ]),
    new_person('Niko Bellic', 3, 'niko.bellic@gmail.com', phones=[
        new_phone_number('123-456-7890', addressbook_pb2.Person.HOME),
        new_phone_number('098-765-4321', addressbook_pb2.Person.WORK)
    ])
])

print(my_address_book)

write_address_book(my_address_book, 'addressbook.bin')

same_address_book = read_address_book('addressbook.bin')

print(same_address_book)

print(get_as_json(same_address_book))
