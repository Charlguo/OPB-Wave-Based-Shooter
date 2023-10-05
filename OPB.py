import pygame
import os
import time
import random

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1250, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One Piece Battle")
programIcon = pygame.image.load(os.path.join("assets", "StrawHat.png"))
pygame.display.set_icon(programIcon)

# Buggy, Nami, Robin, Krieg, Arlong, Chopper, Brook, Usopp, Bege, Apoo, Franky, Moriah, Sanji, Urouge, Hawkins, Smoker,  X_Drake_, Hancock, Crocodile, Jinbei, Magellan, Zoro, Kid, Law, Enel, Kuma, Jack, Doflamingo, Katakuri, Luffy, King, Lucci, Marco, Aokiji, Shiliew, Fujitora, Sengoku, Shiki, Rayleigh, Dragon, Kizaru, Mihawk, Big Mom, Kaido, Shanks, Akainu, Garp, Whitebeard, Blackbeard, Roger

# Load images
Zoro = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Zoro.png")), (150, 150))
Sanji = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Sanji.png")), (150, 150))
Crocodile = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Crocodile.gif")), (170, 170))
Ace = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ace.bmp")), (150, 150))
Akainu = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Akainu.bmp")), (240, 240))
Aokiji = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Aokiji.bmp")), (240, 240))
Brook = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Brook.bmp")), (160, 160))
Enel = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enel.bmp")), (175, 175))
Buggy = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerIdle1.png")), (130, 130))
BuggyDead = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerDead.png")), (130, 130))
walkRight = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight1.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight2.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight3.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight4.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight5.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight6.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerRight7.png")), (130, 130))]
walkLeft = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft1.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft2.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft3.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft4.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft5.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft6.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft7.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerLeft8.png")), (130, 130))]
Dragon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Dragon.bmp")), (170, 170))
Doflamingo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Doflamingo.bmp")), (185, 185))
Franky = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Franky.bmp")), (170, 170))
Garp = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Garp.bmp")), (185, 185))
Arlong = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Arlong.bmp")), (175, 175))
Blackbeard = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Blackbeard.bmp")), (180, 180))
Kizaru = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kizaru.bmp")), (240, 240))
Kuma = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kuma.bmp")), (270, 270))
Law = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Law.bmp")), (150, 150))
Mihawk = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Mihawk.bmp")), (180, 180))
Shanks = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shanks.bmp")), (180, 180))
Shiki = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shiki.bmp")), (180, 180))
Smoker = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Smoker.bmp")), (165, 165))
X_Drake = pygame.transform.scale(pygame.image.load(os.path.join("assets", "X_Drake.bmp")), (165, 165))
Whitebeard = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Whitebeard.bmp")), (230, 230))
Usopp = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Usopp.bmp")), (145, 145))
Urouge = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Urouge.bmp")), (230, 230))
Shiliew = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shiliew.bmp")), (180, 180))
Robin = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Robin.bmp")), (150, 150))
Sengoku = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Sengoku.bmp")), (180, 180))
Roger = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Roger.bmp")), (200, 200))
Rayleigh = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rayleigh.bmp")), (165, 165))
Nami = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Nami.bmp")), (150, 150))
Moriah = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Moriah.bmp")), (225, 225))
Marco = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Marco.bmp")), (150, 150))
Jinbei = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Jinbei.bmp")), (180, 180))
Kid = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kid.bmp")), (150, 150))
Hawkins = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Hawkins.bmp")), (155, 155))
Magellan = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Magellan.bmp")), (185, 185))
Krieg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Krieg.bmp")), (170, 170))
Chopper = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Chopper.bmp")), (70, 70))
Hancock = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Hancock.bmp")), (160, 160))
Bege = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Bege.bmp")), (160, 160))
Apoo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Apoo.bmp")), (155, 155))
Kaido = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kaido.bmp")), (500, 500))
Big_Mom = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BigMom.bmp")), (500, 500))
Marco = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Marco.bmp")), (190, 190))
Katakuri = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Katakuri.bmp")), (240, 240))
Jack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Jack.bmp")), (330, 330))
King = pygame.transform.scale(pygame.image.load(os.path.join("assets", "King.bmp")), (315, 315))
Fujitora = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Fujitora.bmp")), (240, 240))
Lucci = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Lucci.bmp")), (225, 225))

# Menu
Flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Flag.jpg")), (WIDTH, HEIGHT))

# Player
Luffy = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Luffy.bmp")), (130, 130))

# Attacks
Luffy_punch = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Luffy_punch.gif")), (180, 180))
Gear2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Jet_Bazooka.bmp")), (130, 130))
Gear3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Gigante_Pistola.bmp")), (270, 270))
Gear4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "King_kong_gun.bmp")), (230, 230))

Zoro_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Zoro_3TW.bmp")), (125, 125))
Crocodile_spada = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Crocodile_spada.png")), (255, 255))
Sanji_kick = pygame.transform.scale(pygame.image.load(os.path.join("assets", "kick.bmp")), (125, 125))
Ace_fire = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Ace_fire.bmp")), (45, 45))
Akainu_magma = pygame.transform.scale(pygame.image.load(os.path.join("assets", "InugamiGuren.bmp")), (250, 250))
Aokiji_ice = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Aokiji_ice.bmp")), (130, 130))
Brook_3pacehum = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Brook_3pacehum.bmp")), (90, 90))
Enel_thunder = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Enel_thunder.bmp")), (130, 130))
Buggy_knives = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife8.png")), (120, 120))
Buggy_spin = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpinAttack1.png")), (120, 120)),pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerAttack2.png")), (120, 120)),pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerAttack3.png")), (120, 120))]
BuggySpinAnim = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpin1.png")), (120, 120)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpin2.png")), (120, 120)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpin3.png")), (120, 120)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpin4.png")), (120, 120)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerSpin5.png")), (120, 120))]
Buggyknifeanimate = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife1.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife2.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife3.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife4.png")), (130, 130)),pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife5.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife6.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife7.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerKnife8.png")), (130, 130))]
Dragon_wind = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Dragon_wind.bmp")), (555, 555))
Doflamingo_god_thread = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Doflamingo_god_thread.bmp")), (215, 215))
Franky_strong_right = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Franky_strong_right.bmp")), (110, 110))
Garp_fist = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Garp_fist.bmp")), (520, 520))
Arlong_nose = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Arlong_nose.bmp")), (130, 130))
Blackbeard_vortex = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kurozu.bmp")), (145, 145))
Kizaru_light = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kizaru_light.gif")), (60, 60))
Kuma_Ursus_shock = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Kuma_Ursus_shock.bmp")), (65, 65))
Law_Room = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Law_Room.bmp")), (400, 400))
Mihawk_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Mihawk_slash.bmp")), (390, 390))
Shanks_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shanks_slash.bmp")), (300, 300))
Shiki_float = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shiki_float.bmp")), (400, 400))
Smoker_white_blow = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Smoker_white_blow.bmp")), (90, 90))
X_Drake_T_rex = pygame.transform.scale(pygame.image.load(os.path.join("assets", "X_Drake_T_rex.bmp")), (180, 180))
Whitebeard_quake = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Whitebeard_quake.bmp")), (280, 280))
Usopp_impact_dial = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Usopp_impact_dial.bmp")), (85, 85))
Urouge_Dmg_resist = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Retribution.bmp")), (265, 265))
Shiliew_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shiliew_slash.bmp")), (180, 180))
Robin_hand = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Robin_hand.bmp")), (155, 155))
Sengoku_buddha = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Sengoku_buddha.bmp")), (240, 240))
Roger_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Roger_slash.bmp")), (600, 600))
Rayleigh_slash = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rayleigh_slash.bmp")), (165, 165))
Nami_cloud = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Nami_cloud.bmp")), (170, 170))
Moriah_bats = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Moriah_bats.bmp")), (125, 125))
Jinbei_Shoulder_throw = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Jinbei_Shoulder_throw.bmp")), (155, 155))
Kid_magnet = pygame.transform.scale(pygame.image.load(os.path.join("assets", "magnetism.bmp")), (270, 270))
Hawkins_straw = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Hawkins_straw.bmp")), (175, 175))
Magellan_venomdemon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Magellan_venomdemon.bmp")), (250, 250))
Krieg_missile = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Krieg_missile.bmp")), (55, 55))
Chopper_monster_point = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Chopper_monster_point.bmp")), (255, 255))
Hancock_love = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Hancock_love.bmp")), (55, 55))
Bege_BigFather_Cannon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Bege_BigFather_Cannon.bmp")), (310, 310))
Apoo_Scratch = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Apoo_Scratch.bmp")), (95, 95))
Blast_breath = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Blast_breath.bmp")), (650, 650))
Soul = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Soul.bmp")), (215, 215))
Phoenix = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Phoenix.bmp")), (370, 370))
Buzz_Cut_Mochi = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Mochi.bmp")), (195, 195))
Mammoth = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Mammoth.bmp")), (620, 620))
Pteranodan = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Pteranodan.bmp")), (295, 295))
Meteor = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Meteor.bmp")), (330, 330))
Rokuogan = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Rokuogan.bmp")), (350, 350))
BuggyBomb = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall10.bmp")), (55, 55))
BuggyBombAnim = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall1.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall2.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall3.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall4.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall5.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall6.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall7.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall8.png")), (130, 130)), pygame.transform.scale(pygame.image.load(os.path.join("assets", "BuggyPlayerMuggyBall9.png")), (130, 130))]
BlackHole = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BlackHole.bmp")), (555, 555))
DesertSpada = pygame.transform.scale(pygame.image.load(os.path.join("assets", "DesertSpada.bmp")), (220, 220))
DGE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "DGE.bmp")), (200, 200))
Hook = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Hook.bmp")), (55, 55))
Red_Hound =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "InugamiGuren.bmp")), (350, 350))
Sables =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "Sables.bmp")), (450, 450))
Shadow =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shadow.bmp")), (250, 250))
Shadow_Steal =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "ShadowSteal.bmp")), (200, 200))
Poison_Hook =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "Poisonhook.bmp")), (55, 55))
Ground_Death = pygame.transform.scale(pygame.image.load(os.path.join("assets", "GroundDeath.bmp")), (330, 330))
Quake = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Quake.bmp")), (330, 330))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Sabaody.jpg")), (WIDTH, HEIGHT))
Winner = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Winner.png")), (WIDTH, HEIGHT))
ShopBG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Shop.png")), (WIDTH, HEIGHT))

