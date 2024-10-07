import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='dev-only-token',
)

# Writing a secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='/app1/bd1',
    secret=dict(password='Hashi123'),
)

print('Secret written successfully.')
