# InsightFlow: Secure Data Transformation & Visualization Project

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
