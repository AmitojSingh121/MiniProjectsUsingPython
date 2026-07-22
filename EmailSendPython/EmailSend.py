# s is elas    
import smtplib as s 
# we create a variable whose name is Obj
Obj = s.SMTP('smtp.gmail.com',587)
# this is a server
# ehlo which identifies the Script to the mail server
Obj.ehlo() 
# this is a server also
# starttls Unsecured connection nuh secured connection ch convert kar reha ha 
Obj.starttls()
Obj.login("amitojsingh861@gmail.com","wyav ljdh jckz wctv")
# Email Id       Password Generate 
subject = "test Python"
body = "I Love Python"
massage = "subject:{}\n\n{}".format(subject,body) 
massage = "subject:{}\n\n{}".format(subject,body) 
# send the mail 
listadd = ["amitojsingh861@gmail.com"]
Obj.sendmail('amitojs645@gmail.com' , listadd , massage)
print("send mail")
Obj.quit()