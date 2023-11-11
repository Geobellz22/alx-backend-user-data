#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if authentication is required"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return False


    def authorization_header(self, request=None) -> str:
        """Method to get the authorization header"""
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user"""
        return None
