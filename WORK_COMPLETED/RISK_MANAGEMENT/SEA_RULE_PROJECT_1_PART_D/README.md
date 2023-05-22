# Automated Trading Project

## Introduction

This repository contains the implementation of an automated trading solution based on Interactive Brokers' TWS API. The project aims to generate trading positions for various contracts, calculate the net capital requirement under SEA Rule 15c3-1, and produce a detailed report in a CSV format.

## Technologies Used

- **Python**: This project is developed using Python, a widely used programming language in quantitative finance due to its simplicity and rich ecosystem of scientific computation and data analysis libraries.
- **TWS API**: Interactive Brokers' TWS API is utilized for interacting with the TWS trading platform to retrieve contract information, place trading orders, and more.
- **ib_insync**: This Python library simplifies the usage of the TWS API by providing a more Pythonic and asynchronous interface.
- **Pandas**: The project utilizes the Pandas library for data manipulation and analysis, specifically for handling trading data in the form of DataFrames and saving data in CSV files.

## Project Description

The project is structured into three main parts:

### Part 1: Bond Selection

In this phase, the program selects a diverse range of Government Bonds, Corporate Bonds, and Municipal Bonds as potential trading targets. This step is crucial for identifying trading opportunities.

### Part 2: Trading Position Generation

The program establishes a connection with the TWS API and retrieves the details of specified contracts. For each contract, a trading position (long or short) is randomly generated along with an assigned quantity. The generated positions are then formatted and saved in a CSV file named `bond.csv`.

### Part 3: Net Capital Requirement Calculation

In this phase, the program reads the `bond.csv` file generated in Part 2. For each contract, it calculates the net capital requirement based on SEA Rule 15c3-1. The net capital requirement is calculated as 1% of the cash allocation for each contract. Additionally, the program calculates totals for different measures such as the total number of long and short positions, total number of shares, total dollar amount, total cash, and total net capital requirement. These totals are saved in another CSV file named `totals.csv`.

## Challenges and Limitations

There are several challenges and limitations encountered in this project:

- The TWS API does not provide direct access to contract prices and cash allocations. A suitable method to obtain this information needs to be implemented.
- The calculation of the net capital requirement assumes a simplified model (1% of cash allocation). Adjustments may be required to meet specific trader requirements.
- Automated trading code carries inherent risks, especially when leverage is involved. Appropriate risk management practices should be followed.

## Code Explanation

The codebase is organized into several blocks of functions for improved readability and maintainability.

### Helper Functions

These utility functions facilitate interaction with the TWS API and data manipulation. They include:

- `bond_contract_details`: Retrieves contract details from the TWS API.
- `save_to_csv` and `save_to_txt`: Functions for saving data to CSV or text files.
- `format_desc_append`: Formats contract descriptions for better presentation.

### API Connection

The program establishes a connection with the TWS API using the local IP address (127.0.0.1) and a specific client ID.

### Trading Position Generation

The program iterates over a predefined list of contracts. For each contract, it generates a trading position (long or short) and assigns a quantity. The resulting information is then formatted and saved in the `bond.csv` file.

### Net Capital Requirement Calculation

The program reads the `bond.csv` file and calculates the net capital requirement for each contract according to SEA Rule
