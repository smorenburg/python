from employee import Employee, DatabaseError, MissingEmployeeError

file_name = 'test_employee_file.txt'

try:
    remove(file_name)
except:
    pass

try:
    Employee.get_all(file_name)
except Exception as err:
    assert (
        err.__class__ == DatabaseError
    ), f'Expected DatabaseError but got {err.__class__.__name__}'
