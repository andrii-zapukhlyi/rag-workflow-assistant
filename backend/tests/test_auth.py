from unittest.mock import patch


def test_register_user(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python", "fastapi"]

        payload = {
            "full_name": "Test User",
            "email": "test@example.com",
            "password": "password123",
            "department": "WEB",
            "position": "Backend Developer",
            "position_level": "SENIOR",
        }
        response = client.post("/auth/register", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert "refresh_token" in response.cookies


def test_login_user(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python"]
        client.post(
            "/auth/register",
            json={
                "full_name": "Login User",
                "email": "login@example.com",
                "password": "password123",
                "department": "WEB",
                "position": "Login Dev",
                "position_level": "JUNIOR",
            },
        )

    response = client.post(
        "/auth/login", data={"username": "login@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials(client):
    response = client.post(
        "/auth/login",
        data={"username": "nonexistent@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_get_me(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python"]
        reg_res = client.post(
            "/auth/register",
            json={
                "full_name": "Me User",
                "email": "me@example.com",
                "password": "password123",
                "department": "WEB",
                "position": "Me Dev",
                "position_level": "MIDDLE",
            },
        )

    token = reg_res.json()["access_token"]

    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "me@example.com"
    assert data["position"] == "ME DEV"


def test_refresh_token(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python"]
        reg_res = client.post(
            "/auth/register",
            json={
                "full_name": "Refresh User",
                "email": "refresh@example.com",
                "password": "password123",
                "department": "WEB",
                "position": "Refresh Dev",
                "position_level": "INTERN",
            },
        )

    refresh_cookie = reg_res.cookies["refresh_token"]
    client.cookies.set("refresh_token", refresh_cookie)

    response = client.post("/auth/refresh")
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.cookies


def test_register_duplicate_email(client):
    with patch("api.auth_router.generate_skills_for_position") as mock_gen_skills:
        mock_gen_skills.return_value = ["python"]
        user_data = {
            "full_name": "Dup User",
            "email": "dup@example.com",
            "password": "pwd",
            "department": "WEB",
            "position": "Dup Dev",
            "position_level": "JUNIOR",
        }
        client.post("/auth/register", json=user_data)
        response = client.post("/auth/register", json=user_data)
        assert response.status_code == 400
        assert "Email already registered" in response.json()["detail"]


def test_get_me_unauthorized(client):
    response = client.get("/auth/me")
    assert response.status_code == 401
