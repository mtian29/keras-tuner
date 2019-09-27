# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kerastuner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kerastuner.proto',
  package='kerastuner',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10kerastuner.proto\x12\nkerastuner\"\x82\x01\n\x05\x46loat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x02\x12\x11\n\tmax_value\x18\x03 \x01(\x02\x12\x0c\n\x04step\x18\x04 \x01(\x02\x12&\n\x08sampling\x18\x05 \x01(\x0e\x32\x14.kerastuner.Sampling\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\x02\"\x80\x01\n\x03Int\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x12\x12\x11\n\tmax_value\x18\x03 \x01(\x12\x12\x0c\n\x04step\x18\x04 \x01(\x12\x12&\n\x08sampling\x18\x05 \x01(\x0e\x32\x14.kerastuner.Sampling\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\x02\"\x88\x03\n\x06\x43hoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x0c\x66loat_values\x18\x02 \x01(\x0b\x32\x1e.kerastuner.Choice.FloatValuesH\x00\x12\x32\n\nint_values\x18\x03 \x01(\x0b\x32\x1c.kerastuner.Choice.IntValuesH\x00\x12\x38\n\rstring_values\x18\x04 \x01(\x0b\x32\x1f.kerastuner.Choice.StringValuesH\x00\x12\x15\n\x0bint_default\x18\x05 \x01(\x12H\x01\x12\x17\n\rfloat_default\x18\x06 \x01(\x02H\x01\x12\x18\n\x0estring_default\x18\x07 \x01(\tH\x01\x12\x0f\n\x07ordered\x18\x08 \x01(\x08\x1a\x1d\n\x0b\x46loatValues\x12\x0e\n\x06values\x18\x01 \x03(\x02\x1a\x1b\n\tIntValues\x12\x0e\n\x06values\x18\x01 \x03(\x12\x1a\x1e\n\x0cStringValues\x12\x0e\n\x06values\x18\x01 \x03(\tB\x08\n\x06valuesB\t\n\x07\x64\x65\x66\x61ult\"(\n\x07\x42oolean\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x08\"\x96\x05\n\x0fHyperParameters\x12&\n\x0b\x66loat_space\x18\x01 \x03(\x0b\x32\x11.kerastuner.Float\x12\"\n\tint_space\x18\x02 \x03(\x0b\x32\x0f.kerastuner.Int\x12(\n\x0c\x63hoice_space\x18\x03 \x03(\x0b\x32\x12.kerastuner.Choice\x12*\n\rboolean_space\x18\x04 \x03(\x0b\x32\x13.kerastuner.Boolean\x12\x42\n\x0c\x66loat_values\x18\x05 \x03(\x0b\x32,.kerastuner.HyperParameters.FloatValuesEntry\x12>\n\nint_values\x18\x06 \x03(\x0b\x32*.kerastuner.HyperParameters.IntValuesEntry\x12\x44\n\rstring_values\x18\x07 \x03(\x0b\x32-.kerastuner.HyperParameters.StringValuesEntry\x12\x46\n\x0e\x62oolean_values\x18\x08 \x03(\x0b\x32..kerastuner.HyperParameters.BooleanValuesEntry\x1a\x32\n\x10\x46loatValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x30\n\x0eIntValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x33\n\x11StringValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12\x42ooleanValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01*:\n\x08Sampling\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\x07\n\x03LOG\x10\x02\x12\x0f\n\x0bREVERSE_LOG\x10\x03\x62\x06proto3')
)

_SAMPLING = _descriptor.EnumDescriptor(
  name='Sampling',
  full_name='kerastuner.Sampling',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE_LOG', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1398,
  serialized_end=1456,
)
_sym_db.RegisterEnumDescriptor(_SAMPLING)

Sampling = enum_type_wrapper.EnumTypeWrapper(_SAMPLING)
NONE = 0
LINEAR = 1
LOG = 2
REVERSE_LOG = 3



_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='kerastuner.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Float.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='kerastuner.Float.min_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='kerastuner.Float.max_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.Float.step', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='kerastuner.Float.sampling', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Float.default', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=163,
)


_INT = _descriptor.Descriptor(
  name='Int',
  full_name='kerastuner.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Int.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='kerastuner.Int.min_value', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='kerastuner.Int.max_value', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.Int.step', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='kerastuner.Int.sampling', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Int.default', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=294,
)


_CHOICE_FLOATVALUES = _descriptor.Descriptor(
  name='FloatValues',
  full_name='kerastuner.Choice.FloatValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='kerastuner.Choice.FloatValues.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=607,
)

_CHOICE_INTVALUES = _descriptor.Descriptor(
  name='IntValues',
  full_name='kerastuner.Choice.IntValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='kerastuner.Choice.IntValues.values', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=636,
)

_CHOICE_STRINGVALUES = _descriptor.Descriptor(
  name='StringValues',
  full_name='kerastuner.Choice.StringValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='kerastuner.Choice.StringValues.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=668,
)

