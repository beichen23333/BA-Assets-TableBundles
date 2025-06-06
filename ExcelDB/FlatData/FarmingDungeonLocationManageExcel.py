
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FarmingDungeonLocationManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FarmingDungeonLocationManageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def FarmingDungeonLocationId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WeekDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SchoolDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenStartDateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenEndDateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocationButtonImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeCodeTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LocalizeCodeInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddFarmingDungeonLocationId(builder, FarmingDungeonLocationId): builder.PrependInt64Slot(0, FarmingDungeonLocationId, 0)


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(1, ContentType, 0)


    @staticmethod
    def AddWeekDungeonType(builder, WeekDungeonType): builder.PrependInt32Slot(2, WeekDungeonType, 0)


    @staticmethod
    def AddSchoolDungeonType(builder, SchoolDungeonType): builder.PrependInt32Slot(3, SchoolDungeonType, 0)


    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt64Slot(4, Order, 0)


    @staticmethod
    def AddOpenStartDateTime(builder, OpenStartDateTime): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(OpenStartDateTime), 0)

    @staticmethod
    def AddOpenEndDateTime(builder, OpenEndDateTime): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(OpenEndDateTime), 0)

    @staticmethod
    def AddLocationButtonImagePath(builder, LocationButtonImagePath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(LocationButtonImagePath), 0)

    @staticmethod
    def AddLocalizeCodeTitle(builder, LocalizeCodeTitle): builder.PrependUint32Slot(8, LocalizeCodeTitle, 0)


    @staticmethod
    def AddLocalizeCodeInfo(builder, LocalizeCodeInfo): builder.PrependUint32Slot(9, LocalizeCodeInfo, 0)

