SELECT Interview_ID, vacancy.Job_title, employee.emp_FIO, candidate.Candid_FIO, interview.Date_of
FROM interview
JOIN interview_info ON interview.Interview_ID = interview_info.Inter_ID
JOIN vacancy ON interview_info.Vacan_ID = vacancy.Vacancy_ID
JOIN employee ON employee.Employee_ID=interview_info.Empl_ID
JOIN candidate ON interview_info.Candid_ID=candidate.Candidate_ID
WHERE vacancy.Job_title='$jt'
