from request_util import Request_to_Django
def is_registered(id):
   request_emp = Request_to_Django(f"http://localhost:5000/api/v1/employee/{id}")
   res = request_emp.get_request()
   if response.stutus_code == 200:
      return True
   else:
      return False
   