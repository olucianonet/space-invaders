class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 3
        self.ship_limit = 3

        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 240, 20, 160
        self.bullets_allowed = 50

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

