# try:
#     with open("data.txt","w") as file:
#         print(file)
# except FileNotFoundError:
#     print("It failed")
# else:
#     print("It worked")
# finally:
#     print("THIS will always run")

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not exceed 3 meters.")
bmi = weight / height ** 2
print(bmi)