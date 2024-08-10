import io
import pandas as pd
import requests
import json
import time

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load data from the API continuously for 10 seconds and compile into a DataFrame.
    """
    url = 'https://randomuser.me/api/'
    start_time = time.time()  # Start the timer inside the function
    all_data = []

    while time.time() - start_time < 120:
        response = requests.get(url)
        data = response.json()

        for user in data['results']:
            UUID = user['login']['uuid']
            First_Name = user['name']['first']
            Last_Name = user['name']['last']
            Title = user['name']['title']
            Gender = user['gender']
            Nationality = user['nat']
            Email = user['email']
            Age = user['dob']['age']
            DOB = user['dob']['date']
            Address = f"{user['location']['street']['number']} {user['location']['street']['name']}, {user['location']['city']}, {user['location']['state']}, {user['location']['country']}"
            Phone = user['phone']
            Cell = user['cell']
            User_Name = user['login']['username']
            User_Password = user['login']['password']
  
            all_data.append({
                'UUID': UUID,
                'First_Name': First_Name,
                'Last_Name': Last_Name,
                'Title': Title,
                'Gender': Gender,
                'Nationality': Nationality,
                'Email': Email,
                'Age': Age,
                'DOB': DOB,
                'Address': Address,
                'Phone': Phone,
                'Cell': Cell,
                'User_Name': User_Name,
                'User_Password': User_Password

            })

        

    df = pd.DataFrame(all_data)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame), 'The output is not a DataFrame'
    assert len(output) > 0, 'The DataFrame is empty'
