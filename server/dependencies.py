from fastapi.security import OAuth2PasswordBearer

# create instance of PasswordBearer()
"""
'token' is a placeholder for the url that client will send username, password to in order to obtain a token

tokenurl = 'token' is relative url token that has not been implemented, basically its ./token
"""
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="token")
