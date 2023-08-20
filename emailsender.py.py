import smtplib

to = input("Enter the email of the recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enter your email here', 'enter your email password here')
    # enter sender email ID and password, seperated with "," , in the above line
    server.sendmail('enter your email here', to, content)
    # enter the receivers email, in the above statement
    server.close()

sendEmail(to, content)
# enable less secure apps website before exicuting the program
