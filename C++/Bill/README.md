# Bill Management System

This is a simple C++ program that simulates a billing system for items in a store. The program allows the user to input item IDs and their respective prices, then displays the entered information.

## Program Structure

The program consists of a `Bill` class and a `main` function to interact with the class. 

### Bill Class

The `Bill` class has the following private members:
- `itemId[40]`: an array to store the IDs of up to 40 items.
- `itemValue[40]`: an array to store the prices of up to 40 items.
- `itemCounter`: an integer to keep track of the number of items entered.

#### Public Methods

- `void counterNew()`: Initializes the `itemCounter` to 0.
- `void setData()`: Prompts the user to enter the ID and price for an item and stores them in the respective arrays. Increments the `itemCounter` after storing the data.
- `void displayData()`: Displays the ID and price for each item stored in the arrays.

### main Function

The `main` function demonstrates the usage of the `Bill` class:
1. Creates an instance of the `Bill` class named `reciept`.
2. Calls the `counterNew` method to initialize the item counter.
3. Calls the `setData` method four times to input data for four items.
4. Calls the `displayData` method to print the IDs and prices of the entered items.

## How to Run the Program

1. Compile the program using a C++ compiler. For example:
    ```bash
    g++ main.py
    ```
2. Run the compiled program:
    ```bash
    .\a.exe
    ```
3. Follow the prompts to enter the item IDs and prices.
4. After entering the data, the program will display the information for all the items entered.

## Example Output
```bash
Enter the Id of the item no 1
1001
Enter the Price of the item
210 
Enter the Id of the item no 2
1002
Enter the Price of the item
130
Enter the Id of the item no 3
1003
Enter the Price of the item
100
Enter the Id of the item no 4
1004
Enter the Price of the item
140
The Price of the item id 1001 is 210
The Price of the item id 1002 is 130
The Price of the item id 1003 is 100
The Price of the item id 1004 is 140
```
