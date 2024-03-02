select
    Report_ID as "Report ID",
    Job_title as "Job title",
    Opening_date as "Opening date",
    Closing_date as "Closing_date",
    Min_salary as "Minimal salary",
    Max_salary as "Maximal salary"
from report_2
where
    Job_title = '$jt';