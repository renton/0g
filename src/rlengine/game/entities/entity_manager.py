from collections import defaultdict


class EntityManager():
    def __init__(self):
        self.entity_groups = {}
        self.entity_collision_groups = {}
        self.z_index_groups = defaultdict(list)
        self.step_order_groups = defaultdict(list)

    def add_entity_group(self, group_id, z_index=0, step_order=0):
        self.entity_groups[group_id] = []
        self.z_index_groups[z_index].append(group_id)
        self.step_order_groups[step_order].append(group_id)

    def get_ordered_draw_entities(self):
        draw_entities = []
        for z_index, entity_group_ids in self.z_index_groups.items():
            for entity_group_id in entity_group_ids:
                draw_entities += self.entity_groups[entity_group_id]
        return draw_entities

    def get_ordered_step_entities(self):
        step_entities = []
        for step_order, entity_group_ids in self.step_order_groups.items():
            for entity_group_id in entity_group_ids:
                step_entities += self.entity_groups[entity_group_id]
        return step_entities

    def add_entity_collision_group(self, group_id, collision_group_ids, collision_fn):
        if group_id not in self.entity_collision_groups:
            self.entity_collision_groups[group_id] = []
        self.entity_collision_groups[group_id].append({
            'collision_group_ids': collision_group_ids,
            'collision_fn': collision_fn
        })

    # TODO obey step order
    def step_collisions(self):
        for group_id in self.entity_groups.keys():
            if group_id in self.entity_collision_groups:
                self.step_collision_group(group_id)

    def step_collision_group(self, group_id):
        for collision_group in self.entity_collision_groups[group_id]:
            for collision_group_id in collision_group['collision_group_ids']:
                for first_collision_entity in self.entity_groups[group_id]:
                    first_entity_rect = first_collision_entity.get_rect()
                    for second_collision_entity in self.entity_groups[collision_group_id]:
                        second_entity_rect = second_collision_entity.get_rect()                        
                        if first_entity_rect.colliderect(second_entity_rect):
                            collision_group['collision_fn'](first_collision_entity, second_collision_entity)

    def add_entity_to_group(self, entity, group_id):
        self.entity_groups[group_id].append(entity)