# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foodlist.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66oodlist.proto\"7\n\x0f\x46oodListRequest\x12\x12\n\nrecipeList\x18\x01 \x03(\t\x12\x10\n\x08\x66oodList\x18\x02 \x03(\t\"(\n\x10\x46oodListResponse\x12\x14\n\x0cpurchaseList\x18\x01 \x01(\t2K\n\x0f\x46oodListService\x12\x38\n\x0fGetPurchaseList\x12\x10.FoodListRequest\x1a\x11.FoodListResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'foodlist_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FOODLISTREQUEST']._serialized_start=18
  _globals['_FOODLISTREQUEST']._serialized_end=73
  _globals['_FOODLISTRESPONSE']._serialized_start=75
  _globals['_FOODLISTRESPONSE']._serialized_end=115
  _globals['_FOODLISTSERVICE']._serialized_start=117
  _globals['_FOODLISTSERVICE']._serialized_end=192
# @@protoc_insertion_point(module_scope)
