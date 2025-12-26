import jwt
import datetime
from django.conf import settings

def generate_access_token(user):
    # Get current time in UTC (timezone-aware)
    now = datetime.datetime.now(datetime.timezone.utc)
    
    payload = {
        'user_id': user.id,
        'exp': now + datetime.timedelta(days=1), # Expires in 24 hours
        'iat': now,                             # Issued at
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_access_token(token):
    try:
        # PyJWT handles the expiration check automatically
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Token is malformed or signature doesn't match