from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class ApplyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.is_active) + str(user.pk) + str(timestamp)


token_generator = ApplyTokenGenerator()
