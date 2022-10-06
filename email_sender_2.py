import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('rhrahdi@gmail.com', 'password')
subject = 'test python'
body = 'I love python'
message = 'subject:{}\n\n{}'.format(subject, body)
listadd = ['rahdinhussain@gmail.com',
            'kuddus@gmail.com'
            ]
ob.sendmail('rahdinhussain@gmail.com', listadd, message)
print('main sent')
ob.quit()