import pandas as pd
from cryptography.fernet import Fernet

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Generate a key and create a cipher suite
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    """
    Encrypts the given data.

    Args:
        data (str): The data to encrypt.

    Returns:
        str: The encrypted data.
    """
    if isinstance(data, str):
        data = data.encode('utf-8')  # Convert string to bytes
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data.decode('utf-8')  # Convert bytes to string


def decrypt_data(encrypted_data):
    """
    Decrypts the given encrypted data.

    Args:
        encrypted_data (str): The encrypted data to decrypt.

    Returns:
        str: The decrypted data.
    """
    encrypted_data = encrypted_data.encode('utf-8')  # Convert string to bytes
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')  # Convert bytes to string


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
    # Ensure the data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The input data must be a pandas DataFrame.")

    # Check if necessary columns exist
    required_columns = ['User_Name', 'User_Password']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"The DataFrame is missing the following columns: {', '.join(missing_columns)}")

    # Apply the encryption function to each column
    data['User_Name'] = data['User_Name'].apply(encrypt_data)
    data['User_Password'] = data['User_Password'].apply(encrypt_data)

    # Rename columns
    data.rename(columns={
        'User_Name': 'Encrypted_Username',
        'User_Password': 'Encrypted_Password'
    }, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
