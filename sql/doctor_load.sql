SELECT d.name AS dept, d.head,
       COUNT(a.id) AS total_admissions,
       COUNT(a.id) FILTER (WHERE a.status='active') AS now_active,
       AVG(a.discharged - a.admitted) AS avg_stay_days
FROM departments d
LEFT JOIN wards w ON w.dept_id = d.id
LEFT JOIN admissions a ON a.ward_id = w.id
GROUP BY d.id
ORDER BY total_admissions DESC;
