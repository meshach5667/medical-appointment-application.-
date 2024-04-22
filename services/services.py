from typing import List
from schemas.appointment import Appointment

# class PatientService:
#     patients_db = []

#     @classmethod
#     def create_patient(cls, patient: Patient) -> Patient:
#         cls.patients_db.append(patient)
#         return patient

#     @classmethod
#     def get_patients(cls) -> List[Patient]:
#         return cls.patients_db

# class DoctorService:
#     doctors_db = []

#     @classmethod
#     def create_doctor(cls, doctor: Doctor) -> Doctor:
#         cls.doctors_db.append(doctor)
#         return doctor

#     @classmethod
#     def get_doctors(cls) -> List[Doctor]:
#         return cls.doctors_db

#     @classmethod
#     def set_availability(cls, doctor_id: int, is_available: bool):
#         for doctor in cls.doctors_db:
#             if doctor.id == doctor_id:
#                 doctor.is_available = is_available
#                 break

class AppointmentService:
    appointments_db = []

    @classmethod
    def create_appointment(cls, appointment: Appointment) -> Appointment:
        cls.appointments_db.append(appointment)
        return appointment

    @classmethod
    def complete_appointment(cls, appointment_id: int) -> str:
        for appointment in cls.appointments_db:
            if appointment.id == appointment_id:
                appointment_date = appointment.date
                cls.appointments_db.remove(appointment)
                for doctor in cls.doctors_db:
                    if doctor.id == appointment.doctor_id:
                        doctor.is_available = True
                        return f"Appointment completed on {appointment_date}. Doctor {doctor.name} is available now."
        return "Appointment not found"

    @classmethod
    def cancel_appointment(cls, appointment_id: int) -> str:
        for appointment in cls.appointments_db:
            if appointment.id == appointment_id:
                cls.appointments_db.remove(appointment)
                for doctor in cls.doctors_db:
                    if doctor.id == appointment.doctor_id:
                        doctor.is_available = True
                        return "Appointment canceled"
        return "Appointment not found"
