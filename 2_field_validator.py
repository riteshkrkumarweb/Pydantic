from pydantic import BaseModel,EmailStr,AnyUrl , field_validator
from typing import List , Dict,Optional

class Patient(BaseModel):

    name:str
    age: int
    weight: float
    linkedin:AnyUrl 
    email:EmailStr
    allergies: Optional[List[str]] = None 
    contact_details: Optional[Dict[str, str]] = None

    @field_validator('email') # we write email so that we have to work on the email custom validation 
    @classmethod
    def email_validator(cls,value): # cls use for if any other need to customize or validation 
        
        valid_domain = ['hdfc.com','icici.com'] # here we write that email should have these two after @ 
        #abc@gmail.com
        domain_name = value.split('@')[-1] #here we define the after the @ 

        if domain_name not in valid_domain :
            raise ValueError('Not a valid Documenet ')
        return value 
    #To Make the first letter is capital we apply the field_validator()
    #beacuse it give the power to custom validation 
    @field_validator('name')
    @classmethod
    def make_capital_letter(cls,value):
        return value.capitalize()

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

patient_info = {'name': 'nitish', 'age': 30 , 'weight':40.6, 'email':'ritesh@hdfc.com','linkedin':'https://www.linkedin.com/in/riteshkumarweb/'}

patient1 = Patient(**patient_info) #So, ** takes a dictionary and spreads its key-value pairs into separate named arguments. for more see docs 

update_patient_data(patient1)

# Since Field validator() works on the the one field like the age or name or anyting but what if we need the
# logic like if the age is above 60 it has the emergency contact number here we work on both age and contact_datails
# here comes the mode_validator().

