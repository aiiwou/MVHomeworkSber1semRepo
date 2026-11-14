import unittest

from flask import json

from openapi_server.models.create_fish_request import CreateFishRequest  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.fish_list_response import FishListResponse  # noqa: E501
from openapi_server.models.fish_response import FishResponse  # noqa: E501
from openapi_server.models.message_response import MessageResponse  # noqa: E501
from openapi_server.models.update_fish_request import UpdateFishRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFishController(BaseTestCase):
    """FishController integration test stubs"""

    def test_create_fish(self):
        """Test case for create_fish

        Добавить рыбу в каталог
        """
        create_fish_request = {"name":"name","species":"species","sizeCm":0.18008281,"aquariumId":1,"arrivalDate":"2000-01-23","description":"description"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/fish',
            method='POST',
            headers=headers,
            data=json.dumps(create_fish_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_fish(self):
        """Test case for delete_fish

        Удалить рыбу из каталога
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/fish/{fish_id}'.format(fish_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fish_by_id(self):
        """Test case for get_fish_by_id

        Получить информацию о конкретной рыбе
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/fish/{fish_id}'.format(fish_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_fish(self):
        """Test case for list_fish

        Получить список рыб
        """
        query_string = [('species', 'Amphiprion ocellaris'),
                        ('aquariumId', 3)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/fish',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_fish(self):
        """Test case for update_fish

        Частично обновить информацию о рыбе
        """
        update_fish_request = {"name":"name","species":"species","sizeCm":0.18008281,"aquariumId":1,"arrivalDate":"2000-01-23","description":"description"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/fish/{fish_id}'.format(fish_id=56),
            method='PATCH',
            headers=headers,
            data=json.dumps(update_fish_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
