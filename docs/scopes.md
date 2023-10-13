# Notes
## token path
- mod token path operation returning scopes requested
- scopes returned as part of jwt token
[scopes token](../server/queries/token.py)
```py
data={"sub": user.username, "scopes": form_data.scopes},
```
## declare scopes in path ops, dependencies
- declare path op for /users/me/items requiring scope items
    * dep = dependency
    1. import and use FA Security
    2. Security allows for dependencies declaration (Depends), receives scopes parameter with scopes list
    3. pass dep get_current_active_User to Security and scopes list w/ 1 scope `items`
    ```py
        # example
        scopes={"me": "Read information about the current user.", "items": "Read items.", 'user_calendar':'Read calendar.'},
    ```
    4. dep function: get_current_active_user also declares sub-dependencies w/ depends, security and declare sub dep `get_current_user` and additional scope reqs -> req `me` scope
        * Security = depends subclass w/ 1 + parameter
        - allows fa to know it can declare security scopes, use internally, document API w/ OpenAPI

## use security scopes
[get_current_user](../server/queries/users.py)
- update get_current_user dependency where we use same OAuth2 scheme created prior, declare as dependency oauth2_scheme
- no req to use Security, as no need to specify security scopes
- declare param of SecurityScopes type imported from fastapi.security (similar to Request - used to get obj directly)

# use scopes
- in get_current_user,
    * scopes property has list that contains all scopes req by itself, all deps use as sub dep
    * `security_scopes` obj provide `scope_str` attrb w/ single string, has scopes separated

# verify username, data shape
- verify received username, extract scopes
