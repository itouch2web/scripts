import urllib.request
import re
#import os.path

save_path = 'C:/Users/itouch/Desktop/temp/'

print ('### Download File###')
url = input ('Please Type your file url: ')
#http://resyncweb.com/files/contaodemo/theme/img/logo.png
filename = url.split('/')[-1]

urllib.request.urlretrieve (url, filename)
print (filename, 'Downloaded')
