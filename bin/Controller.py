from pygame.locals import *
import pygame


from .Events import *
from .Constants import *

class Controller:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.keepGoing = True

    def Run(self):
        while self.keepGoing:
            ev = TickEvent()
            self.evManager.Post(ev)

            for event in pygame.event.get():
                ev = None
                if event.type == QUIT:
                    ev = QuitEvent()

                # Temporary Test Events
                elif event.type == KEYDOWN and event.key == K_q:
                    ev = BuyIngredientEvent(INGREDIENTS_LIST[0], 5, 10)

                elif event.type == KEYDOWN and event.key == K_a:
                    ev = BuyIngredientEvent(INGREDIENTS_LIST[2], 2, 10)

                elif event.type == KEYDOWN and event.key == K_w:
                    ev = AddDishEvent(DISHES_LIST[1])

                elif event.type == KEYDOWN and event.key == K_e:
                    ev = NewDayEvent()

                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    ev = LeftClickEvent(pos)

                if ev:
                    self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, QuitEvent):
            self.keepGoing = False