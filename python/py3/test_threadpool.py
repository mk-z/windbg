
from multiprocessing.pool import ThreadPool
pool = ThreadPool(5)
pool.map(lambda x: x**2, range(5))
