#import la libreria tkinter, con el alias tk
import tkinter as tk
from tkinter import Frame, BOTH, Canvas, PhotoImage, Scale
# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------

def modificar_arco(angulo):
    c.itemconfig(arc1,start=angulo)  
    c.itemconfig(arc3,start=int(angulo)+120) 
    c.itemconfig(arc5,start=int(angulo)+240)

ventana_principal = tk.Tk()
ventana_principal.title("MOLINO")
ventana_principal.geometry("400x475")
ventana_principal.resizable(False, False)

BASE = 350
ALTURA = 350
#----------------------
# FRAME DE GRAFICACIÓN
#----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg ="black", width=380, height=380)
frame_graficacion.place(x=10, y=10)

# creacion de canvas
c = Canvas(frame_graficacion, width=360, height=360, bg="pink")
c.place(x=10 , y=10)

triangulo= c.create_polygon(100,300,250,300,BASE/2,150, fill="sienna4", outline="sienna4")


arc1 = c.create_arc(95,70,255,230, start=0, extent=60, fill="medium orchid", outline="LightSkyBlue2")
#arc2 = c.create_arc(95,70,255,230, start=60, extent=60, fill="medium orchid", outline="LightSkyBlue2")
arc3 = c.create_arc(95,70,255,230, start=120, extent=60, fill="medium orchid", outline="LightSkyBlue2")
#arc4 = c.create_arc(95,70,255,230, start=180, extent=60, fill="medium orchid", outline="LightSkyBlue2")
arc5 = c.create_arc(95,70,255,230, start=240, extent=60, fill="medium orchid", outline="LightSkyBlue2")
#arc6 = c.create_arc(95,70,255,230, start=360, extent=60, fill="medium orchid", outline="LightSkyBlue2")

frame_2=Frame(ventana_principal)
frame_2.config(bg="black",width=380,height=90)
frame_2.place(x=10,y=380)
barra_deslizamiento = Scale(frame_2, label='ÁNGULO', from_=0, to=360, orient="horizontal", length=355, command=modificar_arco, tickinterval=90)
barra_deslizamiento.place(x=10,y=10)

# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()