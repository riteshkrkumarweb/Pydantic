To Know what is pydentic,  first know what is is TypeValidation and DataValidation

# Type Validation

**Type validation checks what kind of data is being provided.**
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

    name → String ✅
    age → Integer ✅
    is_student → Boolean ✅
