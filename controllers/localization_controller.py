import gettext

from models.localization_model import LocalizationModel


class LocalizationController:
    def __init__(self, domain: str = None, localedir: str = None, model=LocalizationModel()):
        self._model = model
        self._domain = domain if domain is not None else self._model.domain
        self._localedir = localedir if localedir is not None else self._model.localedir

    def initialize_localization(self):
        gettext.bindtextdomain(self._domain, self._localedir)
        gettext.textdomain(self._domain)

    @staticmethod
    def _(text_string):
        return gettext.gettext(text_string)
