protoc -I=simple --python_out=simple ./simple/simple.proto
protoc -I=enums --python_out=enums ./enums/enum_example.proto
protoc -I=complex --python_out=complex ./complex/complex.proto
protoc -I=addressbook --python_out=addressbook ./addressbook/addressbook.proto