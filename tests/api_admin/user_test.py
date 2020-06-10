import pytest

from tests.conftest import root_dict


@pytest.mark.parametrize("user_dict, expected_status_codes",
                         [({'email': 'test@mail.com', 'password': 'Test123!'}, [201, 200, 204, 204, 200]),
                          ({'password': 'Test123!'}, [400, 404, 404, 404, 404]),
                         ({'email': root_dict['email'], 'password': root_dict['password']}, [409, 404, 404, 404, 404])])
def test_user_actions_from_admin(client, user_dict, expected_status_codes):
    response = client.post('/auth/login', json=root_dict)
    assert response.status_code == 204
    response = client.post('/user', json=user_dict)
    assert response.status_code == expected_status_codes[0]
    response = client.get('/api-admin/user/{}'.format(2), json=user_dict)
    assert response.status_code == expected_status_codes[1]
    user_dict = {"firstName": "test"}
    response = client.put('/api-admin/user/{}'.format(2), json=user_dict)
    assert response.status_code == expected_status_codes[2]
    response = client.delete('/api-admin/user/{}'.format(2))
    assert response.status_code == expected_status_codes[3]
    response = client.get('/api-admin/user/{}'.format(2))
    assert response.status_code == expected_status_codes[4]

