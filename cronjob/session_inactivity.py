from config.connect import mongo_connect
from pdf_generate import generate_pdf
import time
import datetime


def inactive_doubts():
    mongo_db = mongo_connect()
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    current_time_l5 = (datetime.datetime.now() - datetime.timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')
    current_time_l10 = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')
    final_user_id = []
    final_doubt_id = []
    doubt_ids = []
    user_ids = []
    latest_user_ids = []
    collection = mongo_db['pdf_user']
    documents = collection.find(
        {
            'timestamp': {'$lt': current_time_l5, '$gte': current_time_l10},
        },
        {
            '_id': 0
        }
    )
    if documents is None:
        obj_data = None
    else:
        for doc in documents:
            user_ids.append(doc['user_id'])
            doubt_ids.append(doc['doubt_id'])
    user_ids = tuple(final_user_id)
    doubt_ids = tuple(doubt_ids)

    user_ids_list = list(user_ids)
    documents = collection.find(
        {'$and': [{'timestamp': {'$lt': current_time, '$gte': current_time_l5}}, {'user_id': {'$in': user_ids_list}}]},
        {
            '_id': 0
        }
    )
    if documents is None:
        obj_data = None
    else:
        for doc in documents:
            latest_user_ids.append(doc['user_id'])
    latest_user_ids = tuple(latest_user_ids)

    active_user_id = tuple(list(set(user_ids) - set(latest_user_ids)))

    for i, j in enumerate(user_ids):
        for a in active_user_id:
            if j == a:
                final_user_id.append(i)
    for k in final_user_id:
        final_doubt_id.append(doubt_ids[k])

    documents = collection.find(
        {'doubt_id': {'$in': final_doubt_id}},
        {
            '_id': 0
        }
    )
    if documents is None:
        obj_data = None
    else:
        for doc in documents:
            for d in final_doubt_id:
                question_json = (doc['question_json'])
                doubt_id = d
                generate_pdf(question_json, doubt_id)
    return True


inactive_doubts()
