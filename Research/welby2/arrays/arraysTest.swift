var arr: [Int] = []

for i in 1 ... 100 {
	arr.append(i)
}

for item in arr {
	print(item)
}

for item in arr.reversed() {
	print(item)
}
