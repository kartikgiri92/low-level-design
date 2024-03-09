# Role-Based-Access-Control LLD (RBAC)

Role-Based-Access-Control, also known as RBAC, is an authorization technique used in pretty much all the systems we interact with. As the name suggests it authorizes people on the basis of their role. For Example, In a Car rental service - A Customer should be allowed to check vehicles prices, but a Mangaer should be allowed to view and update vehicle prices.
While studying about this, I didn't find many implementations for this as this isn't a complete system by Itself and more of smaller service inside larger systems.
But Django uses something similar, So I did a deep dive in the docs/official code. Django stores the permissions inside a table with just strings as the permission value. Then it just makes another table which connects the permissions to the USER_ID (Basically a MANY-TO-MANY relationship). Pretty good approach and easy to implement.

Seeing this problem from LLD pov, we have to use in-memory stores. There are many ways to approach this. Below is my take and implementation for rbac. I created classes for the permissions instead of storing them as strings. A user class has a set of roles, a role has a set of permissions. This way users are assigned with the permission. For storage, I have a global map, which contains the current permission, user and the roles.
For testing, I created a sample-input file which can have the required cases/scenarios.
