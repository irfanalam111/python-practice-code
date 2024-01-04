All_data={'EC': 'Amit', 'Ex': 'Rohan', 'CSE': 'Styam', 'CE': 'Rehan', 'BBA': 'Aarsh', 'BAC': 'Dilip', 'LLB': 'Ashok'}
for i in All_data:
    # print(All_data.get(i))
    print(f"Stream of student : {i} name of student : {All_data.get(i)}")
print(All_data.pop('EC'))
print(All_data.clear())