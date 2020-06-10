import pytest

from app import create_root
from models.error import Error
from tools.config_properties import get_config


#TODO: use PATCH
@pytest.mark.parametrize("user_dict, expected_status_codes",
                         [({'email': 'test@mail.com', 'password': 'Test123!'}, [201, 400, 204, 204, 204, 204])])
def test_login_activated_user(client, user_dict, expected_status_codes):
    response = client.post('/user', json=user_dict)
    assert response.status_code == expected_status_codes[0]
    user_id = response.json['id']
    response = client.post('/auth/login', json={'email': user_dict['email'], 'password': user_dict['password']})
    assert response.status_code == expected_status_codes[1]
    assert response.json['errorKey'] == Error.AUTH_LOGIN_USER_NOT_ACTIVATED.name

    config = get_config()
    create_root(config.get_root_email(), config.get_root_password())

    response = client.post('/auth/login',
                           json={'email': config.get_root_email(), 'password': config.get_root_password()})
    assert response.status_code == expected_status_codes[2]

    response = client.put('/api-admin/user/' + str(user_id), json={'isActive': True})
    assert response.status_code == expected_status_codes[3]

    response = client.get('/auth/logout')
    assert response.status_code == expected_status_codes[4]

    response = client.post('/auth/login', json={'email': user_dict['email'], 'password': user_dict['password']})
    assert response.status_code == expected_status_codes[5]


