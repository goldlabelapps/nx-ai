from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

_TABLES = [
    "github_accounts",
    "github_repos",
    "github_gists",
    "github_projects",
    "github_resources",
]


class _MockCursor:
    def __init__(self, fetchone_values, fetchall_values=None):
        self._fetchone_values = list(fetchone_values)
        self._fetchall_values = list(fetchall_values or [])
        self.executed = []
        self.description = [("id",), ("name",)]

    def execute(self, query, params=None):
        self.executed.append((query, params))

    def fetchone(self):
        if self._fetchone_values:
            return self._fetchone_values.pop(0)
        return None

    def fetchall(self):
        if self._fetchall_values:
            return self._fetchall_values.pop(0)
        return []

    def close(self):
        pass


class _MockConnection:
    def __init__(self, fetchone_values, fetchall_values=None):
        self.cursor_obj = _MockCursor(fetchone_values, fetchall_values)
        self.committed = False
        self.rolled_back = False

    def cursor(self):
        return self.cursor_obj

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        pass


# ---------------------------------------------------------------------------
# GET /github
# ---------------------------------------------------------------------------

def test_github_get_returns_all_tables(monkeypatch):
    # One COUNT fetchone per table, one fetchall of rows per table.
    conn = _MockConnection(
        fetchone_values=[(3,), (7,), (0,), (1,), (2,)],
        fetchall_values=[
            [(1, "Alex Milky")],   # github_accounts rows
            [(10, "fastapi-starter")],  # github_repos rows
            [],                         # github_gists rows (empty)
            [(30, "API Roadmap 2026")],  # github_projects rows
            [(40, "some resource")],     # github_resources rows
        ],
    )

    from app.api.github import github as github_module

    monkeypatch.setattr(github_module, "get_db_connection_direct", lambda: conn)

    response = client.get("/github")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["severity"] == "success"
    assert set(payload["data"].keys()) == set(_TABLES)

    assert payload["data"]["github_accounts"]["count"] == 3
    assert payload["data"]["github_repos"]["count"] == 7
    assert payload["data"]["github_gists"]["count"] == 0
    assert payload["data"]["github_gists"]["rows"] == []
    assert payload["data"]["github_projects"]["count"] == 1
    assert payload["data"]["github_resources"]["count"] == 2


def test_github_get_returns_error_on_db_failure(monkeypatch):
    from app.api.github import github as github_module

    monkeypatch.setattr(
        github_module,
        "get_db_connection_direct",
        lambda: (_ for _ in ()).throw(Exception("connection refused")),
    )

    response = client.get("/github")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["severity"] == "error"
    assert payload["data"] == {}


# ---------------------------------------------------------------------------
# POST /api/github/empty
# ---------------------------------------------------------------------------

def test_github_empty_truncates_all_tables(monkeypatch):
    conn = _MockConnection(fetchone_values=[])

    from app.api.github.sql import empty_tables as empty_module

    monkeypatch.setattr(empty_module, "get_db_connection_direct", lambda: conn)

    response = client.post("/api/github/empty")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["severity"] == "success"
    assert set(payload["data"]["tables"]) == set(_TABLES)
    assert conn.committed is True


# ---------------------------------------------------------------------------
# POST /api/github/createtable
# ---------------------------------------------------------------------------

def test_github_create_tables_succeeds(monkeypatch):
    conn = _MockConnection(fetchone_values=[])

    from app.api.github.sql import create_tables as create_module

    monkeypatch.setattr(create_module, "get_db_connection_direct", lambda: conn)

    response = client.post("/api/github/createtable")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["severity"] == "success"
    assert conn.committed is True
