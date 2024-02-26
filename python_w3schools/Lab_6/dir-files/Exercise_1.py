import os
import sys

if len(sys.argv) < 3:
    print("Write arguments!")
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Path doesn't exist")
    sys.exit()

match sys.argv[2]:
    case "f":
        [
            print(f)
            for f in os.listdir(sys.argv[1])
            if os.path.isfile(os.path.join(sys.argv[1], f))
        ]
    case "d":
        [
            print(d)
            for d in os.listdir(sys.argv[1])
            if os.path.isdir(os.path.join(sys.argv[1], d))
        ]
    case "fd":
        [print(fd) for fd in os.listdir(sys.argv[1])]
