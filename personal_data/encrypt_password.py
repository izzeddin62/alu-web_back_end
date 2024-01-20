#!/usr/bin/env python3
""" encrypt password """

import bcrypt

def hash_password(password: str):
    """ encrypt password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())