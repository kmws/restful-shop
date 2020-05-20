import pytest

from models.error import Error


@pytest.mark.parametrize("user_dict, expected_status_codes",
                         [({'email': 'test@mail.com', 'password': 'Test123!'}, [201, 400])])
def test_login_without_activation(client, user_dict, expected_status_codes):
    response = client.post('/user', json=user_dict)
    assert response.status_code == expected_status_codes[0]
    response = client.post('/auth/login', json={'email': user_dict['email'], 'password': user_dict['password']})
    assert response.status_code == expected_status_codes[1]
    assert response.json['errorKey'] == Error.AUTH_LOGIN_USER_NOT_ACTIVATED.name

