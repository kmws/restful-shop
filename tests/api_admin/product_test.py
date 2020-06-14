import pytest

from tests.conftest import root_dict


@pytest.mark.parametrize("product_dict, expected_status_codes",
                         ([({"name": "Test1", "code": "TT1", "price": 5.43, "description": "This is very cool product"},
                            [204, 204])]))
def test_user_actions_from_admin(client, product_dict, expected_status_codes):
    response = client.post('/auth/login', json=root_dict)
    assert response.status_code == expected_status_codes[0]

    response = client.post('/api-admin/product', json=product_dict)
    assert response.status_code == expected_status_codes[1]

    # TODO: change name
