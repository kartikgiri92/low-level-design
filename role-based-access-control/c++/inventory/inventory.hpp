#pragma once
#include <bits/stdc++.h>
#include "../rbac/account.hpp"
#include "../rbac/role.hpp"
#include "../rbac/permission.hpp"
using namespace std;

class DataStore
{
public:
    unordered_map<string, Account *> USER_INVENTORY;
    unordered_map<string, Role *> ROLE_INVENTORY;
    unordered_map<string, Permission *> PERMISSION_INVENTORY;

    DataStore()
    {
        USER_INVENTORY.clear();
        ROLE_INVENTORY = fetch_role_inventory();
        PERMISSION_INVENTORY = fetch_permission_inventory();
    }
};