
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MoveEnd:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MoveEnd()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Normal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


    def Stand(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


    def Kneel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Motion import Motion
            obj = Motion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddNormal(builder, Normal): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Normal), 0)

    @staticmethod
    def AddStand(builder, Stand): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Stand), 0)

    @staticmethod
    def AddKneel(builder, Kneel): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Kneel), 0)
