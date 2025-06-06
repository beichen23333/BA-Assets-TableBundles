
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopFreeRecruitPeriodExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopFreeRecruitPeriodExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ShopFreeRecruitId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShopFreeRecruitIntervalId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IntervalDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FreeRecruitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddShopFreeRecruitId(builder, ShopFreeRecruitId): builder.PrependInt64Slot(0, ShopFreeRecruitId, 0)


    @staticmethod
    def AddShopFreeRecruitIntervalId(builder, ShopFreeRecruitIntervalId): builder.PrependInt64Slot(1, ShopFreeRecruitIntervalId, 0)


    @staticmethod
    def AddIntervalDate(builder, IntervalDate): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(IntervalDate), 0)

    @staticmethod
    def AddFreeRecruitCount(builder, FreeRecruitCount): builder.PrependInt32Slot(3, FreeRecruitCount, 0)

