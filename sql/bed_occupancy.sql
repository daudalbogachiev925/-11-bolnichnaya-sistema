SELECT d.name AS dept, w.number AS ward, w.beds,
       COUNT(a.id) FILTER (WHERE a.status='active') AS occupied,
       w.beds - COUNT(a.id) FILTER (WHERE a.status='active') AS free,
       ROUND(100.0 * COUNT(a.id) FILTER (WHERE a.status='active') / w.beds, 1) AS pct
FROM wards w
JOIN departments d ON d.id = w.dept_id
LEFT JOIN admissions a ON a.ward_id = w.id
GROUP BY d.name, w.id
ORDER BY pct DESC;
