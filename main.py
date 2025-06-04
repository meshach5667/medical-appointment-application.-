from fastapi import FastAPI
from routers.patient_router import router as patient_router
from routers.doctor_router import router as doctor_router
from routers.appointment_router import router as appointment_router

app = FastAPI()

app.include_router(patient_router, prefix="/patients", tags=["patients"])
app.include_router(doctor_router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment_router, prefix="/appointments", tags=["appointments"])


app.get