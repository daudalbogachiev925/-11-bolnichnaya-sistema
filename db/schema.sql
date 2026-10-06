CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    head TEXT
);

CREATE TABLE wards (
    id SERIAL PRIMARY KEY,
    dept_id INT REFERENCES departments(id),
    number TEXT NOT NULL,
    beds INT NOT NULL,
    floor INT
);

CREATE TABLE patients (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth DATE,
    policy TEXT UNIQUE,
    phone TEXT
);

CREATE TABLE admissions (
    id BIGSERIAL PRIMARY KEY,
    patient_id BIGINT REFERENCES patients(id),
    ward_id INT REFERENCES wards(id),
    admitted DATE NOT NULL,
    discharged DATE,
    diagnosis TEXT,
    cost NUMERIC(12,2),
    status TEXT DEFAULT 'active'
);

CREATE TABLE prescriptions (
    id BIGSERIAL PRIMARY KEY,
    admission_id BIGINT REFERENCES admissions(id) ON DELETE CASCADE,
    drug TEXT,
    dosage TEXT,
    duration_days INT
);

CREATE INDEX idx_adm_patient ON admissions(patient_id);
CREATE INDEX idx_adm_ward ON admissions(ward_id);
CREATE INDEX idx_adm_dates ON admissions(admitted, discharged);
