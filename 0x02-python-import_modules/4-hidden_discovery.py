#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    s_dir = dir(hidden_4)
    for i in range(len(s_dir)):
        if s_dir[i][:2] != "__":
            print("{}".format(s_dir[i]))
