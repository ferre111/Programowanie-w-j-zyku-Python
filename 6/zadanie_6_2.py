# import csv
#
# with open("acc_data.csv", "r") as csv_file:
#     csv_read = csv.reader(csv_file, delimiter=',')
#     for row in csv_read:
#         print(", ".join(row))

import pandas

df = pandas.read_csv("acc_data.csv")
print(df)

while True:
    print("Choose operations:\n -\"N\"-new row\n -\"D\"-delete row")
    input_s = input()

    if input_s == "N":
        print("Pass x axis value: ")
        x_axis = int(input())
        print("Pass y axis value: ")
        y_axis = int(input())
        print("Pass z axis value: ")
        z_axis = int(input())

        data = pandas.DataFrame({'x axis': x_axis, 'y axis': y_axis, 'z axis': z_axis, }, index=[0])
        df = df.append(data, ignore_index=False)
        df = df.sort_index().reset_index(drop=True)
    elif input_s == "D":
        print("Pass index row to drop: ")
        index = int(input())
        try:
            df = df.drop(index=index)
        except:
            print("Wrong index!")
    else:
        print("Wrong operation!")

    df.to_csv("acc_data.csv", index = False)
    print(df)
