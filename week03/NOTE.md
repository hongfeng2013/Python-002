学习笔记


1. python pmap.py -n 10 -f ping -ip 192.168.3.10-192.168.3.102 -w result_ping.json
[wsc@localhost test]$ python pmap.py -n 10 -f ping -ip 192.168.3.10-192.168.3.102 -w result_ping.json 
{'ping passed': ['192.168.3.13', '192.168.3.14', '192.168.3.29', '192.168.3.32', '192.168.3.101']}
ping finished
The execution time is: 30.3233859539
[wsc@localhost test]$ cat result_ping.json 
"{\"ping passed\": [\"192.168.3.13\", \"192.168.3.14\", \"192.168.3.29\", \"192.168.3.32\", \"192.168.3.101\"]}"

2. python pmap.py -n 20 -f ping -ip 192.168.3.10-192.168.3.102 -w result_ping.json
[wsc@localhost test]$ python pmap.py -n 20 -f ping -ip 192.168.3.10-192.168.3.102 -w result_ping.json 
{'ping passed': ['192.168.3.13', '192.168.3.14', '192.168.3.29', '192.168.3.32', '192.168.3.101']}
ping finished
The execution time is: 15.3483908176
[wsc@localhost test]$ cat result_ping.json 
"{\"ping passed\": [\"192.168.3.13\", \"192.168.3.14\", \"192.168.3.29\", \"192.168.3.32\", \"192.168.3.101\"]}"

3. python pmap.py -n 10 -f tcp -ip 127.0.0.1 -w result.json 
[wsc@localhost test]$ python pmap.py -n 10 -f tcp -ip 127.0.0.1 -w result.json
{'tcp port opened': ['127.0.0.1:25', '127.0.0.1:22', '127.0.0.1:111', '127.0.0.1:631']}
tcp finished
The execution time is: 0.556903839111
[wsc@localhost test]$ cat result.json 
"{\"tcp port opened\": [\"127.0.0.1:25\", \"127.0.0.1:22\", \"127.0.0.1:111\", \"127.0.0.1:631\"]}"

4. python pmap.py -n 20 -f tcp -ip 127.0.0.1 -w result.json 
[wsc@localhost test]$ python pmap.py -n 20 -f tcp -ip 127.0.0.1 -w result.json
{'tcp port opened': ['127.0.0.1:25', '127.0.0.1:22', '127.0.0.1:111', '127.0.0.1:631']}
tcp finished
The execution time is: 0.51438498497
[wsc@localhost test]$ cat result.json 
"{\"tcp port opened\": [\"127.0.0.1:25\", \"127.0.0.1:22\", \"127.0.0.1:111\", \"127.0.0.1:631\"]}"
