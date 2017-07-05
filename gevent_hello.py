# from gevent import sleep
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()    # monkey patch all blocking packages of python
from time import sleep



def hello(index):
    print('Hello {}'.format(str(index)))
    sleep(3)
    print('World! {}'.format(str(index)))


if __name__=='__main__':
    pool = Pool(10)
    pool.map(hello, [i for i in range(5)])



