```mermaid
    classDiagram
    Sprite <|-- Bullet
    Sprite <|-- Alien
    class Alien{
        +screen
        +ai_settings
        +image
        +rect
        +x
        +blitme()
        +update()
        +check_edges()
    }
    class Bullet{
        +screen
        +ai_settings
        +rect
        +y
        +color
        +speed_factor
        +update()
        +draw_buller()
    }
    class Ship{
        +screen
        +image
        +rect
        +screen_rect
        +ai_settings
        +center
        +move_right
        +move_left
        +biteme()
        +update()
        +center_ship()
    }
```