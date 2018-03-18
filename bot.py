import requests
import misc
import json
from time import sleep

#https://api.telegram.org/bot467306886:AAGfmu6WaX4Q9_gSbj7uYYoma6z1bSlAv7o/sendmessage?chat_id=475653889&text=hi

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
global last_id
global prssmall, prsbig
last_id = 0

prssmall = dict([('а', "a"), ('ә', "a'"), ('б', 'b'), ('д', 'd'), ('е', 'e'), ('ф', 'f'), ('г', 'g'), ('ғ', "g'"),
           ('х', 'h'), ('һ', 'h'), ('і', 'i'), ('и', "i'"), ('й', "i'"), ('ж', 'j'), ('к', 'k'), ('л', 'l'),
           ('м', 'm'), ('н', 'n'), ('ң', "n'"), ('о', 'o'), ('ө', "o'"), ('п', 'p'), ('р', 'r'), ('с', 's'),
           ('ш', "s'"), ('ч', "c'"), ('т', 't'), ('ұ', 'u'), ('ү', "u'"), ('в', 'v'), ('ы', 'y'), ('у', "y'"),
           ('з', 'z'), ('қ', 'q')
           ])

prsbig = dict([('А', "A"), ('Ә', "A'"), ('Б', 'B'), ('Д', 'D'), ('Е', 'E'), ('Ф', 'F'), ('Г', 'G'), ('Ғ', "G'"),
          ('Х', 'H'), ('Һ', 'H'), ('І', 'I'), ('И', "I'"), ('Й', "I'"), ('Ж', 'J'), ('К', 'K'), ('Л', 'L'),
          ('М', 'M'), ('Н', 'N'), ('Ң', "N'"), ('О', 'O'), ('Ө', "O'"), ('П', 'P'), ('Р', 'R'), ('С', 'S'),
          ('Ш', "S'"), ('Ч', "C'"), ('Т', 'T'), ('Ұ', 'U'), ('Ү', "U'"), ('В', 'V'), ('Ы', 'Y'), ('У', "Y'"),
          ('З', 'Z'), ('Қ', 'Q')
         ])

#print(token)
def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    #print(r.json())
    return r.json()

def latinize(msg):
    global prsbig, prssmall
    nmsg = ""
    for ch in msg:
        if ch in prssmall:
            nmsg += prssmall[ch]
        elif ch in prsbig:
            nmsg += prsbig[ch]
        else:
            nmsg += ch
    return nmsg

def get_message():
    data = get_updates()
    global last_id
    last_object = data['result'][-1]
    update_id = last_object['update_id']
    if last_id != update_id:
        last_id = update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {'chat_id': chat_id,
                    'message_text': message_text,
                  }
        return message
    else :
        return None

def send_message(chat_id, text = 'Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get( url)

def main():
#  st_id
    data = get_updates()
    global last_id
    last_id = data['result'][-1]['update_id']
    while True:
        answer = get_message()
        if answer != None:
            print(answer)
            chat_id = answer['chat_id']
            message_text = answer['message_text']
            #print(len(message_text))
            print(latinize(message_text))
            # for i in range(len(message_text)):
            #      print(message_text[i])
            # for msg in message_text:
            #     print(latinize(msg) + ' ')
            send_message(chat_id, latinize(message_text))

if __name__ == '__main__':
    main()
