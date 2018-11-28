# -*- coding: (utf8 -*-
from modules.permissions import *
from modules.quote import *
from modules.add_user import add_user

modules = {
    "add" : (add_user, [MESSAGE_THREADID,
                       MESSAGE_AUTHOR,
                       FN_ADDUSER]),
    "quote": (imagequote, [MESSAGE_THREADID,
                           FN_SEND_IMAGE]),
    "reroll": (reroll, [MESSAGE_THREADID,
                        FN_SEND_IMAGE]),
    "requote": (requote, [MESSAGE_THREADID,
                          FN_SEND_IMAGE]),
    "savequote": (savequote, [MESSAGE_THREADID]),
    "quotes": (quotes, [MESSAGE_THREADID]),
    "quoteboard": (quoteboard, [MESSAGE_THREADID,
                                FN_SEND_IMAGE]),
    "newquoteboard": (refresh_quoteboard, [MESSAGE_THREADID,
                                           FN_SEND_IMAGE]),
    "lastphoto": (photo, [MESSAGE_THREADID,
                          FN_SEND_IMAGE])
}

tag = {}