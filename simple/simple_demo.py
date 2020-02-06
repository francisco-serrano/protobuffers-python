import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()
simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "this is a simple message"

sample_list = simple_message.sample_list
sample_list.append(3)
sample_list.append(4)
sample_list.append(5)

with open('simple.bin', mode='wb') as f:
    print('write as binary')
    bytes_as_string = simple_message.SerializeToString()
    f.write(bytes_as_string)

with open('simple.bin', mode='rb') as f:
    print('read values')
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(simple_message_read)
