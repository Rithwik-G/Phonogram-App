   
with open("emails.csv", 'a') as emails:
   import socket
   import threading
   import pickle

   from PIL import Image

   # import required module
   import os
   import pandas as pd

   import cv2

   # assign directory
   thumbnail_dir = 'thumbnails'
   vid_dir = 'videos'




   class vid:
      def __init__(self, video, thumb, page):
         self.video = video
         self.thumb = thumb
         self.page = page

         # self.packet = packet

      def __lt__(self, other):
         return self.page < other.page


   emailslist = list(pd.read_csv('emails.csv').iloc[:, 0])
   print(emailslist)

   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = socket.gethostbyaddr('13.52.102.141')[0]
   port = 5555
   server.bind((host, port))

   HEADER = 1024
   FORMAT = 'utf-8'
   DISCONNECT = "!DISCONNECT"

   def send(conn, msg):
      message = pickle.dumps(msg)
      msg_length = len(message)

      print(msg_length)

      send_length = pickle.dumps(str(msg_length))

      send_length += b' ' * (HEADER - len(send_length))

      conn.send(send_length)

      conn.send(message)


   def handle_client(conn, addr):
      msg_length = b''
      while (len(msg_length) != HEADER):
         msg_length += conn.recv(HEADER-len(msg_length))
      
      msg_length = int(pickle.loads(msg_length))

      print('a')
      msg = b''

      while (len(msg) != msg_length):
         msg += conn.recv(msg_length-len(msg))

      msg = pickle.loads(msg)

      print('b')



      print(addr, msg)
      if (msg != '123456789'):
         send(conn, "Wrong Password!")
         conn.close()
         return

      msg_length = b''
      while (len(msg_length) != HEADER):
         msg_length += conn.recv(HEADER-len(msg_length))
      
      msg_length = int(pickle.loads(msg_length))


      msg = b''

      while (len(msg) != msg_length):
         print(len(msg))
         msg += conn.recv(msg_length-len(msg))

      msg = pickle.loads(msg)


      msg = msg.strip('\n')
      print(addr, msg)
      if (msg not in emailslist):
         print(msg, emailslist)
         emails.write('\n' + msg)
         emailslist.append(msg)
      # if (msg not in emails):
      #    send(conn, "Wrong Password!")
      #    conn.close()
      #    return

      


      print(f"{addr} connected")

      send(conn, "Connected!")

      connected = True

      while connected:

         msg_length = pickle.loads(conn.recv(HEADER))
         if (msg_length):
            msg_length = int(msg_length)
            msg = pickle.loads(conn.recv(msg_length))

            if (msg == DISCONNECT):
               connected = False

            if (msg[0] == 'r'): # Request Thumbnails
               count = 0
               for filename in os.listdir(thumbnail_dir):
                  if (filename[0] == msg[1]):
                     count+=1

               send(conn, str(count))
               for filename in os.listdir(thumbnail_dir):
                  if (filename[0] == msg[1]):
                     f = os.path.join(thumbnail_dir, filename)
                     img = open(f, 'rb')
                     cur_vid = vid(filename[4:], img.read(-1), int(filename[1:4]))
                     send(conn, cur_vid)

            if (msg[0] == 'v'):
               for filename in os.listdir(vid_dir):
                  print(filename[:len(msg)-1], msg[1:])
                  if (filename[:len(msg)-1] == msg[1:]):
                     f = os.path.join(vid_dir, filename)
                     
                     file = open(f, 'rb')
                     file = file.read(-1)

                     send(conn, file)


      conn.close()



   def start():
      server.listen()
      while True:
         conn, addr = server.accept()
         thread = threading.Thread(target=handle_client, args=(conn, addr))
         thread.start()

         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

   # s.listen(5)
   # while True:
   #   c, addr = s.accept()
   #   print('Got connection from', addr)
   #   c.send('Thank you for connecting'.encode())
   #   c.close()

   start()