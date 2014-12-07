
class GlobalVars(object):

    scale = 2.0
    registered_objects = []

    @classmethod
    def register_game_obj(cls, obj):
        GlobalVars.registered_objects.append(obj)

    @classmethod
    def mult_scale(cls, multiplier):
        GlobalVars.change_scale(GlobalVars.scale * multiplier)

    @classmethod
    def change_scale(cls, new_scale):
        print('scale: {}'.format(new_scale))
        GlobalVars.scale = new_scale

        for obj in GlobalVars.registered_objects:
            obj.refresh_scale()

