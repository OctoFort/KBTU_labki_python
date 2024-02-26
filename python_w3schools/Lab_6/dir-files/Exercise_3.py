import os
import sys

if len(sys.argv) < 2:
    print("Write arguments!")
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Path doesn't exist")
    sys.exit()

print(f"Dir: {os.path.split(sys.argv[1])[0]}")
print(f"File name : {os.path.split(sys.argv[1])[1]}")
