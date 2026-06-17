from pydantic import BaseModel,EmailStr,AnyUrl,model_validator
from typing import List , Dict,Optional

class Patient(BaseModel):

    name:str
    age: int
    weight: float
    linkedin:AnyUrl 
    email:EmailStr
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]

    # we write the custom validator logic that if we have more than 60 years age then 
    #  patient have the emergency contact details . we are working on the two things 
    # age and contact_details then we use the model_validatior()

    @model_validator(mode='after') # we have to give the mode 'before ' or 'after' so that 
    def should_have_emrgy_contact(cls,model):# we write model beacuse i takes the access of full model of patient like name age and all things 
                                             # not just one value, u can write anything this is parameter but for better understand i write this 

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient is above 60 and have the emergency contact details')
        return model


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
    print('updated')

patient_info = {'name': 'nitish', 'age': 70 , 'weight':40.6, 'email':'ritesh@gmail.com','linkedin':'https://www.linkedin.com/in/riteshkumarweb/','contact_details':{'phone':'821114','emergency':'102'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)

