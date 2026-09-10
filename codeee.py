import csv
with open("students.csv","w")as file:
    writer = csv.writer(file)
    
    writer.writerow(["RollNo","Name","Marks"])
    
    writer.writerow([101,"Diya",85])
    writer.writerow([102,"Bob",90])
    writer.writerow([103,"Paul",78])
    
print("Data written to students.csv successfully.")
    