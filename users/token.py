from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from django.conf import settings


class TokenOperations:
    def create_token(self, email):
        exp = datetime.now() + timedelta(minutes=30)
        payload = {"email": email, "exp": exp}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return token

    def check_token(self, token):
        if not token:
            raise JWTError()

        token_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        check_exp = datetime.fromtimestamp(token_data.get("exp"))

        if check_exp < datetime.now():
            raise JWTError()

        return token_data.get("email")
