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

def put(**kwargs):
	ipNueva = kwargs.get('body')
	ip = ipNueva.get('ip')
	domain = ipNueva.get('domain')

	if not ip or not domain:
		Error = {}
		Error["error"] = "payload is invalid"
		return make_response(Error,400)
	
	notDup = False
	for alumno_existente in dominios.values():
		notDup = domain == alumno_existente.get('domain')
		if not notDup: break
		
		if notDup == False:
			Error = {}
			Error["error"] = "domain not found"
			return make_response(Error,404)
		dominios[domain]['ip'] = ip
		ipNueva = dominios[domain]
		return make_response(ipNueva, 201)
