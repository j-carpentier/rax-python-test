#!/usr/bin/python

import os
import sys
import asyncore, socket
import threading
import time
import Queue
import random

run = True

def handle_message(message):

    outfile = '/tmp/message_handler_file'
    with open(outfile, 'a') as f:
        f.write('%s\n' % message)

    return

class Consumer(threading.Thread):

    __QUEUE_TIMEOUT = 5

    def __init__(self, q, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.__queue = q

    def run(self):
        
        global run

        while run:
            message = None
            try:
                message = self.__queue.get(block=True, timeout=self.__class__.__QUEUE_TIMEOUT)
            except Queue.Empty:
                continue

            worker = threading.Thread(target=handle_message, args=(message,))
            worker.daemon = True
            worker.start()

        print "[Thread %s] is leaving" % self.getName()

        

class RandomProducer(threading.Thread):

    __MESSAGES = [
        'Caution: breathing may be hazardous to your health.',
        'Your love life will be... interesting.',
        'Always do right.  This will gratify some people and astonish the rest.',
        'Always the dullness of the fool is the whetstone of the wits.',
        'Good day to deal with people in high places; particularly lonely stewardesses.',
        'It\'s lucky you\'re going so slowly, because you\'re going in the wrong direction.',
    ]

    def __init__(self, q, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.__queue = q

    @classmethod
    def get_sleep_time(c, minimum=1, maximum=5):
        return random.randint(minimum, maximum)

    @classmethod
    def gen_message(c):
        return c.__MESSAGES[random.randint(0, len(c.__MESSAGES) - 1)]
    
    def run(self):
        
        global run

        while run:
            queue = self.__queue
            time.sleep(RandomProducer.get_sleep_time())

            try:
                m = RandomProducer.gen_message()
                queue.put(m, block=False)
            except Exception as e:
                pass

        print "[Thread %s] is leaving" % self.getName()


def main():

    global run

    q = Queue.Queue(maxsize=0)

    producer = RandomProducer(q, name='producer')
    producer.daemon = True
    producer.start()

    consumer = Consumer(q, name='consumer')
    consumer.daemon = True
    consumer.start()

    try:
        while True:
            time.sleep(60)

    except KeyboardInterrupt as e:
        run = False

    consumer.join()
    producer.join()

    return 0

if __name__ == "__main__":
    main()


