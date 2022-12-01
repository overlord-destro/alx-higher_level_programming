#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    newl = dir(hidden_4)
    for i in range(len(newl)):
        if newl[i][0] != "_":
            print(newl[i])
        else:
            pass
