#!/usr/bin/env python3
"""filter logger"""

import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message

