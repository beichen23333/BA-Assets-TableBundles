
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MultiFloorRaidSeasonManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MultiFloorRaidSeasonManageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LobbyEnterScenario(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ShowLobbyBanner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SeasonStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EndNoteLabelStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeasonEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SettlementEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenRaidBossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnterScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LobbyImgPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LevelImgPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PlayTip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(0, SeasonId, 0)


    @staticmethod
    def AddLobbyEnterScenario(builder, LobbyEnterScenario): builder.PrependUint32Slot(1, LobbyEnterScenario, 0)


    @staticmethod
    def AddShowLobbyBanner(builder, ShowLobbyBanner): builder.PrependBoolSlot(2, ShowLobbyBanner, 0)


    @staticmethod
    def AddSeasonStartDate(builder, SeasonStartDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonStartDate), 0)

    @staticmethod
    def AddEndNoteLabelStartDate(builder, EndNoteLabelStartDate): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(EndNoteLabelStartDate), 0)

    @staticmethod
    def AddSeasonEndDate(builder, SeasonEndDate): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonEndDate), 0)

    @staticmethod
    def AddSettlementEndDate(builder, SettlementEndDate): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(SettlementEndDate), 0)

    @staticmethod
    def AddOpenRaidBossGroupId(builder, OpenRaidBossGroupId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(OpenRaidBossGroupId), 0)

    @staticmethod
    def AddEnterScenarioKey(builder, EnterScenarioKey): builder.PrependUint32Slot(8, EnterScenarioKey, 0)


    @staticmethod
    def AddLobbyImgPath(builder, LobbyImgPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(LobbyImgPath), 0)

    @staticmethod
    def AddLevelImgPath(builder, LevelImgPath): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(LevelImgPath), 0)

    @staticmethod
    def AddPlayTip(builder, PlayTip): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(PlayTip), 0)
