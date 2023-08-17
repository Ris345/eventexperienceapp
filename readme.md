# Event Experience App (EEA)

## Introduction
Event Experience App (EEA) is an event organizer application that allows users to register as admin, organizer, or volunteer. Each user role comes with its own set of privileges and functionalities. EEA provides a platform for users to RSVP for upcoming events, create, update, read, and delete events, and organize tasks specific to each event. This README provides an overview of the application and its key features.

## Table of Contents
- [Features](#features)
- [User Roles](#user-roles)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Features
1. **User Registration**: Users can register with the application and select their role as admin, organizer, or volunteer. The registration process requires basic user information such as name, email, and password.

2. **User Authentication**: EEA provides secure user authentication to ensure that only authorized users can access the application. User login requires a valid email and password.

3. **Event RSVP**: Users can browse and RSVP for upcoming events. This feature allows users to indicate their interest and attendance for specific events.

4. **Event Management**: Admin and organizers have the ability to create, update, read, and delete events. They can provide event details such as name, date, time, location, description, and any additional information.

5. **Task Organization**: Users can create task lists specific to each event. This feature helps in organizing and assigning tasks to different users or teams. Tasks can be marked as completed and tracked for progress.

6. **Notifications**: Users receive notifications regarding event updates, changes, or any important information related to their role or the events they are involved in.

## User Roles
1. **Admin**: The admin role has full access and control over the application. They can manage users, create, update, and delete events, and have access to all features and functionalities.

2. **Organizer**: Organizers have the ability to create, update, and delete events. They can manage tasks, view RSVPs, and communicate with volunteers. However, they do not have administrative privileges such as user management.

3. **Volunteer**: Volunteers can RSVP for events, view event details, and access task lists. They can mark tasks as complete and communicate with organizers or other volunteers. Volunteers have limited access compared to admins and organizers.

## Installation
To run the client-side application locally, clone this repo and open a terminal in the /client directory. If this is the first time you are running the application, first run "npm install" (to install dependencies) and then "npm run prepare" (to set up Material UI themes and compile .scss). After you've done that, "npm run dev" is all you need to do to get a local server working.

## Usage
Once the application is installed and running, users can perform the following actions:

1. Register a new account with the appropriate role (admin, organizer, or volunteer).
2. Log in with valid credentials.
3. Browse upcoming events and RSVP for those they are interested in.
4. Create, update, and delete events (admin and organizers only).
5. Create task lists for events and assign tasks to volunteers.
6. Mark tasks as complete and track progress.
7. Receive notifications about event updates and changes.
8. Communicate with other users through in-app messaging.

## Contributing
We welcome contributions to enhance the Event Experience App. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the codebase is clean and formatted.
4. Commit and push your changes to your forked repository.
5. Submit a pull request, clearly explaining the changes you have made and their purpose.

## Installing Black Formatter
[Black Docs Link](https://black.readthedocs.io/en/stable/)

> - Black is a PEP 8 compliant opinionated formatter

### Black Installation
1. Black requires Python 3.7+ and can be installed by running `pip install black`
    - Viewing python version can be done by performing `python --version`
    - Upgrading python via instructions @ [link](https://blog.enterprisedna.co/how-to-update-python/)

2. In order to get started with current files, run `black {source_file_or_directory}`
    - can also run *Black* as a package via `python -m black {source_file_or_directory}`
