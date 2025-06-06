
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameRhythmExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameRhythmExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RhythmBgmId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PresetName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StageDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsSpecial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OpenStageScoreAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MissDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CriticalHPRestoreValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FeverScoreRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NoteScoreRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ComboScoreRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AttackScoreRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FeverCriticalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def FeverAttackRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MaxHpScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RhythmFileName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ArtLevelSceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ComboImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(20)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddRhythmBgmId(builder, RhythmBgmId): builder.PrependInt64Slot(1, RhythmBgmId, 0)


    @staticmethod
    def AddPresetName(builder, PresetName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(PresetName), 0)

    @staticmethod
    def AddStageDifficulty(builder, StageDifficulty): builder.PrependInt32Slot(3, StageDifficulty, 0)


    @staticmethod
    def AddIsSpecial(builder, IsSpecial): builder.PrependBoolSlot(4, IsSpecial, 0)


    @staticmethod
    def AddOpenStageScoreAmount(builder, OpenStageScoreAmount): builder.PrependInt64Slot(5, OpenStageScoreAmount, 0)


    @staticmethod
    def AddMaxHp(builder, MaxHp): builder.PrependInt64Slot(6, MaxHp, 0)


    @staticmethod
    def AddMissDamage(builder, MissDamage): builder.PrependInt64Slot(7, MissDamage, 0)


    @staticmethod
    def AddCriticalHPRestoreValue(builder, CriticalHPRestoreValue): builder.PrependInt64Slot(8, CriticalHPRestoreValue, 0)


    @staticmethod
    def AddMaxScore(builder, MaxScore): builder.PrependInt64Slot(9, MaxScore, 0)


    @staticmethod
    def AddFeverScoreRate(builder, FeverScoreRate): builder.PrependInt64Slot(10, FeverScoreRate, 0)


    @staticmethod
    def AddNoteScoreRate(builder, NoteScoreRate): builder.PrependInt64Slot(11, NoteScoreRate, 0)


    @staticmethod
    def AddComboScoreRate(builder, ComboScoreRate): builder.PrependInt64Slot(12, ComboScoreRate, 0)


    @staticmethod
    def AddAttackScoreRate(builder, AttackScoreRate): builder.PrependInt64Slot(13, AttackScoreRate, 0)


    @staticmethod
    def AddFeverCriticalRate(builder, FeverCriticalRate): builder.PrependFloat32Slot(14, FeverCriticalRate, 0)


    @staticmethod
    def AddFeverAttackRate(builder, FeverAttackRate): builder.PrependFloat32Slot(15, FeverAttackRate, 0)


    @staticmethod
    def AddMaxHpScore(builder, MaxHpScore): builder.PrependInt64Slot(16, MaxHpScore, 0)


    @staticmethod
    def AddRhythmFileName(builder, RhythmFileName): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(RhythmFileName), 0)

    @staticmethod
    def AddArtLevelSceneName(builder, ArtLevelSceneName): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(ArtLevelSceneName), 0)

    @staticmethod
    def AddComboImagePath(builder, ComboImagePath): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(ComboImagePath), 0)
