
import os
import json
from google.cloud import pubsub_v1


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "zbigdatademos-f095913afe24.json"


def pubsub_callback( message_future ):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('[ ERROR ] Publishing message on {} threw an Exception {}.'.format(topic_name, message_future.exception()))
    else:
        print('[ INFO ] Result: {}'.format(message_future.result()))


def pubsub_publish( pubsub_publisher, project_id, pubsub_topic, message ):
    '''
        Pub/Sub Publish Message
        Notes:
          - When using JSON over REST, message data must be base64-encoded
          - Messages must be smaller than 10MB (after decoding)
          - The message payload must not be empty
          - Attributes can also be added to the publisher payload
        
        
        pubsub_publisher  = pubsub_v1.PublisherClient()
        
    '''
    try:
        # Initialize PubSub Path
        pubsub_topic_path = pubsub_publisher.topic_path( project_id, pubsub_topic )
        
        # If message is JSON, then dump to json string
        if type( message ) is dict:
            message = json.dumps( message )
        
        # When you publish a message, the client returns a Future.
        #message_future = pubsub_publisher.publish(pubsub_topic_path, data=message.encode('utf-8'), attribute1='myattr1', anotherattr='myattr2')
        message_future = pubsub_publisher.publish(pubsub_topic_path, data=message.encode('utf-8') )
        message_future.add_done_callback( pubsub_callback )
    except Exception as e:
        print('[ ERROR ] {}'.format(e))




# Example Syntax:

import datetime
datetimestamp     = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
project_id        = 'zbigdatademos'
pubsub_publisher  = pubsub_v1.PublisherClient()
pubsub_topic      = 'topicz1'
message           = {'name': 'Dan Z', 'email':'d.zaratsian@gmail.com', 'datetimestamp':datetimestamp}
pubsub_publish( pubsub_publisher, project_id, pubsub_topic, message )



#ZEND
