import csv

with open('Var_Values_D.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        try:
            if row[1] == 'DrowsiTime':
                eye_Counter = int(row[2])
                print(eye_Counter)
            else:
                print("eye Not Found!!")
            if row[1] == 'SelectEye':
                index = int(row[2])
                print(index)
            else:
                print("select Not Found!!")
        except:
            continue