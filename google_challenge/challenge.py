# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    l = len(A)
    l1 = l - 1
    possible_pos = 1 # 1 for end

    for m in range(l):
        oddJump = True
        j = m

        while (j < l):
            k = j + 1
            n = -1
            dif = 101

            if oddJump: # odd jump
                for i in range(k, l): # find min
                    if A[j] < A[i] and A[i] - A[j] < dif:
                        dif = A[i] - A[j]
                        n = i # index that satisfies conditions

                if n == l1: # reached end
                    possible_pos += 1
                    break
                elif n > -1: # attempting to reach end
                    print(' ' + str(A[n]))
                    j = n
                else: # couldn't reach end
                    break
            else: # even jump
                for i in range(k, l): # find min
                    if A[j] > A[i] and A[j] - A[i]  < dif:
                        dif = A[j] - A[i]
                        n = i # index that stisfies conditions

                if n == l1: # reached end
                    possible_pos += 1
                    break
                elif n > -1: # attempting to reach end
                    print(n)
                    j = n
                else: # couldn't reach end
                    break

            oddJump = not oddJump # next jump has different parity

    return possible_pos
    
