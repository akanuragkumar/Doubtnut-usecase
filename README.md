# doubtnut_assignment


## Database Setup

```shell
$ create a new DB in Mongodb
```

```Mongodb
create database pdf_user;

create database pdf_record;

```

## Project Structure

### Backend 
```shell
Doubtnut
├── app                                # contains application files
│   ├── task──────┐                    # contains resource files for API
│   └── runserver │                    # serves API and manages the requests
│                 ├── config           # contains db details
│                 └── app.py           # main API file
└── cronjob                            # folder for cronjob scheduling
    ├── assets                         # contains assests which needs to be attached to pdf
    ├── config                         # contains db details
    ├── pdfgenerate.py                 # generates pdf and is called by session_inactivity.py
    └── session_inactivity.py          # checks for session inactivity 
   
```

##  Logic 

### Users

1. **create users** 
    this will create a new user with a random username

### Posts

1. **create post**
    this will create a new post, required fields are 
    - username (the author of this post)
    - title
    - body 

2. **show all posts**
    list all existing posts, we should have following filtering support

    - filter by username
    - filter by query contained in title (search by title)

3. **edit posts** `TBD`

4. **delete posts** `TBD` 

### Comments 

1. **show all comments (of a user)**

2. **show all comments (under a post)**

3. **add a comment**


## API Documentation 

### `users` 

1. `POST /users` 

Creates a new user with random username and an user id

2. `GET /users/{userid}`

Get an user with a given user id

3. `GET /users/{username}`

Get an user with a given username


### `posts` 

1. `GET /posts` 

Get all posts by everyone 

2. `POST /posts` 

Create a new post. 
Required fields in body - 

```
userId=
title=
body=
```



