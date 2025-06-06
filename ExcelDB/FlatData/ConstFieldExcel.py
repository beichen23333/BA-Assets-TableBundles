
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstFieldExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstFieldExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def DialogSmoothTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TalkDialogDurationDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ThinkDialogDurationDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IdleThinkDelayMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IdleThinkDelayMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddDialogSmoothTime(builder, DialogSmoothTime): builder.PrependInt32Slot(0, DialogSmoothTime, 0)


    @staticmethod
    def AddTalkDialogDurationDefault(builder, TalkDialogDurationDefault): builder.PrependInt32Slot(1, TalkDialogDurationDefault, 0)


    @staticmethod
    def AddThinkDialogDurationDefault(builder, ThinkDialogDurationDefault): builder.PrependInt32Slot(2, ThinkDialogDurationDefault, 0)


    @staticmethod
    def AddIdleThinkDelayMin(builder, IdleThinkDelayMin): builder.PrependInt32Slot(3, IdleThinkDelayMin, 0)


    @staticmethod
    def AddIdleThinkDelayMax(builder, IdleThinkDelayMax): builder.PrependInt32Slot(4, IdleThinkDelayMax, 0)

