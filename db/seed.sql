INSERT INTO departments (name, head) VALUES
('Терапия','Иванов И.И.'),('Хирургия','Петров П.П.'),('Кардиология','Сидоров С.С.');

INSERT INTO wards (dept_id, number, beds, floor) VALUES
(1,'101',4,1),(1,'102',4,1),(1,'103',2,1),
(2,'201',3,2),(2,'202',3,2),
(3,'301',2,3),(3,'302',2,3);

INSERT INTO patients (full_name, birth, policy) VALUES
('Сидоров А.А.','1985-05-05','POL001'),
('Кузнецова М.И.','1990-08-15','POL002'),
('Орлов В.П.','1978-02-20','POL003'),
('Никитина Е.С.','1995-11-10','POL004');

INSERT INTO admissions (patient_id, ward_id, admitted, discharged, diagnosis, cost, status) VALUES
(1,1,'2024-01-10','2024-01-20','J18',25000,'closed'),
(1,4,'2024-02-05',NULL,'K35',NULL,'active'),
(2,3,'2024-01-15','2024-01-22','I10',18000,'closed'),
(3,5,'2024-02-01',NULL,'I20',NULL,'active'),
(4,6,'2024-02-10',NULL,'G43',NULL,'active');
