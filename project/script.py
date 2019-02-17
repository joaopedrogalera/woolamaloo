#Woolamaloo Syncronization Report
#Joao Pedro da Matta Galera da Silva

import csv
from tabulate import tabulate #the tabulate library must be installed to run this code with "pip install tabulate"

print("Woolamaloo Syncronization Report")
print("--------------------------------\n")

ldap_employees = {} #Create the dictionary ldap_employees
with open("ldap_export.csv",'r') as ldap_export:
    ldap_data = csv.DictReader(ldap_export) #Opens the .csv file with the ldap exported data and puts in a dictionary

    for row in ldap_data:
        ldap_employees[row["employeeNumber"]]=row #Puts each line from csv file in the ldap_employees using the employeeNumber as key

tableData = [] #Create the list which will be used to make the table with the reports
tableHeaders = ["ID","Name","Status"]#Define the table headers
with open("employees_data.txt","r") as employees_export:
    employees_data = csv.DictReader(employees_export) #Opens the file with the employees exported data and puts in a dictionary

    for row in employees_data: #For each entry
        if len(row["demission_date"])!=0: #If the employee doen't work at Woolamaloo anymore
            if row["id"] in ldap_employees: #And still is in the LDAP
                tableData.append([row["id"],row["name"],"Worked at Woolamaloo from " + row["admission_date"] + " to " + row["demission_date"]]) #Add an item on the tableData list with the report for this employee
        else: #If the employee still works at Woolamaloo
            if not row["id"] in ldap_employees: #and isn't in the LDAP
                tableData.append([row["id"],row["name"],"Started to work at Woolamaloo on " + row["admission_date"]]) #Add an item on the tableData list with the report for this employee
            elif row["department"] != ldap_employees[row["id"]]["department"]: #And department in the LDAP is distinct from the employees system
                tableData.append([row["id"],row["name"],"Changed department. Was " + ldap_employees[row["id"]]["department"] + " and now is " + row["department"]]) #Add an item on the tableData list with the report for this employee
            elif row["position"] != ldap_employees[row["id"]]["position"]: #And position in the LDAP is distinct from the employees system
                tableData.append([row["id"],row["name"],"Changed position. Was " + ldap_employees[row["id"]]["position"] + " and now is " + row["position"]]) #Add an item on the tableData list with the report for this employee

print(tabulate(tableData,tableHeaders)) #Print the table using the "Tabulate library"
