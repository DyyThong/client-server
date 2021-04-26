# client-server
Assignment 1 MMT client-server.

## Client
Send Name, IP, UDP Port, time:day:month:year
through out TCP protocol.

1. Create a TCP socket
2. Call connect to establish connection with server 
3. Read respond of Server
4. Exit

## Server
(Optional) Send alert to Client.
Make an Unit ID and send back to Client.
Display data to user.
Send UDP message for specific Client for changing setting data.
through out UDP protocol.

1. Create TCP i.e Listening socket
2. Create a UDP socket 
3. Bind both socket to server address 
4. Handle new connection of TCP
5. Make new Unit ID 
6. When the connection is accepted write message to client including Unit ID
