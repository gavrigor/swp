def application(environ, start_response):
   status = '200 OK'
   headers = [
   ('Content-Type', 'text/plain')
   ]
   body = environ['QUERY_STRING'].split("&")
   body = [item+"\n" for item in body]
   start_response(status, headers )
   return body 

# def app(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                  encoding="utf8")]
