
import pandas as pd

if __name__ == '__main__':

    ruta = 'C://Users//nuria//Desktop//daniel//Opti//programas//vogel.csv' # ruta del archivo
    esquina_noro = pd.read_csv(ruta) #lee el archivo
    esquina_noro = esquina_noro.set_index('fuentes') # No cambiar de nombre
   
    
    #crea una copia del archivo origel para poder las soluciones
    esquina_noro_sol = esquina_noro.copy()
    for i in range(esquina_noro.shape[0]-1):
        for j in range(len(esquina_noro.columns)-1):
                esquina_noro_sol.iloc[i,j] = 0

    # Esta x y nos sirven para asignar los valores a nuestra tabla de soluciones
    x = 0
    y = 0
    fun_obj = 0
    bandera = True
    ofer = -1
    dem = -1
    while True:
        #Si la oferta y la demanda son 0 salir del proceso
        if (ofer==0 and dem == 0) or (esquina_noro.shape[0]<1):
            print('Proceso terminado')
            bandera = False
            break
        
        #obtiene la posicion de la oferta y demanda de nuestro archivo 
        ind_oferta = len(esquina_noro.columns) -1
        ind_demanda = esquina_noro.shape[0] - 1   
        #obtiene la oferta y demanda de nuestro archivo siempre de la esquina noroeste 
        ofer = esquina_noro.iloc[0, ind_oferta]
        dem = esquina_noro.iloc[ind_demanda, 0]

        # Entrara al proceso si la demanda y la oferta son diferentes de 0
        if dem != 0 and ofer != 0:
            # si la demanda es mayor a la oferta entra en caso contrario pasa el else
            # aqui se hace asigna la maxima cantidad  dependiendo las restricciones de la oferta y demanda
            if dem > ofer:
                esquina_noro_sol.iloc[x, y] = ofer 
                fun_obj += (esquina_noro.iloc[0, 0] * ofer) # multiplica la oferta por el costo
                esquina_noro.iloc[0, ind_oferta] = esquina_noro.iloc[0, ind_oferta] - ofer # Se le quita la oferta a la oferta
                esquina_noro.iloc[ind_demanda, 0] = esquina_noro.iloc[ind_demanda, 0] - ofer  # Se le quita la oferta a la demanda
                esquina_noro.drop(esquina_noro.index[0], inplace=True, axis=0)
                x += 1

            else:
                esquina_noro_sol.iloc[x, y] = dem
                fun_obj += (esquina_noro.iloc[0, 0] * dem)
                esquina_noro.iloc[0, ind_oferta] = esquina_noro.iloc[0, ind_oferta] - dem # Se le quita la demanda a la oferta
                esquina_noro.iloc[ind_demanda, 0] = esquina_noro.iloc[ind_demanda, 0] - dem # Se le quita la demanda a la demanda
                esquina_noro.drop(esquina_noro.columns[0], inplace=True, axis=1)
                y += 1
        else:
            # Si la oferta o la demanda son 0  se elimina de la tabla
            if dem > ofer:
                esquina_noro.drop(esquina_noro.index[0], inplace=True, axis=0)
                x += 1
            else:
                esquina_noro.drop(esquina_noro.columns[0], inplace=True, axis=1)
                y += 1
        #Si la oferta y la demanda son 0 salir del proceso                
        if (ofer==0 and dem == 0) or (esquina_noro.shape[0]<1):
            print('Proceso terminado')
            bandera = False
            break

    print('******************************') 
    print('Funcion Objetivo: ', fun_obj)
    print(esquina_noro_sol)

