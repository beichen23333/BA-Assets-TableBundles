
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticEntityEffectFilterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticEntityEffectFilterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def TargetEffectName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowEffectToVehicle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowEffectToBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddTargetEffectName(builder, TargetEffectName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(TargetEffectName), 0)

    @staticmethod
    def AddShowEffectToVehicle(builder, ShowEffectToVehicle): builder.PrependBoolSlot(1, ShowEffectToVehicle, 0)


    @staticmethod
    def AddShowEffectToBoss(builder, ShowEffectToBoss): builder.PrependBoolSlot(2, ShowEffectToBoss, 0)

