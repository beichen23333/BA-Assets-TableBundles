
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsRefresh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsSoldOutDimmed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CostParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def CostParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def CostParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CostParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0


    def CostParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def CostParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def CostParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def CostParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0


    def AutoRefreshCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RefreshAbleCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GoodsId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def GoodsIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def GoodsIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def GoodsIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0


    def OpenPeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenPeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShopProductUpdateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsShopVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId4(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId5(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId6(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId7(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId8(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId9(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId10(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId11(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopUpdateGroupId12(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(28)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(0, CategoryType, 0)


    @staticmethod
    def AddIsRefresh(builder, IsRefresh): builder.PrependBoolSlot(1, IsRefresh, 0)


    @staticmethod
    def AddIsSoldOutDimmed(builder, IsSoldOutDimmed): builder.PrependBoolSlot(2, IsSoldOutDimmed, 0)


    @staticmethod
    def AddCostParcelType(builder, CostParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(CostParcelType), 0)
    @staticmethod
    def StartCostParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddCostParcelId(builder, CostParcelId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(CostParcelId), 0)
    @staticmethod
    def StartCostParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddAutoRefreshCoolTime(builder, AutoRefreshCoolTime): builder.PrependInt64Slot(5, AutoRefreshCoolTime, 0)


    @staticmethod
    def AddRefreshAbleCount(builder, RefreshAbleCount): builder.PrependInt64Slot(6, RefreshAbleCount, 0)


    @staticmethod
    def AddGoodsId(builder, GoodsId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsId), 0)
    @staticmethod
    def StartGoodsIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddOpenPeriodFrom(builder, OpenPeriodFrom): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodFrom), 0)

    @staticmethod
    def AddOpenPeriodTo(builder, OpenPeriodTo): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodTo), 0)

    @staticmethod
    def AddShopProductUpdateTime(builder, ShopProductUpdateTime): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(ShopProductUpdateTime), 0)

    @staticmethod
    def AddDisplayParcelType(builder, DisplayParcelType): builder.PrependInt32Slot(11, DisplayParcelType, 0)


    @staticmethod
    def AddDisplayParcelId(builder, DisplayParcelId): builder.PrependInt64Slot(12, DisplayParcelId, 0)


    @staticmethod
    def AddIsShopVisible(builder, IsShopVisible): builder.PrependBoolSlot(13, IsShopVisible, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(14, DisplayOrder, 0)


    @staticmethod
    def AddShopUpdateDate(builder, ShopUpdateDate): builder.PrependInt32Slot(15, ShopUpdateDate, 0)


    @staticmethod
    def AddShopUpdateGroupId1(builder, ShopUpdateGroupId1): builder.PrependInt32Slot(16, ShopUpdateGroupId1, 0)


    @staticmethod
    def AddShopUpdateGroupId2(builder, ShopUpdateGroupId2): builder.PrependInt32Slot(17, ShopUpdateGroupId2, 0)


    @staticmethod
    def AddShopUpdateGroupId3(builder, ShopUpdateGroupId3): builder.PrependInt32Slot(18, ShopUpdateGroupId3, 0)


    @staticmethod
    def AddShopUpdateGroupId4(builder, ShopUpdateGroupId4): builder.PrependInt32Slot(19, ShopUpdateGroupId4, 0)


    @staticmethod
    def AddShopUpdateGroupId5(builder, ShopUpdateGroupId5): builder.PrependInt32Slot(20, ShopUpdateGroupId5, 0)


    @staticmethod
    def AddShopUpdateGroupId6(builder, ShopUpdateGroupId6): builder.PrependInt32Slot(21, ShopUpdateGroupId6, 0)


    @staticmethod
    def AddShopUpdateGroupId7(builder, ShopUpdateGroupId7): builder.PrependInt32Slot(22, ShopUpdateGroupId7, 0)


    @staticmethod
    def AddShopUpdateGroupId8(builder, ShopUpdateGroupId8): builder.PrependInt32Slot(23, ShopUpdateGroupId8, 0)


    @staticmethod
    def AddShopUpdateGroupId9(builder, ShopUpdateGroupId9): builder.PrependInt32Slot(24, ShopUpdateGroupId9, 0)


    @staticmethod
    def AddShopUpdateGroupId10(builder, ShopUpdateGroupId10): builder.PrependInt32Slot(25, ShopUpdateGroupId10, 0)


    @staticmethod
    def AddShopUpdateGroupId11(builder, ShopUpdateGroupId11): builder.PrependInt32Slot(26, ShopUpdateGroupId11, 0)


    @staticmethod
    def AddShopUpdateGroupId12(builder, ShopUpdateGroupId12): builder.PrependInt32Slot(27, ShopUpdateGroupId12, 0)

