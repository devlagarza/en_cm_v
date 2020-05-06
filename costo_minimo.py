
import pandas as pd

 
if __name__ == '__main__':

    ruta = r'C:/Users/nuria/Desktop/daniel/Opti/programas/'
    costo_min = pd.read_csv('vogel.csv')
    costo_min.dropna(inplace=True)
    costo_min = costo_min.set_index('fuentes')
    costo_min_sol = costo_min.copy()
    for i in range(costo_min.shape[0]-1):
        for j in range(len(costo_min.columns)-1):
            costo_min_sol.iloc[i, j] = 0

    bandera = True
    fun_obj = 0
    while bandera:
        minimos = costo_min.iloc[:-1, :-1].idxmin(axis=1) # Encuentra el indice del costo minimo por columna
        if minimos.shape[0] == 0:
            bandera = False
            print('Proceso terminado')
            break
            

        minimo = costo_min.loc[costo_min.index[0], minimos[0]] # Obtiene el minimo del primer renglon
        count = 0
        renglon = 0
        columna = minimos[0] # Obtiene la columan del del minimo del primer renglon
        for i in  range(1, costo_min.shape[0]-1):# Recorrera todas las columnas con costos a partir del renglon 1
            #print(i)
            aux = costo_min.loc[costo_min.index[i], minimos[i]] # Obtiene el minimo del renglon
            if aux < minimo: #Compara el minimo de todos los renglonnes contra el minimo del renglon 0
                #Se guarda el renlon y columna de valor minimo
                renglon = i
                columna = minimos[i]
                minimo = aux

        #Obtiene la demanda y oferta del costo minimo
        oferta = costo_min.iloc[renglon, -1]
        demanda = costo_min.loc[costo_min.index[-1], columna]
        # Se hace asigna la maxima cantidad  dependiendo las restricciones de la oferta y demanda
        if demanda != 0 and oferta != 0:
            if oferta > demanda:
                #print('Ofer > demanda')
                #print(str(costo_min.loc[costo_min.index[renglon], columna]),' * ', str(demanda))
                fun_obj += (costo_min.loc[costo_min.index[renglon], columna] * demanda) # multiplica la oferta por el costo
                costo_min_sol.loc[costo_min.index[renglon], columna] = demanda
                costo_min.loc[costo_min.index[-1], columna] = 0
                costo_min.iloc[renglon, -1] = costo_min.iloc[renglon, -1] - demanda # Se le quita la oferta a la demanda
                costo_min.drop(columna, inplace=True, axis=1) #Se elimina la columna
            else:
                #print('Ofer < demanda')
                fun_obj += (costo_min.loc[costo_min.index[renglon], columna] * oferta)
                costo_min_sol.loc[costo_min.index[renglon], columna] = oferta
                costo_min.iloc[renglon, -1] = 0
                costo_min.loc[costo_min.index[-1], columna] = costo_min.loc[costo_min.index[-1], columna] - oferta # Se le quita la demanda a la oferta
                costo_min.drop(costo_min.index[renglon], inplace=True, axis=0) #Se elimina el renglon
            if minimos.shape[0] == 0:
                bandera = False
                break
                print('Proceso terminado')
        else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
            if demanda == 0:
                costo_min.drop(columna, inplace=True, axis=1)
            else:
                costo_min.drop(costo_min.index[renglon], inplace=True, axis=0)

    print('******************************')
    print('Funcion Objetivo: ', fun_obj)
    print(costo_min_sol)
