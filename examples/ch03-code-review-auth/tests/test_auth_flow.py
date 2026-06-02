from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from auth_demo import AuthService


class AuthFlowTests(unittest.TestCase):
    def test_login_and_authenticate_request(self) -> None:
        service = AuthService()
        service.create_user("u_1", "reader@example.com", "old-secret")

        token = service.login("reader@example.com", "old-secret")

        self.assertIsNotNone(token)
        user = service.authenticate_request(token or "")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "reader@example.com")

    def test_disabled_user_cannot_login(self) -> None:
        service = AuthService()
        service.create_user("u_1", "reader@example.com", "old-secret", disabled=True)

        token = service.login("reader@example.com", "old-secret")

        self.assertIsNone(token)

    def test_change_password_rejects_old_password_and_accepts_new_password(self) -> None:
        service = AuthService()
        service.create_user("u_1", "reader@example.com", "old-secret")

        changed = service.change_password("u_1", "old-secret", "new-secret")
        old_token = service.login("reader@example.com", "old-secret")
        new_token = service.login("reader@example.com", "new-secret")

        self.assertTrue(changed)
        self.assertIsNone(old_token)
        self.assertIsNotNone(new_token)

    def test_logout_invalidates_session(self) -> None:
        service = AuthService()
        service.create_user("u_1", "reader@example.com", "old-secret")
        token = service.login("reader@example.com", "old-secret")
        self.assertIsNotNone(token)

        service.logout(token or "")

        self.assertIsNone(service.authenticate_request(token or ""))


if __name__ == "__main__":
    unittest.main()
