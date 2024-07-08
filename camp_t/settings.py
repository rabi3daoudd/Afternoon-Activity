import socket
print(socket.gethostname())
if socket.gethostname()=="Joes-MacBook-Air.local":
    from camp_t.local_settings import *
else:
    from camp_t.production_settings import *