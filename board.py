# total_dictionary = {}

# while True:
#     question = input("질문을 입력해주세요 : ")
#     if question == "q":
#         break
#     else:
# total_dictionary[question] = ""
# 질문이 key, ""가 답변자리로 value인 딕셔너리 생성

# for i in total_dictionary:
#     print(i)
#     answer = input("답변을 입력해주세요 : ")
#     total_dictionary[i] = answer
# print(total_dictionary)

total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문": question, "답변": ""})

for i in total_list:
    print(i["질문"])
    # i[key값] == value 값
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)
