import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()



def send_email(exchange1, amount1, exchange2, amount2, profit):
    amount1 = round(amount1, 2)
    amount2 = round(amount2, 2)
    profit = round(profit, 2)

    email = os.getenv('GMAIL_EMAIL')
    password = os.getenv('GMAIL_PASSWORD')
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "New Trade Opportunity!"
    msg['From'] = email
    msg['To'] = email
    
    # Create the body of the message (a plain-text and an HTML version).
    text = f"You have an opportunity to buy BTC on {exchange1} for {amount1}\nThen you should sell it on {exchange2} for {amount2}\nFor a ${profit} profit"
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        Here is the <a href="https://www.python.org">link</a> you wanted.
        </p>
    </body>
    </html>
    """
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    # part2 = MIMEText(html, 'html')
    
    msg.attach(part1)
    # msg.attach(part2)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.starttls()
    
    server.login(email, password)
    
    server.sendmail(email, email, msg.as_string())
    print('mail sent')
        