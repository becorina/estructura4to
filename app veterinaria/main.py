from tkinter import
#from cliente import
#from masscota import
#from database import
#from agregar_mascotas import abrir_agregar_mascotas
#from agregar_clientes import abrir_agregar_clientes
#from estilos import

root= Tk()
root.geometry("500x700")
marco_principal = frame( root) 


menubar=Menu=(root)

menubasedat=Menu(menubar, tearrof=0)
menubasedat.add_command(label="Crear BBDD", command= crear_base_datos)
menubasedat.add_command(label="salir", command= lambda: root.destroy())
menubar.add_cascade(label= "BBDD", menu = menubasedat)
root.config(menu = menubar,bg= "#DEF2FC")
# label titulo
menu_titulo= label(root, text= "veterinaria", bg= "#FBB7E7", font=("Comic Sans Ms", 35 ,"bold"))
menu_titulo.pack(pady= 3)
marco.pack(pady= 15)

