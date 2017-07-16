import random
import time

from threading import Thread

class MyThread(Thread):
    """
    a thread example
    """

    def __init__(self, name):
        """
        init a thread
        :param name:
        """
        Thread.__init__(self)
        self.name=name

    def run(self):
        """
        run the thread
        :return:
        """
        amount=random.randint(3,15)
        time.sleep(amount)
        msg="%s is runnning" % self.name
        print(msg)

def create_threads():
    """
    create a group of threads
    :return:
    """
    for i in range(5):
        name="Thread #%s" %(i+1)
        my_thrad=MyThread(name)
        my_thrad.start()

if __name__ == '__main__':
    create_threads()