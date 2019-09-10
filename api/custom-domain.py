from flask import abort, make_response
import dns.resolver as resolver
import dns.exception
# Data to serve with our API
dominios = {
    "1": {
        'ip': 1,
        'domain': '1',
        'custom': 'true'
    },
}

def put():
	return {}
