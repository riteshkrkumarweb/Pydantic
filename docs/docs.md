# Pydentic 
    __To Know what is pydentic first know what is is TypeValidation and DataValidation 
    Type Validation vs Data

    Both are used to check whether input data is correct, but they focus on different things.

   ## Type Validation

    Type validation checks what kind of data is being provided.
    In programming, every value has a data type such as:

    int → Integer (25)
    float → Decimal (3.14)
    str → Text ("Ritesh")
    bool → Boolean (True, False)
    list → Collection ([1, 2, 3])

   ### Type validation ensures that the input matches the expected data type.

    Example
    Suppose an API expects age as an integer.
    age = 20   # Correct
    age = "20" # Incorrect type (string)
    If the system expects an integer but receives a string, type validation fails.

    Real-World Example
    Imagine an online form:
    Age → must be a number
    Name → must be text
    Is Student → must be True or False

    Input:
    {
        "name": "Ritesh",
        "age": 20,
        "is_student": True
    }

    Type validation result:
    name → String ✅
    age → Integer ✅
    is_student → Boolean ✅
    2. Data Validation
    Data validation checks whether the actual value is valid according to business rules.
    Even if the type is correct, the value itself may still be invalid.

    Example
    Age should be between 0 and 120.
    age = 500
    The type is correct (int) 
    But the value is unrealistic 
    Therefore:

    Type validation → Passed 
    Data validation → Failed 
    Examples of Data Validation Rules
    Age must be between 0 and 120
    Email must contain @
    Password length must be at least 8
    Salary cannot be negative
    Name cannot be empty

    Example:
    email = "riteshgmail.com"
    Type: String 
    Valid email format 
    Comparison Table
    Feature	Type Validation	Data Validation
    Checks	Data type	Data value/rules
    Example	age is integer	age is between 0–120
    Error	Wrong type	Invalid value
    Purpose	Ensure correct data type Ensure meaningful data

    Real API Example
    Suppose a user sends:
    {
        "name": "Ritesh",
        "age": -5,
        "email": "riteshgmail.com"
    }
    Type Validation
    name is string 
    age is integer 
    email is string 

    All pass.
    Data Validation
    Age cannot be negative 
    Email format is invalid 

    Therefore, the request is rejected.

    Example in FastAPI with Pydantic
    from pydantic import BaseModel, Field
`` class Patient(BaseModel): ``
        name: str
        age: int = Field(gt=0, lt=120)
    Input 1
    {
        "name": "Ritesh",
        "age": 25 
    }

    Result: Accepted 
    Input 2
    {
        "name": "Ritesh",
        "age": "twenty"
    }

    Result:

    Type Validation Failed 
    Input 3
    {
        "name": "Ritesh",
        "age": -10
    }

    Result:

    Type Validation Passed 
    Data Validation Failed 
    Simple Formula
    Type Validation: "Is the data of the correct type?"
    Data Validation: "Is the value logically correct?"

    You can think of it like this:

    Type Validation  → WHAT is the data?
    Data Validation  → IS the data acceptable?