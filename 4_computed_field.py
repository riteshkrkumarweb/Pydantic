from pydantic import BaseModel,EmailStr,AnyUrl,computed_field
from typing import List , Dict,Optional

class Patient(BaseModel):

    name:str
    age: int
    weight: float # in kg 
    height:float # in meter 
    linkedin:AnyUrl 
    email:EmailStr
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float : # -> this sign means we are telling that the output is in the float . 
        bmi = round(self.weight/(self.height**2),2)
        return  bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.linkedin)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact_details)
    print('The BMI is ',patient.calculate_bmi)
    print('updated')

patient_info = {'name': 'nitish', 'age': 70 , 'weight':58,'height':1.62, 'email':'ritesh@gmail.com','linkedin':'https://www.linkedin.com/in/riteshkumarweb/','contact_details':{'phone':'821114','emergency':'102'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)


