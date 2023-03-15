def sd(sec):
    days = sec // (24 * 3600)
    sec %= 24 * 3600
    hours = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print(f'{days}:{hours}:{min}:{sec}')


sd(1000000)