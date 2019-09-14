import dns
from dns import resolver
# Resolve www.yahoo.com
result = dns.resolver.query('www.yahoo.com')
print(result.response.answer[1][0])
print(result.rrset.to_rdataset())
