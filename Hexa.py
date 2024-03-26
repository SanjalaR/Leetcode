#Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
class Solution:
    def toHex(self, num: int) -> str:
        rem = []
        if num==0:
            return "0"
        if num<0:
            num +=2**32
        while(num>0):
            r = int(num%16)
            rem.append(r)
            num=num//16
        for i in range(len(rem)):
            if rem[i]==10:
                rem[i]='a'
            if rem[i]==11:
                rem[i]='b'
            if rem[i]==12:
                rem[i]='c'
            if rem[i]==13:
                rem[i]='d'
            if rem[i]==14:
                rem[i]='e'
            if rem[i]==15:
                rem[i]='f'
        return "".join(map(str, rem[::-1]))
