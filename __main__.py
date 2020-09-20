#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Chaucha python tools
"""
from dotenv import load_dotenv
from chaucha import opreturn
from os import getenv

load_dotenv()

if __name__ == "__main__":

    privkey = getenv("PRIVATE_KEY")
    pubkey = getenv("PUBLIC_KEY")
    sendto = getenv("SEND_TO_PUBLIC_KEY")

    print(opreturn.send(privkey, pubkey, sendto, message="Hello World", force=True))
