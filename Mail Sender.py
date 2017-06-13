#----------------#
#Made By Omkar Shridhar Dixit 
#Contack Me - Email = Adress red.destroy27@gmail.com
#if it doesnt work in first attemt check your gmail there
#comes someone signed like the thing then go to here
#https://support.google.com/accounts/answer/6010255?hl=en
#and say some low apps can asses you
#thank For Warching follow if you want to do

import smtplib

content = input(r'Enter Your Message: ')
email = input(r'Enter Your Mail Adress: ')
password = input(r'Enter Your Mail Password:')
sendm = input(r'Whom You Want to Send His/Her Email Adress:')

mail = smtplib.SMTP ('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login(email,password)

mail.sendmail (email,sendm,content)

mail.close()
