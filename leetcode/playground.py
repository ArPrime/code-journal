nums = [10, 20, 30, 40, 50, 60, 70]
m, n = 2, 5

for i, num in enumerate(nums, start= 100):  # 没有 start=m
    print(f"Index {i}: {num}")