from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    

address_dict={'city':'varanasi','state':'UP','pin':'221011'}
address1 = Address(**address_dict)

patient_dict = {'name':'Ritesh','gender':'Male','age':20,'address':address1}

patient1 = Patient(**patient_dict)

exports = patient1.model_dump() # to export in the dict 
print(exports)
print(type(exports))

exports_json = patient1.model_dump_json() # to export in the json  
print(exports_json)
print(type(exports_json))
                                                                    #ignore for ignoring the fake error by vs code
exports_particular = patient1.model_dump(include=['name','gender']) # type: ignore  #only include the name and gender and export it  
print(exports_particular)
print(type(exports_particular))

exports_particular_ex = patient1.model_dump(exclude=['name','gender'])# type: ignore  #only exclude the name and gender and export all things except name and gender 
print(exports_particular_ex)
print(type(exports_particular_ex))

exports_particular_s = patient1.model_dump(exclude={'address':['state']})  # type: ignore #only exclude the state from the address 
print(exports_particular_s)
print(type(exports_particular_s))