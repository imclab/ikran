# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='test.proto',
  package='sync_pb',
  serialized_pb='\n\ntest.proto\x12\x07sync_pb\"!\n\x12UnknownFieldsTestA\x12\x0b\n\x03\x66oo\x18\x01 \x02(\x08\".\n\x12UnknownFieldsTestB\x12\x0b\n\x03\x66oo\x18\x01 \x02(\x08\x12\x0b\n\x03\x62\x61r\x18\x02 \x02(\x08\x42\x04H\x03X\x01')




_UNKNOWNFIELDSTESTA = descriptor.Descriptor(
  name='UnknownFieldsTestA',
  full_name='sync_pb.UnknownFieldsTestA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='foo', full_name='sync_pb.UnknownFieldsTestA.foo', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=56,
)


_UNKNOWNFIELDSTESTB = descriptor.Descriptor(
  name='UnknownFieldsTestB',
  full_name='sync_pb.UnknownFieldsTestB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='foo', full_name='sync_pb.UnknownFieldsTestB.foo', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bar', full_name='sync_pb.UnknownFieldsTestB.bar', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['UnknownFieldsTestA'] = _UNKNOWNFIELDSTESTA
DESCRIPTOR.message_types_by_name['UnknownFieldsTestB'] = _UNKNOWNFIELDSTESTB

class UnknownFieldsTestA(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNKNOWNFIELDSTESTA
  
  # @@protoc_insertion_point(class_scope:sync_pb.UnknownFieldsTestA)

class UnknownFieldsTestB(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNKNOWNFIELDSTESTB
  
  # @@protoc_insertion_point(class_scope:sync_pb.UnknownFieldsTestB)

# @@protoc_insertion_point(module_scope)