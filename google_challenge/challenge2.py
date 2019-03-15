# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, E):
    # write your code in Python 3.6
    guests = len(S)
    max_chairs = 0
    chairs = 0

    for i in range(1, max(E)):
        chairs -= E.count(i)
        chairs += S.count(i)

        if chairs > max_chairs:
            max_chairs = chairs


    return max_chairs
