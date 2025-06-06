
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CurrencyExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CurrencyExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def CurrencyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CurrencyName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AutoChargeMsc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AutoChargeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CurrencyOverChargeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CurrencyAdditionalChargeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChargeLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OverChargeLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SpriteName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DailyRefillType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DailyRefillAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DailyRefillTime(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def DailyRefillTimeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def DailyRefillTimeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def DailyRefillTimeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def ExpirationDateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExpirationNotifyDateIn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpiryChangeParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpiryChangeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExpiryChangeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddID(builder, ID): builder.PrependInt64Slot(0, ID, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(1, LocalizeEtcId, 0)


    @staticmethod
    def AddCurrencyType(builder, CurrencyType): builder.PrependInt32Slot(2, CurrencyType, 0)


    @staticmethod
    def AddCurrencyName(builder, CurrencyName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(CurrencyName), 0)

    @staticmethod
    def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)

    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(5, Rarity, 0)


    @staticmethod
    def AddAutoChargeMsc(builder, AutoChargeMsc): builder.PrependInt32Slot(6, AutoChargeMsc, 0)


    @staticmethod
    def AddAutoChargeAmount(builder, AutoChargeAmount): builder.PrependInt32Slot(7, AutoChargeAmount, 0)


    @staticmethod
    def AddCurrencyOverChargeType(builder, CurrencyOverChargeType): builder.PrependInt32Slot(8, CurrencyOverChargeType, 0)


    @staticmethod
    def AddCurrencyAdditionalChargeType(builder, CurrencyAdditionalChargeType): builder.PrependInt32Slot(9, CurrencyAdditionalChargeType, 0)


    @staticmethod
    def AddChargeLimit(builder, ChargeLimit): builder.PrependInt64Slot(10, ChargeLimit, 0)


    @staticmethod
    def AddOverChargeLimit(builder, OverChargeLimit): builder.PrependInt64Slot(11, OverChargeLimit, 0)


    @staticmethod
    def AddSpriteName(builder, SpriteName): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SpriteName), 0)

    @staticmethod
    def AddDailyRefillType(builder, DailyRefillType): builder.PrependInt32Slot(13, DailyRefillType, 0)


    @staticmethod
    def AddDailyRefillAmount(builder, DailyRefillAmount): builder.PrependInt64Slot(14, DailyRefillAmount, 0)


    @staticmethod
    def AddDailyRefillTime(builder, DailyRefillTime): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(DailyRefillTime), 0)
    @staticmethod
    def StartDailyRefillTimeVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddExpirationDateTime(builder, ExpirationDateTime): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(ExpirationDateTime), 0)

    @staticmethod
    def AddExpirationNotifyDateIn(builder, ExpirationNotifyDateIn): builder.PrependInt32Slot(17, ExpirationNotifyDateIn, 0)


    @staticmethod
    def AddExpiryChangeParcelType(builder, ExpiryChangeParcelType): builder.PrependInt32Slot(18, ExpiryChangeParcelType, 0)


    @staticmethod
    def AddExpiryChangeId(builder, ExpiryChangeId): builder.PrependInt64Slot(19, ExpiryChangeId, 0)


    @staticmethod
    def AddExpiryChangeAmount(builder, ExpiryChangeAmount): builder.PrependInt64Slot(20, ExpiryChangeAmount, 0)

