#!/usr/bin/env python
#-*- coding:utf-8 -*-
from beepmusic.parser import BMCParser
import beepmusic

def test1():
    bmc = BMCParser("joy.bmc")
    for notations in bmc:
        print(notations)

def test2():
    player = beepmusic.load_music("joy.bmc")
    player.play()

def test3():
    player = beepmusic.load_music("蜜雪冰城.bmc")
    try:
        while True:
                player.play()
                player.reset()
    except KeyboardInterrupt:
        print("明智的选择")
        exit()

if __name__ == "__main__":
    test3()