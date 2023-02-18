import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='TO_NT_SERVER')

class ConnectionManager:
    def __int__(self, queue_name, receiver_queue_name, publisher_queue_name, connection_host):
        self.connection = None
        self.receiver_queue_name = None
        self.publisher_queue_name = None
        self.channel = None
        self.queue_name = queue_name
        self.connection_host = connection_host

    def create_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.publisher_queue_name)



