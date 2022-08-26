class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def anagram(a, b):
            if len(a) != len(b):
                return False
            
            d = Counter(a)
            for each in b:
                if each in d and d[each] != 0:
                    d[each] -= 1
                else:
                    return False
            return True
        
        two = []
        for i in range(30):
            two.append(str(pow(2, i)))
        
        s = str(n)
        
        for each in two:
            check = anagram(each, s)
            if check:
                return True
        return False
