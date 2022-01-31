import pandas as pd

path_1 = r"C:\Users\kangg\Desktop\리포트 마무리\작업 대기"

df = pd.read_excel(path_1 + "\\" + "D01-31 obamjuso M-G-3-3 HDR 1.xlsx").sort_values(by=["Task ID"], ascending=True)

# 1번 column 기준으로 정렬
# sort_df = df.sort_values(by=["Task ID"], ascending=True) # ascending 가 true 명 내림차순, false면 오름차순 정렬

excel = pd.DataFrame()

Web_20_Blogs = df[df["Task ID"].str.contains("Web 2.0 Blogs")]
Authority_Links = df[df["Task ID"].str.contains("Authority Links")]
Edu = df[df["Task ID"].str.contains("Edu")]
Social_Bookmarking = df[df["Task ID"].str.contains("Social Bookmarking")]
URL_Shortener = df[df["Task ID"].str.contains("URL Shortener")]

excel = excel.append(Web_20_Blogs, ignore_index=True)
excel = excel.append(Authority_Links, ignore_index=True)
excel = excel.append(Edu, ignore_index=True)
excel = excel.append(Social_Bookmarking, ignore_index=True)
excel = excel.append(URL_Shortener, ignore_index=True)
print(excel)

# reqd_Index = df[df['Sales']>=300].index.tolist()

# 리스트를 "Web 2.0 Blogs", "URL Shortener", "Authority Links" 등으로 만들어서 
# 1번 column 의 txt 가 일치하면 리스트에 넣었다가 나중에 정렬해서 저장시키면 되겠다.



