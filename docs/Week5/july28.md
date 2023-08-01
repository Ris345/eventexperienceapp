# NOTES FOR JULY 28TH

# Research regarding OAuth and JWTs
- If there is going to be a mobile app then Oauth 2 would be a good recommendation
    ## Stack Overflow Quotes
    > If there are lots of different clients (browser-based, native mobile, server-side, etc) then sticking to OAuth 2.0 rules might make it more manageable than trying to roll your own system.

    > TL;DR If you have very simple scenarios, like a single client application, a single API then it might not pay off to go OAuth 2.0. On the other hand, if there are lots of different clients (browser-based, native mobile, server-side, etc) then sticking to OAuth 2.0 rules might make it more manageable than trying to roll your own system.

    > OAuth uses server-side and client-side storage. If you want to do real logout you must go with OAuth2. Authentication with JWT token can not logout actually. Because you don't have an Authentication Server that keeps track of tokens

# Tasks
- Created a virtual environment for purpose of developing with various team members
    - Setup
        1. Checked python version
            * `python --version`
        2. install pipreqs (had to do this as I had performed development prior to creating virtual environment)
            * `pip install pipreqs`
        3. run pipreqs for current project use its path
            * `pipreqs [global path to project folder]`
    - Activate virtual environment
        1. `cd [root directory]`
        2. `pip install virtualenv`
        3. `virtualenv env`
        - in order to activate virtual env, copy path obtained from activate file in bin directory in env directory
            * /env/bin/activate
        4. `source [activate path in env folder]`
        5. `pip install -r requirements.txt`
