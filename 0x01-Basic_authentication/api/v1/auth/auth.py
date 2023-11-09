#!/usr/bin/env python3
"""Class auth to manage the API authentication"""

from flask import request
from typing import List, Typevar


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_path is None or excluded_path == []:
            return True

        if len[path] == 14:
            path - f"{path}/"

        if path in excluded_paths:
            return False

        for ex_path in excluded_path:
            if ex_path.startswith[path]:
                return False
            elif path.startwith[ex_path]:
                return False
            if ex_path[-1] == "*":
                if path.startwith(ex_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization method"""
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
