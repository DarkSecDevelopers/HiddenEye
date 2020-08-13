import requests

from models.connection_model import ConnectionModel
from views.connection_view import ConnectionView


class ConnectionController:
    def __init__(self, host: str = None, timeout: float = None, model=ConnectionModel()):
        self._model = model
        self._timeout = timeout if timeout is not None else self._model.timeout
        self._host = host if host is not None else self._model.host

    def verify_connection(self):
        try:
            if requests.get(url=self._host, timeout=self._timeout).status_code == 200:
                print(
                    ConnectionView().connection_messages["connection_is_detected"])
        except:  # HAS TO BE BARE EXCEPT
            raise ConnectionError(
                ConnectionView().connection_messages["connection_is_not_detected"]) from None
