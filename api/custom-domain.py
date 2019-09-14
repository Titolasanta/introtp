from flask import abort, make_response
import dns
from dns import resolver
import dns.exception
# Data to serve with our API
dominios = {
	"1": {
		'ip': 1,
        	'domain': '1',
		'custom': 'true'
	},
}

real_dominios = {}

def obtener_uno(dominio):
	if dominio not in dominios:
		try:
			result = dns.resolver.query(dominio)
		except dns.exception.DNSException as ex:
			Error = {}
			Error["error"] = "domain not found"
			return make_response(Error, 404)
		if dominio not in real_dominios:
			dominioNuevo = {}
			dominioNuevo['pos'] = 0
			dominioNuevo['response'] = result.rrset.to_rdataset()
			real_dominios[dominio] = dominioNuevo
		if real_dominios[dominio]['response'] != result.rrset.to_rdataset():
			real_dominios[dominio]['response'] = result.rrset.to_rdataset()
		i = real_dominios[dominio]['pos']
		i = (i+1) % len(real_dominios[dominio]['response'])
		real_dominios[dominio]['pos'] = i
		answer = real_dominios[dominio]['response'][i]	
		ipNueva = {}
		ipNueva['ip'] = str(answer)	
		ipNueva['domain'] = dominio	
		ipNueva['custom'] = 'false'
		return ipNueva

	return custom-domain.dominios.get(dominio)


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


def crear(**kwargs):
    ipNueva = kwargs.get('body')
    ip = ipNueva.get('ip')
    domain = ipNueva.get('domain')
    ipNueva['custom'] = 'true'

    if not ip or not domain:
        return abort(400, 'Faltan datos para crear un ip')

    dup = False
    for alumno_existente in dominios.values():
        dup = domain == alumno_existente.get('domain')
        if dup: break

    if dup:
        Error = {}
        Error["error"] = 'custom domain already exists'
        return make_response(Error, 400)

    dominios[domain] = ipNueva

    return make_response(ipNueva, 201)

def borrar(dominio):
    if dominio not in dominios:
        return abort(404, 'El dominio no fue encontrado')

    del dominios[dominio]

    respuesta = {}
    respuesta['dominio'] = dominio

    return make_response(respuesta, 200)

def obtener_todos(q = ''):
    if q == '{q}':
        return sorted(dominios.values(), key=lambda alumno: alumno.get('domain'))

    return list(filter(lambda val: val.get('domain').find(q) != -1, dominios.values() ))







