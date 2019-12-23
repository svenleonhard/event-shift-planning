import pika
import shift_planning
import json
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='simulations')
channel.queue_declare(queue='results')
def callback(ch, method, properties, body):
  results = shift_planning.make_plan(body)
  # send a message back
  channel.basic_publish(exchange='', routing_key='results', body=json.dumps(results, ensure_ascii=False))
# receive message and complete simulation
channel.basic_consume(queue='simulations', auto_ack=True,
                      on_message_callback=callback)
channel.start_consuming()