SELECT Employee_ID as User_ID, User_group
FROM employee
JOIN user_groups ON
    employee.User_group_ID = user_groups.Group_ID
WHERE Login='$login' AND Password='$password'