from typing import List
from schemas.patient import Patient

class PatientService:
    patients_db = []

    @classmethod
    def create_patient(cls, patient: Patient) -> Patient:
        cls.patients_db.append(patient)
        return patient

    @classmethod
    def get_patients(cls) -> List[Patient]:
        return cls.patients_db