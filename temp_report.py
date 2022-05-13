import os
from os import walk
import pandas as pd

path_1 = r"C:\Users\jonkim\Desktop\리포트 마무리\1. 작업 대기"
path_2 = r"C:\Users\jonkim\Desktop\리포트 마무리\1. 작업 대기\pd작업"
path_3 = r"C:\Users\jonkim\Desktop\리포트 마무리\GSA용"

f = []
f_name = []

# 작업 폴더에 있는 파일의 filenames 만 리스트에 저장 
for (dirpath, dirnames, filenames) in walk(path_1):
    f.extend(filenames)
    for i in filenames:
        temp_i = i.split("HDR")
        if temp_i[0] in f_name:
            continue
        else:
            f_name.append(temp_i[0])
    break # 이 break가 꼭 필요할까?

# 같은 이름의 파일들을 묶어주기
for j in f_name:
    group_f = []
    for q in f:
        temp_q = q.split("HDR")
        if j == temp_q[0]:
            group_f.append(q)
        else:
            continue

    excel = pd.DataFrame()
    for file_name in group_f:
        df = pd.read_excel(path_1 + "\\" + file_name)

        df.dropna(inplace=True)  # 빈 셀이 있는 행을 삭제
        df.drop_duplicates(inplace=True)  # 중복 항목 제거
        # 최종 정리후 저장
        excel = excel.append(df, ignore_index=True)

    # 데이터를 내림차순으로 정렬 (작업 속도가 상승하는지 체크 필요)
    # excel = excel.sort_values(by=["Task ID"], ascending=True)


    # 최종 데이터의 총 row 수를 저장
    las_row = len(excel)

    # 엑셀로 정리하기 전에 정렬하기, 이후 꾸미기까지
    excel.to_excel(f"{path_2}\\{j}{las_row}.xlsx", index=False)

# drop_list를 외부로 꺼내서 def 형식으로 불러오게 해야함
# 판다스 작업은 끝났고 엑셀로 꾸미는 코드를 짜야함

# 이걸 하나하나 코드로 짤것인지 아니면 템플릿과 합쳐서 따로 저장할 것인지 생각해야 한다.