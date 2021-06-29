def solution(nums):
    unique = len(set(nums))
    print(set(nums))
    print(unique)
    if len(nums)/2 >= unique:
        return unique
     # 중복을 제거한 nums의 길이가 unique와 크거나 같으면 가질 수 있는 최대 종류는 pick과 같다.    
    else:
        return len(nums)/2


# 심플, if문 쓸것없이 경우의 수가 2가지이므로 min으로 나눔
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
