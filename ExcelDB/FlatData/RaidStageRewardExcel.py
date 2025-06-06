
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RaidStageRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RaidStageRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsClearStageRewardHideInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ClearStageRewardProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClearStageRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearStageRewardParcelUniqueID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClearStageRewardParcelUniqueName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ClearStageRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)


    @staticmethod
    def AddIsClearStageRewardHideInfo(builder, IsClearStageRewardHideInfo): builder.PrependBoolSlot(1, IsClearStageRewardHideInfo, 0)


    @staticmethod
    def AddClearStageRewardProb(builder, ClearStageRewardProb): builder.PrependInt64Slot(2, ClearStageRewardProb, 0)


    @staticmethod
    def AddClearStageRewardParcelType(builder, ClearStageRewardParcelType): builder.PrependInt32Slot(3, ClearStageRewardParcelType, 0)


    @staticmethod
    def AddClearStageRewardParcelUniqueID(builder, ClearStageRewardParcelUniqueID): builder.PrependInt64Slot(4, ClearStageRewardParcelUniqueID, 0)


    @staticmethod
    def AddClearStageRewardParcelUniqueName(builder, ClearStageRewardParcelUniqueName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ClearStageRewardParcelUniqueName), 0)

    @staticmethod
    def AddClearStageRewardAmount(builder, ClearStageRewardAmount): builder.PrependInt64Slot(6, ClearStageRewardAmount, 0)

