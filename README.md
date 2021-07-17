# Intra-Home-Server
## (An application of socket programming in python)
Let's say that your laptop-to-mobile cord is not working and you want to transfer data(data is basically a stream of bytes) 
between your mobile and laptop. Ofcourse you can upload the files on the drive and then access it from any device where your account is logged in. But if
you want the data to be available to all the devices connected to the same network(like same wi-fi network) then you can implement it using the python and its 
support for socket programming. <br>
## Working
Here one of the device would act as a server(it can be your laptop or your mobile where server.py is running) and all the other devices can act as a client. Now the connection 
establishes as run the client.py file on your desired device. Yes, you can run python files on your android phone. Just go to playstore and install pydroid or qpython. Once the
connection is established the server can send messages to client and the client can send messsage to server and clients and send messages to each other as well.
## Vision for this project
Right now only the transfer of messages is implemented. Messages are basically strings and as we know that everything is object in python. So if we can send strings as a byte 
stream, we can also send pdfs, images as well. Basically any object can be sent via sockets by dumping that object using pickle for example.
