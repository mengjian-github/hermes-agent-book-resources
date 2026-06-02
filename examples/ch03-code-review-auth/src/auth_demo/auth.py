from __future__ import annotations

import hashlib
import secrets
import time
from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    password_hash: str
    disabled: bool = False


@dataclass
class Session:
    token: str
    user_id: str
    expires_at: float


class AuthService:
    def __init__(self, session_ttl_seconds: int = 3600) -> None:
        self.session_ttl_seconds = session_ttl_seconds
        self.users: dict[str, User] = {}
        self.sessions: dict[str, Session] = {}

    def create_user(self, user_id: str, email: str, password: str, disabled: bool = False) -> User:
        user = User(
            id=user_id,
            email=email,
            password_hash=self._hash_password(password),
            disabled=disabled,
        )
        self.users[user_id] = user
        return user

    def login(self, email: str, password: str) -> str | None:
        user = self._find_user_by_email(email)
        if user is None or user.disabled:
            return None
        if user.password_hash != self._hash_password(password):
            return None

        token = secrets.token_urlsafe(24)
        self.sessions[token] = Session(
            token=token,
            user_id=user.id,
            expires_at=time.time() + self.session_ttl_seconds,
        )
        return token

    def authenticate_request(self, token: str) -> User | None:
        session = self.sessions.get(token)
        if session is None:
            return None
        if session.expires_at <= time.time():
            self.sessions.pop(token, None)
            return None

        user = self.users.get(session.user_id)
        if user is None or user.disabled:
            return None
        return user

    def change_password(self, user_id: str, old_password: str, new_password: str) -> bool:
        user = self.users.get(user_id)
        if user is None or user.disabled:
            return False
        if user.password_hash != self._hash_password(old_password):
            return False

        user.password_hash = self._hash_password(new_password)
        # Regression risk for review: this keeps existing sessions alive after
        # a credential change. The book example asks Hermes to catch this.
        return True

    def logout(self, token: str) -> None:
        self.sessions.pop(token, None)

    def _find_user_by_email(self, email: str) -> User | None:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
