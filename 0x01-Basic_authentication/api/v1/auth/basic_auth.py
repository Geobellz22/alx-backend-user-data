#!/usr/bin/env python3
"""
Basic Auth Class
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""
    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Extract Base64 part from Authorization header"""
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        if not base64_authorization_header.startswith("Basic "):
            return None
        base64_part = base64_authorization_header[len("Basic "):].strip()
        return base64_part
