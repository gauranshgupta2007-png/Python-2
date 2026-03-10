Student1={"Name":"William","Age" : 18 ,"DIV": "Soc-19","Course":"Python-II"}
Student2={"Name":"Dustin","Age" : 17 ,"DIV": "Soc-01","Course":"Python-II"}
print(Student1)
Student1["Batch"]="19-B"
print(Student1)
del Student1["DIV"]
Student1.update(Student2)
print(Student1)