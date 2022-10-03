#!/usr/bin/python3
""" module define function to save
args in file using list format"""
import json
import sys


if __name__ == "__main__":
    item = ""
    with open("add_item.json", "r+", encoding="UTF-8") as f:
        for index, item in enumerate(sys.argv):
            if index > 0:
            
