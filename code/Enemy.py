#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = -1  # -1 p cima, 1 p baixo
        self.speed_vertical = ENTITY_SPEED[self.name]

    def move(self):
        # eixo x com movimento da direita p a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]
        #  eixo y com movimento de subir e descer
        self.rect.centery += self.direction * self.speed_vertical

        if self.rect.top <= 0:  # se bate na borda superior
            self.direction = 1  # muda direção p baixo
            self.speed_vertical = ENTITY_SPEED[self.name] * 2  # dobra a velocidade ao descer
        elif self.rect.bottom >= WIN_HEIGHT:  # se bate na borda inferior
            self.direction = -1  # muda direção p cima
            self.speed_vertical = ENTITY_SPEED[self.name]  # reseta velocidade ao subir

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
