
# class Students:

#     def __init__(self, s_name):
#         self.my_name = s_name

#     def say_hello(self):
#         print("hi")
#         print(self.my_name)

# student = Students("Cormac")
# student.say_hello()

# Tuple example
# stock = ("fb", 75.00, 75.03, 74.90)
# print(stock)
# print(stock[1:3])

# from collections import namedtuple

# Stock  = namedtuple("Stock", "symbol current high low")
# stock = Stock("fb",current = 75.00, high = 75.03, low = 74.90)
# print("representation: ", stock)

# for p in [stock]:
#     print('%s: The current is %f and the high is %d, and the low is %d' %p)

#  Counter class
# from collections import Counter
# numbers = [2, 4, 6, 8, 8, 8, 2, 2]
# def get_num_freq(sentence):
#     return Counter(numbers)

# print(get_num_freq(numbers))
# length = len("hello world")
# print(length)

# random_key_dict = {}
# random_key_dict["hello"] = "world"
# random_key_dict[22] = "twenty-two"
# random_key_dict[2.2] = "two point two"
# random_key_dict[('abc', 123)] = "tuples work"
# print(random_key_dict)


# my_list = ["Hello", "hallo", "HELP", "Helo"]
# my_list.sort()
# print(my_list)


# kitchen_favourites = {"apples", "watermelon", "strawberries"}
# print(kitchen_favourites)
# print(kitchen_favourites)
# kitchen_favourites.update(["pears", "grapes"])
# print(kitchen_favourites)
# print(len(kitchen_favourites))
# try:
#     kitchen_favourites.remove("Hello")
# except Exception as e:
#     print(f"error occurred {e}")
# print(kitchen_favourites)

# other_favourites = {"honey", "maple syrup", "apples", "pancakes"}
# all_favourites = other_favourites.union(kitchen_favourites)
# print(all_favourites)



# print(line.empty())

# line.queue.clear()

# print(line.empty())

# fill with loop
# for i in range(1,4):
#    line.put(i)

# for i in line: # causes error that queue is not iterable
#     print(i)

# instead we use while
# while not line.empty():
#     print(line.get()) #get removes them, try just with line, see output in endless loop
#
# print(line.empty())

# for sorting needs to be cast into list first

from queue import Queue
line = Queue(maxsize=10)
line.put(8)
line.put(23)
line.put(18)
line.put(4)


line_list=[]
for i in range (1, 5):
   line_list.append(line.get())
line_list.sort()
print(line_list)

for number in line_list:
   line.put(number)

print(line.get())
# line_list = []
# for i in range(1,4):
#    line_list.append(line.get())
# line_list.sort(reverse=True)
# print(line_list)

# # move back to queue
# for number in line_list:
#    line.put(number)

# while not line.empty():
#    print(line.get())