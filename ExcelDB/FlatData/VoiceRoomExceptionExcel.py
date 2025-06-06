
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class VoiceRoomExceptionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VoiceRoomExceptionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LinkedCharacterVoicePrintType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LinkedCostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCostumeUniqueId(builder, CostumeUniqueId): builder.PrependInt64Slot(0, CostumeUniqueId, 0)


    @staticmethod
    def AddLinkedCharacterVoicePrintType(builder, LinkedCharacterVoicePrintType): builder.PrependInt32Slot(1, LinkedCharacterVoicePrintType, 0)


    @staticmethod
    def AddLinkedCostumeUniqueId(builder, LinkedCostumeUniqueId): builder.PrependInt64Slot(2, LinkedCostumeUniqueId, 0)

