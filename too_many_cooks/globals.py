
class GlobalVars(object):
    scale = 2.5


    @classmethod
    def mult_scale(cls, multiplier):
        GlobalVars.change_scale(GlobalVars.scale * multiplier)

    @classmethod
    def change_scale(cls, new_scale):
        GlobalVars.scale = new_scale
        raise NotImplementedError

