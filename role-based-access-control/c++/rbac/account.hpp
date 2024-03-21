#pragma once
#include <bits/stdc++.h>
#include "./role.hpp"
#include "./permission.hpp"
#include "../constant/my_enums.hpp"

using namespace std;

class Account
{
public:
    virtual string get_account_name() = 0;
    virtual StatusEnum add_role(Role *rl) = 0;
    virtual StatusEnum remove_role(Role *rl) = 0;
    virtual StatusEnum check_role(Role *rl) = 0;
    virtual StatusEnum check_permission(Permission *perm) = 0;
};

class User : public Account
{
public:
    string account_name;
    string name, email;
    unordered_set<Role *> roles;

    User(string name, string email)
    {
        this->account_name = "User";
        this->name = name;
        this->email = email;
        roles.clear();
    }

    string get_account_name() { return account_name; }

    StatusEnum add_role(Role *rl)
    {
        roles.insert(rl);
        return SUCCESS;
    }

    StatusEnum remove_role(Role *rl)
    {
        if (roles.find(rl) != roles.end())
        {
            roles.erase(rl);
        }
        return SUCCESS;
    }

    StatusEnum check_role(Role *rl)
    {
        return roles.find(rl) != roles.end() ? SUCCESS : FAILURE;
    }

    StatusEnum check_permission(Permission *perm)
    {
        for (const auto &rl : roles)
        {
            if (rl->check_permission(perm) == SUCCESS)
            {
                return SUCCESS;
            }
        }
        return FAILURE;
    }
};