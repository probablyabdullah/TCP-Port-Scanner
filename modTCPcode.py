from socket import *
from threading import *
ip = input("Enter your IP address: ")
port_start = int(input("Enter the port to start the scan from: "))
port_stop = int(input("Enter the port to stop the scan on: "))
main_array=[]
print("Searching, Please Wait.")
print("\n")
print("This may take a moment...")
setdefaulttimeout(0.001)
lock= Lock()
thread_array =[]

def conn(ipx,portx,lock):
    addr =(ipx,portx)
    s= socket(AF_INET,SOCK_STREAM)
    result = s.connect_ex(addr)
    s.close()
    lock.acquire()
    if(result ==0 ):
        main_array.append(portx)
    lock.release()
for port in range(port_start,port_stop+1):
    t= Thread(target = conn , args=(ip,port,lock))
    t.start()
    thread_array.append(t)
for thread in thread_array:
    thread.join()
print("-"*40)
print("Scanning Completed!")
print("The ports which are currently open are: ")
print(main_array)
