import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_bullet import CTagBullet

def system_bullet_screen_limit(world:esper.World, screen:pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CTagBullet)

    c_t:CTransform
    c_v:CVelocity
    c_s:CSurface
    for _, (c_t, c_v, c_s, c_b) in components:
        cuad_rect = c_s.surf.get_rect(topleft=c_t.pos)
        if not cuad_rect.colliderect(screen_rect):
            world.delete_entity(_)