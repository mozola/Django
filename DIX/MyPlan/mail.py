# -*- coding: utf-8 -*-
import smtplib

TO = 'molo226@vp.pl'                            #please write TO email
SUBJECT = 'mail od mailny'
TEXT ='Poniżej znajduje się lista zakupów na najbliższy sprint'

gmail_sender = 'mozola.waldemar@gmail.com'      #please write your email
gmail_passwd = 'atb7jwnd'                       #please write your password to email

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo
server.login(gmail_sender,gmail_passwd)


msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Lista zakupow na sprint",
  "",
  "{}"
  ])


def generate_msg(components):
    components_list = []
    components_list.append(TEXT)

    for key, value in components.iteritems():
        components_list.append('{} \t {}'.format(key, value))

    return '\n'.join(components_list)


def send_main(msga):
    try:
        server.sendmail(gmail_sender,[TO],msg.format(generate_msg(msga)))
        print 'SUCCES: Mail was sended'
    except:
        print 'ERROR: Mail not sended'

    server.quit()