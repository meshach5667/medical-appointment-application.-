from fastapi import APIRouter, HTTPException
from typing import List
from schemas.patient import Patient
from services.patientService import PatientService

router = APIRouter()

@router.post("/", response_model=Patient)
def create_patient(patient: Patient):
    return PatientService.create_patient(patient)

@router.get("/", response_model=List[Patient])
def get_patients():
    return PatientService.get_patients()
