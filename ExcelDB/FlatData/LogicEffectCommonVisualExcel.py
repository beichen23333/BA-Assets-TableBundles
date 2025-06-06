
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LogicEffectCommonVisualExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LogicEffectCommonVisualExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def StringID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def IconSpriteName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IconDispelColor(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def IconDispelColorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    def IconDispelColorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def IconDispelColorIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0


    def ParticleEnterPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ParticleEnterSocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParticleLoopPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ParticleLoopSocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParticleEndPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ParticleEndSocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParticleApplyPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ParticleApplySocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParticleRemovedPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ParticleRemovedSocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddStringID(builder, StringID): builder.PrependUint32Slot(0, StringID, 0)


    @staticmethod
    def AddIconSpriteName(builder, IconSpriteName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(IconSpriteName), 0)

    @staticmethod
    def AddIconDispelColor(builder, IconDispelColor): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(IconDispelColor), 0)
    @staticmethod
    def StartIconDispelColorVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddParticleEnterPath(builder, ParticleEnterPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ParticleEnterPath), 0)

    @staticmethod
    def AddParticleEnterSocket(builder, ParticleEnterSocket): builder.PrependInt32Slot(4, ParticleEnterSocket, 0)


    @staticmethod
    def AddParticleLoopPath(builder, ParticleLoopPath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ParticleLoopPath), 0)

    @staticmethod
    def AddParticleLoopSocket(builder, ParticleLoopSocket): builder.PrependInt32Slot(6, ParticleLoopSocket, 0)


    @staticmethod
    def AddParticleEndPath(builder, ParticleEndPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(ParticleEndPath), 0)

    @staticmethod
    def AddParticleEndSocket(builder, ParticleEndSocket): builder.PrependInt32Slot(8, ParticleEndSocket, 0)


    @staticmethod
    def AddParticleApplyPath(builder, ParticleApplyPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ParticleApplyPath), 0)

    @staticmethod
    def AddParticleApplySocket(builder, ParticleApplySocket): builder.PrependInt32Slot(10, ParticleApplySocket, 0)


    @staticmethod
    def AddParticleRemovedPath(builder, ParticleRemovedPath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(ParticleRemovedPath), 0)

    @staticmethod
    def AddParticleRemovedSocket(builder, ParticleRemovedSocket): builder.PrependInt32Slot(12, ParticleRemovedSocket, 0)