_CHOICE = _descriptor.Descriptor(
  name='Choice',
  full_name='kerastuner.Choice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Choice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_values', full_name='kerastuner.Choice.float_values', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_values', full_name='kerastuner.Choice.int_values', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_values', full_name='kerastuner.Choice.string_values', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_default', full_name='kerastuner.Choice.int_default', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_default', full_name='kerastuner.Choice.float_default', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_default', full_name='kerastuner.Choice.string_default', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordered', full_name='kerastuner.Choice.ordered', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHOICE_FLOATVALUES, _CHOICE_INTVALUES, _CHOICE_STRINGVALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='values', full_name='kerastuner.Choice.values',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='default', full_name='kerastuner.Choice.default',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=297,
  serialized_end=689,
)


_BOOLEAN = _descriptor.Descriptor(
  name='Boolean',
  full_name='kerastuner.Boolean',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Boolean.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Boolean.default', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=731,
)


_HYPERPARAMETERS_FLOATVALUESENTRY = _descriptor.Descriptor(
  name='FloatValuesEntry',
  full_name='kerastuner.HyperParameters.FloatValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.HyperParameters.FloatValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.HyperParameters.FloatValuesEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1189,
  serialized_end=1239,
)

_HYPERPARAMETERS_INTVALUESENTRY = _descriptor.Descriptor(
  name='IntValuesEntry',
  full_name='kerastuner.HyperParameters.IntValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.HyperParameters.IntValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.HyperParameters.IntValuesEntry.value', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1241,
  serialized_end=1289,
)

_HYPERPARAMETERS_STRINGVALUESENTRY = _descriptor.Descriptor(
  name='StringValuesEntry',
  full_name='kerastuner.HyperParameters.StringValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.HyperParameters.StringValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.HyperParameters.StringValuesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1291,
  serialized_end=1342,
)

_HYPERPARAMETERS_BOOLEANVALUESENTRY = _descriptor.Descriptor(
  name='BooleanValuesEntry',
  full_name='kerastuner.HyperParameters.BooleanValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.HyperParameters.BooleanValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.HyperParameters.BooleanValuesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1344,
  serialized_end=1396,
)

_HYPERPARAMETERS = _descriptor.Descriptor(
  name='HyperParameters',
  full_name='kerastuner.HyperParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_space', full_name='kerastuner.HyperParameters.float_space', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_space', full_name='kerastuner.HyperParameters.int_space', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choice_space', full_name='kerastuner.HyperParameters.choice_space', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_space', full_name='kerastuner.HyperParameters.boolean_space', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_values', full_name='kerastuner.HyperParameters.float_values', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_values', full_name='kerastuner.HyperParameters.int_values', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_values', full_name='kerastuner.HyperParameters.string_values', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_values', full_name='kerastuner.HyperParameters.boolean_values', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HYPERPARAMETERS_FLOATVALUESENTRY, _HYPERPARAMETERS_INTVALUESENTRY, _HYPERPARAMETERS_STRINGVALUESENTRY, _HYPERPARAMETERS_BOOLEANVALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=1396,
)

_FLOAT.fields_by_name['sampling'].enum_type = _SAMPLING
_INT.fields_by_name['sampling'].enum_type = _SAMPLING
_CHOICE_FLOATVALUES.containing_type = _CHOICE
_CHOICE_INTVALUES.containing_type = _CHOICE
_CHOICE_STRINGVALUES.containing_type = _CHOICE
_CHOICE.fields_by_name['float_values'].message_type = _CHOICE_FLOATVALUES
_CHOICE.fields_by_name['int_values'].message_type = _CHOICE_INTVALUES
_CHOICE.fields_by_name['string_values'].message_type = _CHOICE_STRINGVALUES
_CHOICE.oneofs_by_name['values'].fields.append(
  _CHOICE.fields_by_name['float_values'])
_CHOICE.fields_by_name['float_values'].containing_oneof = _CHOICE.oneofs_by_name['values']
_CHOICE.oneofs_by_name['values'].fields.append(
  _CHOICE.fields_by_name['int_values'])
_CHOICE.fields_by_name['int_values'].containing_oneof = _CHOICE.oneofs_by_name['values']
_CHOICE.oneofs_by_name['values'].fields.append(
  _CHOICE.fields_by_name['string_values'])
_CHOICE.fields_by_name['string_values'].containing_oneof = _CHOICE.oneofs_by_name['values']
_CHOICE.oneofs_by_name['default'].fields.append(
  _CHOICE.fields_by_name['int_default'])
_CHOICE.fields_by_name['int_default'].containing_oneof = _CHOICE.oneofs_by_name['default']
_CHOICE.oneofs_by_name['default'].fields.append(
  _CHOICE.fields_by_name['float_default'])
_CHOICE.fields_by_name['float_default'].containing_oneof = _CHOICE.oneofs_by_name['default']
_CHOICE.oneofs_by_name['default'].fields.append(
  _CHOICE.fields_by_name['string_default'])
