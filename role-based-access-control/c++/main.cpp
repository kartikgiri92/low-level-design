#include <bits/stdc++.h>
#include "./constant/my_enums.hpp"
#include "./handler/util.hpp"
#include "./inventory/inventory.hpp"

using namespace std;

void solve(int argc, char *argv[]);
int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);
    solve(argc, argv);

    cout << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
    return 0;
}

void solve(int argc, char *argv[])
{
    DataStore *data_store = new DataStore();
    string filename = argv[1];
    ifstream inputFile(filename);
    string line;

    long long TOTAL = 0, CORRECT = 0, WRONG = 0;
    while (getline(inputFile, line, '\n'))
    {
        string command;
        vector<string> commands;
        stringstream ss(line);
        while (getline(ss, command, ' '))
        {
            commands.push_back(command);
        }

        command = commands[0];
        TOTAL++;
        if (commands[0] == "ADD_PERMISSION")
        {
            if (stoi(commands.back()) != add_permission_to_role(commands, data_store))
                WRONG++; // cout << "Wrong Answer: " << command << endl;
            else
                CORRECT++; // cout << "Correct Answer: " << command << endl;
        }
        else if (commands[0] == "REMOVE_PERMISSION")
        {
            if (stoi(commands.back()) != remove_permission_from_role(commands, data_store))
                WRONG++; // cout << "Wrong Answer: " << command << endl;
            else
                CORRECT++; // cout << "Correct Answer: " << command << endl;
        }
        else if (commands[0] == "CREATE_USER")
        {
            if (stoi(commands.back()) != create_account(commands, data_store))
                WRONG++; // cout << "Wrong Answer: " << command << endl;
            else
                CORRECT++; // cout << "Correct Answer: " << command << endl;
        }
        else if (commands[0] == "ADD_ROLE")
        {
            {
                if (stoi(commands.back()) != add_role_to_account(commands, data_store))
                    WRONG++; // cout << "Wrong Answer: " << command << endl;
                else
                    CORRECT++; // cout << "Correct Answer: " << command << endl;
            }
        }
        else if (commands[0] == "CHECK_USER_PERMISSION")
        {
            if (stoi(commands.back()) != check_account_permission(commands, data_store))
                WRONG++; // cout << "Wrong Answer: " << command << endl;
            else
                CORRECT++; // cout << "Correct Answer: " << command << endl;
        }
        else if (commands[0] == "REMOVE_ROLE")
        {
            if (stoi(commands.back()) != remove_role_from_account(commands, data_store))
                WRONG++; // cout << "Wrong Answer: " << command << endl;
            else
                CORRECT++; // cout << "Correct Answer: " << command << endl;
        }
        else
        {
            cout << "Wrong Input\n";
        }
    }

    cout << "TOTAL => " << TOTAL << endl;
    cout << "CORRECT => " << CORRECT << endl;
    cout << "WRONG => " << WRONG << endl;

    inputFile.close();
}