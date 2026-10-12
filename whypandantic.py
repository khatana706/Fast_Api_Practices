from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

patient_info = {"name": "Aman", "age": 30}  
      

Patirnt1 = Patient(**patient_info)

insert_patient_data(Patirnt1)