
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeCharProfileExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeCharProfileExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StatusMessageKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatusMessageJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(38)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)


    @staticmethod
    def AddStatusMessageKr(builder, StatusMessageKr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageKr), 0)

    @staticmethod
    def AddStatusMessageJp(builder, StatusMessageJp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageJp), 0)

    @staticmethod
    def AddFullNameKr(builder, FullNameKr): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameKr), 0)

    @staticmethod
    def AddFullNameJp(builder, FullNameJp): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameJp), 0)

    @staticmethod
    def AddFamilyNameKr(builder, FamilyNameKr): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameKr), 0)

    @staticmethod
    def AddFamilyNameRubyKr(builder, FamilyNameRubyKr): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyKr), 0)

    @staticmethod
    def AddPersonalNameKr(builder, PersonalNameKr): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameKr), 0)

    @staticmethod
    def AddPersonalNameRubyKr(builder, PersonalNameRubyKr): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyKr), 0)

    @staticmethod
    def AddFamilyNameJp(builder, FamilyNameJp): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameJp), 0)

    @staticmethod
    def AddFamilyNameRubyJp(builder, FamilyNameRubyJp): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyJp), 0)

    @staticmethod
    def AddPersonalNameJp(builder, PersonalNameJp): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameJp), 0)

    @staticmethod
    def AddPersonalNameRubyJp(builder, PersonalNameRubyJp): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyJp), 0)

    @staticmethod
    def AddSchoolYearKr(builder, SchoolYearKr): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearKr), 0)

    @staticmethod
    def AddSchoolYearJp(builder, SchoolYearJp): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearJp), 0)

    @staticmethod
    def AddCharacterAgeKr(builder, CharacterAgeKr): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeKr), 0)

    @staticmethod
    def AddCharacterAgeJp(builder, CharacterAgeJp): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeJp), 0)

    @staticmethod
    def AddBirthDay(builder, BirthDay): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(BirthDay), 0)

    @staticmethod
    def AddBirthdayKr(builder, BirthdayKr): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayKr), 0)

    @staticmethod
    def AddBirthdayJp(builder, BirthdayJp): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayJp), 0)

    @staticmethod
    def AddCharHeightKr(builder, CharHeightKr): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightKr), 0)

    @staticmethod
    def AddCharHeightJp(builder, CharHeightJp): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightJp), 0)

    @staticmethod
    def AddDesignerNameKr(builder, DesignerNameKr): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameKr), 0)

    @staticmethod
    def AddDesignerNameJp(builder, DesignerNameJp): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameJp), 0)

    @staticmethod
    def AddIllustratorNameKr(builder, IllustratorNameKr): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameKr), 0)

    @staticmethod
    def AddIllustratorNameJp(builder, IllustratorNameJp): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameJp), 0)

    @staticmethod
    def AddCharacterVoiceKr(builder, CharacterVoiceKr): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceKr), 0)

    @staticmethod
    def AddCharacterVoiceJp(builder, CharacterVoiceJp): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceJp), 0)

    @staticmethod
    def AddHobbyKr(builder, HobbyKr): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyKr), 0)

    @staticmethod
    def AddHobbyJp(builder, HobbyJp): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyJp), 0)

    @staticmethod
    def AddWeaponNameKr(builder, WeaponNameKr): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameKr), 0)

    @staticmethod
    def AddWeaponDescKr(builder, WeaponDescKr): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescKr), 0)

    @staticmethod
    def AddWeaponNameJp(builder, WeaponNameJp): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameJp), 0)

    @staticmethod
    def AddWeaponDescJp(builder, WeaponDescJp): builder.PrependUOffsetTRelativeSlot(33, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescJp), 0)

    @staticmethod
    def AddProfileIntroductionKr(builder, ProfileIntroductionKr): builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionKr), 0)

    @staticmethod
    def AddProfileIntroductionJp(builder, ProfileIntroductionJp): builder.PrependUOffsetTRelativeSlot(35, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionJp), 0)

    @staticmethod
    def AddCharacterSSRNewKr(builder, CharacterSSRNewKr): builder.PrependUOffsetTRelativeSlot(36, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewKr), 0)

    @staticmethod
    def AddCharacterSSRNewJp(builder, CharacterSSRNewJp): builder.PrependUOffsetTRelativeSlot(37, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewJp), 0)
