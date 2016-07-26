#!/usr/bin/env python3
import os

fout = os.open("foo", os.O_WRONLY | os.O_CREAT, 0o644)

# Return byte array and save to file descriptor
os.write(fout, bytes("hello world", "utf-8"))
os.close(fout)

