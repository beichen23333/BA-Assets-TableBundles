
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WeekDungeonRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeekDungeonRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RewardParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RewardParcelProbability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DropItemModelPrefabPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)


    @staticmethod
    def AddDungeonType(builder, DungeonType): builder.PrependInt32Slot(1, DungeonType, 0)


    @staticmethod
    def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(2, RewardParcelType, 0)


    @staticmethod
    def AddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(3, RewardParcelId, 0)


    @staticmethod
    def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependInt64Slot(4, RewardParcelAmount, 0)


    @staticmethod
    def AddRewardParcelProbability(builder, RewardParcelProbability): builder.PrependInt64Slot(5, RewardParcelProbability, 0)


    @staticmethod
    def AddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(6, IsDisplayed, 0)


    @staticmethod
    def AddDropItemModelPrefabPath(builder, DropItemModelPrefabPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(DropItemModelPrefabPath), 0)
