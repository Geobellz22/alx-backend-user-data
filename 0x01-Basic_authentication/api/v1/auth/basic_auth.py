#!/usr/bin/env python3
"""
Basic Auth Class
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Base64 part from Authorization header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode Base64 Authorization header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            value = base64_authorization_header.encode('utf-8')
            decoded_value = base64.b64decode(value)
        except Exception:
            return None
