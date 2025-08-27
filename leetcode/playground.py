def trap_water_two_pointers(height):
    """
    双指针解法
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    if not height or len(height) < 3:
        return 0
    
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


def trap_water_four_arrays(height):
    """
    四个数组解法：
    1. 从左向右记录最大值
    2. 从右向左记录最大值
    3. 计算两个数组的最小值（实际水位）
    4. 计算能装的水量
    
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    
    # 1. 从左向右记录每个位置左边的最大高度（包括自己）
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # 2. 从右向左记录每个位置右边的最大高度（包括自己）
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # 3. 计算每个位置的实际水位（左右最大值的最小值）
    water_level = [0] * n
    for i in range(n):
        water_level[i] = min(left_max[i], right_max[i])
    
    # 4. 计算每个位置能装的水量
    trapped_water = [0] * n
    total_water = 0
    for i in range(n):
        trapped_water[i] = max(0, water_level[i] - height[i])
        total_water += trapped_water[i]
    
    return total_water


def visualize_solution(height):
    """
    可视化展示四数组解法的过程
    """
    if not height:
        return
    
    n = len(height)
    print(f"原始高度: {height}")
    
    # 计算四个数组
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    water_level = []
    trapped_water = []
    for i in range(n):
        level = min(left_max[i], right_max[i])
        water_level.append(level)
        trapped_water.append(max(0, level - height[i]))
    
    print(f"左侧最大: {left_max}")
    print(f"右侧最大: {right_max}")
    print(f"水位高度: {water_level}")
    print(f"装水数量: {trapped_water}")
    print(f"总装水量: {sum(trapped_water)}")


# 测试用例
if __name__ == "__main__":
    # 测试用例1
    test_case1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("=== 测试用例1 ===")
    print(f"双指针解法结果: {trap_water_two_pointers(test_case1)}")
    print(f"四数组解法结果: {trap_water_four_arrays(test_case1)}")
    print()
    visualize_solution(test_case1)
    
    print("\n" + "="*50 + "\n")
    
    # 测试用例2
    test_case2 = [3, 0, 2, 0, 4]
    print("=== 测试用例2 ===")
    print(f"双指针解法结果: {trap_water_two_pointers(test_case2)}")
    print(f"四数组解法结果: {trap_water_four_arrays(test_case2)}")
    print()
    visualize_solution(test_case2)