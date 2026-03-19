def Split(x):
	x = x.split(",")
	school = x[0].replace("我是", "")
	print(f"學校:{school}")
	print(f"系級:{x[1]}")
	print(f"姓名:{x[2]}")

Name = "我是靜宜大學,資管二B,謝雨安"
Split(Name)

#只有直接執行example1.py時,以下程式才會跑
if __name__=="__main__":
	Name = "我是靜宜大學,資管二B,謝雨安"
	Split(Name)