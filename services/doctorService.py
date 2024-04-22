from typing import List
from schemas.doctors import  Doctor

class DoctorService:
    doctors_db = []

    @classmethod
    def create_doctor(cls, doctor: Doctor) -> Doctor:
        cls.doctors_db.append(doctor)
        return doctor

    @classmethod
    def get_doctors(cls) -> List[Doctor]:
        return cls.doctors_db

    @classmethod
    def set_availability(cls, doctor_id: int, is_available: bool):
        for doctor in cls.doctors_db:
            if doctor.id == doctor_id:
                doctor.is_available = is_available
                break