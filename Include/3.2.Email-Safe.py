import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
    SMTP_Server = 'smtp.gmail.com'
    SMTP_PORT = 587 #tis: 587, ssl: 465

    # Soan thao email
        #header
    msg = MIMEMultipart()
    msg['From'] = 'boss862000@gmail.com'
    msg['To'] = 'boss862000@gmail.com'
    msg['Subject'] = 'Chu de buc thu'
        #noi dung thu
    body = input("Nhap noi dung thu:")
    part = MIMEText('text','plain')
    part.set_payload(body)
    msg.attach(part)
        #gui thu
        #tao smtp session
    session = smtplib.SMTP(SMTP_Server, SMTP_PORT)
    session.ehlo()
    session.set_debuglevel(1)
    session.ehlo
    password = input("enter password")
        #login vao email
    session.login('boss862000@gmail.com', password)
        #gui thu
    session.sendmail('boss862000@gmail.com','boss862000@gmail.com',msg.as_string())
    session.quit()
