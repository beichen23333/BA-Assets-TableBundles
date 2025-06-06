
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundNodeFlat:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundNodeFlat()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsCanNotUseSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .GroundVector3 import GroundVector3
            obj = GroundVector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


    def NodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OriginalNodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddX(builder, X): builder.PrependInt32Slot(0, X, 0)


    @staticmethod
    def AddY(builder, Y): builder.PrependInt32Slot(1, Y, 0)


    @staticmethod
    def AddIsCanNotUseSkill(builder, IsCanNotUseSkill): builder.PrependBoolSlot(2, IsCanNotUseSkill, 0)


    @staticmethod
    def AddPosition(builder, Position): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Position), 0)

    @staticmethod
    def AddNodeType(builder, NodeType): builder.PrependInt32Slot(4, NodeType, 0)


    @staticmethod
    def AddOriginalNodeType(builder, OriginalNodeType): builder.PrependInt32Slot(5, OriginalNodeType, 0)

