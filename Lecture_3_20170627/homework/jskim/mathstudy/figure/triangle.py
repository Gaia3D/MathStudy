# -*- coding: utf-8 -*-


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def checkPointInThis(self, point):

        # ab
        ab_x = self.x2 - self.x1
        ab_y = self.y2 - self.y1

        # pa
        pa_x = point.x - self.x1
        pa_y = point.y - self.y1

        # ab x pa 외적
        cross_ab_pa = (ab_x * pa_y) - (ab_y * pa_x)
        print "cross_ab_pa : " + str(cross_ab_pa)

        if cross_ab_pa == 0 :
            return True

        # bc
        bc_x = self.x3 - self.x2
        bc_y = self.y3 - self.y2

        # pb
        pb_x = point.x - self.x2
        pb_y = point.y - self.y2

        # ab x pb 외적
        cross_bc_pb = (bc_x * pb_y) - (bc_y * pb_x)
        print "cross_bc_pb : " + str(cross_bc_pb)

        if cross_bc_pb == 0 :
            return True

        if cross_ab_pa * cross_bc_pb < 0:
            return False

        # ca
        ca_x = self.x1 - self.x3
        ca_y = self.y1 - self.y3

        # pc
        pc_x = point.x - self.x3
        pc_y = point.y - self.y3

        # ca x pc 외적
        cross_ca_pc = (ca_x * pc_y) - (ca_y * pc_x)
        print "cross_ca_pc : " + str(cross_ca_pc)

        if cross_ca_pc == 0 :
            return True

        if cross_bc_pb * cross_ca_pc < 0:
            return False

        return True

