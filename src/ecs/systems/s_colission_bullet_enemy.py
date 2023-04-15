import esper
import pygame
from src.ecs.components.c_surface import CSurface

from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

def system_collision_bullet_enemy(world: esper.World, bullet_entity: int) -> None:
    # Revisamos que el entity exista en el mundo y que no sea None
    try:
        if bullet_entity is not None:
            components = world.get_components(CSurface, CTransform, CTagEnemy)
            bl_t = world.component_for_entity(bullet_entity, CTransform)
            bl_s = world.component_for_entity(bullet_entity, CSurface)
            bl_rect = bl_s.surf.get_rect(topleft = bl_t.pos)
            for enemy_entity, (c_s, c_t, _) in components:
                ene_rect = c_s.surf.get_rect(topleft = c_t.pos)
                if ene_rect.colliderect(bl_rect):
                    world.delete_entity(enemy_entity)
                    world.delete_entity(bullet_entity)
    except:
        pass
    
