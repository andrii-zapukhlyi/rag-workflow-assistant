from unittest.mock import patch

import pytest


@pytest.fixture
def auth_headers(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python"]
        response = client.post(
            "/auth/register",
            json={
                "full_name": "Chat User",
                "email": "chat@example.com",
                "password": "password",
                "department": "WEB",
                "position": "Chat Dev",
                "position_level": "SENIOR",
            },
        )
        token = response.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}


def test_create_and_list_chats(client, auth_headers):
    res = client.post("/chat/chats", headers=auth_headers)
    assert res.status_code == 200
    session_id = res.json()["session_id"]

    res = client.get("/chat/chats", headers=auth_headers)
    assert res.status_code == 200
    sessions = res.json()
    assert len(sessions) == 1
    assert sessions[0]["id"] == session_id


def test_rename_chat(client, auth_headers):
    res = client.post("/chat/chats", headers=auth_headers)
    session_id = res.json()["session_id"]

    new_name = "New Chat Name"
    res = client.put(
        f"/chat/chats/{session_id}/rename",
        json={"new_name": new_name},
        headers=auth_headers,
    )
    assert res.status_code == 200
    assert res.json()["name"] == new_name

    res = client.get("/chat/chats", headers=auth_headers)
    assert res.json()[0]["name"] == new_name


def test_delete_chat(client, auth_headers):
    res = client.post("/chat/chats", headers=auth_headers)
    session_id = res.json()["session_id"]

    res = client.delete(f"/chat/chats/{session_id}", headers=auth_headers)
    assert res.status_code == 200

    res = client.get("/chat/chats", headers=auth_headers)
    assert len(res.json()) == 0


def test_ask_in_chat(client, auth_headers):
    res = client.post("/chat/chats", headers=auth_headers)
    session_id = res.json()["session_id"]

    with (
        patch("api.chat_router.handle_user_query") as mock_query,
        patch("api.chat_router.generate_session_name") as mock_gen_name,
    ):

        mock_query.return_value = ("Answer", [], [])
        mock_gen_name.return_value = "Auto Name"

        res = client.post(
            f"/chat/chats/{session_id}/ask",
            json={"query": "Hello"},
            headers=auth_headers,
        )
        assert res.status_code == 200
        data = res.json()
        assert data["answer"] == "Answer"
        assert data["session_name"] == "Auto Name"


def test_access_denied_other_user_chat(client, auth_headers):
    res = client.post("/chat/chats", headers=auth_headers)
    session_id = res.json()["session_id"]

    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["java"]
        res2 = client.post(
            "/auth/register",
            json={
                "full_name": "Other User",
                "email": "other@example.com",
                "password": "password",
                "department": "WEB",
                "position": "Other Dev",
                "position_level": "JUNIOR",
            },
        )
        token2 = res2.json()["access_token"]
        headers2 = {"Authorization": f"Bearer {token2}"}

    res = client.get(f"/chat/chats/{session_id}/messages", headers=headers2)
    assert res.status_code == 403