# Sounds
ursusshocksound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Ursus shock.ogg")
cloudsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/cloud.ogg")
icesound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Ice age.ogg")
rayleighsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/rayleigh.ogg")
venomsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/venomdemon.ogg")
impactsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/impact dial.ogg")
roomsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/room.ogg")
bigfathersound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/bigfather.ogg")
buddhasound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/buddha.ogg")
cracksound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/crack.ogg")
dinosound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/dino.ogg")
elthorsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/elthor.ogg")
fistsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/fist.ogg")
floatsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/float.ogg")
godthreadsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/godthread.ogg")
knivessound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/knives.ogg")
kurozusound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/kurozu.ogg")
lavasound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/lava.ogg")
lightsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/light.ogg")
lovesound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/love.ogg")
magnetsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/magnet.ogg")
mihawksound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/mihawkslash.ogg")
missilesound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/missile.ogg")
monstersound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/monster.ogg")
nosesound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/nose.ogg")
pacehumsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/pacehum.ogg")
rayleighsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/rayleigh.ogg")
retributionsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/retribution.ogg")
rogersound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/roger.ogg")
scratchsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/scratch.ogg")
shadowssound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/shadows.ogg")
shanksslashsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/shanksslash.ogg")
shiliewslashsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/shiliewslash.ogg")
shoulderthrowsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/shoulderthrow.ogg")
spadasound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/spada.ogg")
strongrightsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/strongright.ogg")
tresfleurssound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/tresfleurs.ogg")
whiteblowsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/whiteblow.ogg")
windsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/wind.ogg")
kicksound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/kick.ogg")
strawsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/straw.ogg")
zoroslashsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/3thousandworlds.ogg")
Blast_breathsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Blast_breath.ogg")
Soulsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Soul.ogg")
Phoenixsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Phoenix.ogg")
Buzz_Cut_Mochisound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Buzzcutmochi.ogg")
Mammothsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Mammoth.ogg")
Pteranodansound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Pteranodan.ogg")
Meteorsound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Meteor.ogg")
Rokuogansound = pygame.mixer.Sound("C:/Users/Momo/PycharmProjects/OPBDev/venv/assets/Rokuogan.ogg")

class Attack:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x -= vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack1:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 1
        self.x -= vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack2:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 3
        self.x -= vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack3:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 10
        self.x -= vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack4:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 15
        self.x -= vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack5:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 1
        self.x += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack6:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 3
        self.x += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack7:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 10
        self.x += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Attack8:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        vel = 15
        self.x += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Char:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.char_img = None
        self.attack_img = None
        self.attacks = []
        self.particles = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.char_img, (self.x, self.y))
        for attack in self.attacks:
            attack.draw(window)

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 10
                self.attacks.remove(attack)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def get_width(self):
        return self.char_img.get_width()

    def get_height(self):
        return self.char_img.get_height()

