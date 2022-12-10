from MQ import queue_name_out, routing_key_out
from tg_messenger import TGMessenger
from service import Service

token = 'your tg bot token'

tg_messenger = TGMessenger(token)
service = Service(tg_messenger, queue_name_out, routing_key_out)
service.start_service()

