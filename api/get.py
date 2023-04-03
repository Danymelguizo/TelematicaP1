import time
import os
import constants
import mimetypes


def get(path):

    if path == '/':
        path = 'index.html'

    else:
        path = path[1:]

    rt = os.getcwd()
    new_path = os.path.join(str(os.path.dirname(rt)), path)

    file = open(new_path, 'r')
    file = file.read()
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = mimetypes.guess_type(new_path)[0]
    content_length = os.path.getsize(new_path)

    answer = {
        'Date' : ttime,
        'Server' : 'AWS',
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file
    }

    return answer


request = get('/css/style.css')

print(request)