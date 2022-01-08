import time

def solver_timer(method):
    def timed(*args, **kw):
        start_time = time.time()
        bag_size, value, taken_items = method(*args, **kw)
        end_time = time.time()

        return bag_size, value, taken_items, round((end_time - start_time), 2)
    return timed