__author__ = 'solomina'

def call_count(f):
    def wrapper(*args):
        wrapper.counter += 1
        print "function {0} call #: {1}".format(f.__name__, wrapper.counter)
        return f(*args), wrapper.counter
    wrapper.counter = 0
    return wrapper

class LogIt:
    def __init__(self,t):
        self.t = t

    @call_count
    def log(self,txt):
        print "*************" + txt + "***********" + self.t

log = LogIt("boooo")
[log.log(a) for a in ("ONE", "TWO", "THREE", "FOUR", "FIVE")]
log = LogIt("foooo")
log.log("OLD")


