from Queue import Queue

def split(q):
    """ A split function which will split a queue into two.
        The function returns a tuple containing the two queues.
    """
    q1 = Queue()
    q2 = Queue()
    for i in range(len(q)):
        item = q.dequeue()
        if i % 2 == 0:
            q1.enqueue(item)
        else:
            q2.enqueue(item)
    return (q1, q2)