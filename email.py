import smtplib
import getpass
myemail=input("yours:")
password=getpass.getpass()
recemail=input("receivers:")
s=smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(myemail,password)
message="hello dad and mom"
s.sendmail(myemail,recemail,message)
s,quit()