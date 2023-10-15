from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

SECURITY_KEY = os.getenv("SECRET_SECURITY_KEY")
ALGO = os.getenv("ALGO")
# create instance of PasswordBearer()
"""
'token' is a placeholder for the url that client will send username, password to in order to obtain a token

tokenurl = 'token' is relative url token that has not been implemented, basically its ./token

ex: https://localhost:8000.com/token
"""
# scopes - now declaring scheme w/ 2 available scopes (me, items)
# scopes param reps dict w/ each scope as key, description as value
"""
scopes now show in api docs when logging/authorizing
select scopes to provide access to: me, items
"""
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)
