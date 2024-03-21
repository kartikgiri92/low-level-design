#pragma once
#include <bits/stdc++.h>
#include "../rbac/account.hpp"
#include "../rbac/role.hpp"
#include "../rbac/permission.hpp"
#include "../constant/my_enums.hpp"
#include "../inventory/inventory.hpp"
using namespace std;

StatusEnum add_permission_to_role(vector<string> &commands, DataStore *data_store)
{
    string role_n = commands[1];
    string permission_n = commands[2];
    if (data_store->ROLE_INVENTORY.find(role_n) == data_store->ROLE_INVENTORY.end() ||
        data_store->PERMISSION_INVENTORY.find(permission_n) == data_store->PERMISSION_INVENTORY.end())
    {
        // ROLE / Permission Does not Exist
        return FAILURE;
    }
    Role *rl = data_store->ROLE_INVENTORY[role_n];
    rl->add_permission(data_store->PERMISSION_INVENTORY[permission_n]);
    return SUCCESS;
}

StatusEnum remove_permission_from_role(vector<string> &commands, DataStore *data_store)
{
    string role_n = commands[1];
    string permission_n = commands[2];
    if (data_store->ROLE_INVENTORY.find(role_n) == data_store->ROLE_INVENTORY.end() ||
        data_store->PERMISSION_INVENTORY.find(permission_n) == data_store->PERMISSION_INVENTORY.end())
    {
        // ROLE / Permission Does not Exist
        return FAILURE;
    }
    Role *rl = data_store->ROLE_INVENTORY[role_n];
    rl->remove_permission(data_store->PERMISSION_INVENTORY[permission_n]);
    return SUCCESS;
}

StatusEnum create_account(vector<string> &commands, DataStore *data_store)
{
    string name_n = commands[1];
    string email_n = commands[2];
    if (data_store->USER_INVENTORY.find(email_n) != data_store->USER_INVENTORY.end())
    {
        // Email Already Exists
        return FAILURE;
    }
    data_store->USER_INVENTORY[email_n] = new User(name_n, email_n);
    return SUCCESS;
}

StatusEnum add_role_to_account(vector<string> &commands, DataStore *data_store)
{
    string email_n = commands[1];
    string role_n = commands[2];
    if (data_store->ROLE_INVENTORY.find(role_n) == data_store->ROLE_INVENTORY.end() ||
        data_store->USER_INVENTORY.find(email_n) == data_store->USER_INVENTORY.end())
    {
        // ROLE / Email Does not Exist
        return FAILURE;
    }
    Role *rl = data_store->ROLE_INVENTORY[role_n];
    return data_store->USER_INVENTORY[email_n]->add_role(rl);
}

StatusEnum remove_role_from_account(vector<string> &commands, DataStore *data_store)
{
    string email_n = commands[1];
    string role_n = commands[2];
    if (data_store->ROLE_INVENTORY.find(role_n) == data_store->ROLE_INVENTORY.end() ||
        data_store->USER_INVENTORY.find(email_n) == data_store->USER_INVENTORY.end())
    {
        // ROLE / Email Does not Exist
        return FAILURE;
    }
    Role *rl = data_store->ROLE_INVENTORY[role_n];
    return data_store->USER_INVENTORY[email_n]->remove_role(rl);
}

StatusEnum check_account_permission(vector<string> &commands, DataStore *data_store)
{
    string email_n = commands[1];
    string permission_n = commands[2];
    if (data_store->USER_INVENTORY.find(email_n) == data_store->USER_INVENTORY.end() ||
        data_store->PERMISSION_INVENTORY.find(permission_n) == data_store->PERMISSION_INVENTORY.end())
    {
        //  Email or Role not found
        return FAILURE;
    }
    Permission *perm = data_store->PERMISSION_INVENTORY[permission_n];
    return data_store->USER_INVENTORY[email_n]->check_permission(perm);
}