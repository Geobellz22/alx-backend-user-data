#!/usr/bin/env python3
"""Basic Auth Class"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""
    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """extract_base64_authorization_header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startwith("Basic"):
            return None
