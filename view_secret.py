import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='dev-only-token',
)

print('Secret written successfully.')

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='/app1/bd1')

password = read_response['data']['data']['password']

if password != 'Hashi123':
    sys.exit('unexpected password')

print('Access granted!')
