import smtplib 
mailto = input ("Who are you emailing to?: \n")
msg = input ("What is your message?: \n") 

gmailaddress = "racecarcalander@gmail.com"
gmailpassword = "cars1cars2cars3"
#mailto="testercalander@gmail.com"
#msg = "Warning, Warning, this is a test! \n SHINING ASSAULT HOPPER!"
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
#print(" \n Sent!")
mailServer.quit()
