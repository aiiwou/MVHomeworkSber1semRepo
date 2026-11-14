import flask
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_fish_request import CreateFishRequest  # noqa: E501
from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.fish_list_response import FishListResponse  # noqa: E501
from openapi_server.models.fish_response import FishResponse  # noqa: E501
from openapi_server.models.message_response import MessageResponse  # noqa: E501
from openapi_server.models.update_fish_request import UpdateFishRequest  # noqa: E501
from openapi_server import util


def create_fish(body):  # noqa: E501
    """Добавить рыбу в каталог

    Создаёт запись об обитателе океанариума. # noqa: E501

    :param create_fish_request: 
    :type create_fish_request: dict | bytes

    :rtype: Union[FishResponse, Tuple[FishResponse, int], Tuple[FishResponse, int, Dict[str, str]]
    """
    create_fish_request = body
    if flask.request.is_json:
        create_fish_request = CreateFishRequest.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_fish(fish_id):  # noqa: E501
    """Удалить рыбу из каталога

    Удаляет запись о рыбе по её идентификатору. # noqa: E501

    :param fish_id: Уникальный идентификатор рыбы
    :type fish_id: int

    :rtype: Union[MessageResponse, Tuple[MessageResponse, int], Tuple[MessageResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_fish_by_id(fish_id):  # noqa: E501
    """Получить информацию о конкретной рыбе

    Возвращает публичные данные записи по её идентификатору. # noqa: E501

    :param fish_id: Уникальный идентификатор рыбы
    :type fish_id: int

    :rtype: Union[FishResponse, Tuple[FishResponse, int], Tuple[FishResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_fish(species=None, aquarium_id=None):  # noqa: E501
    """Получить список рыб

    Возвращает каталог рыб с возможностью фильтрации по виду и аквариуму. # noqa: E501

    :param species: Фильтр по биологическому виду
    :type species: str
    :param aquarium_id: Фильтр по идентификатору аквариума
    :type aquarium_id: int

    :rtype: Union[FishListResponse, Tuple[FishListResponse, int], Tuple[FishListResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_fish(fish_id, body):  # noqa: E501
    """Частично обновить информацию о рыбе

    Изменяет только переданные поля; неуказанные поля остаются без изменений. # noqa: E501

    :param fish_id: Уникальный идентификатор рыбы
    :type fish_id: int
    :param update_fish_request: 
    :type update_fish_request: dict | bytes

    :rtype: Union[FishResponse, Tuple[FishResponse, int], Tuple[FishResponse, int, Dict[str, str]]
    """
    update_fish_request = body
    if flask.request.is_json:
        update_fish_request = UpdateFishRequest.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
