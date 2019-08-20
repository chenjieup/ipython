from queue import Queue
from threading import Thread, Event


def producer(out_q):
	i = 0
	while True:
		i += 1
		print("count:",i) 
		evt =Event()
		data="hello world"
		out_q.put(data,evt)
		evt.wait()

def consumer(in_q):
	while True:
		data, evt = in_q.get()
		print(" ",data)
		evt.set()


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
