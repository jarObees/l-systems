from lind_systems import *
class Simulation:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
    
    def crawl_system(self, L_sys: object):
        if isinstance(L_sys, L_sysA):
            L_sys.crawl()
            print(L_sys.string)
    
    def reset(self, L_sys):
        L_sys.reset()
        print(L_sys.string)
        