
import socket #slouží ke komuniaci přes sít
import _thread #slouží pro praci ve více vlaknech
import os #os slouží k použítí příkazu v linux cmd
# import knihoven
client_counts = 0 #počítadlo počtu uživatelu na serveru
os.system("fuser -k 6969/tcp") #slouží k usmrcíení portu, na kterém běží server vždy před jeho puštění.
connected_clients = {} # slovník pro uživatele

def on_new_client(clientsocket,addr):
    global client_counts += 1 # při každém zavolaní funkce se c_count zvyší o 1
    while True:
        msg = clientsocket.recv(1024) #přijmaní byte array
        print (addr)
        if not msg: # kontrola toho že mu přišla zpráva
            break

        print (msg.decode("UTF-8")) #vypis zprávy

        clientsocket.send(msg) #vracní zpět uživateli.
    clientsocket.close()

s = socket.socket()         # uložení serveru do proměnné
host = socket.gethostname() # Získaní hostname mačiny
port = 6969                # proměnná s číslem portu, na kterém server posloucá.
print ('Server started!')
print ('Waiting for clients...')

s.bind((host, port))        # propojení ip s portem v proměnné s.
s.listen(5)                 # Čekaní na clienta 5s,
while True: #nekonečná smyčka, která čeká na připojení uživatele
   c, addr = s.accept()  #pokud se uživatel připojí, přijme mu to
   if global client_counts==0:
        #první uživatel má c_count rovno 0, proto mu do slovníku bude
                               #pod index O přirazená jeho adresa, od této doby systém ví,
                               #že hráč se znakem O má tuto adresu
         connected_clients['O'] = addr #přiřazení na index 0 adresu prvního připojeného
         _thread.start_new_thread(on_new_client,(c,addr))
   else if global client_counts ==1:#druhy uživatel má c_count rovno 1, proto mu do slovníku bude
                                    #pod index X přirazená jeho adresa, od této doby systém ví,
                                    #že hráč se znakem X má tuto adresu
         connected_clients['X'] = addr #přiřazení na index X adresu druhého připojeného
        _thread.start_new_thread(on_new_client,(c,addr))
   else:
         clientsocket.send("Přistup zamítnut")
         print("maximalni pocet hracu, přistup zamítnut") #každý další hrač který se během
       #hry připojí, bude mu vypsaná chyba. Přeci jen všichni víme, že tato hra je pro 2



  #Připojí hrače na vlastní vlákno, kde první parametr je název funkce on_new_client
  #druhá parametr jsou data o uživateli, který se připojuje
s.close()
