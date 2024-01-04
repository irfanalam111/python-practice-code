try:
     class computer_secince:
        subject = {1543: 'phycis', 3456: 'chemistry', 8568: 'math', 5467: 'basic civil', 8976: 'basic machenical'}
        def __init__(self,subject,serial_no):
            self.subject=subject
            self.serial_no=serial_no
        def __str__(self):
            return f"subject is : {self.subject}"




except TypeError:
    print("some error")