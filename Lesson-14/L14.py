from Task3 import Point
from random import randint

l=[Point(randint(-5,5),randint(-5,5)) for i in range(10)]
print(l)
ringPoints=list(filter(lambda p: 3>=abs(p)>=2,l))
print(ringPoints)
bigringPoints=[p*5 for p in ringPoints]
print(bigringPoints)
p1=Point(5,10)
newList=[p1*p for p in bigringPoints]
print(newList)

# p1=Point(4,5)
# p2=Point(1,2)
# print(abs(p1))
# p1.reset()
# print(abs(p1))
# print(-p1)
# p1-=p2
# print(p1)
# print(p1*p2)
# p1/=2
# # print(p1)
# print(p1>=p2)


# for component in p1:
#     print(component)
