import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

from module.producto.model import Producto
from module.producto.service import ProductoService
"""
Vista/interfaz
-Pendiente: Separar archivos en varias clases para mantenimiento
"""

class ProductoForm:
    def _init_(self):
        self.service = ProductoService()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Farmacia Torres")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Articulo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 =ttk.Label(self.labelframe1, text="id:")
        self.label1.grid(column = 0, row=0, padx=4, pady=4)
        self.idcarga=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe1, textvariable=self.idcarga)
        self.entryid.grid(column=1, row=0, padx=4, pady=4)

        
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Formula:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.formulacarga=tk.StringVar()
        self.entryformula=ttk.Entry(self.labelframe1, textvariable=self.formulacarga)
        self.entryformula.grid(column=1, row=2, padx=4, pady=4)


        self.label4=ttk.Label(self.labelframe1, text="Precio:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="Cantidad:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.cantidadcarga=tk.StringVar()
        self.entrycantidad=ttk.Entry(self.labelframe1, textvariable=self.cantidadcarga)
        self.entrycantidad.grid(column=1, row=4, padx=4, pady=4)


        
        self.label6=ttk.Label(self.labelframe1, text="Presentacion:")        
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.presentacioncarga=tk.StringVar()
        self.entrypresentacion=ttk.Entry(self.labelframe1, textvariable=self.presentacioncarga)
        self.entrypresentacion.grid(column=1, row=5, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="Caducidad:")        
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.caducidadcarga=tk.StringVar()
        self.entrycaducidad=ttk.Entry(self.labelframe1, textvariable=self.caducidadcarga)
        self.entrycaducidad.grid(column=1, row=6, padx=4, pady=4)

        self.label8=ttk.Label(self.labelframe1, text="Id Laboratorio")        
        self.label8.grid(column=0, row=7, padx=4, pady=4)
        self.laboratorio_idcarga=tk.StringVar()
        self.entrylaboratorio_id=ttk.Entry(self.labelframe1, textvariable=self.laboratorio_idcarga)
        self.entrylaboratorio_id.grid(column=1, row=7, padx=4, pady=4)

        self.label9=ttk.Label(self.labelframe1, text="Id Ubicacion")        
        self.label9.grid(column=0, row=8, padx=4, pady=4)
        self.ubicacion_idcarga=tk.StringVar()
        self.entryubicacion_id=ttk.Entry(self.labelframe1, textvariable=self.ubicacion_idcarga)
        self.entryubicacion_id.grid(column=1, row=8, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=9, padx=4, pady=4)

    def agregar(self):
        producto = Producto()
        producto.id = self.idcarga.get()
        producto.nombre = self.nombrecarga.get()
        producto.formula = self.formulacarga.get()
        producto.precio = self.preciocarga.get()
        producto.cantidad = self.cantidadcarga.get()
        producto.presentacion = self.presentacioncarga.get()
        producto.caducidad = self.caducidadcarga.get()
        producto.laboratorio_id = self.laboratorio_idcarga.get()
        producto.ubicacion_id = self.ubicacion_idcarga.get()
                 
        
    
        self.service.insertar(producto)
        mb.showinfo("Informacion", "Los datos fueron cargados")
        self.limpiar_agregar()

    def limpiar_agregar(self):
        self.idcarga.set("")
        self.nombrecarga.set("")
        self.formulacarga.set("")
        self.preciocarga.set("")
        self.cantidadcarga.set("")
        self.presentacioncarga.set("")
        self.caducidadcarga.set("")
        self.laboratorio_idcarga.set("")
        self.ubicacion_idcarga.set("")
   

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Articulo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)


        self.label1=ttk.Label(self.labelframe2, text="id:")        
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.id=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe2, textvariable=self.id, state="readonly")
        self.entryid.grid(column=1, row=1, padx=4, pady=4)



        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=2, padx=4, pady=4)


        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)



    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.id.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.id.set('')
            self.precio.set('')
            mb.showinfo("Informacion", "No existe un articulo con dicho codigo")




    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "codigo:"+str(fila[0])+
                                              "\nid:"+fila[1]+
                                              "\nnombre:"+fila[2]+
                                              "\nprecio:"+str(fila[3])+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de articulos")


        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Articulo")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)


        self.label1=ttk.Label(self.labelframe4, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Informacion", "Se borro el articulo con dicho codigo")
        else:
            mb.showinfo("Informacion", "No existe un articulo con dicho codigo")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar articulo")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Articulo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()





        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="id:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.idmod=tk.StringVar()
        self.entryid=ttk.Entry(self.labelframe5, textvariable=self.idmod)
        self.entryid.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.idmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Informacion", "Se modifico el articulo")
        else:
            mb.showinfo("Informacion", "No existe un articulo con dicho codigo")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.idmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.idmod.set('')
            self.preciomod.set('')
            mb.showinfo("Informacion", "No existe un articulo con dicho codigo")