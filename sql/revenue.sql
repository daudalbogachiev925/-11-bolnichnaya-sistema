SELECT d.name AS dept,
       COUNT(a.id) FILTER (WHERE a.status='closed') AS closed,
       COALESCE(SUM(a.cost) FILTER (WHERE a.status='closed'),0) AS revenue,
       COALESCE(AVG(a.cost) FILTER (WHERE a.status='closed'),0) AS avg_check
FROM departments d
LEFT JOIN wards w ON w.dept_id = d.id
LEFT JOIN admissions a ON a.ward_id = w.id
GROUP BY d.id
ORDER BY revenue DESC;
