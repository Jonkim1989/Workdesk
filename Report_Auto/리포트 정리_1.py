import os
from os import walk
import pandas as pd

path_1 = r"C:\Users\kangg\Desktop\리포트 마무리\작업 대기"
path_2 = r"C:\Users\kangg\Desktop\리포트 마무리\pd작업"

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

        # 필요없는 열 삭제
        df.drop(["Status", "Username", "Password", "E-Mail"],
                axis="columns", inplace=True)
        # 필요없는 행 삭제 (아래 도메인 제거 코드에서 작업 가능 함)
        # spac = df[df['Task ID'].str.contains('Task ID')].index
        # df.drop(spac, inplace=True)

        # 제거할 도메인 리스트
        drop_list = ["Site URL",
                     "simplesite.com",
                     "edublogs.org",
                     "penzu.com",
                     "storeboard.com",
                     "theglensecret.com",
                     "theburnward.com",
                     "fotosdefrases.com",
                     "zenwriting.net",
                     "onfeetnation.com"]

        # for문을 통해 도메인이 있는 행을 제거
        for h in drop_list:
            idx = df[df["Site URL"] == h].index     # Site URL 중에 j 값이 저장됨
            df.drop(idx, inplace=True)  # 해당 인덱스를 제거함

        # 인덱스 재정렬
        # df.reset_index(drop=True, inplace=True)

        # 최종 정리후 저장
        excel = excel.append(df, ignore_index=True)

    # 데이터를 내림차순으로 정렬 (작업 속도가 상승하는지 체크 필요)
    # excel = excel.sort_values(by=["Task ID"], ascending=True)

    # 저장 전 Tasks 순서대로 정렬하기
    excel_2 = pd.DataFrame()
    Tasks = ["Web 2.0 Blogs", "Social Bookmarking",
             "Authority Links", "Edu", "URL Shortener"]

    for t in Tasks:
        temp_task = excel[excel["Task ID"].str.contains(t)]
        excel_2 = excel_2.append(temp_task, ignore_index=True)

    # 최종 데이터의 총 row 수를 저장
    las_row = len(excel_2)

    # 엑셀로 정리하기 전에 정렬하기, 이후 꾸미기까지
    excel_2.to_excel(f"{path_2}\\{j}{las_row}.xlsx", index=False)


# drop_list를 외부로 꺼내서 def 형식으로 불러오게 해야함
# 판다스 작업은 끝났고 엑셀로 꾸미는 코드를 짜야함

# 이걸 하나하나 코드로 짤것인지 아니면 템플릿과 합쳐서 따로 저장할 것인지 생각해야 한다.
