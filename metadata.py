"""
Metadata for the game used when installing the app into MC
"""
import os, sys

NAME = "Love Letter"
REF  = "/CartaDeAmor/"
DESC = "Love Letter is a game of risk, deduction, and luck for 2–4 players. Your goal is to get your love letter into Princess Annette's hands while deflecting the letters from competing suitors. From a deck with only sixteen cards, each player starts with only one card in hand; one card is removed from play. On a turn, you draw one card, and play one card, trying to expose others and knock them from the game. Powerful cards lead to early gains, but make you a target. Rely on weaker cards for too long, however, and your letter may be tossed in the fire!"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager.settings")

    from game.models.game_info import GameInfo

    game_check = GameInfo.objects.filter(ref=REF)
    if game_check.count() == 0:
        new_game = GameInfo(name=NAME, ref=REF, desc=DESC)
        new_game.save()
