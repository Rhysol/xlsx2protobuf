# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hero.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hero.proto',
  package='TableProto',
  syntax='proto3',
  serialized_pb=_b('\n\nhero.proto\x12\nTableProto\"\xf6\x03\n\x04hero\x12\x0b\n\x03i_d\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08initials\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x03\x12\r\n\x05level\x18\x05 \x01(\x03\x12\x12\n\nbase_skill\x18\x06 \x01(\x03\x12\x0e\n\x06\x62\x61ttle\x18\x07 \x01(\x03\x12\x0f\n\x07\x64\x65velop\x18\x08 \x01(\x03\x12\x11\n\tauxiliary\x18\t \x01(\x03\x12\x13\n\x0b\x62\x61ttle_base\x18\n \x01(\x03\x12\x14\n\x0c\x64\x65velop_base\x18\x0b \x01(\x03\x12\x16\n\x0e\x61uxiliary_base\x18\x0c \x01(\x03\x12\x13\n\x0b\x62\x61ttle_step\x18\r \x01(\x03\x12\x14\n\x0c\x64\x65velop_step\x18\x0e \x01(\x03\x12\x16\n\x0e\x61uxiliary_step\x18\x0f \x01(\x03\x12\x14\n\x0c\x62\x61ttle_extra\x18\x10 \x01(\x03\x12\x15\n\rdevelop_extra\x18\x11 \x01(\x03\x12\x17\n\x0f\x61uxiliary_extra\x18\x12 \x01(\x03\x12\x10\n\x08item_i_d\x18\x13 \x01(\x03\x12\x12\n\nitem_count\x18\x14 \x01(\x03\x12\x19\n\x11\x65xchange_item_i_d\x18\x15 \x01(\x03\x12\x0b\n\x03tab\x18\x16 \x01(\t\x12\x0b\n\x03\x64\x65s\x18\x17 \x01(\t\x12\x0b\n\x03pic\x18\x18 \x01(\x03\x12\x11\n\tshow_hero\x18\x19 \x01(\x03\x12\x15\n\rrecomme_skill\x18\x1a \x03(\x03\x62\x06proto3')
)




_HERO = _descriptor.Descriptor(
  name='hero',
  full_name='TableProto.hero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i_d', full_name='TableProto.hero.i_d', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='TableProto.hero.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initials', full_name='TableProto.hero.initials', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='TableProto.hero.type', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='TableProto.hero.level', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_skill', full_name='TableProto.hero.base_skill', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle', full_name='TableProto.hero.battle', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='develop', full_name='TableProto.hero.develop', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auxiliary', full_name='TableProto.hero.auxiliary', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_base', full_name='TableProto.hero.battle_base', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='develop_base', full_name='TableProto.hero.develop_base', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auxiliary_base', full_name='TableProto.hero.auxiliary_base', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_step', full_name='TableProto.hero.battle_step', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='develop_step', full_name='TableProto.hero.develop_step', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auxiliary_step', full_name='TableProto.hero.auxiliary_step', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_extra', full_name='TableProto.hero.battle_extra', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='develop_extra', full_name='TableProto.hero.develop_extra', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auxiliary_extra', full_name='TableProto.hero.auxiliary_extra', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_i_d', full_name='TableProto.hero.item_i_d', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_count', full_name='TableProto.hero.item_count', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange_item_i_d', full_name='TableProto.hero.exchange_item_i_d', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tab', full_name='TableProto.hero.tab', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='des', full_name='TableProto.hero.des', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pic', full_name='TableProto.hero.pic', index=23,
      number=24, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_hero', full_name='TableProto.hero.show_hero', index=24,
      number=25, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recomme_skill', full_name='TableProto.hero.recomme_skill', index=25,
      number=26, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=529,
)

DESCRIPTOR.message_types_by_name['hero'] = _HERO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

hero = _reflection.GeneratedProtocolMessageType('hero', (_message.Message,), dict(
  DESCRIPTOR = _HERO,
  __module__ = 'hero_pb2'
  # @@protoc_insertion_point(class_scope:TableProto.hero)
  ))
_sym_db.RegisterMessage(hero)


# @@protoc_insertion_point(module_scope)
