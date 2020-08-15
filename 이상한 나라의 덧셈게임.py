T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    nums = input()
    turn = 0
    answer=""
    while len(nums)!=1:
        nums=str(int(nums[0])+int(nums[1]))+nums[2::]
        turn+=1
    print('#{} {}'.format(test_case, "B" if turn %2 == 0 else "A"))
    # ///////////////////////////////////////////////////////////////////////////////////
