import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from todo_app.app import create_app


class HttpApiTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_full_crud(self):
        self.assertEqual(self.client.get("/todos").json, [])
        response = self.client.post("/todos", json={"title": "  Read book  "})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Location"], "/todos/1")
        self.assertEqual(response.json, {"id": 1, "title": "Read book", "completed": False})
        self.assertEqual(self.client.get("/todos/1").json["title"], "Read book")
        response = self.client.patch("/todos/1", json={"title": "Write tests", "completed": True})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["completed"])
        self.assertEqual(self.client.delete("/todos/1").status_code, 204)
        self.assertEqual(self.client.get("/todos").json, [])
        self.assertEqual(self.client.get("/todos/1").status_code, 404)

    def test_missing_ids(self):
        for method in ("get", "patch", "delete"):
            kwargs = {"json": {"completed": True}} if method == "patch" else {}
            response = getattr(self.client, method)("/todos/99", **kwargs)
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json["error"], "todo not found")

    def test_invalid_create(self):
        for body in ({}, [], None, {"title": ""}, {"title": 2}, {"title": "x", "id": 9}):
            with self.subTest(body=body):
                response = self.client.post("/todos", data=__import__("json").dumps(body),
                                            content_type="application/json")
                self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.get("/todos").json, [])

    def test_invalid_patch_is_atomic(self):
        self.client.post("/todos", json={"title": "original"})
        for body in ({}, {"unknown": 1}, {"completed": 1}, {"title": "changed", "completed": "yes"}):
            self.assertEqual(self.client.patch("/todos/1", json=body).status_code, 400)
            self.assertEqual(self.client.get("/todos/1").json["title"], "original")

    def test_non_json_and_malformed(self):
        self.assertEqual(self.client.post("/todos", data="hello").status_code, 415)
        self.assertEqual(self.client.post("/todos", data="{", content_type="application/json").status_code, 400)

    def test_apps_have_separate_stores(self):
        self.client.post("/todos", json={"title": "private"})
        self.assertEqual(create_app().test_client().get("/todos").json, [])

if __name__ == "__main__":
    unittest.main()
