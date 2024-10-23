#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File : dict_move.py
@Time : 2024-10
@Author : dao_mingze@163.com
@Description :
"""

import os
import shutil
import fnmatch

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 用时 {(end_time-start_time)} 秒")
        return result

    return wrapper


# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录：{current_dir}")


def ispath(path: str):
    if not os.path.exists(path):
        # print(f"路径{path}不存在")
        return False
    return True


src = "raw/rime-ice/"

filetype = "*.schema.yaml"
det = "schema"


def filematch(src, filetype):
    srclist = []
    for file in os.listdir(src):
        if fnmatch.fnmatch(file, filetype):
            srclist.append(file)
    return srclist


@timer
def move(src, filetype, det):
    srclist = filematch(src, filetype)
    x = 0
    for i in srclist:
        if ispath(det + i):
            os.remove(det + i)
        shutil.copy(src + i, det)
        x += 1
    print(f"移动{x}个")


move(src, filetype, det)
