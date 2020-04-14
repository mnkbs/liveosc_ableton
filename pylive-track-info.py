import argparse
import live
import time


if __name__ == "__main__":

    set = live.Set()
    set.scan()
    print(set.tracks)

    while True:
        print(live.query("/live/track/info", 0))
        print('-----------------------')
        time.sleep(0.1)
