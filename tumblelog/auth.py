from functools import wraps
from flask import request, Response

def check_auth(username,password):
	""" auth function """
	return username == 'admin' and password == 'secret'

def authenticate():
	return Response(
		'could not verify your access level for that url.'
		'you hava to login with proper credentials',401,
		{'WWW-Authenticate':'Basic realm = "Login Required"'})



def requires_auth(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username,auth.password):
			return authenticate()
		return f(*args,**kwargs)

	return decorated
