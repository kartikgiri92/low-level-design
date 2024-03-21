#pragma once
#include <bits/stdc++.h>
#include "./permission.hpp"
#include "../constant/my_enums.hpp"
using namespace std;

class Role
{
public:
    virtual string get_role_name() = 0;
    virtual StatusEnum add_permission(Permission *perm) = 0;
    virtual StatusEnum remove_permission(Permission *perm) = 0;
    virtual StatusEnum check_permission(Permission *perm) = 0;
};

class Admin : public Role
{
public:
    string role_name;
    unordered_set<Permission *> permissions;

    Admin()
    {
        role_name = "Admin";
        permissions.clear();
    }

    string get_role_name() { return role_name; }

    StatusEnum add_permission(Permission *perm)
    {
        permissions.insert(perm);
        return SUCCESS;
    }

    StatusEnum remove_permission(Permission *perm)
    {
        if (permissions.find(perm) != permissions.end())
        {
            permissions.erase(perm);
        }
        return SUCCESS;
    }

    StatusEnum check_permission(Permission *perm)
    {
        return permissions.find(perm) != permissions.end() ? SUCCESS : FAILURE;
    }
};

class Customer : public Role
{
public:
    string role_name;
    set<Permission *> permissions;

    Customer()
    {
        role_name = "Customer";
        permissions.clear();
    }

    string get_role_name() { return role_name; }

    StatusEnum add_permission(Permission *perm)
    {
        permissions.insert(perm);
        return SUCCESS;
    }

    StatusEnum remove_permission(Permission *perm)
    {
        if (permissions.find(perm) != permissions.end())
        {
            permissions.erase(perm);
        }
        return SUCCESS;
    }

    StatusEnum check_permission(Permission *perm)
    {
        return permissions.find(perm) != permissions.end() ? SUCCESS : FAILURE;
    }
};

class Owner : public Role
{
public:
    string role_name;
    set<Permission *> permissions;

    Owner()
    {
        role_name = "Owner";
        permissions.clear();
    }

    string get_role_name() { return role_name; }

    StatusEnum add_permission(Permission *perm)
    {
        permissions.insert(perm);
        return SUCCESS;
    }

    StatusEnum remove_permission(Permission *perm)
    {
        if (permissions.find(perm) != permissions.end())
        {
            permissions.erase(perm);
        }
        return SUCCESS;
    }

    StatusEnum check_permission(Permission *perm)
    {
        return permissions.find(perm) != permissions.end() ? SUCCESS : FAILURE;
    }
};

unordered_map<string, Role *> fetch_role_inventory()
{
    Role *obj;
    unordered_map<string, Role *> res;

    obj = new Admin();
    res[obj->get_role_name()] = obj;

    obj = new Customer();
    res[obj->get_role_name()] = obj;

    obj = new Owner();
    res[obj->get_role_name()] = obj;

    return res;
}