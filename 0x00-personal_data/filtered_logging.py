#!/usr/bin/env python3
"""A module for filtering logs
"""

import re
from typing import List



 def filter_datum(fields: str,
                  redaction: str,
                  message: str,
                  separator: str) -> str:
    """returns the log message obsfuscated"""
    return re.sub(f'({separator})({separator.join(fields)})',
                  f'\\1{redaction}', message)