class BuggyChar(Char):
    MUGGYCOOLDOWN = 200
    SPINCOOLDOWN = 120
    def __init__(self, x, y, health=15):
        super().__init__(x, y, health)
        self.char_img = Buggy
        self.dead_img = BuggyDead
        self.attack_img = Buggy_knives
        self.muggy_img = BuggyBomb
        self.muggys = []
        self.spin_img = Buggy_spin
        self.spins = []
        self.walkRight_img = walkRight
        self.walkLeft_img = walkLeft
        self.knifeanim_img = Buggyknifeanimate
        self.muggyanim_img = BuggyBombAnim
        self.spinanim_img = BuggySpinAnim
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.cool_down_counter = 0
        self.muggy_cool_down_counter = 0
        self.spin_cool_down_counter = 0
        self.walkCount = 0
        self.spinCount = 0
        self.spinanimCount = 0
        self.right = False
        self.left = False
        self.knife = False
        self.muggybomb = False
        self.spinknife = False

    def muggy(self):
        if self.muggy_cool_down_counter == 0:
            muggy = Attack6(self.x, self.y, self.muggy_img)
            self.muggys.append(muggy)
            self.muggy_cool_down_counter = 1

    def spin(self):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.spin_cool_down_counter == 0:
            spin = Attack6(self.x, self.y, self.spin_img[self.walkCount // 3])
            self.walkCount += 1
            self.spins.append(spin)
            self.spin_cool_down_counter = 1

    def muggycooldown(self):
        if self.muggy_cool_down_counter >= self.MUGGYCOOLDOWN:
            self.muggy_cool_down_counter = 0
        elif self.muggy_cool_down_counter > 0:
            self.muggy_cool_down_counter += 1

    def spincooldown(self):
        if self.spin_cool_down_counter >= self.SPINCOOLDOWN:
            self.spin_cool_down_counter = 0
        elif self.spin_cool_down_counter > 0:
            self.spin_cool_down_counter += 1

    def move_attacks(self, vel, objs):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            else:
                for obj in objs:
                    if attack.collision(obj):
                        obj.health -= 10
                        if attack in self.attacks:
                            self.attacks.remove(attack)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_muggys(self, vel, objs):
        self.muggycooldown()
        for muggy in self.muggys:
            muggy.move(vel)
            if muggy.off_screen(HEIGHT):
                self.muggys.remove(muggy)
            else:
                for obj in objs:
                    if muggy.collision(obj):
                        obj.health -= 22
                        if muggy in self.muggys:
                            self.muggys.remove(muggy)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_spins(self, vel, objs):
        self.spincooldown()
        for spin in self.spins:
            spin.move(vel)
            if spin.off_screen(HEIGHT):
                self.spins.remove(spin)
            else:
                for obj in objs:
                    if spin.collision(obj):
                        obj.health -= 17
                        if spin in self.spins:
                            self.spins.remove(spin)
                        if obj.health <= 0:
                            objs.remove(obj)

    def draw(self, window):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.spinCount + 1 >= 15:
            self.spinCount = 0
        if self.left:
            window.blit(self.walkLeft_img[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.knife:
            window.blit(self.knifeanim_img[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.muggybomb:
            window.blit(self.muggyanim_img[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.spinknife:
            window.blit(self.spinanim_img[self.spinCount // 3], (self.x, self.y))
            self.spinCount += 1
        elif self.health <= 0:
            window.blit(self.dead_img, (self.x, self.y))
        elif self.right:
            window.blit(self.walkRight_img[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(self.char_img, (self.x, self.y))
            self.walkCount = 0
        for attack in self.attacks:
            attack.draw(window)
        for muggy in self.muggys:
            muggy.draw(window)
        for spin in self.spins:
            spin.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width() * (self.health / self.max_health),
        10))

class MoriahChar(Char):
    SHADOWCOOLDOWN = 200
    SHADOWSTEALCOOLDOWN = 500
    def __init__(self, x, y, health=320):
        super().__init__(x, y, health)
        self.char_img = Moriah
        self.attack_img = Moriah_bats
        self.shadow_img = Shadow
        self.shadows = []
        self.shadowsteal_img = Shadow_Steal
        self.shadowsteals = []
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.cool_down_counter = 0
        self.shadow_cool_down_counter = 0
        self.shadowsteal_cool_down_counter = 0

    def shadow(self):
        if self.shadow_cool_down_counter == 0:
            shadow = Attack(self.x, self.y, self.shadow_img)
            self.shadows.append(shadow)
            self.shadow_cool_down_counter = 1

    def shadowcooldown(self):
        if self.shadow_cool_down_counter >= self.SHADOWCOOLDOWN:
            self.shadow_cool_down_counter = 0
        elif self.shadow_cool_down_counter > 0:
            self.shadow_cool_down_counter += 1

    def shadowsteal(self):
        if self.shadowsteal_cool_down_counter == 0:
            shadowsteal = Attack6(self.x, self.y, self.shadowsteal_img)
            self.shadowsteals.append(shadowsteal)
            self.shadowsteal_cool_down_counter = 1

    def shadowstealcooldown(self):
        if self.shadowsteal_cool_down_counter >= self.SHADOWSTEALCOOLDOWN:
            self.shadowsteal_cool_down_counter = 0
        elif self.shadowsteal_cool_down_counter > 0:
            self.shadowsteal_cool_down_counter += 1

    def move_attacks(self, vel, objs):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            else:
                for obj in objs:
                    if attack.collision(obj):
                        obj.health -= 25
                        if attack in self.attacks:
                            self.attacks.remove(attack)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_shadows(self, vel, objs):
        self.shadowcooldown()
        for shadow in self.shadows:
            shadow.move(vel)
            if shadow.off_screen(HEIGHT):
                self.shadows.remove(shadow)
            else:
                for obj in objs:
                    if shadow.collision(obj):
                        obj.health -= 35
                        if shadow in self.shadows:
                            self.shadows.remove(shadow)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_shadowsteals(self, vel, objs):
        self.shadowstealcooldown()
        for shadowsteal in self.shadowsteals:
            shadowsteal.move(vel)
            if shadowsteal.off_screen(HEIGHT):
                self.shadowsteals.remove(shadowsteal)
            else:
                for obj in objs:
                    if shadowsteal.collision(obj):
                        obj.health -= 400
                        if shadowsteal in self.shadowsteals:
                            self.shadowsteals.remove(shadowsteal)
                        if obj.health <= 0:
                            objs.remove(obj)

    def draw(self, window):
        window.blit(self.char_img, (self.x, self.y))
        for attack in self.attacks:
            attack.draw(window)
        for shadow in self.shadows:
            shadow.draw(window)
        for shadowsteal in self.shadowsteals:
            shadowsteal.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width() * (self.health / self.max_health),
        10))

class CrocodileChar(Char):
    POISONHOOKCOOLDOWN = 70
    DESERTSPADACOOLDOWN = 100
    DGECOOLDOWN = 200
    SABLESCOOLDOWN = 150
    GROUNDDEATHCOOLDOWN = 300
    ESPADACOOLDOWN = 300
    def __init__(self, x, y, health=1200):
        super().__init__(x, y, health)
        self.char_img = Crocodile
        self.attack_img = Hook
        self.desertspada_img = DesertSpada
        self.desertspadas = []
        self.dge_img = DGE
        self.dges = []
        self.poisonhook_img = Poison_Hook
        self.poisonhooks = []
        self.espada_img = Crocodile_spada
        self.espadas = []
        self.sables_img = Sables
        self.sabless = []
        self.grounddeath_img = Ground_Death
        self.grounddeaths = []
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.cool_down_counter = 0
        self.poisonhook_cool_down_counter = 0
        self.dge_cool_down_counter = 0
        self.desertspada_cool_down_counter = 0
        self.sables_cool_down_counter = 0
        self.grounddeath_cool_down_counter = 0
        self.espada_cool_down_counter = 0

    def poisonhook(self):
        if self.poisonhook_cool_down_counter == 0:
            poisonhook = Attack(self.x, self.y, self.poisonhook_img)
            self.poisonhooks.append(poisonhook)
            self.poisonhook_cool_down_counter = 1

    def poisonhookcooldown(self):
        if self.poisonhook_cool_down_counter >= self.POISONHOOKCOOLDOWN:
            self.poisonhook_cool_down_counter = 0
        elif self.poisonhook_cool_down_counter > 0:
            self.poisonhook_cool_down_counter += 1

    def dge(self):
        if self.dge_cool_down_counter == 0:
            dge = Attack7(self.x, self.y, self.dge_img)
            self.dges.append(dge)
            self.dge_cool_down_counter = 1

    def dgecooldown(self):
        if self.dge_cool_down_counter >= self.DGECOOLDOWN:
            self.dge_cool_down_counter = 0
        elif self.dge_cool_down_counter > 0:
            self.dge_cool_down_counter += 1

    def espada(self):
        if self.espada_cool_down_counter == 0:
            espada = Attack(self.x, self.y, self.espada_img)
            self.espadas.append(espada)
            self.espada_cool_down_counter = 1

    def espadacooldown(self):
        if self.espada_cool_down_counter >= self.ESPADACOOLDOWN:
            self.espada_cool_down_counter = 0
        elif self.espada_cool_down_counter > 0:
            self.espada_cool_down_counter += 1

    def sables(self):
        if self.sables_cool_down_counter == 0:
            sables = Attack6(self.x, self.y, self.sables_img)
            self.sabless.append(sables)
            self.sables_cool_down_counter = 1

    def sablescooldown(self):
        if self.sables_cool_down_counter >= self.SABLESCOOLDOWN:
            self.sables_cool_down_counter = 0
        elif self.sables_cool_down_counter > 0:
            self.sables_cool_down_counter += 1

    def desertspada(self):
        if self.desertspada_cool_down_counter == 0:
            desertspada = Attack7(self.x, self.y, self.desertspada_img)
            self.desertspadas.append(desertspada)
            self.desertspada_cool_down_counter = 1

    def desertspadacooldown(self):
        if self.desertspada_cool_down_counter >= self.DESERTSPADACOOLDOWN:
            self.desertspada_cool_down_counter = 0
        elif self.desertspada_cool_down_counter > 0:
            self.desertspada_cool_down_counter += 1

    def grounddeath(self):
        if self.grounddeath_cool_down_counter == 0:
            grounddeath = Attack(self.x, self.y, self.grounddeath_img)
            self.grounddeaths.append(grounddeath)
            self.grounddeath_cool_down_counter = 1

    def grounddeathcooldown(self):
        if self.grounddeath_cool_down_counter >= self.GROUNDDEATHCOOLDOWN:
            self.grounddeath_cool_down_counter = 0
        elif self.grounddeath_cool_down_counter > 0:
            self.grounddeath_cool_down_counter += 1

    def move_attacks(self, vel, objs):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            else:
                for obj in objs:
                    if attack.collision(obj):
                        obj.health -= 20
                        if attack in self.attacks:
                            self.attacks.remove(attack)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_poisonhooks(self, vel, objs):
        self.poisonhookcooldown()
        for poisonhook in self.poisonhooks:
            poisonhook.move(vel)
            if poisonhook.off_screen(HEIGHT):
                self.poisonhooks.remove(poisonhook)
            else:
                for obj in objs:
                    if poisonhook.collision(obj):
                        obj.health -= 40
                        if poisonhook in self.poisonhooks:
                            self.poisonhooks.remove(poisonhook)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_desertspadas(self, vel, objs):
        self.desertspadacooldown()
        for desertspada in self.desertspadas:
            desertspada.move(vel)
            if desertspada.off_screen(HEIGHT):
                self.desertspadas.remove(desertspada)
            else:
                for obj in objs:
                    if desertspada.collision(obj):
                        obj.health -= 290
                        if desertspada in self.desertspadas:
                            self.desertspadas.remove(desertspada)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_dges(self, vel, objs):
        self.dgecooldown()
        for dge in self.dges:
            dge.move(vel)
            if dge.off_screen(HEIGHT):
                self.dges.remove(dge)
            else:
                for obj in objs:
                    if dge.collision(obj):
                        obj.health -= 700
                        if dge in self.dges:
                            self.dges.remove(dge)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_sabless(self, vel, objs):
        self.sablescooldown()
        for sables in self.sabless:
            sables.move(vel)
            if sables.off_screen(HEIGHT):
                self.sabless.remove(sables)
            else:
                for obj in objs:
                    if sables.collision(obj):
                        obj.health -= 10
                        if sables in self.sabless:
                            self.sabless.remove(sables)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_espadas(self, vel, objs):
        self.espadacooldown()
        for espada in self.espadas:
            espada.move(vel)
            if espada.off_screen(HEIGHT):
                self.espadas.remove(espada)
            else:
                for obj in objs:
                    if espada.collision(obj):
                        obj.health -= 230
                        if espada in self.espadas:
                            self.espadas.remove(espada)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_grounddeaths(self, vel, objs):
        self.grounddeathcooldown()
        for grounddeath in self.grounddeaths:
            grounddeath.move(vel)
            if grounddeath.off_screen(HEIGHT):
                self.grounddeaths.remove(grounddeath)
            else:
                for obj in objs:
                    if grounddeath.collision(obj):
                        obj.health -= 1900
                        if grounddeath in self.grounddeaths:
                            self.grounddeaths.remove(grounddeath)
                        if obj.health <= 0:
                            objs.remove(obj)

    def draw(self, window):
        window.blit(self.char_img, (self.x, self.y))
        for attack in self.attacks:
            attack.draw(window)
        for poisonhook in self.poisonhooks:
            poisonhook.draw(window)
        for desertspada in self.desertspadas:
            desertspada.draw(window)
        for sables in self.sabless:
            sables.draw(window)
        for dge in self.dges:
            dge.draw(window)
        for espada in self.espadas:
            espada.draw(window)
        for grounddeath in self.grounddeaths:
            grounddeath.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width() * (self.health / self.max_health),
        10))

class BlackbeardChar(Char):
    KUROZUCOOLDOWN = 1
    BLACKHOLECOOLDOWN = 250
    QUAKECOOLDOWN = 350
    def __init__(self, x, y, health=70000):
        super().__init__(x, y, health)
        self.char_img = Blackbeard
        self.kurozu_img = Blackbeard_vortex
        self.kurozus = []
        self.blackhole_img = BlackHole
        self.blackholes = []
        self.quake_img = Quake
        self.quakes = []
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.cool_down_counter = 0
        self.kurozu_cool_down_counter = 0
        self.blackhole_cool_down_counter = 0
        self.quake_cool_down_counter = 0

    def kurozu(self):
        if self.kurozu_cool_down_counter == 0:
            kurozu = Attack(self.x, self.y, self.kurozu_img)
            self.kurozus.append(kurozu)
            self.kurozu_cool_down_counter = 1

    def kurozucooldown(self):
        if self.kurozu_cool_down_counter >= self.KUROZUCOOLDOWN:
            self.kurozu_cool_down_counter = 0
        elif self.kurozu_cool_down_counter > 0:
            self.kurozu_cool_down_counter += 1

    def blackhole(self):
        if self.blackhole_cool_down_counter == 0:
            blackhole = Attack6(self.x, self.y, self.blackhole_img)
            self.blackholes.append(blackhole)
            self.blackhole_cool_down_counter = 1

    def blackholecooldown(self):
        if self.blackhole_cool_down_counter >= self.BLACKHOLECOOLDOWN:
            self.blackhole_cool_down_counter = 0
        elif self.blackhole_cool_down_counter > 0:
            self.blackhole_cool_down_counter += 1

    def quake(self):
        if self.quake_cool_down_counter == 0:
            quake = Attack(self.x, self.y, self.quake_img)
            self.quakes.append(quake)
            self.quake_cool_down_counter = 1

    def quakecooldown(self):
        if self.quake_cool_down_counter >= self.QUAKECOOLDOWN:
            self.quake_cool_down_counter = 0
        elif self.quake_cool_down_counter > 0:
            self.quake_cool_down_counter += 1

    def move_kurozus(self, vel, objs):
        self.kurozucooldown()
        for kurozu in self.kurozus:
            kurozu.move(vel)
            if kurozu.off_screen(HEIGHT):
                self.kurozus.remove(kurozu)
            else:
                for obj in objs:
                    if kurozu.collision(obj):
                        obj.health -= 1900
                        if kurozu in self.kurozus:
                            self.kurozus.remove(kurozu)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_blackholes(self, vel, objs):
        self.blackholecooldown()
        for blackhole in self.blackholes:
            blackhole.move(vel)
            if blackhole.off_screen(HEIGHT):
                self.blackholes.remove(blackhole)
            else:
                for obj in objs:
                    if blackhole.collision(obj):
                        obj.health -= 50000
                        if blackhole in self.blackholes:
                            self.blackholes.remove(blackhole)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_quakes(self, vel, objs):
        self.quakecooldown()
        for quake in self.quakes:
            quake.move(vel)
            if quake.off_screen(HEIGHT):
                self.quakes.remove(quake)
            else:
                for obj in objs:
                    if quake.collision(obj):
                        obj.health -= 40000
                        if quake in self.quakes:
                            self.quakes.remove(quake)
                        if obj.health <= 0:
                            objs.remove(obj)

    def draw(self, window):
        window.blit(self.char_img, (self.x, self.y))
        for kurozu in self.kurozus:
            kurozu.draw(window)
        for blackhole in self.blackholes:
            blackhole.draw(window)
        for quake in self.quakes:
            quake.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width() * (self.health / self.max_health),
        10))

class LuffyChar(Char):
    GEAR2COOLDOWN = 100
    GEAR3COOLDOWN = 200
    GEAR4COOLDOWN = 300

    def __init__(self, x, y, health=35000):
        super().__init__(x, y, health)
        self.char_img = Luffy
        self.attack_img = Luffy_punch
        self.gear2_img = Gear2
        self.gear2s = []
        self.gear3_img = Gear3
        self.gear3s = []
        self.gear4_img = Gear4
        self.gear4s = []
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.cool_down_counter = 0
        self.gear2_cool_down_counter = 0
        self.gear3_cool_down_counter = 0
        self.gear4_cool_down_counter = 0

    def gear2(self):
        if self.gear2_cool_down_counter == 0:
            gear2 = Attack7(self.x, self.y, self.gear2_img)
            self.gear2s.append(gear2)
            self.gear2_cool_down_counter = 1

    def gear2cooldown(self):
        if self.gear2_cool_down_counter >= self.GEAR2COOLDOWN:
            self.gear2_cool_down_counter = 0
        elif self.gear2_cool_down_counter > 0:
            self.gear2_cool_down_counter += 1

    def gear3(self):
        if self.gear3_cool_down_counter == 0:
            gear3 = Attack6(self.x, self.y, self.gear3_img)
            self.gear3s.append(gear3)
            self.gear3_cool_down_counter = 1

    def gear3cooldown(self):
        if self.gear3_cool_down_counter >= self.GEAR3COOLDOWN:
            self.gear3_cool_down_counter = 0
        elif self.gear3_cool_down_counter > 0:
            self.gear3_cool_down_counter += 1

    def gear4(self):
        if self.gear4_cool_down_counter == 0:
            gear4 = Attack5(self.x, self.y, self.gear4_img)
            self.gear4s.append(gear4)
            self.gear4_cool_down_counter = 1

    def gear4cooldown(self):
        if self.gear4_cool_down_counter >= self.GEAR4COOLDOWN:
            self.gear4_cool_down_counter = 0
        elif self.gear4_cool_down_counter > 0:
            self.gear4_cool_down_counter += 1

    def move_attacks(self, vel, objs):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            else:
                for obj in objs:
                    if attack.collision(obj):
                        obj.health -= 100
                        if attack in self.attacks:
                            self.attacks.remove(attack)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_gear2s(self, vel, objs):
        self.gear2cooldown()
        for gear2 in self.gear2s:
            gear2.move(vel)
            if gear2.off_screen(HEIGHT):
                self.gear2s.remove(gear2)
            else:
                for obj in objs:
                    if gear2.collision(obj):
                        obj.health -= 290
                        if gear2 in self.gear2s:
                            self.gear2s.remove(gear2)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_gear3s(self, vel, objs):
        self.gear3cooldown()
        for gear3 in self.gear3s:
            gear3.move(vel)
            if gear3.off_screen(HEIGHT):
                self.gear3s.remove(gear3)
            else:
                for obj in objs:
                    if gear3.collision(obj):
                        obj.health -= 1900
                        if gear3 in self.gear3s:
                            self.gear3s.remove(gear3)
                        if obj.health <= 0:
                            objs.remove(obj)

    def move_gear4s(self, vel, objs):
        self.gear4cooldown()
        for gear4 in self.gear4s:
            gear4.move(vel)
            if gear4.off_screen(HEIGHT):
                self.gear4s.remove(gear4)
            else:
                for obj in objs:
                    if gear4.collision(obj):
                        obj.health -= 18000
                        if gear4 in self.gear4s:
                            self.gear4s.remove(gear4)
                        if obj.health <= 0:
                            objs.remove(obj)

    def draw(self, window):
        window.blit(self.char_img, (self.x, self.y))
        for attack in self.attacks:
            attack.draw(window)
        for gear2 in self.gear2s:
            gear2.draw(window)
        for gear3 in self.gear3s:
            gear3.draw(window)
        for gear4 in self.gear4s:
            gear4.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width() * (self.health / self.max_health),
        10))


class Enemy(Char):

    def __init__(self, x, y, health=15):
        super().__init__(x, y, health)
        self.char_img = Buggy
        self.attack_img = Buggy_knives
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            knivessound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 5
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 5:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy2(Char):

    def __init__(self, x, y, health=30):
        super().__init__(x, y, health)
        self.char_img = Nami
        self.attack_img = Nami_cloud
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            cloudsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 12
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 10:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy3(Char):

    def __init__(self, x, y, health=40):
        super().__init__(x, y, health)
        self.char_img = Robin
        self.attack_img = Robin_hand
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            tresfleurssound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 24
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 13:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy4(Char):

    def __init__(self, x, y, health=80):
        super().__init__(x, y, health)
        self.char_img = Krieg
        self.attack_img = Krieg_missile
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            missilesound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 30
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 27:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy5(Char):
    NOSECOOLDOWN = 70

    def __init__(self, x, y, health=120):
        super().__init__(x, y, health)
        self.char_img = Arlong
        self.attack_img = Arlong_nose
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.nose_cool_down_counter = 0

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.nose_cool_down_counter == 0:
            attack = Attack3(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.nose_cool_down_counter = 1

    def nosecooldown(self):
        if self.nose_cool_down_counter >= self.NOSECOOLDOWN:
            self.nose_cool_down_counter = 0
        elif self.nose_cool_down_counter > 0:
            self.nose_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.nosecooldown()
        for attack in self.attacks:
            attack.move(vel)
            nosesound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 40
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 40:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy6(Char):
    MONSTERCOOLDOWN = 300

    def __init__(self, x, y, health=170):
        super().__init__(x, y, health)
        self.char_img = Chopper
        self.attack_img = Chopper_monster_point
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.monster_cool_down_counter = 0

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.monster_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.monster_cool_down_counter = 1

    def monstercooldown(self):
        if self.monster_cool_down_counter >= self.MONSTERCOOLDOWN:
            self.monster_cool_down_counter = 0
        elif self.monster_cool_down_counter > 0:
            self.monster_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.monstercooldown()
        for attack in self.attacks:
            attack.move(vel)
            monstersound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 100
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 57:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy7(Char):

    def __init__(self, x, y, health=200):
        super().__init__(x, y, health)
        self.char_img = Brook
        self.attack_img = Brook_3pacehum
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            pacehumsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 90
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 67:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy8(Char):
    IMPACTCOOLDOWN = 250

    def __init__(self, x, y, health=220):
        super().__init__(x, y, health)
        self.char_img = Usopp
        self.attack_img = Usopp_impact_dial
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.impact_cool_down_counter = 0

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.impact_cool_down_counter == 0:
            attack = Attack3(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.impact_cool_down_counter = 1

    def impactcooldown(self):
        if self.impact_cool_down_counter >= self.IMPACTCOOLDOWN:
            self.impact_cool_down_counter = 0
        elif self.impact_cool_down_counter > 0:
            self.impact_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.impactcooldown()
        for attack in self.attacks:
            attack.move(vel)
            impactsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 80
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 73:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy9(Char):
    FATHERCOOLDOWN = 400

    def __init__(self, x, y, health=240):
        super().__init__(x, y, health)
        self.char_img = Bege
        self.attack_img = Bege_BigFather_Cannon
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.father_cool_down_counter = 0

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.father_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.father_cool_down_counter = 1

    def fathercooldown(self):
        if self.father_cool_down_counter >= self.FATHERCOOLDOWN:
            self.father_cool_down_counter = 0
        elif self.father_cool_down_counter > 0:
            self.father_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.fathercooldown()
        for attack in self.attacks:
            attack.move(vel)
            bigfathersound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 150
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 80:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy10(Char):

    def __init__(self, x, y, health=260):
        super().__init__(x, y, health)
        self.char_img = Apoo
        self.attack_img = Apoo_Scratch
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            scratchsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 90
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 87:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy11(Char):

    def __init__(self, x, y, health=300):
        super().__init__(x, y, health)
        self.char_img = Franky
        self.attack_img = Franky_strong_right
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            strongrightsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 120
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 100:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy12(Char):

    def __init__(self, x, y, health=320):
        super().__init__(x, y, health)
        self.char_img = Moriah
        self.attack_img = Moriah_bats
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            shadowssound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 107:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy13(Char):

    def __init__(self, x, y, health=700):
        super().__init__(x, y, health)
        self.char_img = Sanji
        self.attack_img = Sanji_kick
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack3(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            kicksound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 280
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 233:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy14(Char):
    RESISTCOOLDOWN= 250

    def __init__(self, x, y, health=800):
        super().__init__(x, y, health)
        self.char_img = Urouge
        self.attack_img = Urouge_Dmg_resist
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.resist_cool_down_counter = 1

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.resist_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.resist_cool_down_counter = 1

    def resistcooldown(self):
        if self.resist_cool_down_counter >= self.RESISTCOOLDOWN:
            self.resist_cool_down_counter = 0
        elif self.resist_cool_down_counter > 0:
            self.resist_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.resistcooldown()
        for attack in self.attacks:
            attack.move(vel)
            retributionsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 280
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 267:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy15(Char):

    def __init__(self, x, y, health=8000):
        super().__init__(x, y, health)
        self.char_img = Hawkins
        self.attack_img = Hawkins_straw
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            strawsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 250
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 2667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy16(Char):

    def __init__(self, x, y, health=750):
        super().__init__(x, y, health)
        self.char_img = Smoker
        self.attack_img = Smoker_white_blow
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            whiteblowsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 200
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 250:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy17(Char):

    def __init__(self, x, y, health=800):
        super().__init__(x, y, health)
        self.char_img = X_Drake
        self.attack_img = X_Drake_T_rex
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            dinosound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 200
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 267:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy18(Char):

    def __init__(self, x, y, health=10000):
        super().__init__(x, y, health)
        self.char_img = Hancock
        self.attack_img = Hancock_love
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            lovesound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 9000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 3333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy19(Char):

    def __init__(self, x, y, health=1200):
        super().__init__(x, y, health)
        self.char_img = Crocodile
        self.attack_img = Crocodile_spada
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            spadasound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 30
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 400:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy20(Char):

    def __init__(self, x, y, health=2000):
        super().__init__(x, y, health)
        self.char_img = Jinbei
        self.attack_img = Jinbei_Shoulder_throw
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            shoulderthrowsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 4400
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy21(Char):
    VENOMDEMONCOOLDOWN = 150

    def __init__(self, x, y, health=5000):
        super().__init__(x, y, health)
        self.char_img = Magellan
        self.attack_img = Magellan_venomdemon
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.venomdemon_cool_down_counter = 1

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.venomdemon_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.venomdemon_cool_down_counter = 1

    def venomdemoncooldown(self):
        if self.venomdemon_cool_down_counter >= self.VENOMDEMONCOOLDOWN:
            self.venomdemon_cool_down_counter = 0
        elif self.venomdemon_cool_down_counter > 0:
            self.venomdemon_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.venomdemoncooldown()
        for attack in self.attacks:
            attack.move(vel)
            venomsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 2000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 1667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy22(Char):

    def __init__(self, x, y, health=4500):
        super().__init__(x, y, health)
        self.char_img = Zoro
        self.attack_img = Zoro_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            zoroslashsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 800
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 1500:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy23(Char):

    def __init__(self, x, y, health=4600):
        super().__init__(x, y, health)
        self.char_img = Kid
        self.attack_img = Kid_magnet
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            magnetsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 850
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 1533:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy24(Char):
    ROOMCOOLDOWN = 120

    def __init__(self, x, y, health=4700):
        super().__init__(x, y, health)
        self.char_img = Law
        self.attack_img = Law_Room
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.room_cool_down_counter = 1

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.room_cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.room_cool_down_counter = 1

    def roomcooldown(self):
        if self.room_cool_down_counter >= self.ROOMCOOLDOWN:
            self.room_cool_down_counter = 0
        elif self.room_cool_down_counter > 0:
            self.room_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.roomcooldown()
        for attack in self.attacks:
            attack.move(vel)
            roomsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 1100
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 1567:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy25(Char):

    def __init__(self, x, y, health=1100):
        super().__init__(x, y, health)
        self.char_img = Enel
        self.attack_img = Enel_thunder
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack3(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            elthorsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 10000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 367:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy26(Char):
    URSUSSHOCKCOOLDOWN = 200

    def __init__(self, x, y, health=16920):
        super().__init__(x, y, health)
        self.char_img = Kuma
        self.attack_img = Kuma_Ursus_shock
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.ursusshock_cool_down_counter = 1

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.ursusshock_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.ursusshock_cool_down_counter = 1

    def ursusshockcooldown(self):
        if self.ursusshock_cool_down_counter >= self.URSUSSHOCKCOOLDOWN:
            self.ursusshock_cool_down_counter = 0
        elif self.ursusshock_cool_down_counter > 0:
            self.ursusshock_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.ursusshockcooldown()
        for attack in self.attacks:
            attack.move(vel)
            ursusshocksound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 18000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 5640:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy27(Char):

    def __init__(self, x, y, health=17000):
        super().__init__(x, y, health)
        self.char_img = Jack
        self.attack_img = Mammoth
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Mammothsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 4450
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 5667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy28(Char):

    def __init__(self, x, y, health=22000):
        super().__init__(x, y, health)
        self.char_img = Doflamingo
        self.attack_img = Doflamingo_god_thread
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            godthreadsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 16000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 7333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy29(Char):

    def __init__(self, x, y, health=30000):
        super().__init__(x, y, health)
        self.char_img = Katakuri
        self.attack_img = Buzz_Cut_Mochi
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Buzz_Cut_Mochisound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 19000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 10000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy30(Char):

    def __init__(self, x, y, health=40000):
        super().__init__(x, y, health)
        self.char_img = King
        self.attack_img = Pteranodan
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Pteranodansound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 13333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy31(Char):

    def __init__(self, x, y, health=30000):
        super().__init__(x, y, health)
        self.char_img = Lucci
        self.attack_img = Rokuogan
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Rokuogansound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 19000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 10000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy32(Char):

    def __init__(self, x, y, health=60555):
        super().__init__(x, y, health)
        self.char_img = Marco
        self.attack_img = Phoenix
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Phoenixsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 20185:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy33(Char):

    def __init__(self, x, y, health=50000):
        super().__init__(x, y, health)
        self.char_img = Aokiji
        self.attack_img = Aokiji_ice
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            icesound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20050
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 16667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy34(Char):

    def __init__(self, x, y, health=21000):
        super().__init__(x, y, health)
        self.char_img = Shiliew
        self.attack_img = Shiliew_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            shiliewslashsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 21000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 7000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy35(Char):

    def __init__(self, x, y, health=50000):
        super().__init__(x, y, health)
        self.char_img = Fujitora
        self.attack_img = Meteor
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Meteorsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 16667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy36(Char):

    def __init__(self, x, y, health=70000):
        super().__init__(x, y, health)
        self.char_img = Sengoku
        self.attack_img = Sengoku_buddha
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            buddhasound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 21000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 23333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy37(Char):
    FLOATCOOLDOWN = 250

    def __init__(self, x, y, health=70000):
        super().__init__(x, y, health)
        self.char_img = Shiki
        self.attack_img = Shiki_float
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health
        self.float_cool_down_counter = 1

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.float_cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.float_cool_down_counter = 1

    def floatcooldown(self):
        if self.float_cool_down_counter >= self.FLOATCOOLDOWN:
            self.float_cool_down_counter = 0
        elif self.float_cool_down_counter > 0:
            self.float_cool_down_counter += 1

    def move_attacks(self, vel, obj):
        self.floatcooldown()
        for attack in self.attacks:
            attack.move(vel)
            floatsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 21999
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 23333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy38(Char):

    def __init__(self, x, y, health=60000):
        super().__init__(x, y, health)
        self.char_img = Rayleigh
        self.attack_img = Rayleigh_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack3(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            rayleighsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 21000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 20000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy39(Char):

    def __init__(self, x, y, health=80000):
        super().__init__(x, y, health)
        self.char_img = Dragon
        self.attack_img = Dragon_wind
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack1(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            windsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 39000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 26667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy40(Char):

    def __init__(self, x, y, health=50000):
        super().__init__(x, y, health)
        self.char_img = Kizaru
        self.attack_img = Kizaru_light
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack4(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            lightsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 20000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 16667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy41(Char):

    def __init__(self, x, y, health=61000):
        super().__init__(x, y, health)
        self.char_img = Mihawk
        self.attack_img = Mihawk_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            mihawksound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 30000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 20333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy42(Char):

    def __init__(self, x, y, health=100000):
        super().__init__(x, y, health)
        self.char_img = Big_Mom
        self.attack_img = Soul
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Soulsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 60000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 33333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy43(Char):

    def __init__(self, x, y, health=100000):
        super().__init__(x, y, health)
        self.char_img = Kaido
        self.attack_img = Blast_breath
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            Blast_breathsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 60000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 33333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy44(Char):

    def __init__(self, x, y, health=70000):
        super().__init__(x, y, health)
        self.char_img = Shanks
        self.attack_img = Shanks_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            shanksslashsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 60500
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 23333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy45(Char):

    def __init__(self, x, y, health=90000):
        super().__init__(x, y, health)
        self.char_img = Akainu
        self.attack_img = Akainu_magma
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            lavasound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 60500
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 30000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy46(Char):

    def __init__(self, x, y, health=95000):
        super().__init__(x, y, health)
        self.char_img = Garp
        self.attack_img = Garp_fist
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            fistsound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 70000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 31667:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)


class Enemy47(Char):

    def __init__(self, x, y, health=120000):
        super().__init__(x, y, health)
        self.char_img = Whitebeard
        self.attack_img = Whitebeard_quake
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            cracksound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 80000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 40000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy48(Char):

    def __init__(self, x, y, health=70000):
        super().__init__(x, y, health)
        self.char_img = Blackbeard
        self.attack_img = Blackbeard_vortex
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack2(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            kurozusound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 45
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 23333:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

class Enemy49(Char):

    def __init__(self, x, y, health=150000):
        super().__init__(x, y, health)
        self.char_img = Roger
        self.attack_img = Roger_slash
        self.mask = pygame.mask.from_surface(self.char_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel
        if self.y >= 900:
            self.y = 0

    def shoot(self):
        if self.cool_down_counter == 0:
            attack = Attack(self.x - 20, self.y, self.attack_img)
            self.attacks.append(attack)
            self.cool_down_counter = 1

    def move_attacks(self, vel, obj):
        self.cooldown()
        for attack in self.attacks:
            attack.move(vel)
            rogersound.play()
            if attack.off_screen(HEIGHT):
                self.attacks.remove(attack)
            elif attack.collision(obj):
                obj.health -= 90000
                self.attacks.remove(attack)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.char_img.get_height() + 10, self.char_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.char_img.get_height() + 10,
            self.char_img.get_width() * (self.health / self.max_health),
            10))
        if self.health <= 50000:
            self.particles.append([[self.x, self.y], [random.randint(-90, -1) / 10 - 1, -2], random.randint(4, 24)])
            for particle in self.particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] += 0.09
                pygame.draw.circle(window, (138, 3, 3), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    self.particles.remove(particle)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60
    level = 0
    lives = 1
    Beli = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    Win_font = pygame.font.SysFont("comicsans", 60)
    Shop_font = pygame.font.SysFont("comicsans", 70)
    Buy_font = pygame.font.SysFont("comicsans", 30)
    Equip_font = pygame.font.SysFont("comicsans", 30)
    enemies = []
    wave_length = 1
    enemy_vel = 1

    luffy_vel = 7
    buggy_vel = 5
    moriah_vel = 4
    crocodile_vel = 6
    blackbeard_vel = 9
    attack_vel = 5

    luffy = LuffyChar(300, 630)
    luffybought = False
    luffyequipped = False
    buggy = BuggyChar(350, 650)
    buggyequipped = True
    moriah = MoriahChar(350, 650)
    moriahequipped = False
    moriahbought = False
    crocodile = CrocodileChar(350, 650)
    crocodilebought = False
    crocodileequipped = False
    moriahequipped = False
    blackbeard = BlackbeardChar(350, 650)
    blackbeardbought = False
    blackbeardequipped = False
    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    Win = False

    Shop = False

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        Beli_label = main_font.render(f"Beli: {Beli}", 1, (255, 185, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(Beli_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        if luffyequipped == True:
            luffy.draw(WIN)
        if buggyequipped == True:
            buggy.draw(WIN)
        if moriahequipped == True:
            moriah.draw(WIN)
        if crocodileequipped == True:
            crocodile.draw(WIN)
        if blackbeardequipped == True:
            blackbeard.draw(WIN)

        if lost:
            lost_label = lost_font.render(" You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        if Win:
            WIN.blit(Winner, (0, 0))
            Win_label = Win_font.render("You Won!", 1, (0, 0, 0))
            WIN.blit(Win_label, (WIDTH / 2 - Win_label.get_width() / 2, 350))

        if Shop:
            WIN.blit(ShopBG, (0, 0))
            Beli_label = Shop_font.render(f"Beli: {Beli}", 1, (255, 185, 0))
            WIN.blit(Beli_label, (1090, 0))
            Shop_title = Shop_font.render("Shop", 1, (186, 144, 47))
            WIN.blit(Shop_title, (0, 0))
            BuyCrocodile_label = Buy_font.render("Buy 1500$", 1, (255, 255, 0))
            BuyLuffy_label = Buy_font.render("Buy 3200$", 1, (255, 255, 0))
            BuyMoriah_label = Buy_font.render("Buy 375$", 1, (255, 255, 0))
            EquipBuggy_label = Equip_font.render("Equip", 1, (51, 51, 51))
            EquipMoriah_label = Equip_font.render("Equip", 1, (51, 51, 51))
            EquipCrocodile_label = Equip_font.render("Equip", 1, (51, 51, 51))
            EquipLuffy_label = Equip_font.render("Equip", 1, (51, 51, 51))
            EquipBlackbeard_label = Equip_font.render("Equip", 1, (51, 51, 51))
            BuyBlackbeard_label = Buy_font.render("Buy 9565$", 1, (255, 255, 0))
            Bought_label = Buy_font.render("Bought", 1, (140, 140, 140))
            Equipped_label = Buy_font.render("Equipped", 1, (186, 144, 47))
            WIN.blit(Luffy, (250, 100))
            WIN.blit(EquipLuffy_label, (250, 210))
            WIN.blit(Buggy, (100, 100))
            WIN.blit(EquipBuggy_label, (100, 210))
            WIN.blit(Crocodile, (400, 100))
            WIN.blit(EquipCrocodile_label, (400, 250))
            WIN.blit(Moriah, (600, 100))
            WIN.blit(EquipMoriah_label, (600, 305))
            WIN.blit(Blackbeard, (875, 100))
            WIN.blit(EquipBlackbeard_label, (875, 260))
            if moriahbought == False:
                WIN.blit(BuyMoriah_label, (600, 100))
            if moriahbought == True:
                WIN.blit(Bought_label, (600, 100))
            if crocodilebought == False:
                WIN.blit(BuyCrocodile_label, (400, 100))
            if crocodilebought == True:
                WIN.blit(Bought_label, (400, 100))
            if luffybought == False:
                WIN.blit(BuyLuffy_label, (250, 100))
            if luffybought == True:
                WIN.blit(Bought_label, (250, 100))
            if blackbeardbought == False:
                WIN.blit(BuyBlackbeard_label, (875, 100))
            if blackbeardbought == True:
                WIN.blit(Bought_label, (875, 100))
            if moriahequipped == False:
                WIN.blit(EquipMoriah_label, (600, 305))
            if moriahequipped == True:
                WIN.blit(Equipped_label, (600, 305))
            if crocodileequipped == False:
                WIN.blit(EquipCrocodile_label, (400, 250))
            if crocodileequipped == True:
                WIN.blit(Equipped_label, (400, 250))
            if luffyequipped == False:
                WIN.blit(EquipLuffy_label, (250, 210))
            if luffyequipped == True:
                WIN.blit(Equipped_label, (250, 210))
            if blackbeardequipped == False:
                WIN.blit(EquipBlackbeard_label, (875, 260))
            if blackbeardequipped == True:
                WIN.blit(Equipped_label, (875, 260))
            if buggyequipped == False:
                WIN.blit(EquipBuggy_label, (100, 210))
            if buggyequipped == True:
                WIN.blit(Equipped_label, (100, 210))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if buggyequipped == True:
            if lives <= 0 or buggy.health <= 0:
                lost = True
                lost_count += 1

        if luffyequipped == True:
            if lives <= 0 or luffy.health <= 0:
                lost = True
                lost_count += 1

        if moriahequipped == True:
            if lives <= 0 or moriah.health <= 0:
                lost = True
                lost_count += 1

        if crocodileequipped == True:
            if lives <= 0 or crocodile.health <= 0:
                lost = True
                lost_count += 1

        if blackbeardequipped == True:
            if lives <= 0 or blackbeard.health <= 0:
                lost = True
                lost_count += 1

        if level > 49:
            Win = True

        if Win:
            Beli += 500
            level = 0

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 0
            for i in range(wave_length):
                if level == 1:
                    enemy = Enemy(random.randrange(1100, 1105), random.randrange(0, 650))
                    enemies.append(enemy)
                if level == 2:
                    enemy2 = Enemy2(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy2)
                    Beli+= 5
                if level == 3:
                    enemy3 = Enemy3(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy3)
                    Beli += 5
                if level == 4:
                    enemy4 = Enemy4(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy4)
                    Beli += 5
                if level == 5:
                    enemy5 = Enemy5(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy5)
                    Beli += 10
                if level == 6:
                    enemy6 = Enemy6(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy6)
                    Beli += 15
                if level == 7:
                    enemy7 = Enemy7(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy7)
                    Beli += 30
                if level == 8:
                    enemy8 = Enemy8(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy8)
                    Beli += 35
                if level == 9:
                    enemy9 = Enemy9(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy9)
                    Beli += 40
                if level == 10:
                    enemy10 = Enemy10(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy10)
                    Beli += 55
                if level == 11:
                    enemy11 = Enemy11(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy11)
                    Beli += 55
                if level == 12:
                    enemy12 = Enemy12(random.randrange(1020, 1025), random.randrange(0, 650))
                    enemies.append(enemy12)
                    Beli += 45
                if level == 13:
                    enemy13 = Enemy13(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy13)
                    Beli += 75
                if level == 14:
                    enemy14 = Enemy14(random.randrange(1005, 1007), random.randrange(0, 650))
                    enemies.append(enemy14)
                    Beli += 100
                if level == 15:
                    enemy15 = Enemy15(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy15)
                    Beli += 100
                if level == 16:
                    enemy16 = Enemy16(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy16)
                    Beli += 100
                if level == 17:
                    enemy17 = Enemy17(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy17)
                    Beli += 100
                if level == 18:
                    enemy18 = Enemy18(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy18)
                    Beli += 120
                if level == 19:
                    enemy19 = Enemy19(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy19)
                    Beli += 145
                if level == 20:
                    enemy20 = Enemy20(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy20)
                    Beli += 145
                if level == 21:
                    enemy21 = Enemy21(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy21)
                    Beli += 145
                if level == 22:
                    enemy22 = Enemy22(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy22)
                    Beli += 180
                if level == 23:
                    enemy23 = Enemy23(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy23)
                    Beli += 180
                if level == 24:
                    enemy24 = Enemy24(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy24)
                    Beli += 200
                if level == 25:
                    enemy25 = Enemy25(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy25)
                    Beli += 200
                if level == 26:
                    enemy26 = Enemy26(random.randrange(950, 952), random.randrange(0, 650))
                    enemies.append(enemy26)
                    Beli += 200
                if level == 27:
                    enemy27 = Enemy27(random.randrange(915, 917), random.randrange(0, 650))
                    enemies.append(enemy27)
                    Beli += 220
                if level == 28:
                    enemy28 = Enemy28(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy28)
                    Beli += 220
                if level == 29:
                    enemy29 = Enemy29(random.randrange(1001, 1003), random.randrange(0, 650))
                    enemies.append(enemy29)
                    Beli += 230
                if level == 30:
                    enemy30 = Enemy30(random.randrange(912, 914), random.randrange(0, 650))
                    enemies.append(enemy30)
                    Beli += 240
                if level == 31:
                    enemy31 = Enemy31(random.randrange(1000, 1002), random.randrange(0, 650))
                    enemies.append(enemy31)
                    Beli += 260
                if level == 32:
                    enemy32 = Enemy32(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy32)
                    Beli += 265
                if level == 33:
                    enemy33 = Enemy33(random.randrange(982, 984), random.randrange(0, 650))
                    enemies.append(enemy33)
                    Beli += 270
                if level == 34:
                    enemy34 = Enemy34(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy34)
                    Beli += 300
                if level == 35:
                    enemy35 = Enemy35(random.randrange(1005, 1008), random.randrange(0, 650))
                    enemies.append(enemy35)
                    Beli += 300
                if level == 36:
                    enemy36 = Enemy36(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy36)
                    Beli += 300
                if level == 37:
                    enemy37 = Enemy37(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy37)
                    Beli += 340
                if level == 38:
                    enemy38 = Enemy38(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy38)
                    Beli += 340
                if level == 39:
                    enemy39 = Enemy39(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy39)
                    Beli += 340
                if level == 40:
                    enemy40 = Enemy40(random.randrange(1005, 1008), random.randrange(0, 650))
                    enemies.append(enemy40)
                    Beli += 400
                if level == 41:
                    enemy41 = Enemy41(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy41)
                    Beli += 340
                if level == 42:
                    enemy42 = Enemy42(random.randrange(720, 722), random.randrange(0, 650))
                    enemies.append(enemy42)
                    Beli += 350
                if level == 43:
                    enemy43 = Enemy43(random.randrange(720, 722), random.randrange(0, 650))
                    enemies.append(enemy43)
                    Beli += 370
                if level == 44:
                    enemy44 = Enemy44(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy44)
                    Beli += 370
                if level == 45:
                    enemy45 = Enemy45(random.randrange(980, 985), random.randrange(0, 650))
                    enemies.append(enemy45)
                    Beli += 330
                if level == 46:
                    enemy46 = Enemy46(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy46)
                    Beli += 370
                if level == 47:
                    enemy47 = Enemy47(random.randrange(1015, 1017), random.randrange(0, 650))
                    enemies.append(enemy47)
                    Beli += 340
                if level == 48:
                    enemy48 = Enemy48(random.randrange(1050, 1055), random.randrange(0, 650))
                    enemies.append(enemy48)
                    Beli += 380
                if level == 49:
                    enemy49 = Enemy49(random.randrange(1010, 1015), random.randrange(0, 650))
                    enemies.append(enemy49)
                    Beli += 400

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Shop = True

        if moriahbought == False:
            if pygame.mouse.get_pos() == (600, 100):
                Beli -= 375
                moriahbought = True
        if moriahbought == True:
            if pygame.mouse.get_pos() == (600, 100):
                Beli -= 0
        if crocodilebought == False:
            if pygame.mouse.get_pos() == (400, 100):
                Beli -= 1500
                crocodilebought = True
        if crocodilebought == True:
            if pygame.mouse.get_pos() == (400, 100):
                Beli -= 0
        if luffybought == False:
            if pygame.mouse.get_pos() == (250, 100):
                Beli -= 320
                luffybought = True
        if luffybought == True:
            if pygame.mouse.get_pos() == (250, 100):
                Beli -= 0
        if blackbeardbought == False:
            if pygame.mouse.get_pos() == (875, 100):
                Beli -= 9565
                blackbeardbought = True
        if blackbeardbought == True:
            if pygame.mouse.get_pos() == (875, 100):
                Beli -= 0
        if moriahbought == True:
            if pygame.mouse.get_pos() == (600, 305):
                moriahequipped = True
                buggyequipped = False
                luffyequipped = False
                crocodileequipped = False
                blackbeardequipped = False
        if pygame.mouse.get_pos() == (100, 210):
            moriahequipped = False
            buggyequipped = True
            luffyequipped = False
            crocodileequipped = False
            blackbeardequipped = False
        if crocodilebought == True:
            if pygame.mouse.get_pos() == (400, 250):
                moriahequipped = False
                buggyequipped = False
                luffyequipped = False
                crocodileequipped = True
                blackbeardequipped = False
        if luffybought == True:
            if pygame.mouse.get_pos() == (250, 210):
                moriahequipped = False
                buggyequipped = False
                luffyequipped = True
                crocodileequipped = False
                blackbeardequipped = False
        if blackbeardbought == True:
            if pygame.mouse.get_pos() == (875, 260):
                moriahequipped = False
                buggyequipped = False
                luffyequipped = False
                crocodileequipped = False
                blackbeardequipped = True
        keys = pygame.key.get_pressed()

        if buggyequipped == True:
            if keys[pygame.K_a] and buggy.x - buggy_vel > 0:
                buggy.x -= buggy_vel
                buggy.right = False
                buggy.left = True
                buggy.knife = False
                buggy.muggybomb = False
                buggy.spinknife = False
            elif keys[pygame.K_d] and buggy.x + buggy_vel + buggy.get_width() < WIDTH:  # right
                buggy.x += buggy_vel
                buggy.right = True
                buggy.left = False
                buggy.knife = False
                buggy.muggybomb = False
                buggy.spinknife = False
            elif keys[pygame.K_SPACE]:
                buggy.shoot()
                buggy.knife = True
            elif keys[pygame.K_u]:
                buggy.muggy()
                buggy.muggybomb = True
            elif keys[pygame.K_i]:
                buggy.spin()
                buggy.spinknife = True
            else:
                buggy.left = False
                buggy.right = False
                buggy.walkCount = 0
                buggy.spinCount = 0
            if keys[pygame.K_w] and buggy.y - buggy_vel > 0:  # up
                buggy.y -= buggy_vel
                buggy.right = False
                buggy.left = False
            if keys[pygame.K_s] and buggy.y + buggy_vel + buggy.get_height() + 15 < HEIGHT:  # down
                buggy.y += buggy_vel
                buggy.right = False
                buggy.left = False
            if keys[pygame.K_n]:
                Shop = False
            if keys[pygame.K_m]:
                Win = False

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_attacks(attack_vel, buggy)

                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, buggy):
                    buggy.health -= 10
                    enemies.remove(enemy)

                elif enemy.x + enemy.get_width() < 0:
                    lives -= 1
                    enemies.remove(enemy)

                buggy.move_attacks(-attack_vel, enemies)
                buggy.move_muggys(-attack_vel, enemies)
                buggy.move_spins(-attack_vel, enemies)

        if moriahequipped == True:
            if keys[pygame.K_a] and moriah.x - moriah_vel > 0:
                moriah.x -= moriah_vel
            if keys[pygame.K_d] and moriah.x + moriah_vel + moriah.get_width() < WIDTH:  # right
                moriah.x += moriah_vel
            if keys[pygame.K_w] and moriah.y - moriah_vel > 0:  # up
                moriah.y -= moriah_vel
            if keys[pygame.K_s] and moriah.y + moriah_vel + moriah.get_height() + 15 < HEIGHT:  # down
                moriah.y += moriah_vel
            if keys[pygame.K_SPACE]:
                moriah.shoot()
            if keys[pygame.K_u]:
                moriah.shadow()
            if keys[pygame.K_i]:
                moriah.shadowsteal()
            if keys[pygame.K_n]:
                Shop = False
            if keys[pygame.K_m]:
                Win = False

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_attacks(attack_vel, moriah)

                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, moriah):
                    moriah.health -= 10
                    enemies.remove(enemy)

                elif enemy.x + enemy.get_width() < 0:
                    lives -= 1
                    enemies.remove(enemy)

                moriah.move_attacks(-attack_vel, enemies)
                moriah.move_shadows(-attack_vel, enemies)
                moriah.move_shadowsteals(-attack_vel, enemies)

        if crocodileequipped == True:
            if keys[pygame.K_a] and crocodile.x - crocodile_vel > 0:
                crocodile.x -= crocodile_vel
            if keys[pygame.K_d] and crocodile.x + crocodile_vel + crocodile.get_width() < WIDTH:  # right
                crocodile.x += crocodile_vel
            if keys[pygame.K_w] and crocodile.y - crocodile_vel > 0:  # up
                crocodile.y -= crocodile_vel
            if keys[pygame.K_s] and crocodile.y + crocodile_vel + crocodile.get_height() + 15 < HEIGHT:  # down
                crocodile.y += crocodile_vel
            if keys[pygame.K_SPACE]:
                crocodile.shoot()
            if keys[pygame.K_u]:
                crocodile.poisonhook()
            if keys[pygame.K_i]:
                crocodile.desertspada()
            if keys[pygame.K_o]:
                crocodile.sables()
            if keys[pygame.K_j]:
                crocodile.dge()
            if keys[pygame.K_k]:
                crocodile.espada()
            if keys[pygame.K_l]:
                crocodile.grounddeath()
            if keys[pygame.K_n]:
                Shop = False
            if keys[pygame.K_m]:
                Win = False

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_attacks(attack_vel, crocodile)

                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, crocodile):
                    crocodile.health -= 10
                    enemies.remove(enemy)

                elif enemy.x + enemy.get_width() < 0:
                    lives -= 1
                    enemies.remove(enemy)

                crocodile.move_attacks(-attack_vel, enemies)
                crocodile.move_poisonhooks(-attack_vel, enemies)
                crocodile.move_desertspadas(-attack_vel, enemies)
                crocodile.move_sabless(-attack_vel, enemies)
                crocodile.move_dges(-attack_vel, enemies)
                crocodile.move_espadas(-attack_vel, enemies)
                crocodile.move_grounddeaths(-attack_vel, enemies)

        if blackbeardequipped == True:
            if keys[pygame.K_a] and blackbeard.x - blackbeard_vel > 0:
                blackbeard.x -= blackbeard_vel
            if keys[pygame.K_d] and blackbeard.x + blackbeard_vel + blackbeard.get_width() < WIDTH:  # right
                blackbeard.x += blackbeard_vel
            if keys[pygame.K_w] and blackbeard.y - blackbeard_vel > 0:  # up
                blackbeard.y -= blackbeard_vel
            if keys[pygame.K_s] and blackbeard.y + blackbeard_vel + blackbeard.get_height() + 15 < HEIGHT:  # down
                blackbeard.y += blackbeard_vel
            if keys[pygame.K_u]:
                blackbeard.kurozu()
            if keys[pygame.K_i]:
                blackbeard.blackhole()
            if keys[pygame.K_o]:
                blackbeard.quake()
            if keys[pygame.K_n]:
                Shop = False
            if keys[pygame.K_m]:
                Win = False

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_attacks(attack_vel, blackbeard)

                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, blackbeard):
                    blackbeard.health -= 10
                    enemies.remove(enemy)

                elif enemy.x + enemy.get_width() < 0:
                    lives -= 1
                    enemies.remove(enemy)

                blackbeard.move_kurozus(-attack_vel, enemies)
                blackbeard.move_blackholes(-attack_vel, enemies)
                blackbeard.move_quakes(-attack_vel, enemies)

        if luffyequipped == True:
            if keys[pygame.K_a] and luffy.x - luffy_vel > 0:
                luffy.x -= luffy_vel
            if keys[pygame.K_d] and luffy.x + luffy_vel + luffy.get_width() < WIDTH:  # right
                luffy.x += luffy_vel
            if keys[pygame.K_w] and luffy.y - luffy_vel > 0:  # up
                luffy.y -= luffy_vel
            if keys[pygame.K_s] and luffy.y + luffy_vel + luffy.get_height() + 15 < HEIGHT:  # down
                luffy.y += luffy_vel
            if keys[pygame.K_SPACE]:
                luffy.shoot()
            if keys[pygame.K_u]:
                luffy.gear2()
            if keys[pygame.K_i]:
                luffy.gear3()
            if keys[pygame.K_o]:
                luffy.gear4()
            if keys[pygame.K_n]:
                Shop = False
            if keys[pygame.K_m]:
                Win = False

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_attacks(attack_vel, luffy)

                if random.randrange(0, 2 * 60) == 1:
                    enemy.shoot()

                if collide(enemy, luffy):
                    luffy.health -= 10
                    enemies.remove(enemy)

                elif enemy.x + enemy.get_width() < 0:
                    lives -= 1
                    enemies.remove(enemy)

                luffy.move_attacks(-attack_vel, enemies)
                luffy.move_gear2s(-attack_vel, enemies)
                luffy.move_gear3s(-attack_vel, enemies)
                luffy.move_gear4s(-attack_vel, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    Name_font = pygame.font.SysFont("Comicsans", 100)
    run = True
    while run:
        WIN.blit(Flag, (0, 0))
        title = title_font.render("Enter The Battle?", 1, (255, 255, 255))
        Name = Name_font.render("ONE PIECE BATTLE", 1, (255, 255, 255))
        WIN.blit(title, (0, 0))
        WIN.blit(Name, (300, 750))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()


main_menu()