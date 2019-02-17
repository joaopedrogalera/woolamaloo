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
    employees_row = csv.DictReader(employees_data)

    for row in employees_row:
        if len(row["demission_date"])!=0:
            if row["id"] in ldap_employees:
                print(row["name"] + " worked at Woolamaloo from " + row["admission_date"] + " to " + row["demission_date"])
        else:
            if not row["id"] in ldap_employees:
                print(row["name"] + " Started to work at Woolamaloo on " + row["admission_date"])
            elif row["department"] != ldap_employees[row["id"]]["department"]:
                print(row["name"] + " changed department. Was " + ldap_employees[row["id"]]["department"] + " and now is " + row["department"])
            elif row["position"] != ldap_employees[row["id"]]["position"]:
                print(row["name"] + " changed position. Was " + ldap_employees[row["id"]]["position"] + " and now is " + row["position"])
