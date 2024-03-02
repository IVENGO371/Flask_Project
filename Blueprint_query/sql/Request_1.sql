SELECT vacancy.Job_title, Opening_date, staffing.Min_salary FROM vacancy JOIN staffing ON vacancy.Job_title=staffing.Job_title WHERE vacancy.Job_title='$jt' order by Vacancy_ID;
