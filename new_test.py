import pandas as pd

path_1 = r"C:\Users\kangg\Desktop\리포트 마무리\작업 대기"

df = pd.read_excel(path_1 + "\\" + "D01-31 obamjuso M-G-3-3 HDR 1.xlsx")

# 1번 column 기준으로 오름차순으로 정렬
sort_df = df.sort_values(by=["Task ID"], ascending=False)

for i in sort_df:
    print(i[0])



# 리스트를 "Web 2.0 Blogs", "URL Shortener", "Authority Links" 등으로 만들어서 
# 1번 column 의 txt 가 일치하면 리스트에 넣었다가 나중에 정렬해서 저장시키면 되겠다.



