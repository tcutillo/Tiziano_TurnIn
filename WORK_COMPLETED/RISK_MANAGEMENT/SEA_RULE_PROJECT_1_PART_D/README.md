I. Introduction

This document provides an overview of the Automated Trading Project based on Interactive Brokers' TWS API. The project aimed to develop an automated trading solution utilizing the TWS API to generate trading positions, calculate the net capital requirement, and produce detailed reports in CSV format.

II. Technologies Used

The project utilized the following technologies:

Python: The programming language chosen for this project due to its simplicity and wide adoption in quantitative finance. Python offers numerous libraries for scientific computation and data analysis.
TWS API: Interactive Brokers' trading API, which enables interaction with the TWS trading platform to retrieve contract information, place trading orders, and more.
ib_insync: A Python library that simplifies the usage of the TWS API by providing a more Pythonic and asynchronous interface.
Pandas: A Python library for data manipulation and analysis, used to handle trading data in DataFrame format and save it as CSV files.
III. Project Description

The project was divided into three main parts: bond selection, trading position generation, and net capital requirement calculation.

Part 1: Bond Selection
In this part, the program selects a range of Government Bonds, Corporate Bonds, and Municipal Bonds as the target for trading. This step is crucial as it determines the potential opportunities for trading.

Part 2: Trading Position Generation
The program connects to the TWS API and retrieves contract details for each specified contract. It generates a random trading position (long or short) and assigns a quantity to each contract. The resulting information is then formatted and saved in a CSV file named "bond.csv".

Part 3: Net Capital Requirement Calculation
This part involves reading the CSV file generated in Part 2. For each contract, the program calculates the net capital requirement according to SEA Rule 15c3-1. The net capital requirement is determined as 1% of the cash allocation for each contract. The program calculates totals for various measures such as the total number of long and short positions, total number of long and short shares, total long and short dollar amount, total cash, and total net capital requirement. These totals are then saved in another CSV file named "totals.csv".

IV. Challenges and Limitations

There are certain challenges and limitations encountered during the project:

The TWS API does not provide price and cash allocation information directly, requiring the implementation of an appropriate method to obtain this data.
The calculation of the net capital requirement is based on a simplified assumption (1% of cash allocation). This calculation should be adapted to meet the specific needs of traders.
Automated trading code carries inherent risks, particularly when involving leverage. Appropriate risk management practices should be implemented.
V. Code Explanation

The code is structured into several blocks of functions for improved understanding and maintenance.

Helper Functions
These functions serve as utilities for interacting with the TWS API and manipulating data. They include:

bond_contract_details: Retrieves contract details from the TWS API.
save_to_csv and save_to_txt: Functions for saving data to CSV or text files.
format_desc_append: Formats contract descriptions for improved presentation.
API Connection
The program establishes a connection with the TWS API using the local IP address (127.0.0.1) and a specific client ID (1 in this case).

Trading Position Generation
The program iterates over a list of predefined contracts. For each contract, it generates a trading position (long or short) and assigns a quantity. The resulting information is formatted and saved in a CSV file named "bond.csv".

Net Capital Requirement Calculation
The program reads the previously generated CSV file and calculates the net capital requirement for each contract based on SEA Rule