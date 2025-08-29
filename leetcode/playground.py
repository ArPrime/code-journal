position = [3, 1, 4, 2]
speed = [30, 10, 40, 20]

# 创建元组列表
cars = list(zip(position, speed))
print("排序前:", cars)  # [(3, 30), (1, 10), (4, 40), (2, 20)]

# 排序
cars.sort()
print("排序后:", cars)  # [(1, 10), (2, 20), (3, 30), (4, 40)]