class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        for i, each in enumerate(data):
            data[i] = bin(each)[2:]
            n = len(data[i])
            data[i] = (8-n)*'0' + data[i]
        
        data.sort()
        count = 0
        
        for each in data:
            if each[:2] == '10':
                count += 1
            if each[:5] == '11111':
                return False

        i = len(data) - 1
        if count == 0 and data[i][0]>='1':
            return False
        while i >= 0:
            if count < 0:
                return False
            if data[i][:5] == '11110':
                count -= 3
            elif data[i][:4] == '1110':
                count -= 2
            elif data[i][:3] == '110':
                count -= 1
            elif data[i][:2] == '10':
                break
            i -= 1
        if count>0:
            return False
        return True
