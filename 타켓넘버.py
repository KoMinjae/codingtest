def solution(numbers, target):
    stack = [(0, 0)]
    while stack:
        current_sum, num_idx = stack.pop(0)

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

solution([1,1,1,1,1],3)