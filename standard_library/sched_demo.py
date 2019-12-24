import sched
import time
import threading
import queue
import unittest


def event_print():
    print(time.asctime())
    print("hello world")


def timer_event(delay, priority, s: sched.scheduler, q: queue.Queue):
    print("timer event: ", time.asctime(), delay)

    argument = (delay, priority, s, q)
    if q.empty():
        s.enter(delay, priority, timer_event, argument)
    else:
        print("no more!")


def timer_starter(q: queue.Queue):
    s = sched.scheduler()
    delay = 1
    priority = 1

    argument = (delay, priority, s, q)
    s.enter(delay, priority, timer_event, argument)
    s.run()


def timer_controller(q: queue.Queue):
    x = input()
    print("will terminate..........")
    q.put("quit")


class TestScheduler(unittest.TestCase):
    def test_scheduler(self):
        s = sched.scheduler()
        s.enter(2, 1, event_print)
        s.enter(4, 1, event_print)
        print("run:", time.asctime())
        s.run()

    def test_timer(self):
        q = queue.Queue(maxsize=1)

        t0 = threading.Thread(target=timer_controller, args=(q,))
        t1 = threading.Thread(target=timer_starter, args=(q, ))

        t0.start()
        t1.start()
        t0.join()
        t1.join()


if __name__ == "__main__":
    unittest.main()