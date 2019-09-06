import sys, socket
from Client import Client
from Server import Server

def main():    
    
    client = Client(300)
    
    name_complete = False
    while True:
        
        if name_complete == False:
            #collect users display name
            display_name = client.username()
            name_complete = True
            
        if client.menu() == "back":
            name_complete = False
            continue
            
        elif client.menu() == "join":
            option, opp_ip_address = client.get_opp_ip() 
            if option == "back":
                continue
                
            elif option == "start":
                if client.successful_connect() == "back":
                    continue
                elif client.successful_connect() == "begin":
                    client.start_game()
                    server.startGame()
                    
        elif client.menu() == "host":
            if client.start_screen() == "back":
                continue
            elif client.start_screen == "begin":
                client.start_game()
    
if __name__ == "__main__":
    main()
