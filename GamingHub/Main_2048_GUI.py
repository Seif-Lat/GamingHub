from tkinter import *
from Affichage_Mat import*
import grid_2048
import move_2048
import Affichage_Mat



dict={'Up':((4,1),'h'),'Down':((5,1),'b'),'Right':((5,2),'d'),'Left':((5,0),'g')}
Afficher_bouton(dict)

def play():
        global grid
        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        size = int(set_size_grid())
        theme = grid_2048.THEMES[set_theme_grid()]
        grid = grid_2048.init_game(size)
        print("Situation de départ :")
        print(grid_2048.grid_to_string_with_size_and_theme(grid, theme, size))
        Affiche_mat(grid,root)#theme#
        tour = 1
        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        while not move_2048.is_game_over(grid) and grid_2048.get_grid_tile_max(grid) < 2048:
            moves = move_2048.move_possible(grid)
            commands_possible = [dic_move[i] for i in range(4) if moves[i]]
            command=set_direction()
            while not command in commands_possible:
                print("Deplacement impossible")
                Commentaire.delete(0,"end")
                Commentaire.insert(0,"Deplacement impossible, t'es con")
                command=set_direction()
                print("stuck")
            grid = move_2048.move_grid(grid, command)
            print("grid modifiée")
            Affiche_mat(grid,root)
            if not grid_2048.is_full_grid(grid):
                grid = grid_2048.grid_add_new_tile(grid)
            #print("Tour {}, deplacement {} :".format(tour, command))
            #textual_2048.modif_commentaire("Tour {"+str(tour)+"}, deplacement {"+command+"} :")
            #print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
                Affiche_mat(grid,root)
                print("new tile ajoutée")

            #tour += 1
            print("boucle atteinte")
        if grid_2048.get_grid_tile_max(grid) >= 2048:
            Commentaire.delete(0,"end")
            Commentaire.insert(0,"woohoo!! ça t'as pris du temps qd mm")
            print('vic')
            return "Victoire !"
        Commentaire.delete(0,"end")
        Commentaire.insert(0,"ha! comme si t'aurais vraiment gagné ...")
        print('GO')
        return "Game Over"
Start_game=Button(root, text="Commencer le jeu",command=play)
Start_game.grid(row= 2,column=0,sticky=W)


root.mainloop()



