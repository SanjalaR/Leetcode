class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        big = ['Thousand', 'Million', 'Billion']
        res = self.numToWordsHelper(num%1000)
        num//=1000
        for i in range(len(big)):
            if num>0 and num%1000>0:
                res = self.numToWordsHelper(num%1000) + big[i] + " " + res
            num//=1000
        return res.strip()
    def numToWordsHelper(self, num):
        digit = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ten = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        result = ''
        if num>99:
            result+=digit[num//100]+' Hundred '
        num %= 100
        if num<20 and num > 9:
            result += teen[num - 10] + " "
        else:
            if num >= 20:
                result += ten[num // 10] + " "
            num %= 10
            if num > 0:
                result += digit[num] + " "
        
        return result
        
        
