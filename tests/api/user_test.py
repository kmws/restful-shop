import pytest


@pytest.mark.parametrize("user_dict, expected_status_code",
                         [({'email': '', 'password': ''}, 200)])
def test_add_user(client, user_dict, expected_status_code):
    response = client.post('/user', json=user_dict)
    assert response.status_code == expected_status_code


