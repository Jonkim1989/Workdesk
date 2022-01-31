from ast import NotIn
import os
from os import walk
import pandas as pd

path_1 = r"C:\Users\kangg\Desktop\리포트 마무리\작업 대기"
path_2 = r"C:\Users\kangg\Desktop\리포트 마무리"

f = []
f_name = []

for (dirpath, dirnames, filenames) in walk(path_1):
    f.extend(filenames)
    for i in filenames:
        temp_i = i.split("HDR")
        if temp_i[0] in f_name:
            continue
        else:
            f_name.append(temp_i[0])
    break

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

        # 필요없는 열 삭제
        df.drop(["Status", "Username", "Password", "E-Mail"],
                axis="columns", inplace=True)
        # 필요없는 행 삭제
        spac = df[df['Task ID'].str.contains('Task ID')].index
        df.drop(spac, inplace=True)

        # 제거할 도메인 리스트
        drop_list = ["simplesite.com",
                     "edublogs.org",
                     "penzu.com",
                     "storeboard.com",
                     "theglensecret.com",
                     "theburnward.com",
                     "fotosdefrases.com",
                     "zenwriting.net"]

        # for문을 통해 도메인이 있는 행을 제거
        for h in drop_list:
            idx = df[df["Site URL"] == h].index     # Site URL 중에 j 값이 저장됨
            df.drop(idx, inplace=True)  # 해당 인덱스를 제거함


        # 인덱스 재정렬
        # df.reset_index(drop=True, inplace=True)


        # 최종 정리후 저장
        excel = excel.append(df, ignore_index=True)


    # 최종 데이터의 총 row 수를 저장
    las_column = len(excel)

    excel.to_excel(f"{path_2}\\{j}{las_column}.xlsx", index=False)


# drop_list를 외부로 꺼내서 def 형식으로 불러오게 해야함
# 판다스 작업은 끝났고 엑셀로 꾸미는 코드를 짜야함

# 이걸 하나하나 코드로 짤것인지 아니면 템플릿과 합쳐서 따로 저장할 것인지 생각해야 한다.
