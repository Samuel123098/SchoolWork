Student_Data_Base = {}
Name = input("Please enter your name")
Age = int(input("Please enter your age"))
Grade = input("Please enter your Grade")
StudentID = int(input("Please input StudentID"))



Student_Data_Base[StudentID] = {
    "Name" : Name,
    "Age" : Age,
    "Grade" : Grade

}

print(Student_Data_Base)