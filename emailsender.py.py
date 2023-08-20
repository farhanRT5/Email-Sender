import smtplib

to = input("Enter the email of the recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('firstplacejan91889@gmail.com', 'farhanfathima')
    # enter sender email ID and password, seperated with "," , in the above line
    server.sendmail('firstplacejan91889@gmail.com', to, content)
    # enter the receivers email, in the above statement
    server.close()

sendEmail(to, content)
# enable less secure apps website before exicuting the program