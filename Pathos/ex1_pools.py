import pathos

'''
Pools demo
'''
def sum_squared(x,y):
    return (x+y)**2

x = range(5)
y = range(0,10,2)

if __name__ == '__main__':
    sp = pathos.pools.SerialPool()
    pp = pathos.pools.ParallelPool()
    mp = pathos.pools.ProcessPool()
    tp = pathos.pools.ThreadPool()

    for pool in [sp,pp,mp,tp]:
        print pool, "\t", pool.map(sum_squared, x, y)
        pool.close()
        pool.join()
