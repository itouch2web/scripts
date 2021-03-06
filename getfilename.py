import tempfile
#import pycurl
import os

def get_filename_parts_from_url(url):
    fullname = url.split('/')[-1].split('#')[0].split('?')[0]
    t = list(os.path.splitext(fullname))
    if t[1]:
        t[1] = t[1][1:]
    return t

def retrieve(url, filename=None):
    if not filename:
        garbage, suffix = get_filename_parts_from_url(url)
        f = tempfile.NamedTemporaryFile(suffix = '.' + suffix, delete=False)
        filename = f.name
    else:
        f = open(filename, 'wb')
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.WRITEFUNCTION, f.write)
    try:
        c.perform()
    except:
        filename = None
    finally:
        c.close()
        f.close()
    return filename
url = input ('Please Type your file url: ')
retrieve(url, filename=None)
