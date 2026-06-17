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
    pydentic automatically convert '23' to the integer so to stop this automatically we have a parameter 
    strict=True that not convert that type of data to the integer
## What is Meta data ?     
    Metadata (or meta data) is simply data that describes other data.

    Think of it as information about a file, document, photo, or dataset that helps identify, organize, or understand it.

    Examples
    🌐 Web page metadata
    Page title
    Description
    Keywords
    Author information

    📷 Photo metadata
    Date taken
    Camera model
    Location (GPS coordinates)
    Image size and resolution

    📄 Document metadata
    Author
    Creation date
    Last modified date
    File type

    🎵 Music metadata
    Song title
    Artist
    Album
    Genre
    Duration
# Annoted()
 Annotated is a way to attach extra information to a type without changing the type itself.
 In Pydantic, it is often used together with Field().

 In short:
 Field() → Adds validation rules and metadata.
 Annotated[T, ...] → Attaches metadata to a type T.
 Pydantic reads the metadata inside Annotated and applies validation.
# field_validator()
    field_validator() is used to write custom validation logic for one or more fields.

    Pydantic already validates basic things like
    int → must be an integer
    EmailStr → must be a valid email
    Field(gt=0) → must be greater than 0
    But sometimes you need your own rules. That's when field_validator() is used.

    Example Use Cases
    Suppose you want these rules:
    Name must start with a capital letter.
    Age must be even.
    Email must belong to a company domain.

    These rules are not built into Pydantic, so you write a field_validator().

# model_validator() 

    model_validator() is used to validate the entire model (all fields together).

    While field_validator() checks one field at a time, model_validator() can check relationships between multiple fields.

    When do we use it?

    Use model_validator() when validation depends on more than one field.

    Example rules:
    If married=True, then spouse name must be provided.
    start_date must be before end_date.
    Min age should be less than max age.

    These rules involve multiple fields, so field_validator() is not enough.
   ### what is mode after and before in model_validator()
    you know that pydentic automatically convert '30' in to the integer so the after mode is that when the pydentic automatically convert the value when client give like age = '30' to age=30 when the model creates
    and before when before the model created means when the client enter the string age but i have not converted to integer. 

    mode='after'
    Runs after all fields have been validated and converted.
    Input data
       ↓
    Field validation
       ↓
    Type conversion  Type conversion means changing a value from one data type to another. "30"  →  30
       ↓
    model_validator()
      ↓
    Final model

    mode='before'
    Runs before Pydantic creates the model.
    You receive the raw input data (usually a dictionary).

    Input data
        ↓
    model_validator()
        ↓
    Field validation
        ↓
    Model creation
# computed_field() 

    computed_field() is used to create a field whose value is calculated from other fields instead of being provided by the user.

    Think of it as a derived field.

    For example:

    BMI can be calculated from height and weight.
    Full name can be calculated from first name and last name.
    Total price can be calculated from quantity and unit price.

    You don't store these values; Pydantic computes them automatically.
    computed_field() creates fields whose values are automatically calculated from other fields in the model.
    Example:

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

If you create:

Rectangle(width=5, height=4)

the model behaves as if it has:

area = 20

even though you never provided area.

Why use it?

Without computed_field():

You must manually calculate values every time.
The calculated value is not included when exporting the model.

With computed_field():

The value is calculated automatically.
It appears in model output like model_dump().

Example output:

{
    "width": 5,
    "height": 4,
    "area": 20
}
Important

A computed field:

Depends on other fields.
Is read-only by default.
Is not provided by the client.

The client sends:

{
    "width": 5,
    "height": 4
}

Pydantic computes:

area = 20
