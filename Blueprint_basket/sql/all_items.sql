SELECT
    Candidate_ID as c_ID,
    Candid_FIO as c_FIO,
    Vacancy_for_ID as v_ID,
    Job_title as jt
FROM candidate
JOIN Vacancy on
    candidate.Vacancy_for_ID = Vacancy.Vacancy_ID
