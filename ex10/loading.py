import time


def ft_progress(lst):
    start = time.time()
    i = 0
    length = len(lst)

    while (i < length):
        yield lst[i]
        now = time.time()
        elapsed = now - start
        progress = i / length
        i += 1
        bar = '=' * int(progress * 24) + '>'
        eta = (length - i) * elapsed / i
        print(f"ETA: {eta:.2f}s",
              f"[{progress * 100:>3.0f}%][{bar:<24}]",
              f"{i}/{length} | elapsed time {elapsed:.2f}", end="\r")


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
