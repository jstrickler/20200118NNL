import os

# os.system("cmd ...")
# os.popen("cmd...")

os.system("hostname")

with os.popen("hostname") as hostname_in:
    output = hostname_in.read()
    hostname = output.rstrip()
    print(repr(hostname))


with os.popen('netstat -an') as netstat_in:
    for raw_line in netstat_in:
        if 'ESTAB' in raw_line:
            line = raw_line.rstrip()
            proto, local_info, remote_info, status = line.split()
            local_ip, local_port = local_info.split(':')
            remote_ip, remote_port = remote_info.split(':')
            print(local_ip, remote_ip)
