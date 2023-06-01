# TCP-Port-Scanner
**A no-frills TCP Port Scanner using Python**


A TCP port scanner is a tool used to scan a target system for open TCP ports. It works by sending packets to the target system's IP address and port numbers and analyzing the responses to determine which ports are open, closed, or filtered.
This is a simple Python script that performs a port scan on a specified IP address. It prompts the user to input the IP address, the starting port number, and the stopping port number. It then creates a thread for each port to be scanned and calls the conn function for each thread. The conn function attempts to create a socket connection with the specified IP address and port number. If the connection is successful, it adds the port number to the main_array. The lock is used to prevent race conditions when updating the main_array.

Once all the threads have completed their execution, the script prints the list of open ports.
Note that the setdefaulttimeout function is used to set the timeout for the socket connection attempt. In this case, it is set to a very low value of 0.001 seconds, which means that the connection attempt will time out quickly if it fails.

Overall, this script is a basic implementation of a port scanner and can be used for educational purposes. However, it is important to note that port scanning without permission is illegal and can lead to serious consequences.



Read More about this project in the desciption.
 
**Sample Screenshot:**
![image](https://github.com/probablyabdullah/TCP-Port-Scanner/assets/79295754/74ab7989-abde-47e9-904c-db75afd5d61a)
