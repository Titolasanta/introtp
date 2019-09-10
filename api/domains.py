from flask import abort, make_response
import dns.resolver as resolver
import dns.exception


# Data to serve with our API

def obtener_uno(domain):


	if domain not in dominios:
		try:
			result = resolver.query(dominio)
		except dns.exception.DNSException as ex:
			Error = {}
			Error["error"] = "domain not found"
			return make_response(Error, 404)
		for answer in result.response.answer:
			ipNueva = {}
			ipNueva['ip'] = str(answer[0])	
			ipNueva['domain'] = dominio	
			ipNueva['custom'] = 'false'	
			return ipNueva
		return abort(404, 'No Implementado')
	return custom-domain.dominios.get(dominio)
