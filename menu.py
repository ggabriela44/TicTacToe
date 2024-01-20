from button import Button
from enum import Enum
import settings
import pygame

main_menu_buttons = []
player_menu_buttons = []
game_menu_buttons = []
pause_menu_buttons = []
game_mode_buttons = []


class GameState(Enum):
    Exit = 0
    MainMenu = 1
    PlayerMenu = 2
    GameMenu = 3
    Game = 4
    Pause = 5
    Reset = 6


class GameMode(Enum):
    PVP = 1
    Normal = 2
    Extreme = 3


class Move(Enum):
    Player1 = 1
    Player2 = 2
    AI = 3  # computer


# zdarzenia przycisków
def set_pause_state():
    return GameState.Pause


def set_reset_state():
    return GameState.Reset


def set_pvp_mode():
    return GameMode.PVP


def set_normal_mode():
    return GameMode.Normal


def set_extreme_mode():
    return GameMode.Extreme


def set_exit_state():
    return GameState.Exit


def set_game_state():
    return GameState.Game


def set_player_menu_state():
    return GameState.PlayerMenu


def set_main_menu_state():
    return GameState.MainMenu


def add_btn():
    width_btn = 570
    height_btn = 75
    width_center = settings.WIDTH // 2
    height_center = settings.HEIGHT // 2

    exit_button = Button(width_center - width_btn / 2, height_center, width_btn, height_btn, pygame, "WYJŚCIE",
                         set_exit_state)
    exit_button2 = Button(settings.WIDTH-width_btn / 2+20, settings.HEIGHT-settings.MARGIN_HEIGHT+5, 200, 75, pygame, "WYJŚCIE",
                          set_exit_state, 1, 40)

    main_menu_buttons.append(exit_button)
    pause_menu_buttons.append(exit_button2)

    play_button = Button(width_center - width_btn / 2, height_center - 100, width_btn, height_btn, pygame, "GRAJ",
                         set_player_menu_state)
    main_menu_buttons.append(play_button)

    back_button = Button(width_center - width_btn / 2 + 50, settings.HEIGHT-settings.MARGIN_HEIGHT+5, 200, 75, pygame, "MENU",
                         set_reset_state, 1, 40)
    pause_menu_buttons.append(back_button)

    pvp_mode_button = Button(width_center - width_btn / 2, height_center - 150, width_btn, height_btn, pygame, "P1vsP2",
                             set_pvp_mode)
    normal_mode_button = Button(width_center - width_btn / 2, height_center - 50, width_btn, height_btn, pygame,
                                "Normalny", set_normal_mode)
    extreme_mode_button = Button(width_center - width_btn / 2, height_center + 50, width_btn, height_btn, pygame,
                                 "Ekspert", set_extreme_mode)

    game_mode_buttons.append(pvp_mode_button)
    game_mode_buttons.append(normal_mode_button)
    game_mode_buttons.append(extreme_mode_button)


