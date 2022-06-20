import jwt
import code_token

try:
 jwt.decode(code_token.token, code_token.key, algorithms="HS256")
except:
  print("Firma incorrecta.")

