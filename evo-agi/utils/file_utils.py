"""
File system utils.
"""
import collections
import os
import pickle
import sys
import errno
import shutil
import glob

import codecs
import hashlib
import tarfile
import fnmatch
import tempfile
from datetime import datetime
import logging


f_ext = os.path.splitext

f_size = os.path.getsize

is_file = os.path.isfile

is_dir = os.path.isdir

get_dir = os.path.dirname

def load_pickle(*fpaths):
    with open(f_join(*fpaths), "rb") as fp:
        return pickle.load(fp)


def dump_pickle(data, *fpaths):
    with open(f_join(*fpaths), "wb") as fp:
        pickle.dump(data, fp)


def load_text(*fpaths, by_lines=False):
    with open(f_join(*fpaths), "r") as fp:
        if by_lines:
            return fp.readlines()
        else:
            return fp.read()


def load_text_lines(*fpaths):
    return load_text(*fpaths, by_lines=True)


def dump_text(s, *fpaths):
    with open(f_join(*fpaths), "w") as fp:
        fp.write(s)


def dump_text_lines(lines: list[str], *fpaths, add_newline=True):
    with open(f_join(*fpaths), "w") as fp:
        for line in lines:
            print(line, file=fp, end="\n" if add_newline else "")