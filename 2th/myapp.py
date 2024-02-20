from proj.tasks import add, devide


# result = add.delay(3, 5)
# print(result.get())


# result = devide.delay(100, 20)
# print(result.get())


# result = add.apply_async((14,5),countdown=10)
# print(result.get())

# result = devide.apply_async((33,3),countdown=5)
# print(result.get())

func = add.signature((2,19),countdown=10)
res=func.delay()
print(res.get())
res.forget()
