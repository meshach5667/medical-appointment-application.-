from fastapi import APIRouter, HTTPException
from typing import List
from schemas.doctors import Doctor
from services.doctorService import DoctorService

router = APIRouter()

@router.post("/", response_model=Doctor)
def create_doctor(doctor: Doctor):
    return DoctorService.create_doctor(doctor)

@router.get("/", response_model=List[Doctor])
def get_doctors():
    return DoctorService.get_doctors()

@router.put("/{doctor_id}")
def set_availability(doctor_id: int, is_available: bool):
    DoctorService.set_availability(doctor_id, is_available)
    return {"message": f"Doctor {doctor_id} availability set to {is_available}"}
