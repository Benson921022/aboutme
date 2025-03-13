def square(y):
  print("{} 的平方為 {}".format(y, y*y)) 


x = int(input("請輸入一個正整數："))
if (x<0):
	print("您輸入的值是負數")
elif (x==0):
	print("您輸入的質為0")
else:
	for i in range(x):
		square(i)

