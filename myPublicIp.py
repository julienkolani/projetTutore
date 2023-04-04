import urllib.request
import sendMail

previous_ip = ""

def get_public_ip():
    url = 'https://ident.me/'
    req = urllib.request.urlopen(url)
    return req.read().decode('utf8')

sendMail.sendMail(get_public_ip())

print(get_public_ip())

previous_ip = get_public_ip()

while True:
    current_ip = get_public_ip()
    if (previous_ip != current_ip):
        sendMail.sendMail(current_ip)
        previous_ip = current_ip
    previous_ip = current_ip
     
   