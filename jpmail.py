import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender_email, receiver_email, subject, message, smtp_server, smtp_port, username, password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email 
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

    print("Email sent successfully!")

if __name__ == "__main__":
# Color codes
  ORANGE = "\033[33m"
  RED = "\033[31m"
  GREEN = "\033[32m" 
  WHITE = "\033[37m"
  CYAN = "\033[36m"


code = f'''
{RED}   :::::::::::: pppppppppppp   
{RED}             :: pp        pp
{RED}             :: pp        pp
{RED}             :: pp        pp
{RED}   ::        :: pp ppppppppp                                                                               
{RED}   ::        :: pp
{RED}   ::        :: pp
{RED}   ::        :: pp
{RED}   :::::::::::: pp         {ORANGE} MAILL {GREEN}Version : {{1.0}}
                          

{GREEN}[{WHITE}-{GREEN}]{CYAN} Tool Created by PRINCE IMMANUEL (Princeimm){WHITE}
'''


code_with_name = code.replace("MAILL", f"{ORANGE} MAIL")
print(code_with_name)
sender_email = input(f"{GREEN}Your Mail: ")
receiver_email = input(f"{GREEN}Receptionist Mail: ")
subject = input(f"{GREEN}Subject: ")
message = input(f"{GREEN}Body of the message: ")
smtp_server = input(f"{GREEN}SMTP server address: ")
smtp_port = int(input(f"{GREEN}SMTP Port: "))  
username = input(f"{GREEN}Your email account username: ")
password = input(f"{GREEN}Your email account password: ")
send_mail(sender_email, receiver_email, subject, message, smtp_server, smtp_port, username, password)
