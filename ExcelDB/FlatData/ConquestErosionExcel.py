
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestErosionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestErosionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ErosionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Phase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def StepIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseStartConditionType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def PhaseStartConditionTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def PhaseStartConditionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PhaseStartConditionTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def PhaseStartConditionParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def PhaseStartConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PhaseStartConditionParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0


    def PhaseBeforeExposeConditionType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def PhaseBeforeExposeConditionTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def PhaseBeforeExposeConditionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PhaseBeforeExposeConditionTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0


    def PhaseBeforeExposeConditionParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def PhaseBeforeExposeConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PhaseBeforeExposeConditionParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0


    def ErosionBattleConditionParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ErosionBattleConditionParcelUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ErosionBattleConditionParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConquestRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(1, Id, 0)


    @staticmethod
    def AddErosionType(builder, ErosionType): builder.PrependInt32Slot(2, ErosionType, 0)


    @staticmethod
    def AddPhase(builder, Phase): builder.PrependInt32Slot(3, Phase, 0)


    @staticmethod
    def AddPhaseAlarm(builder, PhaseAlarm): builder.PrependBoolSlot(4, PhaseAlarm, 0)


    @staticmethod
    def AddStepIndex(builder, StepIndex): builder.PrependInt32Slot(5, StepIndex, 0)


    @staticmethod
    def AddPhaseStartConditionType(builder, PhaseStartConditionType): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseStartConditionType), 0)
    @staticmethod
    def StartPhaseStartConditionTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPhaseStartConditionParameter(builder, PhaseStartConditionParameter): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseStartConditionParameter), 0)
    @staticmethod
    def StartPhaseStartConditionParameterVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPhaseBeforeExposeConditionType(builder, PhaseBeforeExposeConditionType): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseBeforeExposeConditionType), 0)
    @staticmethod
    def StartPhaseBeforeExposeConditionTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPhaseBeforeExposeConditionParameter(builder, PhaseBeforeExposeConditionParameter): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseBeforeExposeConditionParameter), 0)
    @staticmethod
    def StartPhaseBeforeExposeConditionParameterVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddErosionBattleConditionParcelType(builder, ErosionBattleConditionParcelType): builder.PrependInt32Slot(10, ErosionBattleConditionParcelType, 0)


    @staticmethod
    def AddErosionBattleConditionParcelUniqueId(builder, ErosionBattleConditionParcelUniqueId): builder.PrependInt64Slot(11, ErosionBattleConditionParcelUniqueId, 0)


    @staticmethod
    def AddErosionBattleConditionParcelAmount(builder, ErosionBattleConditionParcelAmount): builder.PrependInt64Slot(12, ErosionBattleConditionParcelAmount, 0)


    @staticmethod
    def AddConquestRewardId(builder, ConquestRewardId): builder.PrependInt64Slot(13, ConquestRewardId, 0)

