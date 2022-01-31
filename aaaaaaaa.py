list = ['D12-16 ceremonyflower M-G-3-1 HDR1.xlsx',
        'D12-16 ceremonyflower M-G-3-1 HDR2.xlsx',
        'D12-16 ceremonyflower M-G-3-1 HDR 3.xlsx',
        'D12-16 keycutstock M-G-3-3 HDR 3.xlsx', 
        'D12-16 msgmon_gunma M-G-3-1 HDR 1.xlsx', 
        'D12-16 msgmon_massage M-G-3-1 HDR 1.xlsx']

f_name =[]
# for i in list:
#     temp_i = i.split()
#     temp_i2 = i.split(temp_i[-2])
#     f_name.append(temp_i2[0])

for i in list:
    temp_i1 = i.split("HDR")
    f_name.append(temp_i1[0])

print(f_name)