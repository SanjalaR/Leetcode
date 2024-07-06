# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        counter = 1
        flag = True
        for i in range(time):
            print(counter)
            if flag:
                counter += 1
            else:
                counter -=1
            if counter == n:
                flag = False
            if counter == 1:
                flag = True
            
        return counter
        
