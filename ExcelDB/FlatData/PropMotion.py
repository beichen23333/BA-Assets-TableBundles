
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PropMotion:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PropMotion()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Positions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .PropVector3 import PropVector3
            obj = PropVector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    def PositionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PositionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0


    def Rotations(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .PropVector3 import PropVector3
            obj = PropVector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    def RotationsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RotationsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddPositions(builder, Positions): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Positions), 0)
    @staticmethod
    def StartPositionsVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddRotations(builder, Rotations): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Rotations), 0)
    @staticmethod
    def StartRotationsVector(builder, numElems): return builder.StartVector(4, numElems, 4)

