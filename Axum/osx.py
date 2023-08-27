import nmap

def os_fingerprinting(target_ip):
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(hosts=target_ip, arguments='-O')
    
    if 'osclass' in nmap_scan[target_ip]:
        operating_sys = nmap_scan[target_ip]['osclass']
        return operating_sys[0]['osfamily']
    else:
        return "Unknown"


