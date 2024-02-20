from proj.tasks import add, devide

from proj.celery import app
from celery import group,chain


# result = add.delay(3, 5)
# print(result.get())


# result = devide.delay(100, 20)
# print(result.get())


# result = add.apply_async((14,5),countdown=10)
# print(result.get())

# result = devide.apply_async((33,3),countdown=5)
# print(result.get())

# func = add.signature((2,19),countdown=10)
# res=func.delay()
# print(res.get())
# res.forget()



# f = lambda x: x+1
# print(f(2))
# g = group(add.s(i,i) for i in range(10))
# print(g().get())

# r = group(add.s(i,i) for i in range(10))().get()
# print(r)

# g = group(add.s(i) for i in range(10))
# print(g(10).get())


# ch = chain(add.s(2,8) | add.s(2))
# print(ch().get())
# 


ch = chain(add.s(3) | add.s(2))
print(ch(5).get())