_CHOICE.fields_by_name['string_default'].containing_oneof = _CHOICE.oneofs_by_name['default']
_HYPERPARAMETERS_FLOATVALUESENTRY.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS_INTVALUESENTRY.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS_STRINGVALUESENTRY.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS_BOOLEANVALUESENTRY.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS.fields_by_name['float_space'].message_type = _FLOAT
_HYPERPARAMETERS.fields_by_name['int_space'].message_type = _INT
_HYPERPARAMETERS.fields_by_name['choice_space'].message_type = _CHOICE
_HYPERPARAMETERS.fields_by_name['boolean_space'].message_type = _BOOLEAN
_HYPERPARAMETERS.fields_by_name['float_values'].message_type = _HYPERPARAMETERS_FLOATVALUESENTRY
_HYPERPARAMETERS.fields_by_name['int_values'].message_type = _HYPERPARAMETERS_INTVALUESENTRY
_HYPERPARAMETERS.fields_by_name['string_values'].message_type = _HYPERPARAMETERS_STRINGVALUESENTRY
_HYPERPARAMETERS.fields_by_name['boolean_values'].message_type = _HYPERPARAMETERS_BOOLEANVALUESENTRY
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
DESCRIPTOR.message_types_by_name['Int'] = _INT
DESCRIPTOR.message_types_by_name['Choice'] = _CHOICE
DESCRIPTOR.message_types_by_name['Boolean'] = _BOOLEAN
DESCRIPTOR.message_types_by_name['HyperParameters'] = _HYPERPARAMETERS
DESCRIPTOR.enum_types_by_name['Sampling'] = _SAMPLING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT,
  '__module__' : 'kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Float)
  })
_sym_db.RegisterMessage(Float)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), {
  'DESCRIPTOR' : _INT,
  '__module__' : 'kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Int)
  })
_sym_db.RegisterMessage(Int)

Choice = _reflection.GeneratedProtocolMessageType('Choice', (_message.Message,), {

  'FloatValues' : _reflection.GeneratedProtocolMessageType('FloatValues', (_message.Message,), {
    'DESCRIPTOR' : _CHOICE_FLOATVALUES,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.Choice.FloatValues)
    })
  ,

  'IntValues' : _reflection.GeneratedProtocolMessageType('IntValues', (_message.Message,), {
    'DESCRIPTOR' : _CHOICE_INTVALUES,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.Choice.IntValues)
    })
  ,

  'StringValues' : _reflection.GeneratedProtocolMessageType('StringValues', (_message.Message,), {
    'DESCRIPTOR' : _CHOICE_STRINGVALUES,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.Choice.StringValues)
    })
  ,
  'DESCRIPTOR' : _CHOICE,
  '__module__' : 'kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Choice)
  })
_sym_db.RegisterMessage(Choice)
_sym_db.RegisterMessage(Choice.FloatValues)
_sym_db.RegisterMessage(Choice.IntValues)
_sym_db.RegisterMessage(Choice.StringValues)

Boolean = _reflection.GeneratedProtocolMessageType('Boolean', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEAN,
  '__module__' : 'kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Boolean)
  })
_sym_db.RegisterMessage(Boolean)

HyperParameters = _reflection.GeneratedProtocolMessageType('HyperParameters', (_message.Message,), {

  'FloatValuesEntry' : _reflection.GeneratedProtocolMessageType('FloatValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_FLOATVALUESENTRY,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.FloatValuesEntry)
    })
  ,

  'IntValuesEntry' : _reflection.GeneratedProtocolMessageType('IntValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_INTVALUESENTRY,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.IntValuesEntry)
    })
  ,

  'StringValuesEntry' : _reflection.GeneratedProtocolMessageType('StringValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_STRINGVALUESENTRY,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.StringValuesEntry)
    })
  ,

  'BooleanValuesEntry' : _reflection.GeneratedProtocolMessageType('BooleanValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_BOOLEANVALUESENTRY,
    '__module__' : 'kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.BooleanValuesEntry)
    })
  ,
  'DESCRIPTOR' : _HYPERPARAMETERS,
  '__module__' : 'kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters)
  })
_sym_db.RegisterMessage(HyperParameters)
_sym_db.RegisterMessage(HyperParameters.FloatValuesEntry)
_sym_db.RegisterMessage(HyperParameters.IntValuesEntry)
_sym_db.RegisterMessage(HyperParameters.StringValuesEntry)
_sym_db.RegisterMessage(HyperParameters.BooleanValuesEntry)


_HYPERPARAMETERS_FLOATVALUESENTRY._options = None
_HYPERPARAMETERS_INTVALUESENTRY._options = None
_HYPERPARAMETERS_STRINGVALUESENTRY._options = None
_HYPERPARAMETERS_BOOLEANVALUESENTRY._options = None
# @@protoc_insertion_point(module_scope)
