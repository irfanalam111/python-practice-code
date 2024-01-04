er_data={'EC':'Amit','Ex':'Rohan','CSE':'Styam','CE':'Rehan'}
gr_data={'BBA':'Aarsh','BAC':'Dilip','LLB':'Ashok'}
for i in er_data:
    print(er_data.get(i))
print(er_data.keys())
print(er_data.items())
er_data.update(gr_data)
print(er_data)



