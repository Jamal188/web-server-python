home_dir = "/home/jamal/dev1/web_server"

def read_request(request):
    
    lines = request.split()
    method = lines[0]
    path= lines[1]
    
    return method, path


def get_handle(path):
    if path=="/" :
        file_path=f"{home_dir}/index.html"
    else : 
        file_path=f"{home_dir}{path}"
    fopen = open(file_path, 'r')
    content = fopen.read()
    fopen.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    return response


handlers = {
        'GET' : get_handle

        }



def request_handler(request):

    method, path = read_request(request)
    response = handlers[method](path)
    return response.encode()





