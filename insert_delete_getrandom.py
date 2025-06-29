import random

class randomizedset():
    def __init__(self):
        self.num_list = []
        self.num_dic = {}
        
    def insert(self, num):
        if num in self.num_dic:
            print("number already added")
            return False
        self.num_list.append(num)
        self.num_dic[num] = len(self.num_list) - 1
        return True
    
    def remove(self,num):
        if num not in self.num_dic:
            return False
        index = self.num_dic[num]
        last_num = self.num_list[-1]
        
        self.num_list[index] = last_num
        self.num_dic[last_num] = index
        
        self.num_list.pop()
        del self.num_dic[num]
        
        return True
            
    def getrandom(self):
        ran = random.choice(self.num_list)
        return ran

rs = randomizedset()
rs.insert(10)
rs.insert(20)
print(rs.num_list)

print(rs.getrandom())