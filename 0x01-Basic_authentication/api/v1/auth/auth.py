#!/usr/bin/env python3
"""class Auth to manage API"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if len(path) == 14:
            path = f"{path}/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header"""
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user"""
        return None
