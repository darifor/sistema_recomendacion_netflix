import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from tkinter import messagebox
from tkinter import ttk

def buscar():
    '''
    if director_var:
        for i in range(len(director_list)):
            print(director_list[i], ": ", director_var[i].get())
    print("----------------")
    if genero_var:
        for i in range(len(genero_list)):
            print(genero_list[i], ": ", genero_var[i].get())
    print("----------------")
    if reparto_var:
        for i in range(len(reparto_list)):
            print(reparto_list[i], ": ", reparto_var[i].get())
    '''
    resultado = df.fillna("--")
    mostrar = True
    

    ## búsqueda de director
    directores = []
    directores_df = []
    if director_var:
        for i in range(len(director_list)):
            if director_var[i].get() == "Checked":
                directores.append(director_list[i])

        for director in directores:
            directores_df.append(resultado.loc[resultado["Director"].str.contains(director), 
                                               ["Title", "Director", "Genres", "Cast", "Production Country", "Content Type"]])

        if directores_df:
            dir_resultado = pd.concat(directores_df)
        else:
            dir_resultado = resultado
    else:
        dir_resultado = resultado

    ## búsqueda de género
    generos = []
    generos_df = []
    if genero_var:
        for i in range(len(genero_list)):
            if genero_var[i].get() == "Checked":
                generos.append(genero_list[i])

        for genero in generos:
            generos_df.append(dir_resultado.loc[dir_resultado["Genres"].str.contains(genero), 
                                                ["Title", "Director", "Genres", "Cast", "Production Country", "Content Type"]])

        if generos_df:
            gen_resultado = pd.concat(generos_df)
        elif directores_df:
            gen_resultado = dir_resultado
        else:
            gen_resultado = resultado
    else:
        if directores_df:
            gen_resultado = dir_resultado
        else:
            gen_resultado = resultado

    ## búsqueda de reparto
    repartos = []
    repartos_df = []
    if reparto_var:
        for i in range(len(reparto_list)):
            if reparto_var[i].get() == "Checked":
                repartos.append(reparto_list[i])

        for reparto in repartos:
            repartos_df.append(gen_resultado.loc[gen_resultado["Cast"].str.contains(reparto), 
                                                 ["Title", "Director", "Genres", "Cast", "Production Country", "Content Type"]])

        if repartos_df:
            rep_resultado = pd.concat(repartos_df)
        elif generos_df:
            rep_resultado = gen_resultado
        elif directores_df:
            rep_resultado = dir_resultado
        else:
            rep_resultado = resultado
    else:
        if generos_df:
            rep_resultado = gen_resultado
        elif directores_df:
            rep_resultado = dir_resultado
        else:
            rep_resultado = resultado

    ## búsqueda de país
    paises = []
    paises_df = []
    if pais_var:
        for i in range(len(pais_list)):
            if pais_var[i].get() == "Checked":
                paises.append(pais_list[i])

        for pais in paises:
            paises_df.append(rep_resultado.loc[rep_resultado["Production Country"].str.contains(pais), 
                                               ["Title", "Director", "Genres", "Cast", "Production Country", "Content Type"]])

        if paises_df:
            pais_resultado = pd.concat(paises_df)
        elif repartos_df:
            pais_resultado = rep_resultado
        elif generos_df:
            pais_resultado = gen_resultado
        elif directores_df:
            pais_resultado = dir_resultado
        else:
            pais_resultado = resultado
    else:
        if repartos_df:
            pais_resultado = rep_resultado
        elif generos_df:
            pais_resultado = gen_resultado
        elif directores_df:
            pais_resultado = dir_resultado
        else:
            pais_resultado = resultado

    ## búsqueda de tipo de contenido
    contenidos = []
    contenidos_df = []
    if tc_var:
        for i in range(len(tc_list)):
            if tc_var[i].get() == "Checked":
                contenidos.append(tc_list[i])

        for contenido in contenidos:
            contenidos_df.append(pais_resultado.loc[pais_resultado["Content Type"].str.contains(contenido), 
                                               ["Title", "Director", "Genres", "Cast", "Production Country", "Content Type"]])

        if contenidos_df:
            contenidos_resultado = pd.concat(contenidos_df)
        elif paises_df:
            contenidos_resultado = pais_resultado
        elif repartos_df:
            contenidos_resultado = rep_resultado
        elif generos_df:
            contenidos_resultado = gen_resultado
        elif directores_df:
            contenidos_resultado = dir_resultado
        else:
            contenidos_resultado = None
            mostrar = False
    else:
        if paises_df:
            contenidos_resultado = pais_resultado
        elif repartos_df:
            contenidos_resultado = rep_resultado
        elif generos_df:
            contenidos_resultado = gen_resultado
        elif directores_df:
            contenidos_resultado = dir_resultado
        else:
            contenidos_resultado = None
            mostrar = False

    if mostrar:
        resultado_final = contenidos_resultado.drop_duplicates()
        new_window = tk.Toplevel(window)
        tabla = Table(new_window, dataframe=resultado_final, showtoolbar=True, showstatusbar=True)
        tabla.show()
    else:
        messagebox.showwarning(title="Error", message="Debe seleccionar al menos una opción")


