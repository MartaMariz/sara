from os import walk

import pygame

def import_folder(path):
    image_list = []
    for _,__,img_files in walk(path):
        print('here')
        for img in img_files:
            full_path = path + '/' + img 
            print(full_path)
            image = pygame.image.load(full_path).convert_alpha()
            image_list.append(image)
    return image_list

