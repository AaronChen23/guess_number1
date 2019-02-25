import random
start = input("請輸入猜的起始值")
end = input("請輸入猜的結束值")
start = int(start)
end = int(end)
r = random.randint(start, end)

while True:
	num = input("請輸入你猜的數字")
	num = int(num)
	if num == r:
		print("恭喜妳!猜對數字嘞")
		break
	elif num > r:
		print("你猜的數字比較大喔")	
	elif num < r:
		print("你猜的數字比較小喔")	