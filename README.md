# Hiring_assignment

## [Link for generated pdf](https://github.com/akanuragkumar/hiring_assignment/blob/master/8a46cdd1-c81a-4e6b-880c-9cb8f4bca9c9.pdf)

## Quickstart

To work in a sandboxed Python environment its recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/hiring_assignment
    $ pip install -r requirements.txt
    ```

1. Setup a Mongo database 

  ```Mongodb
Create database pdf_user

Create database pdf_record

```


1. Run server

   ```bash
   $ python app/runserver.py
   ```

   View at http://127.0.0.1:5000
   
1. Cron-job Scheduling

   ```bash
   $ crontab -e
     */1 * * * * /usr/bin/python desktop/hiring_assignment/cronjob/session_inactivity.py >> log.txt
   ```   

## Project Structure

### Backend 
```shell
hiring_assignment
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
### Mongo database collection Schemas
#### pdf_user

```
pdf_user_schema = {

    'user_id': {
        'type': 'integer',
        'required': True,
    },

    'doubt_id': {
        'type': 'integer',
        'required': True,
    },

    'question_json': {
        'type': 'json',
        'required': True,
    },

    'timestamp': {
        'type': 'datetime',
        'required': True,
    },

    'document_references': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'pdf_user',
                'field': '_id',
                'embeddable': True,
            },
        },
    },
}
```
#### pdf_record

```
pdf_record_schema = {

    'doubt_id': {
        'type': 'integer',
        'required': True,
    },

    'S3_link': {
        'type': 'string',
        'required': True,
    },

    'timestamp': {
        'type': 'datetime',
        'required': True,
    },

    'document_references': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'pdf_record',
                'field': '_id',
                'embeddable': True,
            },
        },
    },
}
```
#### user_asked_question

```
user_asked_question_schema = {

    'user_id': {
        'type': 'integer',
        'required': True,
    },

    'question': {
        'type': 'string',
        'required': True,
    },

    'timestamp': {
        'type': 'datetime',
        'required': True,
    },

    'document_references': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'user_asked_question_schema',
                'field': '_id',
                'embeddable': True,
            },
        },
    },
}
```

##  Logic and Assumptions

1. **When a user asks a question**
     an entry is created in user_asked_question collection with following:
    - user_id
    - doubt_id - id of user_asked_question collection
    - doubt_body

2. **Results are generated**
     from the catalog_questions collection and shown to the user as a list and following things are passed as parameters in               generated list's xpath:        
    - user_id
    - doubt_id
    
3. **When user clicks on any video, API is called.**
     That API has following components:
    - it accepts user_id, doubt_id from parameters
    - it accepts question JSON
    - then it querries in pdf_user collection and checks if the user_id already exists in collection or not
    - if user_id exists then it updates doubt_id, question_json, timestamp
    - else it inserts the new entry with user_id, doubt_id, question_json, timestamp
 4. **Now we schedule a cronjob**
     which works every 1 minute and logs in a file for which we do the following:      
    - We take list of entries in pdf_user made between (current time - 5minutes) and (current time - 10 minutes).
    - We get list of user_ids and doubts ids whose entries where made in that time frame.
    - Now we querry again with those user ids in between current time and (current time - 5minutes).
    - Now we get list of user_ids who were active in this time frame.
    - We now, find the corresponding doubt_id with user_id which was not active.
    - Thus, we get doubt_ids which are most recent,inactive since 5 minutes and the user which is too inactive.
    - Now we querry in pdf_user collection with those doubts_ids for getting question_json.
    - We first convert those question_json to pdf.
    - Now, We assign an unique name to pdf by uuid, add s3 link to it and upload it to S3 bucket.
    - Now we make an entry in pdf_record collection
    with pdf's s3 link, doubt_id, timestamp.
    

## API Documentation 

### `upload` 

1. `POST /upload?user_id=user_id&doubt_id=doubt_id` 

```json
 application/json - [{"class":11,"question_text":"What is photosynthesis?","solution_text":"The process by which green plants and some other organisms use sunlight to synthesize nutrients from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a by-product."}]
```
##### `response`

```json
status- 200 OK
 [
  {
    "class": 11,
    "question_text": "What is photosynthesis?",
    "solution_text": "The process by which green plants and some other organisms use sunlight to synthesize nutrients from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a by-product."
  },
  {
    "class": 5,
    "question_text": "Why is photosynthesis important?",
    "solution_text": "Photosynthesis is important to living organisms because it is the number one source of oxygen in the atmosphere.Green plants and trees use photosynthesis to make food from sunlight, carbon dioxide and water in the atmosphere: It is their primary source of energy."
  }
]
```



