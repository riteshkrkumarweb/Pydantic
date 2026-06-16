To Know what is pydentic,  first know what is is TypeValidation and DataValidation

# Type Validation
    Type validation checks what kind of data is being provided.

    In programming, every value has a data type such as:
    int → Integer (25)
    float → Decimal (3.14)
    str → Text ("Ritesh")
    bool → Boolean (True, False)
    list → Collection ([1, 2, 3])

    Type validation ensures that the input matches the expected data type.

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
    name → String 
    age → Integer 
    is_student → Boolean 
    # This is correct 

# Data Validation

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

    Real Life Examples of Data Validation Rules
    Age must be between 0 and 120
    Email must contain @
    Password length must be at least 8
    Salary cannot be negative
    Name cannot be empty


    Real API Example
    Suppose a user sends
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

    Purpose	Ensure correct data type and Ensure meaningful data

# pydentic 
    Pydantic is a Python library used for data validation, data parsing, and type enforcement using Python type hints.
    It checks whether the data you receive matches the expected data types and structure. If the data is invalid, it raises clear errors.
    Pydantic solves the problem of unsafe, unvalidated, and messy data by automatically validating and converting data according to Python type hints
 ## Exmaple 
    Imagine you are filling out an online form for creating an account.

    The website expects:
    Name → Text
    Age → Number
    Email → Valid email address

    You submit:
    Name: Ritesh
    Age: 20
    Email: ritesh@gmail.com

    Everything is correct, so the form is accepted.

    Now imagine you submit:

    Name: Ritesh
    Age: Twenty
    Email: riteshgmail.com

    There are problems:

    Age is written as text instead of a number.
    Email is missing the @ symbol.

    Without Pydantic, a programmer would have to manually check every field one by one:

    Is age a number?
    Is email valid?
    Is name present?
    Are required fields missing?

    This becomes difficult when there are many fields.

  *** Pydantic acts like an intelligent form checker. Before the data enters your application, it verifies:***

    Are all required fields present?
    Is each field of the correct type?
    Is the data in the correct format?

    If something is wrong, it immediately reports an error.


If u choose the optional parameter  it doesnot means the field the field in not required it give the error so u have to set the (married: Optional[bool] = None) so the it give database to None instead of Empty. 

### In:**patient(why this is using ** ?)
    patient1 = Patient(**patient_info)

    **patient_info is called dictionary unpacking.

    Suppose:
    patient_info = {
        "name": "nitish",
        "age": "30",
        "weight": "40.6"
    }

    When you write:
    Patient(**patient_info)
    Python automatically converts it to:
    Patient(
        name="nitish",
        age="30",
        weight="40.6"
    )

    Why not just write:

    Patient(patient_info)

    Because Patient expects named arguments, not a dictionary as a single argument.

    Writing:
    Patient(patient_info)
    means:
    Patient(one dictionary object>)
    But Patient is expecting:

    Patient(name=..., age=..., weight=...)

    So, ** takes a dictionary and spreads its key-value pairs into separate named arguments.

# Field()
    u can use the custom data validation using the field likin greatherthanequal , lessthanequalto, greatherthat , lessthathan , and many more more see the code . 