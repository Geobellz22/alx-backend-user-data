#!/usr/bin/env python3
"""
Basic Auth Class
"""

from api.v1.auth.auth import Auth
import base64
from model.user import User


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header method"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode_base64_authorization_header method"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            value = base64_authorization_header.encode('utf-8')
            decoded_value = base64.b64decode(value)
            return decoded_value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user email and password from decoded Base64 header"""
        if decoded_base64_authorization_header is None:
            return None
        if type(decoded_base_64_authorization_header) is not str:
            return None
        if ":" not in decoded_base_64authorization_header:
            return None None
        user_email, password = decoded_base64_authorization_header.split(":")
        return (user_email, password)
