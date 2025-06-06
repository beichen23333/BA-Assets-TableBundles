
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClanAssistSlotExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClanAssistSlotExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SlotId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EchelonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SlotNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AssistTermRewardPeriodFromSec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AssistRewardLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AssistRentRewardDailyMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AssistRentalFeeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AssistRentalFeeAmountStranger(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSlotId(builder, SlotId): builder.PrependInt64Slot(0, SlotId, 0)


    @staticmethod
    def AddEchelonType(builder, EchelonType): builder.PrependInt32Slot(1, EchelonType, 0)


    @staticmethod
    def AddSlotNumber(builder, SlotNumber): builder.PrependInt64Slot(2, SlotNumber, 0)


    @staticmethod
    def AddAssistTermRewardPeriodFromSec(builder, AssistTermRewardPeriodFromSec): builder.PrependInt64Slot(3, AssistTermRewardPeriodFromSec, 0)


    @staticmethod
    def AddAssistRewardLimit(builder, AssistRewardLimit): builder.PrependInt64Slot(4, AssistRewardLimit, 0)


    @staticmethod
    def AddAssistRentRewardDailyMaxCount(builder, AssistRentRewardDailyMaxCount): builder.PrependInt64Slot(5, AssistRentRewardDailyMaxCount, 0)


    @staticmethod
    def AddAssistRentalFeeAmount(builder, AssistRentalFeeAmount): builder.PrependInt64Slot(6, AssistRentalFeeAmount, 0)


    @staticmethod
    def AddAssistRentalFeeAmountStranger(builder, AssistRentalFeeAmountStranger): builder.PrependInt64Slot(7, AssistRentalFeeAmountStranger, 0)

