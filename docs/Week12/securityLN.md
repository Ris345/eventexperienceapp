# [LN ARTICLE](https://www.linkedin.com/advice/0/how-do-you-use-http-cookies-sessions-tokens-web)

- Web apps req to verify id, permissions of users who access resources in a joint process of authentication -> authorization
- Relies on various mechanisms to exchange and store info between client, server

> GPT
> - (server-rendered pages, req user-specific data to be maintained across requests) hybrid approach where tokens are used for authentication and sessions for maintaining user-specific data and state.
> vs
> - (app primarily serves api endpoints) using tokens for auth and authorization is a common approahc

## Cookies
- Small data pieces sent by server to client and stored by browser.
- Can be used to store user preferences, track user behavior, maintain user sessions. For authentication + authorization, cookies store unique id linking user to server-side record of credentials and roles
- Browser sends cookie back to server with every request -> server can verify user id and permissions

* Cons
    * vulnerable to theft
    * forgery
    * CORS (cross site scripting attacks)
    * limited by size and number

## Sessions
- maintain stateful comm between client and server, regardless of HTTP being a stateless protocol
- use cookies/other methods to store session id on client side and associate with server-side ids containing user info and state
- sessions can store more data v cookies and can be more secure if session id is encrypted + regn'ed frequently

* Cons
    * require server-side memory/storage
    * difficult to scale
    * across various servers
    * impacted by network failures or timeouts

## Tokens
- stateless authentication, authorization w/o relying on cookies/sessions
- self contained pieces of data that include user id, permissions, other claims that are signed by server with secret key or public-private key pair
- sent by server to client, stored by browser in local storage or memory -> client sends token back to server with every request -> server validate token via signature and payload

* Pros
    * more flexible, portable, scalable vs cookies or sessions
    * support cross-domain, cross-origin requests

* Cons
    * harder to revoke
    * susceptible to replay attack
    * depend on cryptographic algos, keys

## Cookie v Token Auth
* Cookie based auth
    - relies on server to manage user session and state
    - use cookie to store and transmit session id
* token based auth
    - rely on client to store, transmit user info and claims
    - use tokens to encode and sign
* cookie based auth = simpler implementation, better browser compatibility, easier to revoke
* token auth is more efficient, secure, flexible, support more scenarios and platforms

## Choose Best Method
- cookies
    * stateful comm between client and server is required
    * if existing browser fts and frameworks supporting cookies will be used
- tokens
    * req stateless comm between client and server
    * req cross-domain, cross-origin requests
- combo
    * achieve balance between stateful and stateless to enhance security, functionality of app

## Best Practices
1. utilize https to encrypt comm between client and server
2. set secure flags, attributes for cookies and tokens
    - HttpOnly, Secure, SameSite, Expiry
3. Use strong encryption and hashing algos to gen and verify cookies, tokens + keep keys, secrets safe and updated
    - critical to validate, sanitize user input and output to avoid exposing sensitive info or error messages that can reveal system vulnerability
4. use appropriate mech for managing user session, tokens like expiration, revocation, refreshment, invalidation to prevent unauthorized/prolonged access to web resources
