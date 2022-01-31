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
        temp_i = i.split()
        temp_i2 = i.split(temp_i[-2])
        if temp_i2[0] in f_name:
            continue
        else:
            f_name.append(temp_i2[0])
    break

for j in f_name:
    group_f = []
    for q in f:
        temp_q = q.split()
        temp_q2 = q.split(temp_q[-2])

        if j == temp_q2[0]:
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

        excel = excel.append(df, ignore_index=True)
    # 최종 데이터의 총 row 수를 저장
    las_column = len(excel)

    excel.to_excel(f"{path_2}\\{j}{las_column}.xlsx", index=False)
