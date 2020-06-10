import os
import pytest

migration_path = os.path.dirname(os.path.abspath(__file__))


@pytest.mark.parametrize("user_dict, expected_status_codes",
                         [({'email': 'test@mail.com', 'password': 'Test123!'}, 201),
                         ({'password': 'Test123!'}, 400)])
def test_user_creation(client, user_dict, expected_status_codes):
    response = client.post('/user', json=user_dict)
    assert response.status_code == expected_status_codes
