student_data={13:'amit',12:'rohan',15:'chetan',17:'ram',18:'shyam'}
student_data2={14:'rahul',19:'shyam',20:'bittu'}
for i in student_data:
    print("roll is : ",i,"name is : ",student_data[i])
    print(student_data.get(i))
print(student_data.keys())
student_data[13]="sonu"
print(student_data)
student_data.update(student_data2)
print(student_data)
