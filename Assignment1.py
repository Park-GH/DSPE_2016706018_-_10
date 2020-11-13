import torch
import socket
import platform
#ip_address 받아옴
ip_address = socket.gethostbyname(socket.gethostname())

#pytorch gpu버전이면 true, 아니면false
if torch.cuda.is_available():
    print("cuda is available")
else:
    print("cuda is not available")

print(ip_address)
#platform uname 시스템에 대한 여러가지 정보값 확인
#3.3이상버전 namedTuple리턴
print(platform.uname(), "\n")