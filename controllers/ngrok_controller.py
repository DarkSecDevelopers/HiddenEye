from pyngrok import conf as pyngrok_config
from pyngrok import exception as pyngrok_exceptions
from pyngrok import installer as pyngrok_installer
from pyngrok import ngrok


class NgrokController:
    def __init__(self, config_path: str = ".config/ngrok.yml", model=ngrok, exceptions=pyngrok_exceptions, installer=pyngrok_installer, config=pyngrok_config):
        self._model = model
        self._exceptions = exceptions
        self._installer = installer
        self._config = config
        self._config_path = config_path
        self._tunnels = None
        self._ngrok_url = None
        self._ngrok_config = None

    def close_latest_connection(self):
        try:
            self._model.disconnect(self._ngrok_url)
        except self._exceptions.PyngrokError:
            # FIXME replace with View entry
            print("Can't find any latest connections.")
            pass

    def maintain_default_config(self):
        self._installer.install_default_config(self._config_path)

    def activate_config_path(self):
        self._ngrok_config = self._config.PyngrokConfig(
            config_path=self._config_path)

    def establish_connection(self, port='80'):
        self._model.connect(port=port, name='HiddenEye Connection',
                            pyngrok_config=self._ngrok_config)

    def obtain_tunnels(self):
        self._tunnels = self._model.get_tunnels()

    @property
    def ngrok_url(self):
        return self._ngrok_url

    def obtain_ngrok_url(self):
        self._ngrok_url = self._tunnels[0]
