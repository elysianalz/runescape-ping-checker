from pythonping import ping
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', type=int, help='which world to check ping for')
args = parser.parse_args()

worlds = 281
world_pings = dict()

def ping_server(world):
    w = "oldschool"+ str(world+1) + ".runescape.com"
    res = ping(w, verbose=False, count=1)
    world_pings[world+301] = round(res.rtt_avg_ms)

if args.w is not None:
    try:
        ping_server(args.w - 301)
    except:
        print("world does not exist.")
else:
    print("checking servers.... this may take a moment")
    for world in range(worlds):
        try:
            ping_server(world)
        except Exception as e:
            continue

for world, ping in world_pings.items():
    print("world: "+str(world), "ms: "+str(ping))
