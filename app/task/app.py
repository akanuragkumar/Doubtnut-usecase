from flask import Flask, request, jsonify
from healthcheck import HealthCheck
from task.config.connect import mongo_connect
import time
import datetime

ts = time.time()
data = []
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
mongo_db = mongo_connect()
app = Flask(__name__)
app.config["DEBUG"] = True

health = HealthCheck(app, "/healthcheck")


def insert_pdf_user(data):
    user_id = request.args['user_id']
    doubt_id = request.args['doubt_id']
    my_dict = {"user_id": user_id, "doubt_id": doubt_id, "question_json": data, "timestamp": timestamp}
    collection = mongo_db['pdf_user']
    documents = collection.find_one(
        {
            'user_id': user_id,
        },
        {
            '_id': 0
        }
    )
    if documents is None:
        x = collection.insert_one(my_dict)
    else:
        query = {'user_id': user_id}
        values = {"$set": {"doubt_id": doubt_id, "question_json":data, "timestamp": timestamp}}

        x = collection.update_one(query, values)

    return x


@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    insert_pdf_user(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
