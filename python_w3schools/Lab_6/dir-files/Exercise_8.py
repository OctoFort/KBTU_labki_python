import os
import sys

if len(sys.argv) < 2:
    print("Write arguments!")
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Path doesn't exist")
    sys.exit()

try:
    os.remove(sys.argv[1])
    print("File successfully deleted")
except PermissionError:
    print("You don't have permission to delete file")


# if not (os.access(sys.argv[1], os.R_OK) and os.access(sys.argv[1], os.W_OK)):
#     print("You don't have permission to delete file")
#     sys.exit()
