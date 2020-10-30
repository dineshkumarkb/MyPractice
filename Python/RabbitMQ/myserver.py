import pika



def start_conn():

    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.queue_declare(queue="test")

    count = 0
    while(count < 10):

        mystr = raw_input(" Please send a message : ")
        channel.basic_publish(exchange='',
                          routing_key='test',
                          body=mystr)
        count+=1

    print("Message Testing sent to test ")

    conn.close()




if __name__ == "__main__":
    start_conn()