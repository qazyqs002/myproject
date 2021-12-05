"""
二分法算法是一个查找算法
要求：数据是有序序列
核心思想：掐头结尾取中间
"""
lis = [12, 14, 54, 111, 123, 145, 167, 189, 198, 231, 213, 255, 2445]


def get_index(num):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if num > lis[mid]:
            left = mid + 1
        elif num < lis[mid]:
            right = mid - 1
        else:  # 等于则是目标数
            print(f"找到数据，下标号为：{mid}")
            break
    else:
        print("在序列中没有找到数据")


if __name__ == "__main__":
    get_index(125)




