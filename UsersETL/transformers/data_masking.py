import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def mask_Email(Email):
    """
    Mask the Email address, keeping the first letter and the domain part.

    Args:
        Email (str): The Email address to mask.

    Returns:
        str: The masked Email address.
    """
    if pd.isna(Email) or '@' not in Email:
        return Email  # Return as is if it's not a valid Email

    local_part, domain = Email.split('@')
    masked_local_part = local_part[0] + '*' * (len(local_part) - 1)
    return f"{masked_local_part}@{domain}"

def mask_Address(Address):
    """
    Mask the Address, keeping the first part visible.

    Args:
        Address (str): The Address to mask.

    Returns:
        str: The masked Address.
    """
    if pd.isna(Address):
        return Address  # Return as is if it's not a valid Address

    parts = Address.split(', ')
    if len(parts) > 1:
        masked_address = f"{parts[0]}, {'*' * len(parts[1])}, {'*' * len(parts[2])}, {'*' * len(parts[3])}"
        return masked_address
    return Address

def mask_Phone(Phone):
    """
    Mask the Phone number, keeping the format visible.

    Args:
        Phone (str): The Phone number to mask.

    Returns:
        str: The masked Phone number.
    """
    if pd.isna(Phone):
        return Phone  # Return as is if it's not a valid Phone number

    # Keep the format and mask the digits
    return f"({Phone[1]})-XXX-XXXX"

def mask_Cell(Cell):
    """
    Mask the Cell number, keeping the format visible.

    Args:
        Cell (str): The Cell number to mask.

    Returns:
        str: The masked Cell number.
    """
    if pd.isna(Cell):
        return Cell  # Return as is if it's not a valid Cell number

    # Keep the format and mask the digits
    return f"({Cell[1]})-XXX-XXXX"



@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Ensure the data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The input data must be a pandas DataFrame.")

    # Check if the Email column exists
    if 'Email' not in data.columns:
        raise ValueError("The DataFrame does not contain an 'Email' column.")

    # Apply the masking function to the Email column
    data['Email'] = data['Email'].apply(mask_Email)
    data['Address'] = data['Address'].apply(mask_Address)
    data['Phone'] = data['Phone'].apply(mask_Phone)
    data['Cell'] = data['Cell'].apply(mask_Cell)
    data.rename(columns={'Email': 'Masked_Email', 'Address': 'Masked_Address', 'Phone': 'Masked_Phone', 'Cell': 'Masked_Cell'}, inplace=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
