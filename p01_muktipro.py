import os

pid = os.fork()
print("Hello")
if pid == 0:
    print("Child Process", os.getpid(), os.getppid())

else:
    print("Parent Process", os.getpid(), os.getppid())
