import subprocess, re, os, datetime

def check_dir(dirname, days):
    for name in os.listdir(dirname):
        name = os.path.join(dirname, name)
        if os.path.isdir(name):
            check_dir(name, days)
        elif name.endswith('.crt'):
            check_file(name, days)

def cert_expiry_date(filename):
    valid_not_after = subprocess.check_output(["openssl", "x509", "-enddate", "-in", filename, "-noout"]).decode('utf-8')
    match = re.match("notAfter=([a-zA-Z0-9: ]+)", valid_not_after)
    assert match is not None, "Unexpected output from openssl: " + valid_not_after
    enddate = match.group(1)
    return datetime.datetime.strptime(enddate, '%b %d %X %Y %Z')

def check_file(filename, days):
    enddate = cert_expiry_date(filename)
    delta = enddate - datetime.datetime.now()
    if delta < datetime.timedelta(days=days):
        print("{} expires at {}, which is in {} days".format(filename, enddate, delta.days))
