# Notes

## [Python-FastAPI+JWTs](https://dev.to/moadennagi/role-based-access-control-using-fastapi-h59)
- __ROLE BASED ACCESS CONTROL USING FASTAPI__
    - Achieve role based access control w/ fastapi using dependency injection w/ the idea that a dependency acts as an authorization
        - Endpoint function either response with resource or unauthorized response
        ```py
        import datetime
        from typing import Any

        import bcrypt
        import jwt
        from fastapi import Depends, FastAPI, HTTPException, Security, status
        from fastapi.security import OAuth2PasswordBearer, SecurityScopes
        from fastapi.testclient import TestClient
        from pydantic import BaseModel

        fake_users = [
            # password foo
            {'id': 1, 'username': 'admin', 'password': '$2b$12$N.i74Kle18n5Toxhas.rVOjZreVC2WM34fCidNDyhSNgxVlbKwX7i',
            'permissions': ['items:read', 'items:write', 'users:read', 'users:write']
            },
            # password bar
            {'id': 2, 'username': 'client', 'password': '$2b$12$KUgpw1m0LF/s9NS1ZB5rRO2cA5D13MqRm56ab7ik2ixftXW/aqEyq',
            'permissions': ['items:read']}
        ]

        class UserBase(BaseModel):
            username: str
            password: str

        class LoginData(UserBase):
            pass

        class PyUser(UserBase):
            id: int
            permissions: list[str] = []

        class Token(BaseModel):
            access_token: str
            token_type: str

        app = FastAPI()

        # creation of a dependency OAuth2PasswordBearer passing 'token' as tokenurl, which is the url used to obtain the token
        oauth_scheme = OAuth2PasswordBearer(
            tokenUrl="token",
            scopes={'items': 'permissions to access items'}
        )

        def authenticate_user(username: str, password: str) -> PyUser:
            exception = HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials'
                        )
            for obj in fake_users:
                if obj['username'] == username:
                    if not bcrypt.checkpw(password.encode(), obj['password'].encode()):
                        raise exception
                    user = PyUser(**obj)
                    return user
            raise exception

        # dependency takes an arg ot type 'str' that default to Depends(oauth_scheme) -> oauth_scheme dependency returns token that is then decoded and the dependency returns instance of PyUser which is a pydantic BaseModel
        def get_current_user(
            token: str = Depends(oauth_scheme)
        ) -> PyUser:
            decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
            username = decoded['sub']
            for obj in fake_users:
                if obj['username'] == username:
                    user = PyUser(**obj)
                    return user
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials'
            )

        def create_token(user: PyUser) -> str:
            payload = {'sub': user.username, 'iat': datetime.datetime.utcnow(),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90)}
            token = jwt.encode(payload, key='secret')
            return token

        class PermissionChecker:
                def __init__(self, required_permissions: list[str]) -> None:
        self.required_permissions = required_permissions

                def __call__(self, user: PyUser = Depends(get_current_user)) -> bool:
                    for r_perm in self.required_permissions:
                        if r_perm not in user.permissions:
                            raise HTTPException(
                                status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Permissions'
                            )
                    return True

        @app.post('/token')
        def login(login_data: LoginData) -> Token:
            user = authenticate_user(**login_data.dict())
            token_str = create_token(user)
            token = Token(access_token=token_str, token_type='bearer')
            return token

        @app.get('/users/me')
        def get_user(current_user: PyUser = Depends(get_current_user)):
            return current_user

        # 2 routes with varying access control reqs
        @app.get('/items')
        def items(
            authorize: bool = Depends(PermissionChecker(required_permissions=['items:read',]))
        ):
            return 'items'

        @app.get('/users')
        def users(
            authorize: bool = Depends(PermissionChecker(required_permissions=['users:read',]))
        ):
            return 'users'
        ```

## [NodeJS](https://dev.to/zenstack/authorize-users-like-a-pro-libraries-that-help-you-implement-access-control-with-nodejs-5109)

- Implementing security measures in a web app is critical, poorly implemented security can be devastating to a good product

    - __Authentication vs Authorization__
        - Two main pillars of a secure application as they are related but different
        - Authentication
            - Verify who you are and is the process of converting credentials into identities that a system understands
            - Simple as email/password or email/OTP
            - Modern apps favor OAuth-based auth that delegates id verification to a trusted 3rd party to avoid credential storing in own system
        - Authorization
            - Controls 'who takes what action to which asset' -> assuming a user's id is verified by authentication, authorization can be understood as a function
                * `request(identity, action, asset)-> allow | deny`
            - Actions are defined as CRUD, but can be freely defined as req by an implementer
            - Authorization and 'access control' are equal

    - Role Based Access Control
        - RBAC = traditional method of modeling authorization. You define roles, assign user to roles, control asset access permissions by roles v indv users
            - User role can = privilege, department, duty, etc.
            - Example:
                * Admin users can delete anything
                * Sales department can read revenue report

    - Attribute-Based Access Control
        - ABAC makes permission grants based on user and attributes of asset that one is attempting to access
            - Attribute can be anything like blog post author, todo item completion status
            - Examples:
                * Blog post can be deleted by author
                * Deal can't be updated when stage = CLOSED

    - RBAC + ABAC are not mutually exclusive, often will beed to combine them
        - RBAC for coarse control at asset type level, ABAC is more dynamic
        - [More info](https://www.okta.com/identity-101/role-based-access-control-vs-attribute-based-access-control/)

    - Example Scenario
        - User Roles: Member and Admin
        - Assets: Post
        - Asset attributes:
            * Post.owner = User
            * Post.published = Boolean
        - Actions: CRUD
        - Rules:
            * Admin has full access to all posts
            * Owner has full access to owned posts
            * All users have 'read' access to published posts
            * Other requests are denied

- accesscontrol
    - ZenStack with Prisma ORM (powerful access control layer)
        - Toolkit for simplifying the process of building secure CRUD apps w/ Next.js
        - Shares similarities with Remult - generate be services, fe library based on a declarative access policy model and is schema first
        ```js

        // four authorization rules
        model Post {
            id String @id @default(cuid())
            title String
            published Boolean @default(false)
            owner User? @relation(fields: [authorId], references: [id])
            ownerId String?

            // must signin to access any post
            @@deny('all', auth() == null)

            // allow full CRUD by owner or admin
            @@allow('all', owner == auth() || auth().role == 'Admin')

            // published posts are readable to everyone (logged in)
            @@allow('read', published == true)
        }

        // 2 annotations being @@allow, @@deny for access policies, can access current user, current entity, both use info to make a verdict
        // post is updated by user who is a member of post editors
        model Post {
            ...
            // a relation field storing editors of this post
            editors User[]

            ...
            // use a Collection Predicate to check if the current user
            // matches any entity in editors field
            @@allow('update', editors?[id == auth().id])
        }

        // sample fe
        const { find, update } = usePost();
        const {data: publishedPosts} = find({ where: { published: true }});
        ...
        await update(postId, { title: "newTitle" });

        //have the freedom to implement custom next.js api endpoints, enhance policy behavior, bypass and interact with db directly
        ```
