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

# Create a handler for our read (GET) people
def obtener_todos(q = ''):
    # Create the list of people from our data
    if q == '':
        return sorted(dominios.values(), key=lambda alumno: alumno.get('domain'))
    return q

    return filter(dominios.values(), key=lambda alumno: alumno.get('domain').find(q) != -1)



def obtener_uno(dominio):

	if dominio not in dominios:
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
	return dominios.get(dominio)




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



def borrar(id_alumno):
    if id_alumno not in dominios:
        return abort(404, 'El alumno no fue encontrado')

    del dominios[id_alumno]

    return make_response('', 204)



def put(**kwargs):

    ipNueva = kwargs.get('body')
    ip = ipNueva.get('ip')
    domain = ipNueva.get('domain')

    if not ip or not domain:
        return abort(400, 'Faltan datos para alterar una ip')

    dup = False
    for alumno_existente in dominios.values():
        dup = domain == alumno_existente.get('domain')
        if dup: break

    if dup == False:
        return abort(400, 'El domain no existe')

    dominios[domain]['ip'] = ip

    return make_response(ipNueva, 201)
