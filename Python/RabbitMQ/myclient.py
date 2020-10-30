import pika


def receive():

    credentials = pika.PlainCredentials('eai','yDDYl50qy7I1')
    conn = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials,
                                                            host='10.88.11.186',
                                                             virtual_host='eai',
                                                            port=32552))
    #conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()
    #channel.queue_declare(queue='test')
    channel.queue_declare(queue='edisonai-results-execution-test',durable=True)
    # channel.basic_consume(queue='test',
    #                        on_message_callback=test_callback,
    #                        auto_ack=True)
    channel.basic_consume(queue='edisonai-results-execution-test',
                          on_message_callback=test_callback)
    channel.start_consuming()


def test_callback(channel,method,properties,body):
    print(" Received the body ",body)

if __name__ == "__main__":

    receive()
