import json
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from django.contrib.auth.models import User
    from rest_framework.test import APIClient

TEST_PASSWORD = 'test_pass'


@pytest.fixture
def user_with_password(user: 'User'):
    user.set_password(TEST_PASSWORD)
    user.save()
    return user


@pytest.mark.django_db
def test_auth_using_login_pass(anon_client: 'APIClient', user_with_password: 'User'):
    username = user_with_password.username
    response = anon_client.post(
        '/api/auth/login/',
        data={'username': username, 'password': 'incorrect_password'},
    )
    assert response.status_code == 403

    response = anon_client.post(
        '/api/auth/login/', data={'username': username, 'password': TEST_PASSWORD}
    )
    assert response.status_code == 200, response.content

    data = response.json()

    assert data['username'] == username


@pytest.mark.django_db
def test_user_flow(admin_client: 'APIClient', anon_client: 'APIClient'):
    users_count = 20
    users_data = [
        {
            'username': f'user_{i}',
            'password': f'password_{i}',
            'email': f'email_{i}@mail.ru',
        }
        for i in range(users_count)
    ]

    # 1
    created_users_id = []
    for user in users_data:
        response = admin_client.post('/api/v1/users/', data=user)
        assert response.status_code == 200
        created_users_id.append(response.json()['id'])

    # 2
    response = admin_client.get('/api/v1/users/')
    assert response.status_code == 200
    assert len(response.json()) == len(users_data)

    # 3
    for user_id in created_users_id:
        response = anon_client.post(f'/api/v1/users/{user_id}/')
        assert response.status_code == 200

    # 4
    for user_id in created_users_id:
        response = admin_client.delete(f'/api/v1/users/{user_id}/')
        assert response.status_code == 204
