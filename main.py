"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import arcade
from game_state import GameState
from attack_animation import AttackType, AttackAnimation
from random import choice

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"


class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       self.game_state = None

       self.victor = None
       self.player_score = None
       self.computer_score = None

       self.computer = None
       self.player = None
       self.roche = None
       self.papier =None
       self.ciseaux = None
       self.computer_roche = None
       self.computer_papier = None
       self.computer_ciseaux = None

       self.player_attack_type = None
       self.computer_attack_type = None

       self.sprite_list = None
       arcade.set_background_color(arcade.color.AMAZON)
       self.background_list = arcade.SpriteList()
       self.cat2_list = arcade.SpriteList()
       self.cat_hitler_list = arcade.SpriteList()

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # C'est aussi ici que vous charger les sons de votre jeu.
       self.sprite_list = arcade.SpriteList()

       self.game_state = GameState.NOT_STARTED

       self.computer_score = 0
       self.player_score = 0

       self.computer = arcade.Sprite("assets/compy.png", 2, center_x=565, center_y=300)
       self.computer = arcade.Sprite("assets/compy.png", 0.5, center_x=175, center_y=300)

       self.roche = AttackAnimation(AttackType.ROCHE, 0.5, center_x=120, center_y=200)
       self.paper = AttackAnimation(AttackType.PAPIER, 0.5, center_x=220, center_y=200)
       self.ciseaux = AttackAnimation(AttackType.CISEAUX, 0.5, center_x=320, center_y=200)
       self.computer_roche = AttackAnimation(AttackType.ROCHE, 0.5, center_x=590, center_y=200)
       self.computer_papier = AttackAnimation(AttackType.PAPIER, 0.5, center_x=590, center_y=200)
       self.computer_ciseaux = AttackAnimation(AttackType.CISEAUX, 0.5, center_x=590, center_y=200)


       background = arcade.Sprite("assets/background_2.png", 1.85)
       background.center_x = 390
       background.center_y = 270

       cat2 = arcade.Sprite("assets/cat2.png", 0.085)
       cat2.center_x = 200
       cat2.center_y = 300

       cat_hitler = arcade.Sprite("assets/cat_hitler.png", 0.5)
       cat_hitler.center_x = 575
       cat_hitler.center_y = 290

       self.sprite_list = arcade.SpriteList()
       self.sprite_list.append(background)
       self.sprite_list.append(cat2)
       self.sprite_list.append(cat_hitler)

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".

       arcade.start_render()
       self.sprite_list.draw()

       arcade.draw_rectangle_outline(100, 140, 65, 65, (148, 0, 211), 3)
       arcade.draw_rectangle_outline(190, 140, 65, 65, (148, 0, 211), 3)
       arcade.draw_rectangle_outline(280, 140, 65, 65, (148, 0, 211), 3)
       arcade.draw_rectangle_outline(575, 140, 65, 65, (148, 0, 211), 3)

       if self.game_state == GameState.NOT_STARTED:
           arcade.draw_text("CLIQUEZ SUR ESPACE POUR COMMENCER", 100, 80, (148, 0, 211), 35, font_name="Rockwell")

       elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("CLIQUEZ SUR UNE IMAGE", 100, 475, (148, 0, 211), 35, font_name="Rockwell")
            arcade.draw_text("POINT DU JOUEUR:{self.player_score}", 100, 100, (148, 0, 211), 35, font_name="Rockwell")
            arcade.draw_text("POINT De L'ORDI:{self.computer_score}", 100, 100, (148, 0, 211), 35, font_name="Rockwell")

       self.roche.draw()
       self.papier.draw()
       self.ciseaux.draw()

       elif self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER
            arcade.draw_text("POINT DU JOUEUR:{self.player_score}", 100, 100, (148, 0, 211), 35, font_name="Rockwell")
            arcade.draw_text("POINT De L'ORDI:{self.computer_score}", 100, 100, (148, 0, 211), 35, font_name="Rockwell")

       if self.game_state == GameState.ROUND_DONE:
            arcade.draw_text("CLIQUEZ SUR ESPACE POUR JOUEZ À NOUVEAU", 35, 36, (148, 0, 211), 35, font_name="Rockwell")

       elif self.game_state == GameState.GAME_OVER:
            arcade.draw_text("JEU TERMINÉ", 100, 475, (148, 0, 211), 35, font_name="Rockwell")

       if self.player_attack_type == AttackType.ROCHE:
           self.roche.draw()
       elif self.player_attack_type == AttackType.PAPIER:
           self.papier.draw()
       elif self.player_attack_type == AttackType.CISEAUX:
           self.ciseaux.draw()


       if self.computer_attack_type == AttackType.ROCHE:
           self.computer_roche.draw()
       elif self.computer_attack_type == AttackType.PAPIER:
           self.computer_papier.draw()
       elif self.computer_attack_type == AttackType.CISEAUX:
           self.computer_ciseaux.draw()

       arcade.finish_render()

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       self.roche.on_update()
       self.papier.on_update()
       self.ciseaux.on_update()

       self.computer_roche.on_update()
       self.computer_papier.on_update()
       self.computer_ciseaux.on_update()

       if self.game_state == GameState.VICTORY:
           if self.player_attack_type == AttackType.ROCHE:
               if self.computer_attack_type == AttackType.ROCHE:
                   pass
               elif self.computer_attack_type == AttackType.PAPIER:
                   self.computer_ascore += 1
               else:
                   self.player_score += 1

           elif self.player_attack_type == AttackType.PAPIER:
               if self.computer_attack_type == AttackType.ROCHE:
                   self.player_score += 1
               elif self.computer_attack_type == AttackType.PAPIER:
                   pass
               else:
                   self.computer_score += 1

           else:
               if self.computer_attack_type == AttackType.ROCHE:
                   self.player_score += 1
               elif self.computer_attack_type == AttackType.PAPIER:
                   self.player_score += 1
               else:
                   pass

           if self.player_score == 3:
               self.victor = "JOUEUR"
               self.game_state = GameState.GAME_OVER

           elif self.computer_score == 3:
               self.victor = "ORDINATEUR"
               self.game_state = GameState.GAME_OVER

           else:
               self.game_state = GameState.ROUND_DONE

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
       if key == arcade.key.SPACE:
           if self.game_state ==GameState.NOT_STARTED:
               self.game_state == GameState.ROUND_ACTIVE

           if self.game_state == GameState.ROUND_DONE:
               self.game_state == GameState.ROUND_ACTIVE

           if self.game_state ==GameState.GAME_OVER:
               self.setup()

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """
       if self.game_state == GameState.ROUND_ACTIVE:
           if self.roche.collides_with_point((x, y)):
               self.game_state = GameState.VICTORY
               self.player_attack_type = AttackType.ROCHE
               self.computer_attack_type = choice([AttackType.ROCHE, AttackType.PAPIER, AttackType.CISEAUX])

           elif self.papier.collides_with_point((x, y)):
               self.game_state = GameState.VICTORY
               self.player_attack_type = AttackType.PAPIER
               self.computer_attack_type = choice([AttackType.ROCHE, AttackType.PAPIER, AttackType.CISEAUX])

           elif self.ciseaux.collides_with_point((x, y)):
               self.game_state = GameState.VICTORY
               self.player_attack_type = AttackType.CISEAUX
               self.computer_attack_type = choice([AttackType.ROCHE, AttackType.PAPIER, AttackType.CISEAUX])





def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()


