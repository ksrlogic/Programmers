MONTH = 28
YEAR = MONTH * 12

def list_to_dict(data):
    dict1 = {}
    for i in data:
        key = i.split()[0]
        value = i.split()[1]

        dict1[key] = value

    return dict1

#날짜를 전부 day에 맞추어주는 함수
def everything_to_day(date):
    splited_day = date.split(".")
    for i in [0, 1, 2]:
        if splited_day[i][0] == "0":  # 첫번째 글자가 0이면
            splited_day[i] = splited_day[i][1]  # 지워라

    total = 0
    total += int(splited_day[0]) * YEAR
    total += int(splited_day[1]) * MONTH
    total += int(splited_day[2])

    return  total
# 날짜 차이를 구하는 함수
def day_diff(today, day2): #2020.01.01 #2019.11.15
    return  everything_to_day(today) - everything_to_day(day2)


def privacies_to_two_dimension(privacies):  # privacies를 2차원 배열화
    target = []
    for privacy in privacies:
        target.append(privacy.split(" "))

    return target

def solution(today, terms, privacies):
    answer = []

    terms_dict = list_to_dict(terms)
    # print(terms_dict)
    privacies_2d = privacies_to_two_dimension(privacies) #[['2000.06.16', 'A'], ['2008.02.15', 'A']]
    # print(terms_dict)
    # print(privacies_2d)
    i = 1
    # print("오늘날짜: {}".format(today))
    for privacy in privacies_2d:
        date = privacy[0]
        privacy[1] = int(terms_dict[privacy[1]]) * MONTH # 각각의 등급에 맞는 최대 날짜 수 로 등급을 변환
        day_difference = day_diff(today, date)#날짜 차이 계산
        # print("{}  vs  {}".format(day_difference, privacy[1]))
        if day_difference >= privacy[1]: # 한계 차이보다 날짜 차이가 작거나 같은 경우
            answer.append(i)
        i += 1
    return answer

a = list_to_dict(["Z 3", "D 5"])
b= list_to_dict( ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])

# print(solution( "2016.02.15", ["A 100"], ["2000.06.16 A", "2008.02.15 A"]))