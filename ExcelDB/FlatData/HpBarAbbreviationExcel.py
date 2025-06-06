
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class HpBarAbbreviationExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = HpBarAbbreviationExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def MonsterLv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StandardHpBar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidBossHpBar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddMonsterLv(builder, MonsterLv): builder.PrependInt32Slot(0, MonsterLv, 0)


    @staticmethod
    def AddStandardHpBar(builder, StandardHpBar): builder.PrependInt32Slot(1, StandardHpBar, 0)


    @staticmethod
    def AddRaidBossHpBar(builder, RaidBossHpBar): builder.PrependInt32Slot(2, RaidBossHpBar, 0)

