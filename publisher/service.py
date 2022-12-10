import json

from MQ import channel, routing_key_in
from tg_messenger import BaseMessenger
from utils import compress_message, decompress_body


class Service():
    def __init__(self, messenger: BaseMessenger, queue_name_out: str, routing_key_out: str):
        self.messenger = messenger
        self.queue_name_out = queue_name_out
        self.routing_key_out = routing_key_out

    def start_service(self):
        self.messenger.start_bot(self.messenger_callback)
        self.waiting_queue_message()

    def messenger_callback(self, update, context) -> None:
        mess_dict = {"recipient": self.messenger.get_user_id(update), "message": update.message.text}
        message = json.dumps(mess_dict)
        compressed_message = compress_message(message)
        channel.basic_publish(exchange='', routing_key=routing_key_in, body=compressed_message)

    def queue_callback(self, chanel, method, properties, body):
        body = decompress_body(body)
        message_data = json.loads(body)
        message = message_data['message']
        recipient = message_data['recipient']
        self.messenger.send_message(recipient, message)

    def waiting_queue_message(self):
        channel.basic_consume(self.queue_name_out, self.queue_callback, auto_ack=True)
        channel.start_consuming()
