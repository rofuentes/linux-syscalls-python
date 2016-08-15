#!/usr/bin/env python3
import os


def create_file(fname):
    fout = os.open(fname, os.O_WRONLY | os.O_CREAT, 0o644)

    # Return byte array and save to file descriptor
    os.write(fout, bytes("hello world", "utf-8"))
    os.close(fout)


def test_create_file(tmpdir):
    tmp_file = tmpdir.join('foo')
    create_file(tmp_file.strpath)
    assert tmp_file.read() == 'hello world'
