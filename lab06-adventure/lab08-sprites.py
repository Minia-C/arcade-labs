import arcade
class Habitacion:
    def __init__(self,description,north,south,east,weast):
        self.description=description
        self.north=north
        self.south=south
        self.east=east
        self.weast=weast
def main():
    room_list=[]
    room0=Habitacion("estas en un bosque,al norte hay una cabaña",1,None,None,None)
    room_list.append(room0)
    room1=Habitacion("estas dentrp de la cabaña,al norte hay una puerta que lleva a un sotano,en el este esta el salon",4,0,2,None)
    room2=Habitacion("estas en el salon,al este esta la cocina y al norte una habitacion",3,None,5,1)
    room3=Habitacion("estas en la habitacion,no hay mucho por aqui",None,2,None,None)
    room4=Habitacion("estas en el sotano",None,1,None,None)
    room5=Habitacion("estas en la cocina",None,None,None,2)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)
    current_room=0
    done=False
    while done!=True:
        print("")
        print(room_list[current_room].description)
        a_donde_vas=input("a donde te diriges? ")
        if a_donde_vas.lower() in ("n", "north"):
            next_room=room_list[current_room].north

        elif a_donde_vas.lower() in("s","south"):
            next_room=room_list[current_room].south

        elif a_donde_vas.lower() in("e","east"):
            next_room=room_list[current_room].east

        elif a_donde_vas.lower() in("w","weast"):
            next_room=room_list[current_room].weast
           
        else:
            print("no entiendo,prueba de nuevo")
            continue

        if next_room is None:
            print("no hay camino por ahi,prueba de nuevo")
            continue
        else:
            current_room=next_room
        

     
main()
