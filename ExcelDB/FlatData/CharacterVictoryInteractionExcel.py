
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterVictoryInteractionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterVictoryInteractionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def InteractionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CostumeId01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeId02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeId03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeId04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeId05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeId06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PositionIndex06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VictoryStartAnimationPath06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VictoryEndAnimationPath06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceEvent06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(31)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddInteractionId(builder, InteractionId): builder.PrependInt64Slot(0, InteractionId, 0)


    @staticmethod
    def AddCostumeId01(builder, CostumeId01): builder.PrependInt64Slot(1, CostumeId01, 0)


    @staticmethod
    def AddPositionIndex01(builder, PositionIndex01): builder.PrependInt32Slot(2, PositionIndex01, 0)


    @staticmethod
    def AddVictoryStartAnimationPath01(builder, VictoryStartAnimationPath01): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath01), 0)

    @staticmethod
    def AddVictoryEndAnimationPath01(builder, VictoryEndAnimationPath01): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath01), 0)

    @staticmethod
    def AddVoiceEvent01(builder, VoiceEvent01): builder.PrependInt32Slot(5, VoiceEvent01, 0)


    @staticmethod
    def AddCostumeId02(builder, CostumeId02): builder.PrependInt64Slot(6, CostumeId02, 0)


    @staticmethod
    def AddPositionIndex02(builder, PositionIndex02): builder.PrependInt32Slot(7, PositionIndex02, 0)


    @staticmethod
    def AddVictoryStartAnimationPath02(builder, VictoryStartAnimationPath02): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath02), 0)

    @staticmethod
    def AddVictoryEndAnimationPath02(builder, VictoryEndAnimationPath02): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath02), 0)

    @staticmethod
    def AddVoiceEvent02(builder, VoiceEvent02): builder.PrependInt32Slot(10, VoiceEvent02, 0)


    @staticmethod
    def AddCostumeId03(builder, CostumeId03): builder.PrependInt64Slot(11, CostumeId03, 0)


    @staticmethod
    def AddPositionIndex03(builder, PositionIndex03): builder.PrependInt32Slot(12, PositionIndex03, 0)


    @staticmethod
    def AddVictoryStartAnimationPath03(builder, VictoryStartAnimationPath03): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath03), 0)

    @staticmethod
    def AddVictoryEndAnimationPath03(builder, VictoryEndAnimationPath03): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath03), 0)

    @staticmethod
    def AddVoiceEvent03(builder, VoiceEvent03): builder.PrependInt32Slot(15, VoiceEvent03, 0)


    @staticmethod
    def AddCostumeId04(builder, CostumeId04): builder.PrependInt64Slot(16, CostumeId04, 0)


    @staticmethod
    def AddPositionIndex04(builder, PositionIndex04): builder.PrependInt32Slot(17, PositionIndex04, 0)


    @staticmethod
    def AddVictoryStartAnimationPath04(builder, VictoryStartAnimationPath04): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath04), 0)

    @staticmethod
    def AddVictoryEndAnimationPath04(builder, VictoryEndAnimationPath04): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath04), 0)

    @staticmethod
    def AddVoiceEvent04(builder, VoiceEvent04): builder.PrependInt32Slot(20, VoiceEvent04, 0)


    @staticmethod
    def AddCostumeId05(builder, CostumeId05): builder.PrependInt64Slot(21, CostumeId05, 0)


    @staticmethod
    def AddPositionIndex05(builder, PositionIndex05): builder.PrependInt32Slot(22, PositionIndex05, 0)


    @staticmethod
    def AddVictoryStartAnimationPath05(builder, VictoryStartAnimationPath05): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath05), 0)

    @staticmethod
    def AddVictoryEndAnimationPath05(builder, VictoryEndAnimationPath05): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath05), 0)

    @staticmethod
    def AddVoiceEvent05(builder, VoiceEvent05): builder.PrependInt32Slot(25, VoiceEvent05, 0)


    @staticmethod
    def AddCostumeId06(builder, CostumeId06): builder.PrependInt64Slot(26, CostumeId06, 0)


    @staticmethod
    def AddPositionIndex06(builder, PositionIndex06): builder.PrependInt32Slot(27, PositionIndex06, 0)


    @staticmethod
    def AddVictoryStartAnimationPath06(builder, VictoryStartAnimationPath06): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryStartAnimationPath06), 0)

    @staticmethod
    def AddVictoryEndAnimationPath06(builder, VictoryEndAnimationPath06): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryEndAnimationPath06), 0)

    @staticmethod
    def AddVoiceEvent06(builder, VoiceEvent06): builder.PrependInt32Slot(30, VoiceEvent06, 0)

