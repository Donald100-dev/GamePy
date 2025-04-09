import msvcrt, os, time

time_get_keyboard: float = 0.01
dict_direc = {
            "a": (-1, 0),
            "s": (0, 1),
            "d": (1, 0),
            "w": (0, -1)
            }
defeault_direc = [-1, 0]

def get_direc():
    if msvcrt.kbhit():
        char: chr = msvcrt.getch().decode('latin-1')
        if char in dict_direc:
            return dict_direc[char]
        else: return None

def move(pos, direc):
    x, y = pos
    x += direc[0]
    y += direc[1]
    return (x, y)

def clock_frame(FPS):
    time_frame = 1/FPS
    while True:
        start_frame = time.time()
        yield
        end_frame = time.time()
        delta = end_frame - start_frame
        if delta < time_frame:
            time.sleep(1/FPS - delta)

def main():
    direc = (0, 0)
    pos = (0, 0)
    clock = clock_frame(12)
    while True:
        next(clock)
        os.system('cls')
        d = get_direc()
        direc = d if d else direc
        pos = move(pos, direc)
        print(pos)

if __name__ == '__main__':
    main()