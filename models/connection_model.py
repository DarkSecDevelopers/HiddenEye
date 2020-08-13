class ConnectionModel:
    def __init__(self, timeout: float = 16, host: str = "https://google.com"):
        self._host = host
        self._timeout = timeout

    @property
    def host(self):
        # TODO add verbose output
        return self._host

    @host.setter
    def host(self, new_host: str):
        # TODO add verbose output
        self._host = new_host

    @property
    def timeout(self):
        # TODO add verbose output
        return self._timeout

    @timeout.setter
    def timeout(self, new_timeout):
        # TODO add verbose output
        self._timeout = new_timeout
