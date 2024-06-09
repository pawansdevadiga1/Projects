#include <iostream>
using namespace std;

class Bill
{
    int itemId[40];
    int itemValue[40];
    int itemCounter;

public:
    void counterNew()
    {
        itemCounter = 0;
    }

    void setData()
    {
        cout << "Enter the Id of the item no " << itemCounter + 1 << endl;
        cin >> itemId[itemCounter];
        cout << "Enter the Price of the item " << endl;
        cin >> itemValue[itemCounter];
        itemCounter++;
    }

    void displayData(void)
    {
        for (int i = 0; i < itemCounter; i++)
        {
            cout << "The Price of the item id " << itemId[i] << " is " << itemValue[i] << endl;
        }
    }
};

int main()
{
    Bill reciept;
    reciept.counterNew();
    reciept.setData();
    reciept.setData();
    reciept.setData();
    reciept.setData();
    reciept.displayData();
    return 0;
}
