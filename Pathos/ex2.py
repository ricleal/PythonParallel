import pathos
from math import sin, cos

if __name__ == '__main__':
    mp = pathos.pools.ProcessPool()
    tp = pathos.pools.ThreadPool()

    print mp.amap(tp.map, [sin, cos], [range(3),range(3)]).get()
    mp.close(); tp.close()
    mp.join(); tp.join()
