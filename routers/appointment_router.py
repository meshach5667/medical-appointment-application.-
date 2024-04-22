from fastapi import APIRouter, HTTPException
from schemas.appointment import Appointment
from services.services import AppointmentService
from services.doctorService import DoctorService

router = APIRouter()

@router.post("/", response_model=Appointment)
def create_appointment(patient_id: int):
    # Find an available doctor
    for doctor in DoctorService.doctors_db:
        if doctor.is_available:
            appointment_id = len(AppointmentService.appointments_db) + 1
            appointment = Appointment(id=appointment_id, patient_id=patient_id, doctor_id=doctor.id, date="2024-04-20")
            AppointmentService.create_appointment(appointment)
            doctor.is_available = False
            return appointment
    # If no available doctor found
    raise HTTPException(status_code=404, detail="No available doctors")

@router.put("/{appointment_id}")
def complete_appointment(appointment_id: int):
    return AppointmentService.complete_appointment(appointment_id)

@router.delete("/{appointment_id}")
def cancel_appointment(appointment_id: int):
    return AppointmentService.cancel_appointment(appointment_id)
@router.get("/", response_model=list[Appointment])
def get_appointments():
    return AppointmentService.get_appointments()

@router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    return AppointmentService.get_appointment(appointment_id)

@router.get("/patient/{patient_id}", response_model=list[Appointment])
def get_appointments_by_patient(patient_id: int):
    return AppointmentService.get_appointments_by_patient(patient_id)