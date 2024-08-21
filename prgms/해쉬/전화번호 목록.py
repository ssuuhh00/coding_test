'''
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer
'''
def solution(phone_book):
    phone_dict = {}
    
    # 1단계: 전화번호 목록을 해시 테이블(딕셔너리)에 저장합니다.
    for number in phone_book:
        phone_dict[number] = 1
    
    # 2단계: 각 전화번호에 대해 접두사(prefix)를 하나씩 추가하면서 해시 테이블에서 접두사가 존재하는지 확인합니다.
    for number in phone_book:
        temp = ""
        for digit in number:
            temp += digit
            # 접두사가 해시 테이블에 있고, 그것이 현재 번호와 다르다면 접두사 관계가 존재합니다.
            if temp in phone_dict and temp != number:
                return False
                
    return True
