import csv

# filename = "Criminal_count.csv"
# num=0
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([5])
def insertData(data):
    field=['Name', "Father's Name", "Gender", "DOB","Crimes"]
    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    filen = "Criminal.csv"
    with open(filen, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)
