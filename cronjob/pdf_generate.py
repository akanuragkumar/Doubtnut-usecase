from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from uuid import uuid4
from config.connect import mongo_connect
import time
import datetime


def generate_pdf(question_json, doubt_id):
    mongo_db = mongo_connect()
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    upload_key = str(uuid4())+".pdf"
    doc = SimpleDocTemplate(upload_key, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    Story = []
    logo = "python_logo.jpeg"
    serial_no = 1
    question_class = []
    question_text = []
    question_answer = []

    for i in question_json:
        question_class.append(i['class'])
        question_text.append(i['question_text'])
        question_answer.append(i['solution_text'])

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    Story.append(Spacer(1, 12))

    for x,y,z in zip(question_class, question_text, question_answer):
        ctext = '<font size="12">Q.%s: Class: %s</font>' % (serial_no, x)
        Story.append(Paragraph(ctext, styles["Normal"]))
        qtext = '<font size="12">%s</font>' % (y)
        Story.append(Paragraph(qtext, styles["Normal"]))
        atext = '<font size="12">Sol: %s</font>' % (z)
        Story.append(Paragraph(atext, styles["Normal"]))
        Story.append(Spacer(2, 12))
        serial_no = serial_no+1
    doc.build(Story)

    doubt_id = doubt_id
    link = "http://s3-us-east-1.amazonaws.com/bucket/"+upload_key
    timestamp = current_time
    collection = mongo_db['pdf_record']
    my_dict = {"doubt_id": doubt_id, "S3_link": link, "timestamp": timestamp}
    x = collection.insert_one(my_dict)
    return x

