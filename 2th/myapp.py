from proj.tasks import add, devide

result = add.delay(3, 5)
print(result.get())


result = devide.delay(100, 20)
print(result.get())
