import enums.enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 345
enum_message.day_of_the_week = enum_example_pb2.THURSDAY


print(enum_message)
print(enum_message.day_of_the_week == enum_example_pb2.THURSDAY)

with open('enums.bin', mode='wb') as f:
    f.write(enum_message.SerializeToString())
    print('content written to file')

with open('enums.bin', mode='rb') as f:
    enum_message_read = enum_example_pb2.EnumMessage().FromString(f.read())
    print('content read', enum_message_read)