def update():
    global director_var
    global director_list
    global genero_var
    global genero_list
    global reparto_list
    global reparto_var
    global pais_var
    global pais_list
    global tc_var
    global tc_list

    index = listbox1.curselection()[0]
    titlelabel2.config(text=df.iloc[index]['Title'])
    descriptionlabel2.config(text=df.iloc[index]['Description'])
    director = df.iloc[index]['Director']
    genero = df.iloc[index]['Genres']
    reparto = df.iloc[index]['Cast']
    pais = df.iloc[index]['Production Country']
    tipo_de_contenido = df.iloc[index]['Content Type']

    ##### director
    white_dir_label = tk.Label(director_frame, text="")
    white_dir_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    director_var = []
    director_check = []
    if pd.isnull(director):
        director_empty = tk.Checkbutton(director_frame, text="No disponible", state='disabled')
        director_empty.place(relx=0.01, rely=0.1)
    else:
        director_list = director.split(", ")
        for i in range(len(director_list)):
            director_var.append(tk.StringVar(value="Not Checked"))
            director_check.append(tk.Checkbutton(director_frame, text=director_list[i], variable=director_var[i],
                                                onvalue='Checked', offvalue="Not Checked"))
    
        # ubicación director
        for i in range(len(director_list)):
            director_check[i].place(relx=0.03, rely=(i+1)*0.1)
    
    ###### género
    white_gen_label = tk.Label(genero_frame, text="")
    white_gen_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    genero_var = []
    genero_check = []
    if pd.isnull(genero):
        genero_empty = tk.Checkbutton(director_frame, text="No disponible", state='disabled')
        genero_empty.place(relx=0.01, rely=0.1)
    else:
        genero_list = genero.split(", ")
        for i in range(len(genero_list)):
            genero_var.append(tk.StringVar(value="Not Checked"))
            genero_check.append(tk.Checkbutton(genero_frame, text=genero_list[i], variable=genero_var[i],
                                                onvalue='Checked', offvalue="Not Checked"))
        
        # ubicación género
        for i in range(len(genero_list)):
            genero_check[i].place(relx=0.01, rely=(i+1)*0.1)

    ###### reparto
    white_rep_label = tk.Label(reparto_frame, text="")
    white_rep_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    reparto_var = []
    reparto_check = []
    if pd.isnull(reparto):
        reparto_empty = tk.Checkbutton(reparto_frame, text="No disponible", state='disabled')
        reparto_empty.place(relx=0.01, rely=0.1)
    else:
        reparto_list = reparto.split(", ")
        for i in range(len(reparto_list)):
            reparto_var.append(tk.StringVar(value="Not Checked"))
            reparto_check.append(tk.Checkbutton(reparto_frame, text=reparto_list[i], variable=reparto_var[i],
                                                onvalue='Checked', offvalue="Not Checked"))
        
        # ubicación reparto
        for i in range(len(reparto_list)):
            reparto_check[i].place(relx=0.01, rely=(i+1)*0.1)

    ###### país
    white_pais_label = tk.Label(pais_frame, text="")
    white_pais_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    pais_var = []
    pais_check = []
    if pd.isnull(pais):
        pais_empty = tk.Checkbutton(pais_frame, text="No disponible", state='disabled')
        pais_empty.place(relx=0.01, rely=0.1)
    else:
        pais_list = pais.split(", ")
        for i in range(len(pais_list)):
            pais_var.append(tk.StringVar(value="Not Checked"))
            pais_check.append(tk.Checkbutton(pais_frame, text=pais_list[i], variable=pais_var[i],
                                                onvalue='Checked', offvalue="Not Checked"))
        
        # ubicación país
        for i in range(len(pais_list)):
            pais_check[i].place(relx=0.01, rely=(i+1)*0.1)

    ###### tipo de contenido
    white_tc_label = tk.Label(contenido_frame, text="")
    white_tc_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    tc_var = []
    tc_check = []
    if pd.isnull(tipo_de_contenido):
        tc_empty = tk.Checkbutton(contenido_frame, text="No disponible", state='disabled')
        tc_empty.place(relx=0.01, rely=0.1)
    else:
        tc_list = tipo_de_contenido.split(", ")
        for i in range(len(tc_list)):
            tc_var.append(tk.StringVar(value="Not Checked"))
            tc_check.append(tk.Checkbutton(contenido_frame, text=tc_list[i], variable=tc_var[i],
                                                onvalue='Checked', offvalue="Not Checked"))
        
        # ubicación tipo de contenido
        for i in range(len(tc_list)):
            tc_check[i].place(relx=0.01, rely=(i+1)*0.1)

    ###### botón buscar
    buton2 = tk.Button(buscador_frame, text="Buscar", command=buscar)
    buton2.place(relx=0.43, rely=0.78, relheight=0.15, relwidth=0.15)



