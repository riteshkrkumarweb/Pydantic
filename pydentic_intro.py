from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List , Dict,Optional

class Patient(BaseModel):

    name: str = Field(max_length=50) #Field is use for the custom data validation 
    age: int = Field(gt=0)
    weight: float
    linkedin:AnyUrl # If define the url and also validate the url instead of writing manually logic 
    email:EmailStr # instead of only string use Email that validate the email 
    married: Optional[bool] = None # With optional parameter It is option, but also write = None so that database donot have null value instead in have NONE vlaue
    allergies: Optional[List[str]] = None 

    contact_details: Optional[Dict[str, str]] = None

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
    print('updated')

patient_info = {'name': 'nitish', 'age': 30 , 'weight':40.6, 'email':'ritesh@gmail.com','linkedin':'https://www.linkedin.com/in/riteshkumarweb/'}

patient1 = Patient(**patient_info) #So, ** takes a dictionary and spreads its key-value pairs into separate named arguments. for more see docs 

update_patient_data(patient1)

