from time import sleep
import sys, time

def ft_progress(listy):
    width = 20
    start = time.time()
    for i in listy:
        filled = int(round(width * i / len(listy)))
        percents = int(round(100 * i / len(listy)))
        bar = '=' * filled + '>' + ' ' * (width - filled)
        elapsed = time.time() - start
        eta = round(elapsed / (i + 1) * len(listy) - elapsed, 2)
        sys.stdout.write('\rETA: %.2fs [%s%%][%s] %s/%s | elapsed time %.2fs\r' % (eta, percents, bar, i + 1, len(listy), elapsed))
        sys.stdout.flush()
        yield i

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)