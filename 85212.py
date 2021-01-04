data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
data_count = len(data)
target = 16
found_index = binary_search(data, 0, data_count-1, target)
if found_index == -1:
    print('無法找到搜尋目標', target)
else:
    print('發現搜尋目標', target, ', 位於陣列中第', found_index, '個位置')