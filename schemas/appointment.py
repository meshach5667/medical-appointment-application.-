from pydantic import BaseModel
from typing import Optional


class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str