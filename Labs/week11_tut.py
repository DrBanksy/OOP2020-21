class MyDemo:
    def __init__(self,a_list):
        self.my_list = a_list
    
    def mean(self):
        return sum(self.my_list) / len(self.my_list)
    
    def median(self):
        if len(self.my_list) % 2:
            return int(len(self.my_list) / 2)
        else:
            idx = int(len(self.my_list) / 2)
            return (self.my_list[idx] + self.my_list[idx-1]) / 2
        
# demo = MyDemo([1,2,3,4,5,6,7,7,7])
# print(demo.mean())