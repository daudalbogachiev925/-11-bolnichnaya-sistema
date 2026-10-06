SELECT a.id, p.full_name, a.admitted, a.discharged,
       a.discharged - a.admitted AS days,
       a.diagnosis, a.cost
FROM admissions a
JOIN patients p ON p.id = a.patient_id
WHERE a.discharged >= NOW() - INTERVAL '30 days'
ORDER BY a.discharged DESC;
