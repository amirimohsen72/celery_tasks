from tasks import add ,devide

# result = add.delay(2,5)
# result.start()
# print(result.get())

result = add.delay(4, 3)
print(result)

print(result.status)

print(result.status)

# print(result.get())
# result22= add.apply_async([4, 5])


# s= devide.delay(3,1)
# print(s.get())

# def sumx(x,y):
#     print (str(x)  + '+' + str(y) )
#     return x+y
# r = sumx(545,100)

# a = add(2 ,8)
# print(a)