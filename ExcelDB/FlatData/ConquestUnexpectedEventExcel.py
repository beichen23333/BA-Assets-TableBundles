
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestUnexpectedEventExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestUnexpectedEventExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventOccurDailyLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnitCountPerStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventPrefab(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def UnexpectedEventPrefabLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def UnexpectedEventPrefabIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def UnexpectedEventUnitId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def UnexpectedEventUnitIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def UnexpectedEventUnitIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def UnexpectedEventUnitIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddUnexpectedEventConditionType(builder, UnexpectedEventConditionType): builder.PrependInt32Slot(1, UnexpectedEventConditionType, 0)


    @staticmethod
    def AddUnexpectedEventConditionUniqueId(builder, UnexpectedEventConditionUniqueId): builder.PrependInt64Slot(2, UnexpectedEventConditionUniqueId, 0)


    @staticmethod
    def AddUnexpectedEventConditionAmount(builder, UnexpectedEventConditionAmount): builder.PrependInt64Slot(3, UnexpectedEventConditionAmount, 0)


    @staticmethod
    def AddUnexpectedEventOccurDailyLimitCount(builder, UnexpectedEventOccurDailyLimitCount): builder.PrependInt32Slot(4, UnexpectedEventOccurDailyLimitCount, 0)


    @staticmethod
    def AddUnitCountPerStep(builder, UnitCountPerStep): builder.PrependInt32Slot(5, UnitCountPerStep, 0)


    @staticmethod
    def AddUnexpectedEventPrefab(builder, UnexpectedEventPrefab): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(UnexpectedEventPrefab), 0)
    @staticmethod
    def StartUnexpectedEventPrefabVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddUnexpectedEventUnitId(builder, UnexpectedEventUnitId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(UnexpectedEventUnitId), 0)
    @staticmethod
    def StartUnexpectedEventUnitIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)

