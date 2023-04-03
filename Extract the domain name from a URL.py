from urllib.parse import urlparse

def domain_name(url):
    domain = urlparse(url).netloc if url.startswith("http://") or url.startswith("https://") else url   
    domain = domain[4:] if domain.startswith("www.") else domain
    return(domain[:domain.index(".")])

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com" ))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
