select
    Report_ID as "ID отчёта",
    Inter_ID as "ID интервью",
    Candidate_FIO as "ФОИ кандидата",
    Employee_FIO as "ФИО интервьюер",
    Job_title as "Должность",
    Inter_date as "Дата"
from report_1
where
    year(Inter_date) = '$year' and
    month(Inter_date) = '$month';