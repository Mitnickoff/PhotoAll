import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import time
import random

def main():

    vk_session = vk_api.VkApi(login='+79894627437', password='abasovsex', app_id='2685278')
    
    vk_session.auth(token_only=True)
    longpoll = VkLongPoll(vk_session)
    vks = vk_session
    print("бот начал свою работу.возможен частый флуд-контроль!")
    def send(peer_id, message):
    	m = vks.method("messages.send", {"peer_id": peer_id, "random_id": 0, "message": message})
    	return m
    
    for event in longpoll.listen():
    	try:
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower() == "!помощь":
    			send(event.peer_id, "!фото {кол-во} {айди альбома}                                                         для остановки накрутки,зайди в termux и введи комбинацию ctrl+c.                                                 создатель скрипта Абсов. вк:*abasovsex *smotryawiy")
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower()[:6] == "!photo":
    			count = event.text[6:].split()[0]
    			al = event.text[6:].split()[1]
    			upload = VkUpload(vk_session)
    			for x in range(int(count)):
    				s = upload.photo(photos="1.png", album_id=int(al))
    				s = upload.photo(photos="2.png", album_id=int(al))
    			
    	except Exception as s:
    		print(f"Error: {s}")
   

while True:
	main()