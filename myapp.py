from tasks import add ,devide
import time
# result = add.delay(2,5)
# result.start()
# print(result.get())

result = add.delay(4, 3)

print(result)
print(result.status)
time.sleep(3)
print(result.status)
# --------------------------------
result22 = add.apply_async([4, 5])
print(result22)
print(result22.status)
time.sleep(3)
print(result22.status)
print(result22.get())

print('end')


# s= devide.delay(3,1)

# def sumx(x,y):
#     print (str(x)  + '+' + str(y) )
#     return x+y
# r = sumx(545,100)

# a = add(2 ,8)
# print(a)