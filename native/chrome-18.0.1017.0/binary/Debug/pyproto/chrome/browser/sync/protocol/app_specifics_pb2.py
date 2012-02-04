# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import sync_pb2
import extension_specifics_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='app_specifics.proto',
  package='sync_pb',
  serialized_pb='\n\x13\x61pp_specifics.proto\x12\x07sync_pb\x1a\nsync.proto\x1a\x19\x65xtension_specifics.proto\"`\n\x17\x41ppNotificationSettings\x12\x1a\n\x12initial_setup_done\x18\x01 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\x17\n\x0foauth_client_id\x18\x03 \x01(\t\"\xb1\x01\n\x0c\x41ppSpecifics\x12.\n\textension\x18\x01 \x01(\x0b\x32\x1b.sync_pb.ExtensionSpecifics\x12?\n\x15notification_settings\x18\x02 \x01(\x0b\x32 .sync_pb.AppNotificationSettings\x12\x1a\n\x12\x61pp_launch_ordinal\x18\x03 \x01(\t\x12\x14\n\x0cpage_ordinal\x18\x04 \x01(\t:>\n\x03\x61pp\x12\x18.sync_pb.EntitySpecifics\x18\xec\xf9\x02 \x01(\x0b\x32\x15.sync_pb.AppSpecificsB\x04H\x03X\x01')


APP_FIELD_NUMBER = 48364
app = descriptor.FieldDescriptor(
  name='app', full_name='sync_pb.app', index=0,
  number=48364, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_APPNOTIFICATIONSETTINGS = descriptor.Descriptor(
  name='AppNotificationSettings',
  full_name='sync_pb.AppNotificationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='initial_setup_done', full_name='sync_pb.AppNotificationSettings.initial_setup_done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='disabled', full_name='sync_pb.AppNotificationSettings.disabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='oauth_client_id', full_name='sync_pb.AppNotificationSettings.oauth_client_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=71,
  serialized_end=167,
)


_APPSPECIFICS = descriptor.Descriptor(
  name='AppSpecifics',
  full_name='sync_pb.AppSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='extension', full_name='sync_pb.AppSpecifics.extension', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notification_settings', full_name='sync_pb.AppSpecifics.notification_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='app_launch_ordinal', full_name='sync_pb.AppSpecifics.app_launch_ordinal', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page_ordinal', full_name='sync_pb.AppSpecifics.page_ordinal', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=170,
  serialized_end=347,
)

_APPSPECIFICS.fields_by_name['extension'].message_type = extension_specifics_pb2._EXTENSIONSPECIFICS
_APPSPECIFICS.fields_by_name['notification_settings'].message_type = _APPNOTIFICATIONSETTINGS
DESCRIPTOR.message_types_by_name['AppNotificationSettings'] = _APPNOTIFICATIONSETTINGS
DESCRIPTOR.message_types_by_name['AppSpecifics'] = _APPSPECIFICS

class AppNotificationSettings(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPNOTIFICATIONSETTINGS
  
  # @@protoc_insertion_point(class_scope:sync_pb.AppNotificationSettings)

class AppSpecifics(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPSPECIFICS
  
  # @@protoc_insertion_point(class_scope:sync_pb.AppSpecifics)

app.message_type = _APPSPECIFICS
sync_pb2.EntitySpecifics.RegisterExtension(app)
# @@protoc_insertion_point(module_scope)