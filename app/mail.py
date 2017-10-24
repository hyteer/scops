from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    #EMAIL SETTINGS  
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'hyteer@qq.com',
    MAIL_PASSWORD = 'rvkxxmswbjeseabj')

mail = Mail(app)

@app.route("/mail/<content>")
def send_mail(content):
    msg = Message(subject="FlaskMailTest", sender='hyteer@qq.com', recipients=['yotong@qq.com)'])
    msg.html = "<h3>Flask Mail</h3><p>Content: %s</p>" % content
    mail.send(msg)
    return "sent..."

if __name__ == '__main__':
    app.run(debug=True,port=5001)
