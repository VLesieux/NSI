import Othello as jeu

JOUEUR1 = 1
JOUEUR2 = 2

def jouer():
    choix=input("1. Jeu contre un humain 2. Jeu contre l'ordinateur : ")
    config = jeu.creer_config_init()
    joueur_courant = jeu.choisir_premier_joueur()
    jeu.afficher_config(config)

    while not jeu.est_jeu_fini(config):
        if jeu.est_coup_possible(config, joueur_courant) :
            coup = jeu.coup_joueur(config, joueur_courant,choix)
            config = jeu.incrementer_config(config,coup,joueur_courant)
            jeu.afficher_config(config)
        joueur_courant = jeu.incrementer_joueur(joueur_courant)
    jeu.afficher_fin(config,joueur_courant)


def min_max(config, profondeur, joueur):
    '''
    Renvoie la valeur de la configuration passée en paramètre
    :param config: configuration du jeu
    :param profondeur: (int) profondeur restante pour l'évaluation de la configuration
    :param joueur: (int) numero du joueur courant
    
    '''
    if jeu.est_jeu_fini(config) or profondeur == 0:
        return jeu.evaluation(config,joueur)*jeu.coef_joueur(joueur)
    else:
        if joueur == JOUEUR1:
            liste_configs_suivantes = jeu.creer_liste_configs_suivantes(config, JOUEUR1)
            return min([min_max(suivante, profondeur-1, JOUEUR2) for suivante in liste_configs_suivantes])
        else:
            liste_configs_suivantes = jeu.creer_liste_configs_suivantes(config, JOUEUR2)
            return max([min_max(suivante, profondeur-1, JOUEUR1) for suivante in liste_configs_suivantes])


if __name__ == "__main__":
    jouer()