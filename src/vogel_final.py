# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:49:18 2020

@author: Carlos

Modified on Mon Jun 13 17:17 2022
@modified by: Alejo Torres 
"""
import os
import pandas as pd

import sys


if __name__ == '__main__':

    path = os.path.dirname(os.path.abspath(__file__))  # ruta del archivo
    vogel = pd.read_csv(os.path.join(path, 'data', 'data.csv'))
    vogel.dropna(inplace=True)
    vogel = vogel.set_index('silos')

    ls_col = []
    for col in list(vogel.columns)[:-1]:
        # print([col])
        val_x_ren = vogel[col][:-1].sort_values(ascending=True)
        val_x_ren = list(val_x_ren[0:2])
        ls_col.append(abs(val_x_ren[0] - val_x_ren[1]))
    ls_col.append(0)
    row_df = pd.DataFrame([ls_col], columns=vogel.columns)
    vogel = pd.concat([vogel, row_df], ignore_index=True)

    ls_ren = []
    indice_fila = 0
    for indice_fila in range(vogel.shape[0]-2):
        # print(indice_fila)
        val_x_ren = vogel.iloc[indice_fila][:-1].sort_values(ascending=True)
        val_x_ren = list(val_x_ren[0:2])
        ls_ren.append(abs(val_x_ren[0] - val_x_ren[1]))
    ls_ren.append(0)
    ls_ren.append(0)
    vogel['penalizacion'] = ls_ren

    vogel_sol = vogel.copy()
    for i in range(vogel.shape[0]-2):
        for j in range(len(vogel.columns)-2):
            vogel_sol.iloc[i, j] = 0

    bandera = True
    fun_obj = 0
    while bandera:
        # Penalizacion columna
        if len(vogel.columns) == 2 or vogel.shape[0] == 2:
            print('Se acabaron las columnas')
            bandera = False
            break
        indice_pen_col = vogel.iloc[:-2, -1].idxmax()
        max_pen_col = vogel.iloc[:-2, -1].max()

        # Penalizacion renglon
        indice_pen_ren = vogel.iloc[-1, :-2].idxmax()
        max_pen_ren = vogel.iloc[-1, :-2].max()
        if max_pen_col == 0 and max_pen_ren == 0:
            print('Se termino el proceso')
            for i in list(vogel.columns)[:-2]:
                vogel_sol[i][list(vogel.index)[0]] = vogel[i][-2:-1].values[0]
            bandera = False

        else:
            if max_pen_col > max_pen_ren:  # Si esto occure buscara el valor minimo de la columna de los contrario buscara el minimo del renglon
                print('Buscara por renglon', indice_pen_col)
                # list(vogel.index).index(2)
#               indice_val_min = vogel.iloc[indice_pen_col, :-2].idxmin()
                indice_pen_col_sol = indice_pen_col
                indice_pen_col = list(vogel.index).index(indice_pen_col)
                indice_val_min = vogel.iloc[indice_pen_col, :-2].idxmin()
                oferta = vogel.iloc[indice_pen_col, -2]
                demanda = vogel[indice_val_min][-2:-1].values[0]
                if demanda != 0 and oferta != 0:
                    if oferta > demanda:
                        print('oferta > demanda')
                        fun_obj += (vogel.iloc[indice_pen_col]
                                    [indice_val_min] * demanda)
                        vogel_sol.iloc[indice_pen_col_sol][indice_val_min] = demanda
                        vogel[indice_val_min][-2:-1].values[0] = 0
                        vogel.iloc[indice_pen_col, -
                                   2] = vogel.iloc[indice_pen_col, -2] - demanda
                        vogel.iloc[indice_pen_col, -1] = 0
                        vogel.drop(indice_val_min, inplace=True, axis=1)
                        if oferta == demanda:
                            vogel.drop(indice_pen_col, inplace=True, axis=0)
                    else:
                        print('demanda < oferta')
                        fun_obj += (vogel.iloc[indice_pen_col]
                                    [indice_val_min] * oferta)
                        vogel_sol.iloc[indice_pen_col_sol][indice_val_min] = oferta
                        vogel.iloc[indice_pen_col, -2] = 0
                        vogel[indice_val_min][-2:-
                                              1].values[0] = vogel[indice_val_min][-2:-1].values[0] - oferta
                        vogel.iloc[indice_pen_col, -1] = 0
                        vogel.drop(indice_pen_col_sol, inplace=True, axis=0)
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_pen_col, inplace=True, axis=1)
# =============================================================================
                else:
                    # Si la oferta o la demanda son 0  se elimina de la tabla
                    if demanda == 0:
                        vogel.drop(indice_val_min, inplace=True, axis=1)
                    else:
                        vogel.drop(indice_pen_col_sol, inplace=True, axis=0)

            else:
                print('Buscara por columna', indice_pen_ren)
                indice_val_min = vogel[indice_pen_ren].iloc[:-2].idxmin()
                # vogel.iloc[indice_val_min,-2]
                oferta = vogel.loc[indice_val_min, :][-2]
                demanda = vogel[indice_pen_ren][-2:-1].values[0]
                if demanda != 0 and oferta != 0:
                    if oferta > demanda:
                        print('oferta > demanda')
                        fun_obj += (vogel[indice_pen_ren]
                                    [indice_val_min] * demanda)
                        vogel_sol[indice_pen_ren][indice_val_min] = demanda
                        vogel[indice_pen_ren][-2:-1].values[0] = 0
                        #vogel.iloc[indice_val_min,-2] = vogel.iloc[indice_val_min,-2] - demanda
                        vogel.iloc[indice_val_min, -2] = vogel.iloc[list(
                            vogel.index).index(indice_val_min), -2] - demanda
                        vogel[indice_pen_ren].iloc[-1] = 0
                        vogel.drop(indice_pen_ren, inplace=True, axis=1)
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_val_min, inplace=True, axis=0)
# =============================================================================
                    else:
                        print('demanda < oferta')
                        fun_obj += (vogel[indice_pen_ren]
                                    [indice_val_min] * oferta)
                        vogel_sol[indice_pen_ren][indice_val_min] = oferta
                        vogel.iloc[indice_val_min, -2] = 0
                        vogel[indice_pen_ren][-2:-
                                              1].values[0] = vogel[indice_pen_ren][-2:-1].values[0] - oferta
                        vogel[indice_pen_ren].iloc[-1] = 0
                        vogel.drop(indice_val_min, inplace=True, axis=0)
                else:
                    # Si la oferta o la demanda son 0  se elimina de la tabla
                    if demanda == 0:
                        vogel.drop(indice_pen_ren, inplace=True, axis=1)
                    else:
                        vogel.drop(indice_val_min, inplace=True, axis=0)
# =============================================================================
#                         if oferta==demanda:
#                             vogel.drop(indice_val_min, inplace=True, axis=1)
# =============================================================================
    print('******************************')
    print('Funcion Objetivo: ', fun_obj)
    print(vogel_sol)
