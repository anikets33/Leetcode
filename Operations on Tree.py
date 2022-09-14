class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.lockedBy = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.lockedBy:
            return False
        else:
            self.lockedBy[num] = user
            return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockedBy and self.lockedBy[num] == user:
            del self.lockedBy[num]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.lockedBy:
            return False
        i = num
        while i != -1:
            i = self.parent[i]
            if i in self.lockedBy:
                return False
        
        lockedDescendants = []
        def isDescendant(key, num):
            i = key
            while i != -1:
                i = self.parent[i]
                if i == num:
                    return True
            return False

        for key in self.lockedBy:
            if isDescendant(key, num):
                lockedDescendants.append(key)
                
        if not lockedDescendants:
            return False

        for each in lockedDescendants:
            del self.lockedBy[each]
        
        self.lockedBy[num] = user
        return True            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
