def http_status(status):
  match status:
    case 200:
      return "OK"
    case 404:
      return "Not Found"
    case 500:
      return "Internal Srver Error"
    case _:
      return "Unknow Status"
    

print(http_status(5004))
