#!/usr/bin/python3

for i in range(0, 100):
    print(f"{'0' if i < 10 else ''}{i:d}", end=('\n' if i == 99 else ", "))
