import smtplib

from string import Template
from email import encoders
from email.mime.application import MIMEApplication
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = '<your email>'
PASSWORD = '<password>'

def read_template(filename):
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main(names,emails):
    # names = names
    # emails = emails
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    # for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=names.title())

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=emails
    msg['Subject']="You left some questions unseened, download pdf!"
    
    # add in the message body
    file-link = "https://aws-s3/ifjf/bucket/a46cdd1-c81a-4e6b-880c-9cb8f4bca9c9.pdf" 
    # msg.attach(MIMEText(message, 'plain'))
    html = """\
        <!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
 
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Doubtnet</title>
  <style type="text/css">
  body {{margin: 0; padding: 0; min-width: 100%!important;}}
  img {{height: auto;}}
  .content {{width: 100%; max-width: 600px;}}
  .header {{padding: 40px 30px 20px 30px;}}
  .innerpadding {{padding: 30px 30px 30px 30px;}}
  .borderbottom {{border-bottom: 1px solid #f2eeed;}}
  .subhead {{font-size: 15px; color: #ffffff; font-family: sans-serif; letter-spacing: 10px;}}
  .h1, .h2, .bodycopy {{color: #153643; font-family: sans-serif;}}
  .h1 {{font-size: 33px; line-height: 38px; font-weight: bold;}}
  .h2 {{padding: 0 0 15px 0; font-size: 24px; line-height: 28px; font-weight: bold;}}
  .bodycopy {{font-size: 16px; line-height: 22px;}}
  .button {{text-align: center; font-size: 18px; font-family: sans-serif; font-weight: bold; padding: 0 30px 0 30px;}}
  .button a {{color: #ffffff; text-decoration: none;}}
  .footer {{padding: 20px 30px 15px 30px;}}
  .footercopy {{font-family: sans-serif; font-size: 14px; color: #ffffff;}}
  .footercopy a {{color: #ffffff; text-decoration: underline;}}

  @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {{
  body[yahoo] .hide {{display: none!important;}}
  body[yahoo] .buttonwrapper {{background-color: transparent!important;}}
  body[yahoo] .button {{padding: 0px!important;}}
  body[yahoo] .button a {{background-color: #e05443; padding: 15px 15px 13px!important;}}
  body[yahoo] .unsubscribe {{display: block; margin-top: 20px; padding: 10px 50px; background: #2f3942; border-radius: 5px; text-decoration: none!important; font-weight: bold;}}
  }}

  /*@media only screen and (min-device-width: 601px) {{
    .content {{width: 600px !important;}}
    .col425 {{width: 425px!important;}}
    .col380 {{width: 380px!important;}}
    }}*/

  </style>
</head>

<body yahoo bgcolor="#f6f8f1">
<table width="100%" bgcolor="#f6f8f1" border="0" cellpadding="0" cellspacing="0">
<tr>
  <td>
    <!--[if (gte mso 9)|(IE)]>
      <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td>
    <![endif]-->     
    <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td bgcolor="#c7d8a7" class="header">
          <table width="70" align="left" border="0" cellpadding="0" cellspacing="0">  
            <tr>
              <td height="70" style="padding: 0 20px 20px 0;">
                <img class="fix" src="images/icon.gif" width="70" height="70" border="0" alt="" />
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
            <table width="425" align="left" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
          <![endif]-->
          <table class="col425" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 425px;">  
            <tr>
              <td height="70">
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td class="subhead" style="padding: 0 0 0 3px;">
                      DOUBTS
                    </td>
                  </tr>
                  <tr>
                    <td class="h1" style="padding: 5px 0 0 0;">
                      FORGOT TO READ SOME QUESTIONS
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td class="h2">
                {names},welcome to Doubtnut!
              </td>
            </tr>
            <tr>
              <td class="bodycopy">
                It seems that you did not continue reading the questions regarding your doubts. Complete reading all the questions so that your doubts can be cleared fully. Complete Knowledge is complete gain.
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          <table width="115" align="left" border="0" cellpadding="0" cellspacing="0">  
            <tr>
              <td height="115" style="padding: 0 20px 20px 0;">
                <img class="fix" src="images/article1.png" width="115" height="115" border="0" alt="" />
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
            <table width="380" align="left" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
          <![endif]-->
          <table class="col380" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 380px;">  
            <tr>
              <td>
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td class="bodycopy">
                      Here is the download link for the pdf which has attached all the questions. These questions you did not complete reading. Download and complete your learning.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding: 20px 0 0 0;">
                      <table class="buttonwrapper" bgcolor="#e05443" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td class="button" height="45">
                            <a href={filename}>Download Pdf!</a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          <img class="fix" src="images/wide.png" width="100%" border="0" alt="" />
        </td>
      </tr>
      <tr>
        <td class="innerpadding bodycopy">
          The platform uses image recognition technologies to provide solutions of some mathematical and science questions.To find the solution to a question, one has to upload an image depicting the question. The app extracts text from the image and tries to match it in its database of questions which are pre-answered, having recorded video solutions.
        </td>
      </tr>
      <tr>
        <td class="footer" bgcolor="#44525f">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td align="center" class="footercopy">
                &reg; Doubtnut 2020<br/>
                <a href="#" class="unsubscribe"><font color="#ffffff">Unsubscribe</font></a> 
                <span class="hide">from this notification instantly</span>
              </td>
            </tr>
            
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <!--[if (gte mso 9)|(IE)]>
          </td>
        </tr>
    </table>
    <![endif]-->
    </td>
  </tr>
</table>
</body>
</html>
""".format(names=names, filename=filename)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)    
     # In same directory as script
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    import sys
    main(names,emails)
