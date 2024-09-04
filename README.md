# Conjur Onboarding

Welcome to the Conjur onboarding repository! This repo contains information on how to use Conjur for secrets management.

## What is a Policy?

In Conjur, a policy is a set of rules that defines how secrets and permissions are managed. Policies dictate who has access to secrets, what kind of secrets can be stored, and how secrets are organized within the Conjur system. Policies are written in YAML format and are used to:

- Define roles (such as users, machines, or applications)
- Set permissions for these roles
- Specify how secrets should be structured and accessed

A policy essentially provides the blueprint for how your secrets are handled, ensuring that access is controlled and managed securely.

## Defining a Policy

Policies in Conjur are defined using YAML syntax. The structure typically includes:

- **Roles:** Defines the entities (users, applications, etc.) that will interact with Conjur.
- **Permissions:** Specifies what actions (read, write, execute) roles are allowed to perform on secrets.
- **Secrets:** Details how secrets are organized and accessed.

Here's a basic example to illustrate how you might define a policy:

```yaml
# Define a policy to manage access to database credentials

# Define roles
- !group
  id: developers
  # This defines a group role named 'developers'. This role can be assigned to multiple users or applications.

- !host
  id: webserver
  annotations:
    role: webserver
  # This defines a host role named 'webserver'. It represents a server or application that needs access to secrets.

- !user
  id: alice
  # This defines a user role named 'alice'. This role represents an individual user.

# Define secrets
- !secret
  id: db/password
  value: "supersecretpassword"
  # This defines a secret named 'db/password' with the value 'supersecretpassword'. In practice, you would store secrets securely rather than hardcoding them.

# Define permissions
- !grant
  role: !group developers
  privileges: [read]
  resource: !secret db/password
  # This grants the 'developers' group read access to the 'db/password' secret.

- !grant
  role: !user alice
  privileges: [read]
  resource: !secret db/password
  # This grants the 'alice' user read access to the 'db/password' secret.

- !grant
  role: !host webserver
  privileges: [read]
  resource: !secret db/password
  # This grants the 'webserver' host read access to the 'db/password' secret.
