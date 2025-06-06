
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BossExternalBTExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BossExternalBTExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ExternalBTId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AIPhase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExternalBTNodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExternalBTTrigger(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TriggerArgument(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BehaviorRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExternalBehavior(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BehaviorArgument(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddExternalBTId(builder, ExternalBTId): builder.PrependInt64Slot(0, ExternalBTId, 0)


    @staticmethod
    def AddAIPhase(builder, AIPhase): builder.PrependInt64Slot(1, AIPhase, 0)


    @staticmethod
    def AddExternalBTNodeType(builder, ExternalBTNodeType): builder.PrependInt32Slot(2, ExternalBTNodeType, 0)


    @staticmethod
    def AddExternalBTTrigger(builder, ExternalBTTrigger): builder.PrependInt32Slot(3, ExternalBTTrigger, 0)


    @staticmethod
    def AddTriggerArgument(builder, TriggerArgument): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(TriggerArgument), 0)

    @staticmethod
    def AddBehaviorRate(builder, BehaviorRate): builder.PrependInt64Slot(5, BehaviorRate, 0)


    @staticmethod
    def AddExternalBehavior(builder, ExternalBehavior): builder.PrependInt32Slot(6, ExternalBehavior, 0)


    @staticmethod
    def AddBehaviorArgument(builder, BehaviorArgument): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(BehaviorArgument), 0)
