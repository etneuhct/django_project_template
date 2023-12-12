from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class CustomTokenGenerator(PasswordResetTokenGenerator):
    key_salt = "django.contrib.auth.tokens.PasswordResetTokenGenerator"
    token_timeout = settings.PASSWORD_RESET_TIMEOUT

    def __init__(self):
        super(CustomTokenGenerator, self).__init__()


class GenericPublicToken(CustomTokenGenerator):
    token_timeout = 120

    def __init__(self, ttl=None):
        super(GenericPublicToken, self).__init__()
        self.token_timeout = ttl if ttl else self.token_timeout

    def _make_hash_value(self, data: dict, timestamp):
        text = "".join([f"{k}{data[k]}" for k in sorted(data.keys())])
        return text
