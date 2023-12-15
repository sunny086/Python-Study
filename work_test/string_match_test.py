def can_construct(target, strings):
    def backtrack(curr_index):
        if curr_index == len(target):
            result.append(list(combination))
            return
        for i in range(len(strings)):
            if visited[i] or len(strings[i]) + curr_index > len(target):
                continue
            if target[curr_index:curr_index + len(strings[i])] == strings[i]:
                visited[i] = True
                combination.append(i)
                backtrack(curr_index + len(strings[i]))
                visited[i] = False
                combination.pop()

    result = []
    visited = [False] * len(strings)
    combination = []

    backtrack(0)
    return result


# 已知字符串
known_string = "aabbbccc"

# 乱序集合
string_set = ['a', 'b', 'c', 'aa', 'aab', 'aabbb', 'cc', 'cc', 'ab', 'abbb', 'abbbc', 'aab', 'bccc', 'bc']

possible_combinations = can_construct(known_string, string_set)
sorted_combinations = sorted(possible_combinations)  # 排序索引组合

# 输出排序后的索引和对应数据
for i, combination in enumerate(sorted_combinations):
    print(f"第 {i + 1} 组索引：{' '.join(str(index) for index in combination)}")

    output = '\n'.join([string_set[i] for i in combination])
    print(output)
