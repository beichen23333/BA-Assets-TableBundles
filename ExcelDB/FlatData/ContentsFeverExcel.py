
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ContentsFeverExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContentsFeverExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ConditionContent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillFeverCheckCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillCostFever(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FeverStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FeverDurationTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddConditionContent(builder, ConditionContent): builder.PrependInt32Slot(0, ConditionContent, 0)


    @staticmethod
    def AddSkillFeverCheckCondition(builder, SkillFeverCheckCondition): builder.PrependInt32Slot(1, SkillFeverCheckCondition, 0)


    @staticmethod
    def AddSkillCostFever(builder, SkillCostFever): builder.PrependInt64Slot(2, SkillCostFever, 0)


    @staticmethod
    def AddFeverStartTime(builder, FeverStartTime): builder.PrependInt64Slot(3, FeverStartTime, 0)


    @staticmethod
    def AddFeverDurationTime(builder, FeverDurationTime): builder.PrependInt64Slot(4, FeverDurationTime, 0)

