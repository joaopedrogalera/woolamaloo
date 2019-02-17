#Woolamaloo Syncronization Report
#Joao Pedro da Matta Galera da Silva

import csv

print("Woolamaloo Syncronization Report")
print("--------------------------------")

ldap_employees = {}
with open("ldap_export.csv",'r') as ldap_export:
    ldap_row = csv.DictReader(ldap_export)

    for row in ldap_row:
        ldap_employees[row["employeeNumber"]]=row

with open("employees_data.txt","r") as employees_data: #Open the file with the Employees data
    employees_data.readline() #skip 1st line
    employees_row = employees_data.readline()

    while len(employees_row)!=0:
        employees_row_fields = employees_row.split(',')


        if len(employees_row_fields)==6:
            if employees_row_fields[0] in ldap_employees:
                print(employees_row_fields[1] + " worked at Woolamaloo from " + employees_row_fields[2] + " to " + employees_row_fields[2])
        elif len(employees_row_fields)==5:
            if not employees_row_fields[0] in ldap_employees:
                print(employees_row_fields[1] + " Started to work at Woolamaloo on " + employees_row_fields[2])
            elif employees_row_fields[3] != ldap_employees[employees_row_fields[0]]["department"]:
                print(employees_row_fields[1] + " changed department. Was " + ldap_employees[employees_row_fields[0]]["department"] + " and now is " + employees_row_fields[3])
            elif employees_row_fields[4].rstrip('\n') != ldap_employees[employees_row_fields[0]]["position"]:
                print(employees_row_fields[1] + " changed position. Was " + ldap_employees[employees_row_fields[0]]["position"] + " and now is " + employees_row_fields[4].rstrip('\n'))
        print("-----------------------------")
        employees_row = employees_data.readline()
