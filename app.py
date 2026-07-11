from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_info
from modules.ip_lookup import get_ip_info
from modules.ssl_lookup import get_ssl_info
from modules.headers_lookup import get_headers_info
from modules.technology_lookup import get_technology_info
from modules.robots_lookup import get_robots_info
from modules.port_scan import port_scan
from modules.subdomain_lookup import get_subdomain_info
from modules.geoip_lookup import get_geoip_info
from modules.reverse_dns_lookup import get_reverse_dns
from modules.email_security import get_email_security
from modules.http_methods import get_http_methods

domain = input("Enter a domain: ")

get_whois_info(domain)
get_dns_info(domain)
get_ip_info(domain)
get_ssl_info(domain)
get_headers_info(domain)
get_technology_info(domain)
get_robots_info(domain)
port_scan(domain)
get_subdomain_info(domain)
get_geoip_info(domain)
get_reverse_dns(domain)
get_email_security(domain)
get_http_methods(domain)
