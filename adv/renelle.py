from core.advbase import *
from slot.a import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')
    
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Elegant_Escort()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `fs, x=5
        """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Marth', 'Serena']

    def s1_proc(self, e):
        self.afflics.burn('s1',100,0.803)
    
    def s2_proc(self, e):
        self.afflics.burn('s2',100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
