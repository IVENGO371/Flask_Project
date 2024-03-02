SELECT ROUTINE_NAME as proc_name, ROUTINE_COMMENT as href_name FROM information_schema.routines
WHERE routine_schema = 'rk6-43b_rogovmv' and ROUTINE_NAME = '$proc';