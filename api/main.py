from fastapi import FastAPI
from routes import departments, wards, patients, admissions, prescriptions, reports

app = FastAPI(title="Hospital API")
app.include_router(departments.router, prefix="/departments", tags=["departments"])
app.include_router(wards.router, prefix="/wards", tags=["wards"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(admissions.router, prefix="/admissions", tags=["admissions"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
