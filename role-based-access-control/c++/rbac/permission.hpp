#pragma once
#include <bits/stdc++.h>
using namespace std;

class Permission
{
public:
    virtual string get_permission_name() = 0;
};

class DefaultPermission1 : public Permission
{
private:
    string permission_name;

public:
    DefaultPermission1()
    {
        permission_name = "DefaultPermission1";
    }

    string get_permission_name()
    {
        return permission_name;
    }
};

class DefaultPermission2 : public Permission
{
private:
    string permission_name;

public:
    DefaultPermission2()
    {
        permission_name = "DefaultPermission2";
    }

    string get_permission_name()
    {
        return permission_name;
    }
};

class AdminPermission1 : public Permission
{
private:
    string permission_name;

public:
    AdminPermission1()
    {
        permission_name = "AdminPermission1";
    }

    string get_permission_name()
    {
        return permission_name;
    }
};

class AdminPermission2 : public Permission
{
private:
    string permission_name;

public:
    AdminPermission2()
    {
        permission_name = "AdminPermission2";
    }

    string get_permission_name()
    {
        return permission_name;
    }
};

unordered_map<string, Permission *> fetch_permission_inventory()
{
    Permission *obj;
    unordered_map<string, Permission *> res;

    obj = new DefaultPermission1();
    res[obj->get_permission_name()] = obj;

    obj = new DefaultPermission2();
    res[obj->get_permission_name()] = obj;

    obj = new AdminPermission1();
    res[obj->get_permission_name()] = obj;

    obj = new AdminPermission2();
    res[obj->get_permission_name()] = obj;
    return res;
}