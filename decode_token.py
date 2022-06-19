import jwt
import code_token
key='my_super_secret'
jwt.decode(code_token.token, key, algorithms="HS256")