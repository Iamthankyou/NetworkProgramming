import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
    SMTP_Server = 'aspmx.l.google.com'
    SMTP_PORT = 25

    # Soan thao email
        #header
    msg = MIMEMultipart()
    msg['From'] = 'diachigui@gmail.com'
    msg['To'] = 'diachinhan@gmail.com'
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
        #gui thu
    session.sendmail('diachi','diachinhan',msg.as_string())
    session.quit()
