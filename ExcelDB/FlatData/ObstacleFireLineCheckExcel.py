
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleFireLineCheckExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleFireLineCheckExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def MyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def AllyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EnemyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EmptyObstacleFireLineCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddMyObstacleFireLineCheck(builder, MyObstacleFireLineCheck): builder.PrependBoolSlot(0, MyObstacleFireLineCheck, 0)


    @staticmethod
    def AddAllyObstacleFireLineCheck(builder, AllyObstacleFireLineCheck): builder.PrependBoolSlot(1, AllyObstacleFireLineCheck, 0)


    @staticmethod
    def AddEnemyObstacleFireLineCheck(builder, EnemyObstacleFireLineCheck): builder.PrependBoolSlot(2, EnemyObstacleFireLineCheck, 0)


    @staticmethod
    def AddEmptyObstacleFireLineCheck(builder, EmptyObstacleFireLineCheck): builder.PrependBoolSlot(3, EmptyObstacleFireLineCheck, 0)

