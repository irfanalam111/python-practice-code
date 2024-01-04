def find_large(*name):
    max=0
    largest=""
    for s in name:
        if len(s)>max:
            max=len(s)
            largest=s
            return largest
print(find_large("january","february","march"))
