import pygame as py
from funcoes import *
from config import *

demon_images = {}
img_list = []
for i in range(1,7):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo idle/01_demon_idle/demon_idle_{i}.png").convert_alpha(),
        (864,480)))
demon_images['idle'] = img_list
img_list = []
for i in range(1,13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo andando/02_demon_walk/demon_walk_{i}.png").convert_alpha(),
        (864,480)))
demon_images['walking'] = img_list
for i in range(1,16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo batendo/03_demon_cleave/demon_cleave_{i}.png").convert_alpha(),
        (864,480)))
demon_images['beating'] = img_list
for i in range(1,23):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo morte/05_demon_death/demon_death_{i}.png").convert_alpha(),
        (864,480)))
demon_images['death'] = img_list
for i in range(1,6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo tomando/04_demon_take_hit/demon_take_hit_{i}.png").convert_alpha(),
        (864,480)))
demon_images['hit'] = img_list

#Animando mon
mon_images = {}
img_list = []
for i in range(1,16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon idle/idle/idle_{i}.png").convert_alpha(),
        (768,448)))
mon_images['idle'] = img_list
img_list = []
for i in range(1,13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon andando/walk/walk_{i}.png").convert_alpha(),
        (768,448)))
mon_images['walking'] = img_list
for i in range(1,8):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon batendo1/1atk/1atk_{i}.png").convert_alpha(),
        (768,448)))
mon_images['beating'] = img_list
img_list = []
for i in range(1,12):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon morte/death/death_{i}.png").convert_alpha(),
        (768,448)))
mon_images['death'] = img_list
for i in range(1,6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon tomando/hurt/hurt_{i}.png").convert_alpha(),
        (768,448)))
mon_images['hit'] = img_list