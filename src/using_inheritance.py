from manager import Manager
from employee import Employee
from datetime import datetime

manager_1 = Manager('Bruce Wayne', 'bwayne@example.com', 'CEO')
employee_1 = Employee(
    name='Kevin Bacon',
    title='Executive Producer',
    email_address='kbacon@example.com',
    phone_number='555-867-5309'
)

assert (
    manager_1.email_signature() == 'Bruce Wayne - CEO\nbwayne@example.com'
)

assert (
    manager_1.email_signature(include_phone=True)
    == 'Bruce Wayne - CEO\nbwayne@example.com'
)

assert (
    manager_1.meetings == []
)

meeting_time1 = datetime(2020, 2, 29, 12, 0, 0)
meeting_time2 = datetime(2020, 1, 1, 15, 0, 0)
meeting_time3 = datetime(2020, 1, 1, 14, 0, 0)

invitees = [employee_1]

manager_1.schedule_meeting(invitees, meeting_time1)
manager_1.schedule_meeting(invitees, meeting_time2)
manager_1.schedule_meeting(invitees, meeting_time3)

expected_meeting = {'time': meeting_time3, 'invitees': invitees}

assert (
    manager_1.meetings[0] == expected_meeting
)

result = manager_1.run_next_meeting()

assert (
    result == expected_meeting
)

assert (
    len(manager_1.meetings) == 2
)
