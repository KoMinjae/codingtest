for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    ans = 0
    idx = 0
    tmp = 0
    while idx < len(numbers):
        if not tmp:
            tmp = int(numbers[idx])
            idx += 1
            continue
 
 
        while idx < len(numbers) and numbers[idx] != '+':
            if numbers[idx].isdigit():
                tmp *= int(numbers[idx])
            idx += 1
        ans += tmp
        tmp = 0
        idx += 1
    ans += tmp
    print(f'#{tc} {ans}')