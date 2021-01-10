from employee import Employee

file_name = 'test_employee_file.txt'

with open(file_name, 'w') as f:
    f.writelines(
        [
            'Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n',
            'Bruce Wayne,bwayne@example.com,President,\n'
        ]
    )

employees = Employee.get_all(file_name)

assert len(employees) == 2

assert (
    Employee.get_at_line(1, file_name).__dict__ == employees[0].__dict__
)

cmo = Employee('Batty White', 'bwhite@example.com', 'CMO')
cmo.save(file_name)

assert len(Employee.get_all(file_name)) == 3

president = employees[1]

president.phone_number = '555-555-5555'
president.save(file_name)

new_president = Employee.get_at_line(president.identifier, file_name)

assert new_president.phone_number == '555-555-5555'
