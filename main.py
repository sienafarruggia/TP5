"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
from random import randint

import arcade

import game_state
#import arcade.gui

from attack_animation import AttackType, AttackAnimation
#from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = game_state.GameState.NOT_STARTED

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = game_state.GameState.NOT_STARTED
       self.player = arcade.Sprite("assets/faceBeard.png", 0.6)
       self.computer = arcade.Sprite("assets/compy.png", 2.8)
       self.rock = AttackAnimation(AttackType.ROCK)
       self.paper = AttackAnimation(AttackType.PAPER)
       self.scissors = AttackAnimation(AttackType.SCISSORS)

       self.players = arcade.SpriteList()
       self.players.append(self.player)
       self.players.append(self.computer)
       self.player.center_x = 260
       self.player.center_y = 200
       self.computer.center_x = 800
       self.computer.center_y = 200
       self.rock.center_x = 170
       self.rock.center_y = 60
       self.paper.center_x = 265
       self.paper.center_y = 60
       self.scissors.center_x = 345
       self.scissors.center_y = 60



       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

       pass



   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """
       if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER:
           self.computer_score += 1
           self.player_won_round = False
           self.draw_round = False

       elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
           self.player_score += 1
           self.player_won_round = True
           self.draw_round = False

       elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS:
           self.computer_score += 1
           self.player_won_round = False
           self.draw_round = False

       elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
           self.player_score += 1
           self.player_won_round = True
           self.draw_round = False

       elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
           self.computer_score += 1
           self.player_won_round = False
           self.draw_round = False

       elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
           self.player_score += 1
           self.player_won_round = True
           self.draw_round = False

       else:
           self.draw_round = True


   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)

       """

       arcade.draw_lrtb_rectangle_outline(136, 206, 95, 25, arcade.color.RED)
       arcade.draw_lrtb_rectangle_outline(223, 295, 95, 25, arcade.color.RED)
       arcade.draw_lrtb_rectangle_outline(310, 382, 95, 25, arcade.color.RED)
       arcade.draw_lrtb_rectangle_outline(770, 840, 95, 25, arcade.color.RED)
       self.rock.draw()
       self.paper.draw()
       self.scissors.draw()
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")
       if self.game_state == game_state.GameState.NOT_STARTED:
           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer la partie!",
                        10,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3.1,
                        arcade.color.AERO_BLUE,
                        30,
                        width=SCREEN_WIDTH,
                        align="center")

       if self.game_state == game_state.GameState.ROUND_ACTIVE:
           arcade.draw_text("Appuyer sur une image pour faire une attaque!",
                        10,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3.1,
                        arcade.color.AERO_BLUE,
                        30,
                        width=SCREEN_WIDTH,
                        align="center")

       arcade.draw_text("Le pointage du joueur est " + str(self.player_score),
                        130,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 6.5,
                        arcade.color.AERO_BLUE,
                        15,
                        width=SCREEN_WIDTH,
                        align="left")

       arcade.draw_text("Le pointage de l'ordinateur est " + str(self.computer_score),
                        -80,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 6.5,
                        arcade.color.AERO_BLUE,
                        15,
                        width=SCREEN_WIDTH,
                        align="right")
       if self.game_state == game_state.GameState.GAME_OVER and self.player_score == 3:
            arcade.draw_text("Vous avez gagné la partie! Appuyer sur 'ESPACE' pour débuter une nouvelle partie.",
            10,
            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3.1,
            arcade.color.AERO_BLUE,
            24,
            width=SCREEN_WIDTH,
            align="center")

       if self.game_state == game_state.GameState.GAME_OVER and self.computer_score == 3:
           arcade.draw_text("Vous avez perdu la partie! Appuyer sur 'ESPACE' pour débuter une nouvelle partie.",
                            10,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3.1,
                            arcade.color.AERO_BLUE,
                            24,
                            width=SCREEN_WIDTH,
                            align="center")

       if self.game_state == game_state.GameState.ROUND_DONE:
           arcade.draw_text("Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!",
             20,
             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3.1,
             arcade.color.AERO_BLUE,
             30,
             width = SCREEN_WIDTH,
             align = "center")

        #Afficher le vainqueur de chaque ronde
       if self.player_won_round == True and self.draw_round == False and self.game_state == game_state.GameState.ROUND_DONE:
           arcade.draw_text("Tu as gagné la ronde!",
             10,
             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 5.4,
             arcade.color.AERO_BLUE,
             25,
             width=SCREEN_WIDTH,
             align="center")

       elif self.player_won_round == False and self.draw_round == False and self.game_state == game_state.GameState.ROUND_DONE:
           arcade.draw_text("L'ordinateur a gagné la ronde!",
             10,
             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 5.4,
             arcade.color.AERO_BLUE,
             25,
             width=SCREEN_WIDTH,
             align="center")

       if self.game_state == game_state.GameState.ROUND_DONE:
           arcade.draw_lrtb_rectangle_outline(136, 206, 95, 25, arcade.color.RED)
           arcade.draw_lrtb_rectangle_outline(223, 295, 95, 25, arcade.color.RED)
           arcade.draw_lrtb_rectangle_outline(310, 382, 95, 25, arcade.color.RED)
           arcade.draw_lrtb_rectangle_outline(770, 840, 95, 25, arcade.color.RED)
           if self.player_attack_type == AttackType.ROCK:
               self.rock.draw()
           elif self.player_attack_type == AttackType.PAPER:
               self.paper.draw()
           elif self.player_attack_type == AttackType.SCISSORS:
               self.scissors.draw()

       else:
           self.draw_possible_attack()

       self.draw_instructions()
       self.players.draw()

       self.draw_scores()

       if self.computer_attack_type == AttackType.ROCK:
           self.computer_rock = AttackAnimation(AttackType.ROCK)
           self.computer_rock.center_x = 810
           self.computer_rock.center_y = 65
           self.computer_rock.draw()

       elif self.computer_attack_type == AttackType.PAPER:
           self.computer_paper = AttackAnimation(AttackType.PAPER)
           self.computer_paper.center_x = 810
           self.computer_paper.center_y = 62
           self.computer_paper.draw()

       elif self.computer_attack_type == AttackType.SCISSORS:
           self.computer_scissors = AttackAnimation(AttackType.SCISSORS)
           self.computer_scissors.center_x = 804
           self.computer_scissors.center_y = 60
           self.computer_scissors.draw()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)
       self.scissors.on_update()
       self.rock.on_update()
       self.paper.on_update()
       if self.game_state ==game_state.GameState.ROUND_ACTIVE and self.player_attack_chosen == True:
           pc_attack = randint(0, 2)
           if pc_attack == 0:
               self.computer_attack_type = AttackType.ROCK
           elif pc_attack == 1:
               self.computer_attack_type = AttackType.PAPER
           else:
               self.computer_attack_type = AttackType.SCISSORS
           self.game_state = game_state.GameState.ROUND_DONE
           self.validate_victory()

       if self.player_score == 3 or self.computer_score == 3:
           self.game_state = game_state.GameState.GAME_OVER




       self.player_attack_chosen = False

   def on_key_press(self, key, key_modifiers):
       """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """
       if self.game_state == game_state.GameState.NOT_STARTED:
           self.game_state = game_state.GameState.ROUND_ACTIVE
       elif self.game_state == game_state.GameState.ROUND_DONE:
           self.reset_round()
           self.game_state = game_state.GameState.ROUND_ACTIVE
       elif self.game_state == game_state.GameState.GAME_OVER:
           self.setup()

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       self.computer_attack_type = -1
       self.player_attack_chosen = False
       self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       self.player_won_round = False
       self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
       if self.rock.collides_with_point((x, y)):
           self.player_attack_chosen = True
           self.player_attack_type = AttackType.ROCK

       elif self.paper.collides_with_point((x, y)):
           self.player_attack_chosen = True
           self.player_attack_type = AttackType.PAPER

       elif self.scissors.collides_with_point((x, y)):
            self.player_attack_chosen = True
            self.player_attack_type = AttackType.SCISSORS


#Attaque aleatoire de l'ordinateur






def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()
