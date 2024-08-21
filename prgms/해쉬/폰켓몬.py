def solution(nums):
    ll = len(nums)
    answer = 0
    list = []
    for i in range(ll):
        if nums[i] not in list:
            list.append(nums[i])
            answer += 1
    if answer > ll/2:
        answer = ll/2
    return answer