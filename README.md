Here's the updated README file reflecting the scheduling done using MAGE AI:

---

# InsightFlow: Secure Data Transformation & Visualization

## Overview

**InsightFlow** is a robust ETL (Extract, Transform, Load) pipeline that ingests user data from the RandomUser API, applies advanced data transformation and security practices, and stores the data securely in MongoDB. The project also includes data visualization using Tableau, turning raw data into meaningful insights while maintaining high standards of data privacy and security.

## Table of Contents

1. [Project Architecture](#project-architecture)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Data Flow](#data-flow)
5. [Data Security & Masking](#data-security--masking)
6. [Scheduling & Automation](#scheduling--automation)


## Project Architecture

![Architecture Diagram](https://github.com/DivineSamOfficial/InsightFlow-Secure-Data-Transformation-Visualization/blob/main/Assets/ArchDiag.jpg)

The project architecture ensures modularity and data security at every stage, from ingestion to final visualization.

## Features

- **Data Ingestion:** 
  - Fetches user data from the RandomUser API.
  - Utilizes MAGE AI for efficient data loading.

- **Data Transformation:**
  - **Block 1:** Removal of nulls and duplicate records.
  - **Block 2:** Data type transformations and adjustments.
  - **Block 3:** **Data masking** of sensitive information, including phone numbers, emails, and addresses, to protect user privacy.
  - **Block 4:** Encryption of user passwords and usernames, with templates provided for future decryption.
  - **Block 5:** Securely loads the transformed data into MongoDB.

- **Data Visualization:**
  - **Tool:** Tableau.
  - **Connection:** MongoDB BI Connector.
  - **Outcome:** Visualized insights from the transformed user data.

## Technologies Used

- **MAGE AI** for data ingestion, transformation, scheduling, and automation.
- **Python** for scripting and data processing.
- **MongoDB** for data storage.
- **MongoDB BI Connector** for connecting MongoDB to Tableau.
- **Tableau** for data visualization.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/InsightFlow.git
   cd InsightFlow
   ```

2. **Install Dependencies:**
   Ensure you have Python, MAGE AI, MongoDB, and Tableau installed. Then install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**
   Set up your MongoDB instance and ensure it’s running. Configure the connection settings in the project files.

4. **Run the ETL Pipeline:**
   Execute the data ingestion and transformation scripts:
   ```bash
   python main.py
   ```

5. **Visualize Data:**
   Connect Tableau to your MongoDB instance using the BI Connector, and load the provided `.twbx` file to explore the visualizations.

## Data Flow

```plaintext
[RandomUser API]
       |
       v
[MAGE AI: Ingestion & Transformation]
       |
       v
[Local MongoDB]
       |
       v
[Tableau: Visualization]
```

## Data Security & Masking

**Data Masking** is a critical aspect of this project, ensuring that sensitive user information is protected throughout the ETL process. Here's how it's handled:

- **Phone Numbers & Emails:** 
  - Masked to obscure personal details while maintaining data integrity.
  - Example: `+91 99XXXXXXXX` for phone numbers, `d*********m@gmail.com` for emails.
  
- **Addresses:**
  - Partial masking of street information to prevent full disclosure of residential addresses.
  
- **Encryption:**
  - User passwords and usernames are encrypted using secure algorithms, ensuring they remain protected at rest.
  - Decryption templates are provided for future use cases where access to original data might be necessary.

This approach ensures compliance with data privacy regulations while allowing meaningful analysis and visualization.

## Scheduling & Automation

The ETL pipeline is scheduled to run daily using MAGE AI's built-in scheduling and triggering features. This automation ensures that the data is always up-to-date, with transformations and load operations executed at regular intervals without manual intervention.

## Usage

1. **Run the ETL Process:**
   - Ingest, transform, and load the data.
  
2. **Access Visualizations:**
   - Open Tableau and connect to MongoDB.
   - Explore the dashboards to gain insights from the transformed user data.

## Future Enhancements

- **Extended Data Security:** 
  - Integrate more advanced encryption methods and user access controls.
  
- **Scalable Deployment:** 
  - Deploy the pipeline on cloud infrastructure for handling larger datasets.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README now includes details about the scheduling aspect using MAGE AI, making it comprehensive and suitable for showcasing your project on GitHub.
