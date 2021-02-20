import uuid, time


class Entity():
    def __init__(self, e_id, attr_data=None):
        self.e_id = e_id
        self.u_id = uuid.uuid4().hex

        self.is_active = True

        self.name = ''
        self.description = ''

        # TODO should get called in a set_active fn
        self.spawn_time = time.time()

        self.delay = 2
        self.max_delay = self.delay
        self.life_steps = 0

        if attr_data:
            self._load_data(attr_data)

    def get_lifespan(self):
        return self.life_steps

    def get_tiles_to_draw(self):
        return [self._generate_base_tile()]

    def _generate_base_tile(self):
        return (self.tileset_id, self.tile_id)

    def _load_data(self, dataset):
        for k, v in dataset.items():
            if hasattr(v, '__call__'):
                setattr(self, k, v())
            else:
                setattr(self, k, v)

    def _modify_data(self, dataset):
        for k, v in dataset.items():
            if hasattr(self, k):
                if hasattr(v, '__call__'):
                    setattr(self, k, getattr(self, k) + v())
                else:
                    setattr(self, k, getattr(self, k) + v)

    def step(self):
        if self.is_active:
            if self.delay <= 0:
                self.delay = self.max_delay
            else:
                self.delay -= 1
            self.life_steps += 1

    def print_stats(self):
        for attr in dir(self):
            value = getattr(self, attr)
            if not hasattr(value, '__call__'):
                print(attr + ' : ' + str(getattr(self, attr)))

    def adjust_delay(self, amount):
        if self.alive:
            self.delay += amount

