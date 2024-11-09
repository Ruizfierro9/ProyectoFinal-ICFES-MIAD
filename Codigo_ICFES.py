import pandas as pd
df_2022 = pd.read_csv("data/df_2022.csv")

df_2022

# Lista con variables de interés (se escogen 24 inicialmente como las que podrían ser interesantes). Esto se hace no solo por el hecho de creer que podrían ser inyteresantes, sino que hay algunas variables con información repetitiva y no relevante, como por ejemplo, municipio y código de municipio (solo sería suficiente con tener el municipio).
variables_iniciales = ["ESTU_GENERO","ESTU_DEPTO_RESIDE","FAMI_EDUCACIONPADRE","FAMI_EDUCACIONMADRE","FAMI_ESTRATOVIVIENDA","FAMI_PERSONASHOGAR","FAMI_TIENEINTERNET","FAMI_TIENECONSOLAVIDEOJUEGOS","FAMI_NUMLIBROS","ESTU_HORASSEMANATRABAJA","FAMI_COMELECHEDERIVADOS","FAMI_COMECARNEPESCADOHUEVO","COLE_JORNADA","COLE_GENERO","COLE_NATURALEZA","COLE_BILINGUE","COLE_CARACTER","COLE_AREA_UBICACION","PUNT_MATEMATICAS","PUNT_INGLES","PUNT_C_NATURALES","PUNT_LECTURA_CRITICA","PUNT_SOCIALES_CIUDADANAS","PUNT_GLOBAL"]
#Nuevos DataFrame con las 24 variables seleccionadas
new_2022 = df_2022[variables_iniciales]
new_2022

#Calcular datos faltantes
def contar_faltantes(dataframe, lista):
    dicc_cont_faltantes = {}
    for i in lista:
        datos_faltantes = dataframe[i].isna().sum()
        dicc_cont_faltantes[i] = datos_faltantes
    return dicc_cont_faltantes
print("A continuación está el diccionario con los faltantes de la base 2022")
print(contar_faltantes(new_2022, variables_iniciales))

df_total=new_2022
#Eliminar las columnas que tienen más del 10% de datos faltantes, ya que eliminar las filas correspondientes sería perder tamaño en los datos, e imputar datos no es considerado para las variables dadas una buena opción ya que puede distorsionar el análisis descriptivo de los datos debido a la gran cantidad de datos faltantes.
#Por otro lado, para las columnas con menos de 10% de datos faltantes, se decide imputar los datos con la moda para variables categóricas en las que aplique, y con la media para variables numéricas en las que aplique.
diccionario = contar_faltantes(df_total, variables_iniciales)
columnas_a_eliminar = [llave for llave, valor in diccionario.items() if valor > 0.10*len(df_total)]
df_definitivo = df_total.drop(columns=columnas_a_eliminar)
imputar_moda = ['ESTU_GENERO','ESTU_DEPTO_RESIDE','FAMI_EDUCACIONPADRE','FAMI_EDUCACIONMADRE','FAMI_ESTRATOVIVIENDA','FAMI_TIENEINTERNET','FAMI_TIENECONSOLAVIDEOJUEGOS','ESTU_HORASSEMANATRABAJA','FAMI_NUMLIBROS','FAMI_PERSONASHOGAR','COLE_JORNADA','COLE_GENERO','COLE_NATURALEZA','COLE_CARACTER','COLE_AREA_UBICACION','FAMI_COMELECHEDERIVADOS','FAMI_COMECARNEPESCADOHUEVO']
imputar_media = ['PUNT_MATEMATICAS','PUNT_INGLES','PUNT_C_NATURALES','PUNT_LECTURA_CRITICA','PUNT_SOCIALES_CIUDADANAS','PUNT_GLOBAL']
for columna in imputar_moda:
    moda = df_definitivo[columna].mode()[0]
    df_definitivo[columna] = df_definitivo[columna].fillna(moda)
for columna in imputar_media:
    media = df_definitivo[columna].mean()
    df_definitivo[columna] = df_definitivo[columna].fillna(media)
df_definitivo


nombres_columnas = df_definitivo.columns.tolist()
diccionario2 = contar_faltantes(df_definitivo, nombres_columnas)
print(diccionario2) #Verifiqué que ya no hay datos nulos en el dataframe final.
print(len(df_definitivo)) #El dataframe final queda con 53279 observaciones y 23 columnas.
tipos_datos = df_definitivo.dtypes #Validar el tipo de datos.
print(tipos_datos)


