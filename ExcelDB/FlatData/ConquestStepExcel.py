
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestStepExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestStepExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MapDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Step(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StepGoalLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StepEnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StepEnterItemType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StepEnterItemUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StepEnterItemAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventUnitId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def UnexpectedEventUnitIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def UnexpectedEventUnitIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def UnexpectedEventUnitIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0


    def UnexpectedEventPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TreasureBoxObjectId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TreasureBoxCountPerStepOpen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddMapDifficulty(builder, MapDifficulty): builder.PrependInt32Slot(1, MapDifficulty, 0)


    @staticmethod
    def AddStep(builder, Step): builder.PrependInt32Slot(2, Step, 0)


    @staticmethod
    def AddStepGoalLocalize(builder, StepGoalLocalize): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(StepGoalLocalize), 0)

    @staticmethod
    def AddStepEnterScenarioGroupId(builder, StepEnterScenarioGroupId): builder.PrependInt64Slot(4, StepEnterScenarioGroupId, 0)


    @staticmethod
    def AddStepEnterItemType(builder, StepEnterItemType): builder.PrependInt32Slot(5, StepEnterItemType, 0)


    @staticmethod
    def AddStepEnterItemUniqueId(builder, StepEnterItemUniqueId): builder.PrependInt64Slot(6, StepEnterItemUniqueId, 0)


    @staticmethod
    def AddStepEnterItemAmount(builder, StepEnterItemAmount): builder.PrependInt64Slot(7, StepEnterItemAmount, 0)


    @staticmethod
    def AddUnexpectedEventUnitId(builder, UnexpectedEventUnitId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(UnexpectedEventUnitId), 0)
    @staticmethod
    def StartUnexpectedEventUnitIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddUnexpectedEventPrefab(builder, UnexpectedEventPrefab): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(UnexpectedEventPrefab), 0)

    @staticmethod
    def AddTreasureBoxObjectId(builder, TreasureBoxObjectId): builder.PrependInt64Slot(10, TreasureBoxObjectId, 0)


    @staticmethod
    def AddTreasureBoxCountPerStepOpen(builder, TreasureBoxCountPerStepOpen): builder.PrependInt32Slot(11, TreasureBoxCountPerStepOpen, 0)

