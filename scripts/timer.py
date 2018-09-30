import time, sys
timer = time.time

# Total time to run func() reps times
# Returns (total time, last result)
def total(reps, func, *pargs, **kargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

# Quickest func() among reps runs
# Returns (best time, last result)
def bestof(reps, func, *pargs, **kargs):
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

# Best of reps1 runs of (total of reps2 runs of func)
def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    return bestof(reps1, total, reps2, func, *pargs, **kargs)