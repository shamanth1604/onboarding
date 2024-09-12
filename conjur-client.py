"""

Initializes the Conjur client with the user's credentials.
Creates (adds) new secrets with placeholder values.
Reads (retrieves) the values of the secrets and prints them.
Updates (replaces) the secrets with new placeholder values.
Note that the Conjur API does not support the deletion of variable values.
"""

# https://pypi.org/project/conjur-client/
from conjur import Client

client = Client(api_key="", login_id="host/it/hc_service_account/shupendr_s3/prod_host", account="cisco", url="https://conjur-nonprod-write.cisco.com")

print(" ")
whoami = client.whoami()
print(f"The value of whoami is: {whoami}")
print(" ")

# Define the variable IDs
variable_ids = {
    'bucket_access_key': 'it/hc_service_account/shupendr_s3/s3_buckets/bucket_access_key',
    'bucket_secret_key': 'it/hc_service_account/shupendr_s3/s3_buckets/bucket_secret_key'
}

# Create (Add) new secrets
for var_id, value in variable_ids.items():
    print(f"Set var_id: {var_id} --> var_value: {value}")
    client.set(value, f'secret-value-for-{var_id}')

# Read (Retrieve) the secrets' values
for var_id in variable_ids.values():
    secret_value = client.get(var_id)
    print(f"The secret value for {var_id} is: {secret_value}")

# Update (Replace) the secrets' values
for var_id in variable_ids.values():
    print(f"Update var_id: {var_id} --> var_value: new-secret-value-for-{var_id}")
    client.set(var_id, f'new-secret-value-for-{var_id}')

# Read (Retrieve) the secrets' values
for var_id in variable_ids.values():
    secret_value = client.get(var_id)
    print(f"The secret value for {var_id} is: {secret_value}")