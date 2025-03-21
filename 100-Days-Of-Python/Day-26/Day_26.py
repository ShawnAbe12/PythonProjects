student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56,76,98]
}

# for (key,value) in student_dict.items():
#     # print(value[/0])
#     # print(key)
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (key,values) in student_data_frame.items():
#     print(key)
#     print(values)

for (index, row) in student_data_frame.iterrows():
    # print(index)
    if row.student == "Angela":
        print(row.score)