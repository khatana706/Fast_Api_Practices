from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Any

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr  # Changed to lowercase 'e' to match your data
    weight: float
    married: bool    # Corrected spelling from 'marriged'
    allergies: List[Any]  # Changed to Any since you are passing a list of strings
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        # In mode='after', 'self' is the instance, not 'model'
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)  # Matches the corrected field name
    print('updated')

# Input data matching the schema exactly
patient_info = {
    'name': 'nitish', 
    'email': 'abc@icici.com', 
    'age': 65, 
    'weight': 75.2, 
    'married': True, 
    'allergies': ['pollen', 'dust'], 
    'contact_details': {'phone': '2353462', 'emergency': '235236'}
}

# This will now initialize successfully
patient1 = Patient(**patient_info) 

# This will now print the outputs
update_patient_data(patient1)

    


