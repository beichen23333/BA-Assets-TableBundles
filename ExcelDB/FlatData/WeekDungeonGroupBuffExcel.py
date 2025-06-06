
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WeekDungeonGroupBuffExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeekDungeonGroupBuffExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def WeekDungeonBuffId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def School(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def FormationLocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def SkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddWeekDungeonBuffId(builder, WeekDungeonBuffId): builder.PrependInt64Slot(0, WeekDungeonBuffId, 0)


    @staticmethod
    def AddSchool(builder, School): builder.PrependInt32Slot(1, School, 0)


    @staticmethod
    def AddRecommandLocalizeEtcId(builder, RecommandLocalizeEtcId): builder.PrependUint32Slot(2, RecommandLocalizeEtcId, 0)


    @staticmethod
    def AddFormationLocalizeEtcId(builder, FormationLocalizeEtcId): builder.PrependUint32Slot(3, FormationLocalizeEtcId, 0)


    @staticmethod
    def AddSkillGroupId(builder, SkillGroupId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(SkillGroupId), 0)