# abrir archivo y convertir csv en dataframe
filename = 'netflixData.csv'
df = pd.read_csv(filename)
titulos = list(df['Title'])


# interfaz gráfica
window = tk.Tk()
window.title("Sistema de recomendación de Netflix")
icono = tk.PhotoImage(file='flix.png')
window.iconphoto(True, icono)
window.geometry("1100x700")


# marco buscador
# elementos
buscador_frame = tk.LabelFrame(window, text="Buscador")
listbox_frame = tk.Frame(buscador_frame)
my_scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical")
var = tk.StringVar(value=titulos)
listbox1 = tk.Listbox(listbox_frame, listvariable=var, width="40", yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=listbox1.yview)
my_scrollbar.pack(side="right", fill="y")
listbox_frame.pack()
buton1 = tk.Button(buscador_frame, text="Seleccionar", command=update)
titlelabel = tk.Label(buscador_frame, text='Título:')
descriptionlabel = tk.Label(buscador_frame, text='Descripción:')
titlelabel2 = tk.Label(buscador_frame, text='')
descriptionlabel2 = tk.Label(buscador_frame, text='')


# marco buscador
# ubicaciones
buscador_frame.place(relx=0.03, rely=0.02, relheight=0.43, relwidth=0.94)
listbox_frame.place(relx=0.015, rely=0.03, relheight=0.95, relwidth=0.20)
listbox1.place(relx=0.015, rely=0.03, relheight=0.9, relwidth=0.9)
titlelabel.place(relx=0.23, rely=0.5)
descriptionlabel.place(relx=0.23, rely=0.6)
titlelabel2.place(relx=0.3, rely=0.5)
descriptionlabel2.place(relx=0.3, rely=0.6)
buton1.place(relx=0.23, rely=0.78, relheight=0.15, relwidth=0.15)

# marco criterios de búsqueda
# marcos interiores: director, género, reparto, país, tipo de contenido
criterios_frame = tk.LabelFrame(window, text="Criterios de búsqueda")
director_frame = tk.LabelFrame(criterios_frame, text="Director")
genero_frame = tk.LabelFrame(criterios_frame, text="Género")
reparto_frame = tk.LabelFrame(criterios_frame, text="Reparto")
pais_frame = tk.LabelFrame(criterios_frame, text="País")
contenido_frame = tk.LabelFrame(criterios_frame, text="Tipo de contenido")

# marco criterios de búsqueda
# ubicaciones de marcos interiores
criterios_frame.place(relx=0.03, rely=0.47, relheight=0.5, relwidth=0.94)
director_frame.place(relx=0.03, rely=0.03, relheight=0.9, relwidth=0.15)
genero_frame.place(relx=0.23, rely=0.03, relheight=0.9, relwidth=0.15)
reparto_frame.place(relx=0.43, rely=0.03, relheight=0.9, relwidth=0.15)
pais_frame.place(relx=0.63, rely=0.03, relheight=0.9, relwidth=0.15)
contenido_frame.place(relx=0.83, rely=0.03, relheight=0.9, relwidth=0.15)

window.mainloop()
