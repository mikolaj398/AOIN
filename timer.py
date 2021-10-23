import time

def solver_timer(method):
    def timed(*args, **kw):
        start_time = time.time()
        bag_size, value, taken_items = method(*args, **kw)
        end_time = time.time()

        print(end_time - start_time)
        return bag_size, value, taken_items, (end_time - start_time) * 1000
    return timed