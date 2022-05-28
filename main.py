import sys
import time


# 꼬욤꼬욤 오토바이 시뮬레이터

def main():
    mx = 35
    for i in range(mx):
        sys.stdout.write(f"\r{' ' * i}ㅁ{' ' * (mx - i - 1)}ㅇ")
        sys.stdout.flush()
        time.sleep(0.1)
    print("으악TV")


while True:
    main()
