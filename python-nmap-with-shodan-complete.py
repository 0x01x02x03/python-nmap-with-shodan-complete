import shodan

api = shodan.Shodan("Shodan_api_key")
print 'ip address to search'
ip = raw_input ()
host = api.host(ip)


print """
        IP: %s
        Organization: %s
        Operating System: %s
""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))


for item in host['data']:
        print """
                Port: %s
                Banner: %s

        """ % (item['port'], item['data'])