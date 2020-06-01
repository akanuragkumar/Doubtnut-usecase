# doubtnut_assignment


## Database Setup

```shell
 Create 2 new databases in Mongodb
```

```Mongodb
Create database pdf_user

Create database pdf_record

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

##  Logic and Assumptions

1. **User asks a question**
    When a user asks a question an entry is created in user_asked_question table with following:
    - user_id
    - doubt_id
    - doubt_body

2. **Results are generated**
    Based on this, a set of results is generated from the catalog_questions table and shown to the user as a list and             following things are passed as parameters in generated list's xpath:      
    - user_id
    - doubt_id
    
3. **When user clicks on any video, API is called**
    When a student views a video from the above list, an API is called.That API has following components:
    - it accepts user_id, doubt_id from parameters
    - it accepts question JSON
    - then it querries in pdf_user table and checks if the user_id already exists in table or not
    - if user_id exists then it updates doubt_id, question_json, timestamp
    - else it inserts the new entry with user_id, doubt_id, question_json, timestamp
 2. **Cronjob scheduling**
    Now we schedule a cronjob which works every 1 minute and logs in a file for which we do the following:      
    - We take list of entries in pdf_user made between (current time - 5minutes) and (current time - 10 minutes).
    - We get list of user_ids and doubts ids whose entries where made in that time frame.
    - Now we querry again with those user ids in between current time and (current time - 5minutes).
    - Now we get list of user_ids who were active in this time frame.
    - We now, find the corresponding doubt_id with user_id which was not active.
    - Thus, we get doubt_ids which are most recent,inactive since 5 minutes and the user which is too inactive.
    - Now we querry in pdf_user table with those doubts_ids for getting question_json.
    - We first convert those question_json to pdf.
    - Now, We assign an unique name to pdf by uuid, add s3 link to it and upload it to S3 bucket.
    - Now we make an entry in pdf_record table with pdf's s3 link, doubt_id, timestamp.
    
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



