
class GlobalVars(object):
    scale = 1.0


    @classmethod
    def mult_scale(cls, multiplier):
        GlobalVars.change_scale(GlobalVars.scale * multiplier)

    @classmethod
    def change_scale(cls, new_scale):
        GlobalVars.scale = new_scale
        raise NotImplementedError

