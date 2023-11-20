#!/usr/bin/env python3
"""authentication"""

import bcrypt
from user import User
from db import DB
import uuid
from sqlalchemy.orm.exc import NoResultFound
fromm typing import User


def _hash_password(password: str) -> bytes:
    """Hash input password."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """Generate and return a string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            password_hash = _hash_password(password)
            return self._db.add_user(email, password_hash)
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login."""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(password.encode
                                      ("utf-8"), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for the user."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Get user from session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

        return user
