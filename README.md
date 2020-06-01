# doubtnut_assignment


## Quickstart

To work in a sandboxed Python environment we recommend installing the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/doubnut
    $ pip install -r requirements.txt
    ```

1. Setup a Mongo database 

  ```Mongodb
Create database pdf_user

Create database pdf_record

```


1. Run server

   ```bash
   $ python app.runser.py
   ```

   View at http://127.0.0.1:5000
   
1. Cron-job Scheduling

   ```bash
   $ crontab -e
     */1 * * * * /usr/bin/python desktop/Doubtnut/cronjob/session_inactivity.py >> log.txt
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

1. **When a user asks a question**
     an entry is created in user_asked_question table with following:
    - user_id
    - doubt_id
    - doubt_body

2. **Results are generated**
     from the catalog_questions table and shown to the user as a list and following things are passed as parameters in               generated list's xpath:        
    - user_id
    - doubt_id
    
3. **When user clicks on any video, API is called.**
     That API has following components:
    - it accepts user_id, doubt_id from parameters
    - it accepts question JSON
    - then it querries in pdf_user table and checks if the user_id already exists in table or not
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
    - Now we querry in pdf_user table with those doubts_ids for getting question_json.
    - We first convert those question_json to pdf.
    - Now, We assign an unique name to pdf by uuid, add s3 link to it and upload it to S3 bucket.
    - Now we make an entry in pdf_record table with pdf's s3 link, doubt_id, timestamp.
    

## API Documentation 

### `upload` 

1. `POST /upload?user_id=user_id&doubt_id=doubt_id` 

```json
 application/json - [{"class":11,"question_text":"What is photosynthesis?","solution_text":"The process by which green plants and some other organisms use sunlight to synthesize nutrients from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a by-product."}]
```





