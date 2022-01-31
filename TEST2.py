from os import walk
import os
import pandas as pd

path_1 = r"C:\Users\kangg\Desktop\리포트 마무리\작업 대기"
path_2 = r"C:\Users\kangg\Desktop\리포트 마무리"
f = []
for (dirpath, dirnames, filenames) in walk(path_1):
    f.extend(filenames)
    break

f1 = f[0]
print(f1[0:15])
# for i in f:
#     F_name = i.replace(".xlsx", "")
#     sn = "Sheet1"
#     df = pd.read_excel(path_1 + "\\" + i, sheet_name=sn)
    
#     result = pd.concat(i)


# las_column = len(result)

# result.to_excel(f"{path_2}\\{F_name} {las_column}.xlsx", index=False)

# 해당 리스트에 있는 항목을 하나로 합치고 다른 폴더로 저장 후 기존 리포트들 삭제
# 끝나면 가공 작업 시작 or 합치고 가공해서 배출

