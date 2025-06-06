
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameAudioAnimatorExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameAudioAnimatorExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ControllerNameHash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def VoiceNamePrefix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StateNameHash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StateName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IgnoreInterruptDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IgnoreInterruptPlay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Volume(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def Delay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def AudioPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AudioClipPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def AudioClipPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AudioClipPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0


    def VoiceHash(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def VoiceHashAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    def VoiceHashLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def VoiceHashIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddControllerNameHash(builder, ControllerNameHash): builder.PrependUint32Slot(0, ControllerNameHash, 0)


    @staticmethod
    def AddVoiceNamePrefix(builder, VoiceNamePrefix): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceNamePrefix), 0)

    @staticmethod
    def AddStateNameHash(builder, StateNameHash): builder.PrependUint32Slot(2, StateNameHash, 0)


    @staticmethod
    def AddStateName(builder, StateName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(StateName), 0)

    @staticmethod
    def AddIgnoreInterruptDelay(builder, IgnoreInterruptDelay): builder.PrependBoolSlot(4, IgnoreInterruptDelay, 0)


    @staticmethod
    def AddIgnoreInterruptPlay(builder, IgnoreInterruptPlay): builder.PrependBoolSlot(5, IgnoreInterruptPlay, 0)


    @staticmethod
    def AddVolume(builder, Volume): builder.PrependFloat32Slot(6, Volume, 0)


    @staticmethod
    def AddDelay(builder, Delay): builder.PrependFloat32Slot(7, Delay, 0)


    @staticmethod
    def AddAudioPriority(builder, AudioPriority): builder.PrependInt32Slot(8, AudioPriority, 0)


    @staticmethod
    def AddAudioClipPath(builder, AudioClipPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipPath), 0)
    @staticmethod
    def StartAudioClipPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddVoiceHash(builder, VoiceHash): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceHash), 0)
    @staticmethod
    def StartVoiceHashVector(builder, numElems): return builder.StartVector(4, numElems, 4)

