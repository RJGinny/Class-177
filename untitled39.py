#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 19:16:38 2022

@author: riddhiekajain
"""

class score():
    def __init__(self):
        self.__score = 1
        
    def showscore(self):
        print(self.__score)
        
    def update_score(self):
        self.__score = self.__score +1
        print(self.__score)
        
player = score()
player.score = 100
player.update_score()
player.update_score()