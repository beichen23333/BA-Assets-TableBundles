from enum import IntEnum
from lib.encryption import convert_short, convert_ushort, convert_int, convert_long, convert_float, convert_double, convert_string, convert_uint, convert_ulong, create_key
import inspect

def dump_table(table_instance) -> list:
    excel_name = table_instance.__class__.__name__.removesuffix("Table")
    current_module = inspect.getmodule(inspect.currentframe())
    dump_func = next(
        f
        for n, f in inspect.getmembers(current_module, inspect.isfunction)
        if n.removeprefix("dump_") == excel_name
    )
    password = create_key(excel_name.removesuffix("Excel"))
    return [dump_func(table_instance.DataList(j), password) for j in range(table_instance.DataListLength())]

class GroundNodeType(IntEnum):
    None_ = 0
    WalkAble = 1
    JumpAble = 2
    TSSOnly = 3
    NotWalkAble = 2147483647

class BubbleType(IntEnum):
    Idle = 0
    Monologue = 1
    EmoticonNormal = 2
    EmoticonFavorite = 3
    EmoticonReward = 4
    EmoticonGiveGift = 5

class FurnitureCategory(IntEnum):
    Furnitures = 0
    Decorations = 1
    Interiors = 2

class FurnitureSubCategory(IntEnum):
    Table = 0
    Closet = 1
    Chair = 2
    Bed = 3
    Prop = 4
    FurnitureEtc = 5
    FurnitureSubCategory1 = 6
    HomeAppliance = 7
    WallDecoration = 8
    FloorDecoration = 9
    DecorationEtc = 10
    DecorationSubCategory1 = 11
    Floor = 12
    Background = 13
    Wallpaper = 14
    InteriorsSubCategory1 = 15
    All = 16

class FurnitureLocation(IntEnum):
    None_ = 0
    Inventory = 1
    Floor = 2
    WallLeft = 3
    WallRight = 4

class AcademyMessageConditions(IntEnum):
    None_ = 0
    FavorRankUp = 1
    AcademySchedule = 2
    Answer = 3
    Feedback = 4

class AcademyMessageTypes(IntEnum):
    None_ = 0
    Text = 1
    Image = 2

class VoiceEvent(IntEnum):
    OnTSA = 0
    FormationPickUp = 1
    CampaignResultDefeat = 2
    CampaignResultVictory = 3
    CharacterLevelUp = 4
    CharacterTranscendence = 5
    SkillLevelUp = 6
    Formation = 7
    CampaignCharacterSpawn = 8
    BattleStartTimeline = 9
    BattleVictoryTimeline = 10
    CharacterFavor = 11
    BattleMiss = 12
    BattleBlock = 13
    BattleCover = 14
    BattleMove = 15
    BattleMoveToForamtionBeacon = 16
    MGS_GameStart = 17
    MGS_CharacterSelect = 18
    MGS_Attacking = 19
    MGS_GeasGet = 20
    EXSkill = 21
    EXSkillLevel = 22
    EXSkill2 = 23
    EXSkillLevel2 = 24
    EXSkill3 = 25
    EXSkillLevel3 = 26
    EXSkill4 = 27
    EXSkillLevel4 = 28
    PublicSkill01 = 29
    PublicSkill02 = 30
    InteractionPublicSkill01 = 31
    InteractionPublicSkill02 = 32
    FormationStyleChange = 33
    BattleInteractionVictoryTimeline = 34

class UnitType(IntEnum):
    None_ = 0
    AR = 1
    RF = 2
    HG = 3
    MG = 4
    SMG = 5
    SG = 6
    HZ = 7
    Melee = 8

class AttackType(IntEnum):
    Single = 0
    Splash = 1
    Through = 2
    Heal = 3

class ProjectileType(IntEnum):
    Guided = 0
    Ground = 1
    GuidedExplosion = 2
    GroundConstDistance = 3
    AirConstDistance = 4

class DamageFontColor(IntEnum):
    Blue = 0
    White = 1
    Yellow = 2
    Red = 3
    Green = 4

class TargetingCellType(IntEnum):
    None_ = 0
    Near = 1
    Far = 2

class TargetingUnitType(IntEnum):
    None_ = 0
    Near = 1
    Far = 2
    MinHp = 3
    MaxHp = 4
    Random = 5

class ProjectileAction(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2

class FontType(IntEnum):
    None_ = 0
    Damage = 1
    Block = 2
    Heal = 3
    Miss = 4
    Critical = 5
    Skill = 6
    Immune = 7
    DamageResist = 8
    DamageWeak = 9
    CriticalResist = 10
    CriticalWeak = 11
    Effective = 12
    CriticalEffective = 13

class EmoticonEvent(IntEnum):
    CoverEnter = 0
    ShelterEnter = 1
    Panic = 2
    NearlyDead = 3
    Reload = 4
    Found = 5
    GetBeacon = 6
    Warning = 7

class BulletType(IntEnum):
    Normal = 0
    Pierce = 1
    Explosion = 2
    Siege = 3
    Mystic = 4
    None_ = 5
    Sonic = 6

class ActionType(IntEnum):
    Crush = 0
    Courage = 1
    Tactic = 2

class BuffOverlap(IntEnum):
    Able = 0
    Unable = 1
    Change = 2
    Additive = 3

class ReArrangeTargetType(IntEnum):
    AllySelf = 0
    AllyAll = 1
    AllyUnitType = 2
    AllyGroup = 3

class ArmorType(IntEnum):
    LightArmor = 0
    HeavyArmor = 1
    Unarmed = 2
    Structure = 3
    Normal = 4
    ElasticArmor = 5

class WeaponType(IntEnum):
    None_ = 0
    SG = 1
    SMG = 2
    AR = 3
    GL = 4
    HG = 5
    RL = 6
    SR = 7
    DSMG = 8
    RG = 9
    DSG = 10
    Vulcan = 11
    Missile = 12
    Cannon = 13
    Taser = 14
    MG = 15
    Binah = 16
    MT = 17
    Relic = 18
    FT = 19
    Akemi = 20

class EntityMaterialType(IntEnum):
    Wood = 0
    Stone = 1
    Flesh = 2
    Metal = 3

class CoverMotionType(IntEnum):
    All = 0
    Kneel = 1

class TargetSortBy(IntEnum):
    DISTANCE = 0
    HP = 1
    DAMAGE_EFFICIENCY = 2
    TARGETED_COUNT = 3
    RANDOM = 4
    FRONT_FORMATION = 5

class PositioningType(IntEnum):
    CloseToObstacle = 0
    CloseToTarget = 1

class DamageType(IntEnum):
    Normal = 0
    Critical = 1
    IgnoreDefence = 2

class FormationLine(IntEnum):
    Students = 0
    TSS = 1

class ExternalBTNodeType(IntEnum):
    Sequence = 0
    Selector = 1
    Instant = 2
    SubNode = 3
    ExecuteAll = 4

class ExternalBTTrigger(IntEnum):
    None_ = 0
    HPUnder = 1
    ApplySkillEffectCategory = 2
    HaveNextExSkillActiveGauge = 3
    UseNormalSkill = 4
    UseExSkill = 5
    CheckActiveGaugeOver = 6
    CheckPeriod = 7
    CheckSummonCharacterCountOver = 8
    CheckSummonCharacterCountUnder = 9
    ApplyGroggy = 10
    ApplyLogicEffectTemplateId = 11
    OnSpawned = 12
    CheckActiveGaugeBetween = 13
    DestroyParts = 14
    CheckHallucinationCountOver = 15
    CheckHallucinationCountUnder = 16
    UseSkillEndGroupId = 17

class ExternalBehavior(IntEnum):
    UseNextExSkill = 0
    ChangePhase = 1
    ChangeSection = 2
    AddActiveGauge = 3
    UseSelectExSkill = 4
    ClearNormalSkill = 5
    MoveLeft = 6
    MoveRight = 7
    AllUseSelectExSkill = 8
    ConnectCharacterToDummy = 9
    ConnectExSkillToParts = 10
    SetMaxHPToParts = 11
    AlivePartsUseExSkill = 12
    ActivatePart = 13
    AddGroggy = 14
    SelectTargetToUseSkillAlly = 15
    ForceChangePhase = 16
    ClearUseSkillEndGroupId = 17

class TacticEntityType(IntEnum):
    None_ = 0
    Student = 1
    Minion = 2
    Elite = 4
    Champion = 8
    Boss = 16
    Obstacle = 32
    Servant = 64
    Vehicle = 128
    Summoned = 256
    Hallucination = 512
    DestructibleProjectile = 1024

class BuffIconType(IntEnum):
    None_ = 0
    Debuff_DyingPenalty = 1
    CC_MindControl = 2
    CC_Inoperative = 3
    CC_Confusion = 4
    CC_Provoke = 5
    CC_Silence = 6
    CC_Blind = 7
    Dot_Damage = 8
    Dot_Heal = 9
    Buff_AttackPower = 10
    Buff_CriticalChance = 11
    Buff_CriticalDamage = 12
    Buff_DefensePower = 13
    Buff_Dodge = 14
    Buff_Hit = 15
    Buff_WeaponRange = 16
    Buff_SightRange = 17
    Buff_MoveSpeed = 18
    Buff_Mind = 19
    Debuf_AttackPower = 20
    Debuff_CriticalChance = 21
    Debuff_CriticalDamage = 22
    Debuff_DefensePower = 23
    Debuff_Dodge = 24
    Debuff_Hit = 25
    Debuff_WeaponRange = 26
    Debuff_SightRange = 27
    Debuff_MoveSpeed = 28
    Debuff_Mind = 29
    Buff_AttackTime = 30
    Debuff_AttackTime = 31
    Buff_MaxHp = 32
    Debuff_MaxHp = 33
    Buff_MaxBulletCount = 34
    Debuff_MaxBulletCount = 35
    Debuff_SuppliesCondition = 36
    Buff_HealEffectivenessRate = 37
    Debuff_HealEffectivenessRate = 38
    Buff_HealPower = 39
    Debuff_HealPower = 40
    Buff_CriticalChanceResistPoint = 41
    Debuff_CriticalChanceResistPoint = 42
    CC_Stunned = 43
    Debuff_ConcentratedTarget = 44
    Buff_Immortal = 45
    Max = 46

class Difficulty(IntEnum):
    Normal = 0
    Hard = 1
    VeryHard = 2
    Hardcore = 3
    Extreme = 4
    Insane = 5
    Torment = 6
    Lunatic = 7

class EngageType(IntEnum):
    SearchAndMove = 0
    HoldPosition = 1

class HitEffectPosition(IntEnum):
    Position = 0
    HeadBone = 1
    BodyBone = 2
    Follow = 3

class StageTopography(IntEnum):
    Street = 0
    Outdoor = 1
    Indoor = 2

class TerrainAdaptationStat(IntEnum):
    D = 0
    C = 1
    B = 2
    A = 3
    S = 4
    SS = 5

class SquadType(IntEnum):
    None_ = 0
    Main = 1
    Support = 2
    TSS = 3

class ObstacleClass(IntEnum):
    MAIN = 0
    SUB = 1

class ObstacleDestroyType(IntEnum):
    Remain = 0
    Remove = 1

class ObstacleHeightType(IntEnum):
    Low = 0
    Middle = 1
    High = 2

class ObstacleCoverType(IntEnum):
    None_ = 0
    Cover = 1
    Shelter = 2

class SkillCategory(IntEnum):
    None_ = 0

class LogicEffectCategory(IntEnum):
    None_ = 0
    Attack = 1
    Heal = 2
    Buff = 3
    Debuff = 4
    CrowdControl = 5
    Boss = 6
    Dummy = 7

class AimIKType(IntEnum):
    None_ = 0
    OneHandRight = 1
    OneHandLeft = 2
    TwoHandRight = 3
    TwoHandLeft = 4
    Tripod = 5
    Dual = 6
    Max = 7

class DamageAttribute(IntEnum):
    Resist = 0
    Normal = 1
    Weak = 2
    Effective = 3

class SkillPriorityCheckCondition(IntEnum):
    None_ = 0
    HPRateUnder = 1
    DebuffCountOver = 2
    BuffCountOver = 3
    CrowdControlOver = 4

class SkillPriorityCheckTarget(IntEnum):
    Ally = 0
    Enemy = 1
    All = 2

class StageType(IntEnum):
    Main = 0
    Sub = 1

class OperatorCondition(IntEnum):
    None_ = 0
    StrategyStart = 1
    StrategyVictory = 2
    StrategyDefeat = 3
    AdventureCombatStart = 4
    AdventureCombatVictory = 5
    AdventureCombatDefeat = 6
    ArenaCombatStart = 7
    ArenaCombatVictory = 8
    ArenaCombatDefeat = 9
    WeekDungeonCombatStart = 10
    WeekDungeonCombatVictory = 11
    WeekDungeonCombatDefeat = 12
    SchoolDungeonCombatStart = 13
    SchoolDungeonCombatVictory = 14
    SchoolDungeonCombatDefeat = 15
    StrategyWarpUnitFromHideTile = 16
    TimeAttackDungeonStart = 17
    TimeAttackDungeonVictory = 18
    TimeAttackDungeonDefeat = 19
    WorldRaidBossSpawn = 20
    WorldRaidBossKill = 21
    WorldRaidBossDamaged = 22
    WorldRaidScenarioBattle = 23
    MinigameTBGThemaOpen = 24
    MinigameTBGThemaComeback = 25
    MinigameTBGAllyRevive = 26
    MinigameTBGItemUse = 27

class KnockbackDirection(IntEnum):
    TargetToCaster = 0
    CasterToTarget = 1
    TargetToHitPosition = 2
    HitPositionToTarget = 3
    CasterToHitPosition = 4
    HitPositionToCaster = 5
    Caster = 6
    Target = 7

class EndCondition(IntEnum):
    Duration = 0
    ReloadCount = 1
    AmmoCount = 2
    AmmoHit = 3
    HitCount = 4
    None_ = 5
    UseExSkillCount = 6

class AmplifyDoTRemoveCondition(IntEnum):
    None_ = 0
    ApplyCount = 1

class LogicEffectSound(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2
    Knockback = 3

class EffectBone(IntEnum):
    None_ = 0
    Shot = 1
    Head = 2
    Body = 3
    Shot2 = 4
    Shot3 = 5
    Extra = 6
    Extra2 = 7
    Extra3 = 8

class ArenaSimulatorServer(IntEnum):
    Preset = 0
    Live = 1
    Dev = 2
    QA = 3

class ClearCheck(IntEnum):
    None_ = 0
    Success_Play = 1
    Success_Sweep = 2
    Fail_Timeout = 3
    Fail_PlayerGiveUp = 4
    Fail_Annihilation = 5

class BuffType(IntEnum):
    None_ = 0
    Buff_AttackPower = 1
    Buff_CriticalChance = 2
    Buff_CriticalDamage = 3
    Buff_DefensePower = 4
    Buff_Dodge = 5
    Buff_Hit = 6
    Buff_WeaponRange = 7
    Buff_SightRange = 8
    Buff_MoveSpeed = 9
    Buff_AttackTime = 10
    Buff_MaxHp = 11
    Buff_MaxBulletCount = 12
    DeBuff_AttackPower = 13
    DeBuff_CriticalChance = 14
    DeBuff_CriticalDamage = 15
    DeBuff_DefensePower = 16
    DeBuff_Dodge = 17
    DeBuff_Hit = 18
    DeBuff_WeaponRange = 19
    DeBuff_SightRange = 20
    DeBuff_MoveSpeed = 21
    DeBuff_AttackTime = 22
    DeBuff_MaxHp = 23
    DeBuff_MaxBulletCount = 24

class WorldRaidDifficulty(IntEnum):
    None_ = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7

class TacticSpeed(IntEnum):
    None_ = 0
    Slow = 1
    Normal = 2
    Fast = 3

class TacticSkillUse(IntEnum):
    None_ = 0
    Auto = 1
    Manual = 2

class ShowSkillCutIn(IntEnum):
    None_ = 0
    Once = 1
    Always = 2

class BattleCalculationStat(IntEnum):
    FinalDamage = 0
    FinalHeal = 1
    FinalDamageRatio = 2
    FinalDamageRatio2 = 3
    FinalCriticalRate = 4

class StatTransType(IntEnum):
    SpecialTransStat = 0
    TSATransStat = 1

class BattleDialogType(IntEnum):
    Talk = 0
    Think = 1
    Shout = 2

class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2
    Obstacle = 3
    TimeAttack = 4

class GrowthCategory(IntEnum):
    None_ = 0
    LevelUp = 1
    Transcend = 2
    SkillLevelUp = 3

class StatType(IntEnum):
    None_ = 0
    MaxHP = 1
    AttackPower = 2
    DefensePower = 3
    HealPower = 4
    AccuracyPoint = 5
    AccuracyRate = 6
    DodgePoint = 7
    DodgeRate = 8
    CriticalPoint = 9
    CriticalChanceRate = 10
    CriticalResistChanceRate = 11
    CriticalDamageRate = 12
    MoveSpeed = 13
    SightRange = 14
    ActiveGauge = 15
    StabilityPoint = 16
    StabilityRate = 17
    ReloadTime = 18
    MaxBulletCount = 19
    IgnoreDelayCount = 20
    WeaponRange = 21
    BlockRate = 22
    BodyRadius = 23
    ActionCount = 24
    StrategyMobility = 25
    StrategySightRange = 26
    StreetBattleAdaptation = 27
    OutdoorBattleAdaptation = 28
    IndoorBattleAdaptation = 29
    HealEffectivenessRate = 30
    CriticalChanceResistPoint = 31
    CriticalDamageResistRate = 32
    LifeRecoverOnHit = 33
    NormalAttackSpeed = 34
    AmmoCost = 35
    GroggyGauge = 36
    GroggyTime = 37
    DamageRatio = 38
    DamagedRatio = 39
    OppressionPower = 40
    OppressionResist = 41
    RegenCost = 42
    InitialWeaponRangeRate = 43
    DefensePenetration = 44
    DefensePenetrationResisit = 45
    ExtendBuffDuration = 46
    ExtendDebuffDuration = 47
    ExtendCrowdControlDuration = 48
    EnhanceExplosionRate = 49
    EnhancePierceRate = 50
    EnhanceMysticRate = 51
    EnhanceLightArmorRate = 52
    EnhanceHeavyArmorRate = 53
    EnhanceUnarmedRate = 54
    EnhanceSiegeRate = 55
    EnhanceNormalRate = 56
    EnhanceStructureRate = 57
    EnhanceNormalArmorRate = 58
    DamageRatio2Increase = 59
    DamageRatio2Decrease = 60
    DamagedRatio2Increase = 61
    DamagedRatio2Decrease = 62
    EnhanceSonicRate = 63
    EnhanceElasticArmorRate = 64
    ExDamagedRatioIncrease = 65
    ExDamagedRatioDecrease = 66
    EnhanceExDamageRate = 67
    ReduceExDamagedRate = 68
    HealRate = 69
    HealLightArmorRate = 70
    HealHeavyArmorRate = 71
    HealUnarmedRate = 72
    HealElasticArmorRate = 73
    HealNormalArmorRate = 74
    HealedExplosionRate = 75
    HealedPierceRate = 76
    HealedMysticRate = 77
    HealedSonicRate = 78
    HealedNormalRate = 79
    Max = 80

class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3

class TacticRole(IntEnum):
    None_ = 0
    DamageDealer = 1
    Tanker = 2
    Supporter = 3
    Healer = 4
    Vehicle = 5

class TacticRange(IntEnum):
    Back = 0
    Front = 1
    Middle = 2

class CVCollectionType(IntEnum):
    CVNormal = 0
    CVEvent = 1
    CVEtc = 2

class CVPrintType(IntEnum):
    CharacterOverwrite = 0
    PrefabOverwrite = 1
    Add = 2

class CVExceptionTarget(IntEnum):
    CharacterId = 0
    SquadType = 1

class PotentialStatBonusRateType(IntEnum):
    None_ = 0
    MaxHP = 1
    AttackPower = 2
    HealPower = 3

class ClanSocialGrade(IntEnum):
    None_ = 0
    President = 1
    Manager = 2
    Member = 3
    Applicant = 4
    Refused = 5
    Kicked = 6
    Quit = 7
    VicePredisident = 8

class ClanJoinOption(IntEnum):
    Free = 0
    Permission = 1
    All = 2

class ClanSearchOption(IntEnum):
    Name = 0
    Id = 1

class ClanRewardType(IntEnum):
    None_ = 0
    AssistTerm = 1
    AssistRent = 2
    Attendance = 3

class ConquestEnemyType(IntEnum):
    None_ = 0
    Normal = 1
    MiddleBoss = 2
    Boss = 3
    UnexpectedEvent = 4
    Challenge = 5
    IndividualErosion = 6
    MassErosion = 7

class ConquestTeamType(IntEnum):
    None_ = 0
    Team1 = 1
    Team2 = 2
    Team3 = 3

class ConquestTileType(IntEnum):
    None_ = 0
    Start = 1
    Normal = 2
    Battle = 3
    Base = 4

class ConquestObjectType(IntEnum):
    None_ = 0
    ParcelOneTimePerAccount = 1

class ConquestItemType(IntEnum):
    None_ = 0
    EventPoint = 1
    EventToken1 = 2
    EventToken2 = 3
    EventToken3 = 4
    EventToken4 = 5
    EventToken5 = 6

class ConquestProgressType(IntEnum):
    None_ = 0
    Upgrade = 1
    Manage = 2

class TileState(IntEnum):
    None_ = 0
    PartiallyConquested = 1
    FullyConquested = 2

class ConquestEventType(IntEnum):
    None_ = 0
    Event01 = 1
    Event02 = 2

class ConquestConditionType(IntEnum):
    None_ = 0
    OpenDateOffset = 1
    ItemAcquire = 2
    ParcelUse = 3
    KillUnit = 4

class ConquestErosionType(IntEnum):
    None_ = 0
    IndividualErosion = 1
    MassErosion = 2

class ContentType(IntEnum):
    None_ = 0
    CampaignMainStage = 1
    CampaignSubStage = 2
    WeekDungeon = 3
    EventContentMainStage = 4
    EventContentSubStage = 5
    CampaignTutorialStage = 6
    EventContentMainGroundStage = 7
    SchoolDungeon = 8
    TimeAttackDungeon = 9
    Raid = 10
    Conquest = 11
    EventContentStoryStage = 12
    CampaignExtraStage = 13
    StoryStrategyStage = 14
    ScenarioMode = 15
    EventContent = 16
    WorldRaid = 17
    EliminateRaid = 18
    Chaser = 19
    FieldContentStage = 20
    MultiFloorRaid = 21
    MinigameDefense = 22

class EventContentType(IntEnum):
    Stage = 0
    Gacha = 1
    Mission = 2
    Shop = 3
    Raid = 4
    Arena = 5
    BoxGacha = 6
    Collection = 7
    Recollection = 8
    MiniGameRhythm = 9
    CardShop = 10
    EventLocation = 11
    MinigameRhythmEvent = 12
    FortuneGachaShop = 13
    SubEvent = 14
    EventMeetup = 15
    BoxGachaResult = 16
    Conquest = 17
    WorldRaid = 18
    DiceRace = 19
    MiniGameRhythmMission = 20
    WorldRaidEntrance = 21
    MiniEvent = 22
    MiniGameShooting = 23
    MiniGameShootingMission = 24
    MiniGameTBG = 25
    TimeAttackDungeon = 26
    EliminateRaid = 27
    Treasure = 28
    Field = 29
    MultiFloorRaid = 30
    MinigameDreamMaker = 31
    MiniGameDefense = 32
    OpenWebView = 33
    SpecialMiniEvent = 34
    ScenarioCollection = 35
    ScenarioShortcut = 36
    SeasonalEvent = 37
    MiniShop = 38
    MiniGameRoad = 39

class OpenCondition(IntEnum):
    Hide = 0
    Lock = 1
    Open = 2

class ResetContentType(IntEnum):
    None_ = 0
    HardStagePlay = 1
    StarategyMapHeal = 2
    ShopRefresh = 3
    ArenaDefenseVictoryReward = 4
    WeeklyMasterCoin = 5
    WorldRaidGemEnterCount = 6
    ConquestDailyErosionCheck = 7
    MiniEventToken = 8

class WeekDungeonType(IntEnum):
    None_ = 0
    ChaserA = 1
    ChaserB = 2
    ChaserC = 3
    FindGift = 4
    Blood = 5

class StarGoalType(IntEnum):
    None_ = 0
    AllAlive = 1
    Clear = 2
    GetBoxes = 3
    ClearTimeInSec = 4
    AllyBaseDamage = 5

class OpenConditionContent(IntEnum):
    Shop = 0
    Gacha = 1
    LobbyIllust = 2
    Raid = 3
    Cafe = 4
    Unit_Growth_Skill = 5
    Unit_Growth_LevelUp = 6
    Unit_Growth_Transcendence = 7
    Arena = 8
    Academy = 9
    Equip = 10
    Item = 11
    Favor = 12
    Prologue = 13
    Mission = 14
    WeekDungeon_Chase = 15
    __Deprecated_WeekDungeon_FindGift = 16
    __Deprecated_WeekDungeon_Blood = 17
    Story_Sub = 18
    Story_Replay = 19
    WeekDungeon = 20
    None_ = 21
    Shop_Gem = 22
    Craft = 23
    Student = 24
    GuideMission = 25
    Clan = 26
    Echelon = 27
    Campaign = 28
    EventContent = 29
    Guild = 30
    EventStage_1 = 31
    EventStage_2 = 32
    Talk = 33
    Billing = 34
    Schedule = 35
    Story = 36
    Tactic_Speed = 37
    Cafe_Invite = 38
    EventMiniGame_1 = 39
    SchoolDungeon = 40
    TimeAttackDungeon = 41
    ShiftingCraft = 42
    WorldRaid = 43
    Tactic_Skip = 44
    Mulligan = 45
    EventPermanent = 46
    Main_L_1_2 = 47
    Main_L_1_3 = 48
    Main_L_1_4 = 49
    EliminateRaid = 50
    Cafe_2 = 51
    Cafe_Invite_2 = 52
    MultiFloorRaid = 53
    StrategySkip = 54
    MinigameDreamMaker = 55
    MiniGameDefense = 56

class ContentLockType(IntEnum):
    None_ = 0
    NotUseControlledByOtherSetting = 1
    Academy = 2
    MultiFloorRaid = 3
    EventContent = 4
    EventNotice = 5
    GuideMission = 6
    Campaign = 7
    Story = 8
    WeekDungeon_Chase = 9
    WeekDungeon = 10
    SchoolDungeon = 11
    Raid = 12
    EliminateRaid = 13
    TimeAttackDungeon = 14
    Arena = 15
    Cafe = 16
    GemShop = 17
    Gacha = 18
    Craft = 19
    MomoTalk = 20

class TutorialFailureContentType(IntEnum):
    None_ = 0
    Campaign = 1
    WeekDungeon = 2
    Raid = 3
    TimeAttackDungeon = 4
    WorldRaid = 5
    Conquest = 6
    EliminateRaid = 7
    MultiFloorRaid = 8

class FeverBattleType(IntEnum):
    Campaign = 0
    Raid = 1
    WeekDungeon = 2
    Arena = 3

class EventContentScenarioConditionType(IntEnum):
    None_ = 0
    DayAfter = 1
    EventPoint = 2

class EventTargetType(IntEnum):
    WeekDungeon = 0
    Chaser = 1
    Campaign_Normal = 2
    Campaign_Hard = 3
    SchoolDungeon = 4
    AcademySchedule = 5
    TimeAttackDungeon = 6
    AccountLevelExpIncrease = 7
    Raid = 8
    EliminateRaid = 9
    MultiFloorRaid = 10

class ContentResultType(IntEnum):
    Failure = 0
    Success = 1

class EventContentItemType(IntEnum):
    EventPoint = 0
    EventToken1 = 1
    EventToken2 = 2
    EventToken3 = 3
    EventToken4 = 4
    EventToken5 = 5
    EventMeetUpTicket = 6
    EventEtcItem = 7

class RaidSeasonType(IntEnum):
    None_ = 0
    Open = 1
    Close = 2
    Settlement = 3

class BuffConditionType(IntEnum):
    All = 0
    Character = 1
    School = 2
    Weapon = 3

class CollectionUnlockType(IntEnum):
    None_ = 0
    ClearSpecificEventStage = 1
    ClearSpecificEventScenario = 2
    ClearSpecificEventMission = 3
    PurchaseSpecificItemCount = 4
    SpecificEventLocationRank = 5
    DiceRaceConsumeDiceCount = 6
    MinigameTBGThemaClear = 7
    MinigameEnter = 8
    MinigameDreamMakerParameter = 9
    ClearSpecificScenario = 10

class ShortcutContentType(IntEnum):
    None_ = 0
    CampaignStage = 1
    EventStage = 2
    Blood = 3
    WeekDungeon = 4
    Arena = 5
    Raid = 6
    Shop = 7
    ItemInventory = 8
    Craft = 9
    SchoolDungeon = 10
    Academy = 11
    Mission = 12
    MultiFloorRaid = 13

class JudgeGrade(IntEnum):
    None_ = 0
    Miss = 1
    Attack = 2
    Critical = 3

class SchoolDungeonType(IntEnum):
    SchoolA = 0
    SchoolB = 1
    SchoolC = 2
    None_ = 3

class EventContentBuffFindRule(IntEnum):
    None_ = 0
    WeaponType = 1
    SquadType = 2
    StreetBattleAdaptation = 3
    OutdoorBattleAdaptation = 4
    IndoorBattleAdaptation = 5
    BulletType = 6
    School = 7
    TacticRange = 8

class TimeAttackDungeonRewardType(IntEnum):
    Fixed = 0
    TimeWeight = 1

class TimeAttackDungeonType(IntEnum):
    None_ = 0
    Defense = 1
    Shooting = 2
    Destruction = 3
    Escort = 4

class SuddenMissionContentType(IntEnum):
    OrdinaryState = 0
    CampaignNormalStage = 1
    CampaignHardStage = 2
    EventStage = 3
    WeekDungeon = 4
    Chaser = 5
    SchoolDungeon = 6
    TimeAttackDungeon = 7
    Raid = 8

class ContentsChangeType(IntEnum):
    None_ = 0
    WorldRaidBossDamageRatio = 1
    WorldRaidBossGroupDate = 2

class EventNotifyType(IntEnum):
    RewardIncreaseEvent = 0
    AccountExpIncreaseEvent = 1
    RaidSeasonManager = 2
    TimeAttackDungeonSeasonManage = 3
    EliminateRaidSeasonManage = 4
    MultiFloorRaidSeasonManage = 5

class EventContentDiceRaceResultType(IntEnum):
    DiceResult1 = 0
    DiceResult2 = 1
    DiceResult3 = 2
    DiceResult4 = 3
    DiceResult5 = 4
    DiceResult6 = 5
    MoveForward = 6
    LapFinish = 7
    EventOccur = 8
    DiceResultFixed1 = 9
    DiceResultFixed2 = 10
    DiceResultFixed3 = 11
    DiceResultFixed4 = 12
    DiceResultFixed5 = 13
    DiceResultFixed6 = 14
    SpecialReward = 15

class EventContentDiceRaceNodeType(IntEnum):
    StartNode = 0
    RewardNode = 1
    MoveForwardNode = 2
    SpecialRewardNode = 3

class MeetupConditionType(IntEnum):
    None_ = 0
    EventContentStageClear = 1
    ScenarioClear = 2

class MeetupConditionPrintType(IntEnum):
    None_ = 0
    Lock = 1
    Hide = 2

class GuideMissionTabType(IntEnum):
    None_ = 0
    Daily = 1
    StageClear = 2

class RankingSearchType(IntEnum):
    None_ = 0
    Rank = 1
    Score = 2

class EventContentReleaseType(IntEnum):
    None_ = 0
    Permanent = 1
    MainStory = 2
    PermanentSpecialOperate = 3
    PermanentConquest = 4

class CraftSlotIndex(IntEnum):
    Slot00 = 0
    Slot01 = 1
    Slot02 = 2
    Max = 3

class CraftNodeTier(IntEnum):
    Base = 0
    Node01 = 1
    Node02 = 2
    Node03 = 3
    Max = 4

class SubEventType(IntEnum):
    None_ = 0
    SubEvent = 1
    SubEventPermanent = 2

class EquipmentCategory(IntEnum):
    Unable = 0
    Exp = 1
    Bag = 2
    Hat = 3
    Gloves = 4
    Shoes = 5
    Badge = 6
    Hairpin = 7
    Charm = 8
    Watch = 9
    Necklace = 10
    WeaponExpGrowthA = 11
    WeaponExpGrowthB = 12
    WeaponExpGrowthC = 13
    WeaponExpGrowthZ = 14

class EquipmentOptionType(IntEnum):
    None_ = 0
    MaxHP_Base = 1
    MaxHP_Coefficient = 2
    AttackPower_Base = 3
    AttackPower_Coefficient = 4
    DefensePower_Base = 5
    DefensePower_Coefficient = 6
    HealPower_Base = 7
    HealPower_Coefficient = 8
    CriticalPoint_Base = 9
    CriticalPoint_Coefficient = 10
    CriticalChanceRate_Base = 11
    CriticalDamageRate_Base = 12
    CriticalDamageRate_Coefficient = 13
    SightRange_Base = 14
    SightRange_Coefficient = 15
    MaxBulletCount_Base = 16
    MaxBulletCount_Coefficient = 17
    HPRecoverOnKill_Base = 18
    HPRecoverOnKill_Coefficient = 19
    StreetBattleAdaptation_Base = 20
    OutdoorBattleAdaptation_Base = 21
    IndoorBattleAdaptation_Base = 22
    HealEffectivenessRate_Base = 23
    HealEffectivenessRate_Coefficient = 24
    CriticalChanceResistPoint_Base = 25
    CriticalChanceResistPoint_Coefficient = 26
    CriticalDamageResistRate_Base = 27
    CriticalDamageResistRate_Coefficient = 28
    ExSkillUpgrade = 29
    OppressionPower_Base = 30
    OppressionPower_Coefficient = 31
    OppressionResist_Base = 32
    OppressionResist_Coefficient = 33
    StabilityPoint_Base = 34
    StabilityPoint_Coefficient = 35
    AccuracyPoint_Base = 36
    AccuracyPoint_Coefficient = 37
    DodgePoint_Base = 38
    DodgePoint_Coefficient = 39
    MoveSpeed_Base = 40
    MoveSpeed_Coefficient = 41
    Max = 42
    NormalAttackSpeed_Base = 43
    NormalAttackSpeed_Coefficient = 44
    DefensePenetration_Base = 45
    DefensePenetrationResisit_Base = 46
    ExtendBuffDuration_Base = 47
    ExtendDebuffDuration_Base = 48
    ExtendCrowdControlDuration_Base = 49
    EnhanceExplosionRate_Base = 50
    EnhanceExplosionRate_Coefficient = 51
    EnhancePierceRate_Base = 52
    EnhancePierceRate_Coefficient = 53
    EnhanceMysticRate_Base = 54
    EnhanceMysticRate_Coefficient = 55
    EnhanceLightArmorRate_Base = 56
    EnhanceLightArmorRate_Coefficient = 57
    EnhanceHeavyArmorRate_Base = 58
    EnhanceHeavyArmorRate_Coefficient = 59
    EnhanceUnarmedRate_Base = 60
    EnhanceUnarmedRate_Coefficient = 61
    EnhanceSiegeRate_Base = 62
    EnhanceSiegeRate_Coefficient = 63
    EnhanceNormalRate_Base = 64
    EnhanceNormalRate_Coefficient = 65
    EnhanceStructureRate_Base = 66
    EnhanceStructureRate_Coefficient = 67
    EnhanceNormalArmorRate_Base = 68
    EnhanceNormalArmorRate_Coefficient = 69
    DamageRatio2Increase_Base = 70
    DamageRatio2Increase_Coefficient = 71
    DamageRatio2Decrease_Base = 72
    DamageRatio2Decrease_Coefficient = 73
    DamagedRatio2Increase_Base = 74
    DamagedRatio2Increase_Coefficient = 75
    DamagedRatio2Decrease_Base = 76
    DamagedRatio2Decrease_Coefficient = 77
    EnhanceSonicRate_Base = 78
    EnhanceSonicRate_Coefficient = 79
    EnhanceElasticArmorRate_Base = 80
    EnhanceElasticArmorRate_Coefficient = 81
    IgnoreDelayCount_Base = 82
    WeaponRange_Base = 83
    BlockRate_Base = 84
    BlockRate_Coefficient = 85
    AmmoCost_Base = 86
    RegenCost_Base = 87
    RegenCost_Coefficient = 88

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class Language(IntEnum):
    Kr = 0
    Jp = 1
    Th = 2
    Tw = 3
    En = 4

class SoundType(IntEnum):
    UI = 0
    BGM = 1
    FX = 2

class WeekDay(IntEnum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    All = 7

class EchelonType(IntEnum):
    None_ = 0
    Adventure = 1
    Raid = 2
    ArenaAttack = 3
    ArenaDefence = 4
    WeekDungeonChaserA = 5
    Scenario = 6
    WeekDungeonBlood = 7
    WeekDungeonChaserB = 8
    WeekDungeonChaserC = 9
    WeekDungeonFindGift = 10
    EventContent = 11
    SchoolDungeonA = 12
    SchoolDungeonB = 13
    SchoolDungeonC = 14
    TimeAttack = 15
    WorldRaid = 16
    Conquest = 17
    ConquestManage = 18
    StoryStrategyStage = 19
    EliminateRaid01 = 20
    EliminateRaid02 = 21
    EliminateRaid03 = 22
    Field = 23
    MultiFloorRaid = 24
    MinigameDefense = 25

class EchelonExtensionType(IntEnum):
    Base = 0
    Extension = 1

class NoticeType(IntEnum):
    None_ = 0
    Notice = 1
    Event = 2

class RewardTag(IntEnum):
    Default = 0
    FirstClear = 1
    StrategyObject = 2
    Event = 3
    ThreeStar = 4
    ProductMonthly = 5
    Rare = 6
    EventBonus = 7
    TimeWeight = 8
    ProductWeekly = 9
    ProductBiweekly = 10
    EventPermanentReward = 11
    ConquestManageEvent = 12
    ConquestManageDefault = 13
    ConquestCalculateDefault = 14
    ConquestCalculateLevel2 = 15
    ConquestCalculateLevel3 = 16
    ConquestFootholdUpgrade2 = 17
    ConquestFootholdUpgrade3 = 18
    ConquestErosionPenalty = 19
    GemBonus = 20
    GemPaid = 21
    ConquestTileConquer = 22

class ArenaRewardType(IntEnum):
    None_ = 0
    Time = 1
    Daily = 2
    SeasonRecord = 3
    OverallRecord = 4
    SeasonClose = 5
    AttackVictory = 6
    DefenseVictory = 7
    RankIcon = 8

class ServiceActionType(IntEnum):
    ClanCreate = 0
    HardAdventurePlayCountRecover = 1

class RaidStatus(IntEnum):
    None_ = 0
    Playing = 1
    Clear = 2
    Close = 3

class WebAPIErrorLevel(IntEnum):
    None_ = 0
    Warning = 1
    Error = 2

class GachaTicketType(IntEnum):
    None_ = 0
    PackageThreeStar = 1
    ThreeStar = 2
    TwoStar = 3
    Normal = 4
    NormalOnce = 5
    SelectRecruit = 6
    PackagePropertyThreeStar = 7
    Temp_1 = 8
    PackageAcademyThreeStar = 9

class EventChangeType(IntEnum):
    MainSub = 0
    SubMain = 1

class CafeCharacterState(IntEnum):
    None_ = 0
    Idle = 1
    Walk = 2
    Reaction = 3
    Interaction = 4
    Max = 5

class FurnitureFunctionType(IntEnum):
    None_ = 0
    EventCollection = 1
    VideoPlay = 2
    TrophyCollection = 3
    InteractionBGMPlay = 4

class NotificationEventReddot(IntEnum):
    StagePointReward = 0
    MissionComplete = 1
    MiniGameMissionComplete = 2
    WorldRaidReward = 3
    ConquestCalculateReward = 4
    DiceRaceLapReward = 5

class EmblemCategory(IntEnum):
    None_ = 0
    Default = 1
    Mission = 2
    GroupStory = 3
    Event = 4
    MainStory = 5
    Favor = 6
    Boss = 7
    Etc = 8
    Etc_Anniversary = 9
    MultiFloorRaid = 10
    Potential = 11

class EmblemDisplayType(IntEnum):
    Always = 0
    Time = 1
    Favor = 2
    Potential = 3

class EmblemCheckPassType(IntEnum):
    None_ = 0
    Default = 1
    Favor = 2
    Story = 3
    Potential = 4

class StickerGetConditionType(IntEnum):
    None_ = 0
    StickerCheckPass = 1
    GetStickerCondition = 2

class Nation(IntEnum):
    None_ = 0
    All = 1
    JP = 2
    GL = 3
    KR = 4

class FilterCategory(IntEnum):
    Character = 0
    Equipment = 1
    Item = 2
    Craft = 3
    ShiftCraft = 4
    Shop = 5
    MemoryLobby = 6
    Trophy = 7
    Emblem = 8

class FilterIcon(IntEnum):
    TextOnly = 0
    TextWithIcon = 1
    Pin = 2
    Role = 3
    CharacterStar = 4
    WeaponStar = 5
    Attack = 6
    Defense = 7
    Range = 8
    MemoryLobby = 9
    Obscuration = 10

class CVUnlockScenarioType(IntEnum):
    Main = 0
    Event = 1
    SpecialOperation = 2

class FieldConditionType(IntEnum):
    Invalid = 0
    Interaction = 1
    QuestInProgress = 2
    QuestClear = 3
    Date = 4
    StageClear = 5
    HasKeyword = 6
    HasEvidence = 7
    OpenDate = 8
    OpenDateAfter = 9

class FieldInteractionType(IntEnum):
    None_ = 0
    Scenario = 1
    Reward = 2
    Dialog = 3
    Stage = 4
    KeywordFound = 5
    EvidenceFound = 6
    SceneChange = 7
    Timeline = 8
    ActionTrigger = 9
    Interplay = 10
    UnderCoverStage = 11

class FieldConditionClass(IntEnum):
    AndOr = 0
    OrAnd = 1
    Multi = 2

class FieldDialogType(IntEnum):
    None_ = 0
    Talk = 1
    Think = 2
    Exclaim = 3
    Question = 4
    Upset = 5
    Surprise = 6
    Bulb = 7
    Heart = 8
    Sweat = 9
    Angry = 10
    Music = 11
    Dot = 12
    Momotalk = 13
    Phone = 14
    Keyword = 15
    Evidence = 16
    Chat = 17
    Keyword_843 = 18

class FieldTutorialType(IntEnum):
    None_ = 0
    MasteryHUD = 1
    QuestHUD = 2
    WorldMapHUD = 3

class FieldWorldMapButtonType(IntEnum):
    DefaultMode = 0
    Normal = 1
    Combat = 2
    Combat_VeryHard = 3
    UnderCover = 4

class FriendSearchLevelOption(IntEnum):
    Recommend = 0
    All = 1
    Level1To30 = 2
    Level31To40 = 3
    Level41To50 = 4
    Level51To60 = 5
    Level61To70 = 6
    Level71To80 = 7
    Level81To90 = 8
    Level91To100 = 9

class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    InvisibleToken = 8

class MailType(IntEnum):
    System = 0
    Attendance = 1
    Event = 2
    MassTrade = 3
    InventoryFull = 4
    ArenaDefenseVictory = 5
    CouponUsageReward = 6
    ArenaSeasonClose = 7
    ProductReward = 8
    MonthlyProductReward = 9
    ExpiryChangeItem = 10
    ClanAttendance = 11
    AccountLink = 12
    NewUserBonus = 13
    LeftClanAssistReward = 14
    AttendanceImmediately = 15
    WeeklyProductReward = 16
    BiweeklyProductReward = 17
    Temp_1 = 18
    Temp_2 = 19
    Temp_3 = 20
    CouponCompleteReward = 21
    BirthdayMail = 22
    FromCS = 23
    ExpiryChangeCurrency = 24

class AttendanceType(IntEnum):
    Basic = 0
    Event = 1
    Newbie = 2
    EventCountDown = 3
    Event20Days = 4

class AttendanceCountRule(IntEnum):
    Accumulation = 0
    Date = 1

class AttendanceResetType(IntEnum):
    User = 0
    Server = 1

class MailSortingRule(IntEnum):
    ReceiptDate = 0
    ExpireDate = 1

class DreamMakerMultiplierCondition(IntEnum):
    None_ = 0
    Round = 1
    CollectionCount = 2
    EndingCount = 3

class DreamMakerParameterType(IntEnum):
    None_ = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4

class DreamMakerResult(IntEnum):
    None_ = 0
    Fail = 1
    Success = 2
    Perfect = 3

class DreamMakerParamOperationType(IntEnum):
    None_ = 0
    GrowUpHigh = 1
    GrowUp = 2
    GrowDownHigh = 3
    GrowDown = 4

class DreamMakerEndingCondition(IntEnum):
    None_ = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4
    Round = 5
    CollectionCount = 6

class DreamMakerVoiceCondition(IntEnum):
    None_ = 0
    Fail = 1
    Success = 2
    Perfect = 3
    DailyResult = 4

class DreamMakerEndingType(IntEnum):
    None_ = 0
    Normal = 1
    Special = 2

class DreamMakerEndingRewardType(IntEnum):
    None_ = 0
    FirstEndingReward = 1
    LoopEndingReward = 2

class RoadPuzzleMapTileType(IntEnum):
    None_ = 0
    Start = 1
    End = 2
    Transit = 3
    Obstacle = 4
    Empty = 5

class RoadPuzzleRailTileType(IntEnum):
    None_ = 0
    Straight = 1
    CurveBig = 2
    CurveSmall = 3

class RoadPuzzleVoiceCondition(IntEnum):
    None_ = 0
    TrainDepart = 1
    RailConnectSuccess = 2
    SaveSuccess = 3

class Geas(IntEnum):
    ForwardProjectile = 0
    DiagonalProjectile = 1
    SideProjectile = 2
    Pierce = 3
    Reflect = 4
    Burn = 5
    Chill = 6
    AttackPower = 7
    AttackSpeed = 8
    Critical = 9
    Heal = 10
    MoveSpeed = 11
    LifeSteal = 12
    Evasion = 13

class TBGObjectType(IntEnum):
    None_ = 0
    EnemyBoss = 1
    EnemyMinion = 2
    Random = 3
    Facility = 4
    TreasureBox = 5
    Start = 6
    Portal = 7

class TBGOptionSuccessType(IntEnum):
    None_ = 0
    TBGItemAcquire = 1
    ItemAcquire = 2
    TBGDiceAcquire = 3
    Portal = 4

class TBGItemType(IntEnum):
    None_ = 0
    Dice = 1
    Heal = 2
    HealExpansion = 3
    Defence = 4
    Guide = 5
    DiceResultValue = 6
    DefenceCritical = 7
    DiceResultConfirm = 8

class TBGItemEffectType(IntEnum):
    None_ = 0
    PermanentContinuity = 1
    TemporaryContinuation = 2
    Immediately = 3

class TBGTileType(IntEnum):
    None_ = 0
    Start = 1
    Movable = 2
    UnMovable = 3

class TBGThemaType(IntEnum):
    None_ = 0
    Normal = 1
    Hidden = 2

class TBGPortalCondition(IntEnum):
    None_ = 0
    ObjectAllEncounter = 1
    Round = 2

class TBGProbModifyCondition(IntEnum):
    None_ = 0
    AllyRevive = 1
    DicePlayFail = 2

class TBGVoiceCondition(IntEnum):
    None_ = 0
    DiceResultSuccess = 1
    DiceResultFailBattle = 2
    DiceResultFailRandom = 3
    EnemyDie = 4
    TreasureBoxNormal = 5
    TreasureBoxSpecial = 6
    FacilityResult = 7

class MiniGameTBGThemaRewardType(IntEnum):
    TreasureReward = 0
    EmptyTreasureReward = 1
    HiddenThemaTreasureReward = 2

class MissionCategory(IntEnum):
    Challenge = 0
    Daily = 1
    Weekly = 2
    Achievement = 3
    GuideMission = 4
    All = 5
    MiniGameScore = 6
    MiniGameEvent = 7
    EventAchievement = 8
    DailySudden = 9
    DailyFixed = 10
    EventFixed = 11

class MissionResetType(IntEnum):
    None_ = 0
    Daily = 1
    Weekly = 2
    Limit = 3

class MissionCompleteConditionType(IntEnum):
    None_ = 0
    Reset_DailyLogin = 1
    Reset_DailyLoginCount = 2
    Reset_CompleteMission = 3
    Achieve_EquipmentLevelUpCount = 4
    Achieve_EquipmentTierUpCount = 5
    Achieve_CharacterLevelUpCount = 6
    Reset_CharacterTranscendenceCount = 7
    Reset_ClearTaticBattleCount = 8
    Achieve_ClearCampaignStageCount = 9
    Reset_KillSpecificEnemyCount = 10
    Reset_KillEnemyWithTagCount = 11
    Reset_GetCharacterCount = 12
    Reset_GetCharacterWithTagCount = 13
    Reset_GetSpecificCharacterCount = 14
    Reset_AccountLevelUp = 15
    Reset_GetEquipmentCount = 16
    Reset_GachaCount = 17
    Reset_UseGem = 18
    Reset_GetGem = 19
    Reset_GetGemPaid = 20
    Achieve_GetGold = 21
    Achieve_GetItem = 22
    Reset_GetFavorLevel = 23
    Reset___Deprecated_EquipmentAtSpecificLevelCount = 24
    Reset_EquipmentAtSpecificTierUpCount = 25
    Reset_CharacterAtSpecificLevelCount = 26
    Reset_CharacterAtSpecificTranscendenceCount = 27
    Achieve_CharacterSkillLevelUpCount = 28
    Reset_CharacterAtSpecificSkillLevelCount = 29
    Reset_CompleteScheduleCount = 30
    Reset_CompleteScheduleGroupCount = 31
    Reset_AcademyLocationRankSum = 32
    Reset_CraftCount = 33
    Achieve_GetComfortPoint = 34
    Achieve_GetWeaponCount = 35
    Reset_EquipWeaponCount_Obsolete = 36
    Reset_CompleteScheduleWithSpecificCharacter = 37
    Reset_CafeInteractionCount = 38
    Reset_SpecificCharacterAtSpecificLevel = 39
    Reset_SpecificCharacterAtSpecificTranscendence = 40
    Reset_LobbyInteraction = 41
    Achieve_ClearFindGiftAndBloodDungeonCount = 42
    Reset_ClearSpecificFindGiftAndBloodDungeonCount = 43
    Achieve_JoinRaidCount = 44
    Reset_JoinSpecificRaidCount = 45
    Achieve_JoinArenaCount = 46
    Reset_ArenaVictoryCount = 47
    Reset_RaidDamageAmountOnOneBattle = 48
    Reset_ClearEventStageCount = 49
    Reset_UseSpecificCharacterCount = 50
    Achieve_UseGold = 51
    Reset_UseTiket = 52
    Reset_ShopBuyCount = 53
    Reset_ShopBuyActionPointCount = 54
    Reset_SpecificCharacterAtSpecificFavorRank = 55
    Reset_ClearSpecificScenario = 56
    Reset_GetSpecificItemCount = 57
    Achieve_TotalGetClearStarCount = 58
    Reset_CompleteCampaignStageMinimumTurn = 59
    Achieve_TotalLoginCount = 60
    Reset_LoginAtSpecificTime = 61
    Reset_CompleteFavorSchedule = 62
    Reset_CompleteFavorScheduleAtSpecificCharacter = 63
    Reset_GetMemoryLobbyCount = 64
    Reset_GetFurnitureGroupCount = 65
    Reset_AcademyLocationAtSpecificRank = 66
    Reset_ClearCampaignStageDifficultyNormal = 67
    Reset_ClearCampaignStageDifficultyHard = 68
    Achieve_ClearChaserDungeonCount = 69
    Reset_ClearSpecificChaserDungeonCount = 70
    Reset_GetCafeRank = 71
    Reset_SpecificStarCharacterCount = 72
    Reset_EventClearCampaignStageCount = 73
    Reset_EventClearSpecificCampaignStageCount = 74
    Reset_EventCompleteCampaignStageMinimumTurn = 75
    Reset_EventClearCampaignStageDifficultyNormal = 76
    Reset_EventClearCampaignStageDifficultyHard = 77
    Reset_ClearSpecificCampaignStageCount = 78
    Reset_GetItemWithTagCount = 79
    Reset_GetFurnitureWithTagCount = 80
    Reset_GetEquipmentWithTagCount = 81
    Reset_ClearCampaignStageTimeLimitFromSecond = 82
    Reset_ClearEventStageTimeLimitFromSecond = 83
    Reset_ClearRaidTimeLimitFromSecond = 84
    Reset_ClearBattleWithTagCount = 85
    Reset_ClearFindGiftAndBloodDungeonTimeLimitFromSecond = 86
    Reset_CompleteScheduleWithTagCount = 87
    Reset_ClearChaserDungeonTimeLimitFromSecond = 88
    Reset_GetTotalScoreRhythm = 89
    Reset_GetBestScoreRhythm = 90
    Reset_GetSpecificScoreRhythm = 91
    Reset_ClearStageRhythm = 92
    Reset_GetComboCountRhythm = 93
    Reset_GetFullComboRhythm = 94
    Reset_GetFeverCountRhythm = 95
    Reset_UseActionPoint = 96
    Achieve_ClearSchoolDungeonCount = 97
    Reset_ClearSchoolDungeonTimeLimitFromSecond = 98
    Reset_ClearSpecificSchoolDungeonCount = 99
    Reset_GetCriticalCountRhythm = 100
    Achieve_WeaponTranscendenceCount = 101
    Achieve_WeaponLevelUpCount = 102
    Reset_WeaponAtSpecificTranscendenceCount = 103
    Reset_WeaponAtSpecificLevelUpCount = 104
    Reset_BuyShopGoods = 105
    Reset_ClanLogin = 106
    Reset_AssistCharacterSetting = 107
    Reset_DailyMissionFulfill = 108
    Reset_SelectedMissionFulfill = 109
    Reset_TotalDamageToWorldRaid = 110
    Reset_JoinWorldRaidTypeNumber = 111
    Reset_JoinWorldRaidBattleWithTagCount = 112
    Reset_ClearWorldRaidTimeLimitFromSecond = 113
    Achieve_KillEnemyWithDecagrammatonSPOTagCount = 114
    Reset_ConquerTileCount = 115
    Reset_ConquerSpecificStepTileCount = 116
    Reset_ConquerSpecificStepTileAll = 117
    Reset_UpgradeConquestBaseTileCount = 118
    Reset_KillConquestBoss = 119
    Reset_ClearEventConquestTileTimeLimitFromSecond = 120
    Reset_DiceRaceUseDiceCount = 121
    Reset_DiceRaceFinishLapCount = 122
    Reset_FortuneGachaCount = 123
    Reset_FortuneGachaCountByGrade = 124
    Reset_ClearCountShooting = 125
    Reset_ClearSpecificStageShooting = 126
    Reset_ClearSpecificCharacterShooting = 127
    Reset_ClearSpecificSectionShooting = 128
    Achieve_JoinEliminateRaidCount = 129
    Reset_TBGCompleteRoundCount = 130
    Reset_CompleteStage = 131
    Reset_TBGClearSpecificThema = 132
    Reset_ClearGeneralChaserDungeonCount = 133
    Reset_ClearGeneralFindGiftAndBloodDungeonCount = 134
    Reset_ClearGeneralSchoolDungeonCount = 135
    Reset_JoinArenaCount = 136
    Reset_GetCafe2ndRank = 137
    Achieve_GetComfort2ndPoint = 138
    Reset_ClearSpecificTimeAttackDungeonCount = 139
    Reset_GetScoreTimeAttackDungeon = 140
    Reset_GetTotalScoreTimeAttackDungeon = 141
    Reset_JoinRaidCount = 142
    Reset_ClearTimeAttackDungeonCount = 143
    Reset_JoinEliminateRaidCount = 144
    Reset_FieldClearSpecificDate = 145
    Reset_FieldGetEvidenceCount = 146
    Reset_FieldMasteryLevel = 147
    Reset_TreasureCheckedCellCount = 148
    Reset_TreasureGetTreasureCount = 149
    Reset_TreasureRoundRefreshCount = 150
    Achieve_UseTicketCount = 151
    Reset_ClearMultiFloorRaidStage = 152
    Achieve_CharacterPotentialUpCount = 153
    Reset_CharacterPotentialUpCount = 154
    Reset_CharacterAtSpecificPotentialCount = 155
    Reset_PotentialAttackPowerAtSpecificLevel = 156
    Reset_PotentialMaxHPAtSpecificLevel = 157
    Reset_PotentialHealPowerAtSpecificLevel = 158
    Reset_DreamGetSpecificParameter = 159
    Reset_DreamGetSpecificScheduleCount = 160
    Reset_DreamGetScheduleCount = 161
    Reset_DreamGetEndingCount = 162
    Reset_DreamGetSpecificEndingCount = 163
    Reset_DreamGetCollectionScenarioCount = 164
    Reset_ClearCountDefense = 165
    Reset_ClearSpecificDefenseStage = 166
    Reset_ClearCharacterLimitDefense = 167
    Reset_ClearTimeLimitDefenseFromSecond = 168
    Reset_JoinMultiFloorRaidCount = 169
    Reset_GivePresentCharacterCount = 170
    Reset_CharacterInviteCount = 171
    Reset_RoadpuzzleTileCount = 172
    Reset_ClearSpecificRoundRoadpuzzle = 173
    Reset_ClearCountRoadpuzzle = 174

class AccountAchievementType(IntEnum):
    TotalLoginCount = 0
    TotalGetClearStarCount = 1
    TotalCharacterLevelUpCount = 2
    TotalCharacterSkillLevelUpCount = 3
    TotalClearCampaignStageCount = 4
    TotalClearChaserDungeonCount = 5
    TotalClearFindGiftAndBloodDungeonCount = 6
    TotalEquipmentLevelUpCount = 7
    TotalEquipmentTierUpCount = 8
    MaxComfortPoint = 9
    TotalGetGold = 10
    TotalUseGold = 11
    TotalJoinArenaCount = 12
    TotalJoinRaidCount = 13
    TotalClearSchoolDungeonCount = 14
    TotalGetWeaponCount = 15
    TotalWeaponLevelUpCount = 16
    TotalWeaponTranscendenceCount = 17
    KillEnemyWithDecagrammatonSPOTagCount = 18
    EventPoint = 19
    ConquestCalculateReward = 20
    TotalJoinEliminateRaidCount = 21
    Cafe2MaxComfortPoint = 22
    TotalRaidTicketUseCount = 23
    TotalEliminateTicketUseCount = 24
    TotalCharacterPotentialUpCount = 25

class MissionToastDisplayConditionType(IntEnum):
    Always = 0
    Complete = 1
    Never = 2

class GetStickerConditionType(IntEnum):
    None_ = 0
    Reset_StikcerGetCondition_AccountLevel = 1
    Reset_StickerGetCondition_ScenarioModeId = 2
    Reset_StickerGetCondition_EnemyKillCount = 3
    Reset_StickerGetCondition_GetItemCount = 4
    Reset_StickerGetCondition_BuyItemCount = 5
    Reset_StickerGetCondition_ScheduleRank = 6
    Reset_StickerGetCondition_Change_LobbyCharacter = 7
    Reset_StickerGetCondition_Cafe_Character_Visit_Count = 8
    Reset_StickerGetCondition_Cafe_Chracter_Invite_Count = 9
    Reset_StickerGetCondition_GetChracterCount = 10
    Reset_StickerGetCondition_Cafe_Furniture_Interaction = 11
    Reset_StickerGetCondition_GetFurniture = 12
    Reset_StickerGetCondition_SetFurniture = 13
    Reset_StickerGetCondition_GivePresentChracterCount = 14
    Reset_StickerGetCondition_GivePresentCount = 15
    Reset_StickerGetCondition_MomotalkStudentCount = 16
    Reset_StickerGetCondition_CombatwithCharacterCount = 17
    Reset_StickerGetCondition_GachaCharacterCount = 18
    Reset_StickerGetCondition_TouchLobbyCharacter = 19
    Reset_StickerGetCondition_UseCircleEmoticonCount = 20
    Reset_StickerGetCondition_CraftCount = 21
    Reset_StickerGetCondition_NormalStageClear = 22
    Reset_StickerGetCondition_NormalStageClear3Star = 23
    Reset_StickerGetCondition_HardStageClear = 24
    Reset_StickerGetCondition_HardStageClear3Star = 25
    Achieve_StikcerGetCondition_AccountLevel = 26
    Achieve_StickerGetCondition_ClearStageId = 27
    Achieve_StickerGetCondition_ScenarioModeId = 28
    Achieve_StickerGetCondition_EnemyKillCount = 29
    Achieve_StickerGetCondition_GetItemCount = 30
    Achieve_StickerGetCondition_BuyItemCount = 31
    Achieve_StickerGetCondition_ScheduleRank = 32
    Achieve_StickerGetCondition_Change_LobbyCharacter = 33
    Achieve_StickerGetCondition_Cafe_Character_Visit_Count = 34
    Achieve_StickerGetCondition_Cafe_Chracter_Invite_Count = 35
    Achieve_StickerGetCondition_GetChracterCount = 36
    Achieve_StickerGetCondition_Cafe_Furniture_Interaction = 37
    Achieve_StickerGetCondition_GetFurniture = 38
    Achieve_StickerGetCondition_SetFurniture = 39
    Achieve_StickerGetCondition_GivePresentChracterCount = 40
    Achieve_StickerGetCondition_GivePresentCount = 41
    Achieve_StickerGetCondition_MomotalkStudentCount = 42
    Achieve_StickerGetCondition_CombatwithCharacterCount = 43
    Achieve_StickerGetCondition_GachaCharacterCount = 44
    Achieve_StickerGetCondition_TouchLobbyCharacter = 45
    Achieve_StickerGetCondition_UseCircleEmoticonCount = 46
    Achieve_StickerGetCondition_CraftCount = 47
    Achieve_StickerGetCondition_NormalStageClear = 48
    Achieve_StickerGetCondition_NormalStageClear3Star = 49
    Achieve_StickerGetCondition_HardStageClear = 50
    Achieve_StickerGetCondition_HardStageClear3Star = 51
    Reset_StickerGetCondition_EnemyKillCountbyTag = 52
    Reset_StickerGetCondition_GetItemCountbyTag = 53
    Reset_StickerGetCondition_ClearCampaignOrEventStageCount = 54
    Reset_StickerGetCondition_CompleteCampaignStageMinimumTurn = 55
    Reset_StickerGetCondition_ClearCampaignStageDifficultyNormal = 56
    Reset_StickerGetCondition_ClearCampaignStageDifficultyHard = 57
    Reset_StickerGetCondition_EventClearCampaignStageCount = 58
    Reset_StickerGetCondition_EventClearSpecificCampaignStageCount = 59
    Reset_StickerGetCondition_EventCompleteCampaignStageMinimumTurn = 60
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyNormal = 61
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyHard = 62
    Reset_StickerGetCondition_ClearSpecificCampaignStageCount = 63
    Reset_StickerGetCondition_ClearCampaignStageTimeLimitFromSecond = 64
    Reset_StickerGetCondition_ClearEventStageTimeLimitFromSecond = 65
    Reset_StickerGetCondition_ClearStageRhythm = 66
    Reset_StickerGetCondition_ClearSpecificStageShooting = 67
    Reset_StickerGetCondition_CompleteStage = 68
    Achieve_StickerGetCondition_ClearCampaignStageCount = 69
    Achieve_StickerGetCondition_ClearChaserDungeonCount = 70
    Reset_StickerGetCondition_ClearSpecificChaserDungeonCount = 71
    Achieve_StickerGetCondition_ClearSchoolDungeonCount = 72
    Reset_StickerGetCondition_ClearSpecificSchoolDungeonCount = 73
    Reset_StickerGetCondition_ClearSpecificWeekDungeonCount = 74
    Achieve_StickerGetCondition_ClearFindGiftAndBloodDungeonCount = 75

class StickerCheckPassType(IntEnum):
    None_ = 0
    ClearScenarioModeId = 1
    ClearCampaignStageId = 2

class ParcelType(IntEnum):
    None_ = 0
    Character = 1
    Currency = 2
    Equipment = 3
    Item = 4
    GachaGroup = 5
    Product = 6
    Shop = 7
    MemoryLobby = 8
    AccountExp = 9
    CharacterExp = 10
    FavorExp = 11
    TSS = 12
    Furniture = 13
    ShopRefresh = 14
    LocationExp = 15
    Recipe = 16
    CharacterWeapon = 17
    CharacterGear = 18
    IdCardBackground = 19
    Emblem = 20
    Sticker = 21
    Costume = 22
    PossessionCheck = 23

class Rarity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3

class Tier(IntEnum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3

class CurrencyTypes(IntEnum):
    Invalid = 0
    Gold = 1
    GemPaid = 2
    GemBonus = 3
    Gem = 4
    ActionPoint = 5
    AcademyTicket = 6
    ArenaTicket = 7
    RaidTicket = 8
    WeekDungeonChaserATicket = 9
    WeekDungeonFindGiftTicket = 10
    WeekDungeonBloodTicket = 11
    WeekDungeonChaserBTicket = 12
    WeekDungeonChaserCTicket = 13
    SchoolDungeonATicket = 14
    SchoolDungeonBTicket = 15
    SchoolDungeonCTicket = 16
    TimeAttackDungeonTicket = 17
    MasterCoin = 18
    WorldRaidTicketA = 19
    WorldRaidTicketB = 20
    WorldRaidTicketC = 21
    ChaserTotalTicket = 22
    SchoolDungeonTotalTicket = 23
    EliminateTicketA = 24
    EliminateTicketB = 25
    EliminateTicketC = 26
    EliminateTicketD = 27
    Max = 28

class SortingTarget(IntEnum):
    None_ = 0
    Rarity = 1
    Level = 2
    StarGrade = 3
    Tier = 4

class CurrencyOverChargeType(IntEnum):
    CanNotCharge = 0
    FitToLimit = 1
    ChargeOverLimit = 2

class CurrencyAdditionalChargeType(IntEnum):
    EnableAutoChargeOverLimit = 0
    DisableAutoChargeOverLimit = 1

class RecipeType(IntEnum):
    None_ = 0
    Craft = 1
    SkillLevelUp = 2
    CharacterTranscendence = 3
    EquipmentTierUp = 4
    CafeRankUp = 5
    SelectionItem = 6
    WeaponTranscendence = 7
    SelectRecruit = 8
    CharacterPotential = 9

class GachaGroupType(IntEnum):
    None_ = 0
    Reward_General = 1
    System_Craft = 2
    Reward_Pack = 3

class ParcelChangeReason(IntEnum):
    None_ = 0
    Acquire_NewAccount = 1
    Acquire_PlayReward = 2
    Acquire_ChapterReward = 3
    Acquire_LoginReward = 4
    Acquire_EventReward = 5
    Acquire_GMPush = 6
    Acquire_ShopBuy = 7
    Acquire_GachaBuy = 8
    Acquire_CurrencyBuy = 9
    Equipment_Equip = 10
    Equipment_Unequip = 11
    Equipment_Levelup = 12
    Equipment_LimitBreak = 13
    Equipment_Transcendence = 14
    Equipment_Enchant = 15
    Item_Use = 16
    Item_Lock = 17
    Item_CharacterGrowthMaterial = 18
    Item_Change = 19
    Item_Delete = 20
    Item_Consume = 21
    Item_SelectTicket = 22
    Character_ExpGrowth = 23
    Character_Transcendence = 24
    Character_SkillLevelUp = 25
    Character_FavorGrowth = 26
    Furniture_CafeSet = 27
    Furniture_CafeRecall = 28
    Academy_AttendSchedule = 29
    Academy_MessageList = 30
    Adventure_EnterMainStage = 31
    Adventure_EnterSubStage = 32
    Adventure_MainStageBattleResult = 33
    Adventure_SubStageBattleResult = 34
    Adventure_ChapterClearReward = 35
    Adventure_Retreat = 36
    Adventure_PurchasePlayCountHardStage = 37
    Adventure_TutorialStage = 38
    Adventure_TutorialStageBattleResult = 39
    ContentSweep_Sweep = 40
    Arena_TimeReward = 41
    Arena_DailyReward = 42
    Arena_EnterBattle = 43
    Arena_BattleResult = 44
    Cafe_Interact = 45
    Cafe_Production = 46
    Cafe_RankUp = 47
    Cafe_GiveGift = 48
    WeekDungeon_BattleResult = 49
    WeekDungeon_EnterBattle = 50
    WeekDungeon_Retreat = 51
    Mission_Clear = 52
    Shop_Refresh = 53
    Shop_BuyEligma = 54
    Shop_BuyMerchandise = 55
    Shop_BuyGacha = 56
    Scenario_Clear = 57
    Recipe_Craft = 58
    Raid_Failed = 59
    Raid_Reward = 60
    Raid_SeasonReward = 61
    Raid_CreateBattle = 62
    CumulativeTimeReward_Reward = 63
    Mail_Receive = 64
    MomoTalk_FavorSchedule = 65
    WeekDungeon_EnterBlood = 66
    WeekDungeon_EnterGift = 67
    Acquire_ActionPoint = 68
    Acquire_ArenaTicket = 69
    EventContent_TotalReward = 70
    Craft_UpdateNode = 71
    Craft_CompleteProcess = 72
    Craft_Reward = 73
    EventContent_BattleResult = 74
    Adventure_Sweep = 75
    EventContent_Sweep = 76
    WeekDungeon_Sweep = 77
    Acquire_MonthlyProduct = 78
    Acquire_DailyReward = 79
    Billing_PurchaseProduct = 80
    EventContent_EnterMainStage = 81
    EventContent_EnterSubStage = 82
    EventContent_MainStageResult = 83
    EventContent_SubStageResult = 84
    EventContent_Retreat = 85
    WeekDungeon_BloodResult = 86
    WeekDungeon_GiftResult = 87
    WeekDungeon_EnterChaserA = 88
    WeekDungeon_EnterChaserB = 89
    WeekDungeon_EnterChaserC = 90
    WeekDungeon_ChaserAResult = 91
    WeekDungeon_ChaserBResult = 92
    WeekDungeon_ChaserCResult = 93
    EventContent_BoxGacha = 94
    Raid_Sweep = 95
    Clan_AssistReward = 96
    EventContent_CardShop = 97
    CharacterWeapon_ExpGrowth = 98
    CharacterWeapon_Transcendence = 99
    MiniGameMission_Clear = 100
    SchoolDungeon_EnterSchoolA = 101
    SchoolDungeon_EnterSchoolB = 102
    SchoolDungeon_EnterSchoolC = 103
    SchoolDungeon_SchoolAResult = 104
    SchoolDungeon_SchoolBResult = 105
    SchoolDungeon_SchoolCResult = 106
    TimeAttackDungeon_CreateBattle = 107
    TimeAttackDungeon_EndBattle = 108
    TimeAttackDungeon_Reward = 109
    Clan_Create = 110
    Arena_SeasonReward = 111
    Arena_OverallReward = 112
    EventContent_AttendSchedule = 113
    EventContent_BuyFortuneGacha = 114
    Equipment_BatchGrowth = 115
    EventContent_EnterStoryStage = 116
    EventContent_StoryStageResult = 117
    WorldRaid_EndBattle = 118
    WorldRaid_Reward = 119
    Conquest_EnterBattle = 120
    Conquest_EnterUnExpectBattle = 121
    Conquest_BattleResult = 122
    Conquest_UnExpectBattleResult = 123
    Conquest_UpgradeBase = 124
    Conquest_ManageBase = 125
    Conquest_CalculatedReward = 126
    Conquest_TakeEventBoxObject = 127
    Conquest_ConquerNormalTile = 128
    Item_SelectRecruit = 129
    Adventure_EnterExtraStage = 130
    Adventure_ExtraStageBattleResult = 131
    Scenario_EnterMainStage = 132
    Scenario_MainStageResult = 133
    Scenario_RetreatMainStage = 134
    EventContent_DiceRaceRollReward = 135
    EventContent_DiceRaceLapReward = 136
    ShiftingCraft_BeginProcess = 137
    ShiftingCraft_CompleteProcess = 138
    ShiftingCraft_Reward = 139
    MiniGame_ShootingBattleResult = 140
    MiniGame_ShootingSweep = 141
    EliminateRaid_Failed = 142
    EliminateRaid_Reward = 143
    EliminateRaid_SeasonReward = 144
    EliminateRaid_CreateBattle = 145
    EliminateRaid_Sweep = 146
    Item_AutoSynth = 147
    ContentSweep_MultiSweep = 148
    Emblem_Acquire = 149
    MiniGame_TBGMove = 150
    MiniGame_TBGEncounterInput = 151
    MiniGame_TBGResurrect = 152
    MiniGame_TBGSweep = 153
    Shop_BeforehandGacha = 154
    EliminateRaid_LimitedReward = 155
    Craft_AutoBeginProcess = 156
    Craft_CompleteProcessAll = 157
    Craft_RewardAll = 158
    ShiftingCraft_CompleteProcessAll = 159
    ShiftingCraft_RewardAll = 160
    Temp_1 = 161
    Temp_2 = 162
    Temp_3 = 163
    Temp_4 = 164
    EventContent_Treasure = 165
    Field_EnterStage = 166
    Field_StageResult = 167
    Field_Interaction = 168
    Field_Quest = 169
    Character_PotentialGrowth = 170
    MultiFloorRaid_EndBattle = 171
    MultiFloorRaid_Reward = 172
    MiniGame_DreamSchedule = 173
    MiniGame_DreamDailyClosing = 174
    MiniGame_DreamEnding = 175
    Item_ExpireChange = 176
    MiniGame_DefenseBattleResult = 177
    Raid_FailCompensateReward = 178
    EliminateRaid_FailCompensateReward = 179
    Currency_ExpireChange = 180
    Conquest_ErosionBattleResult = 181
    Conquest_EnterErosionBattle = 182

class ConsumeCondition(IntEnum):
    And = 0
    Or = 1

class DailyRefillType(IntEnum):
    None_ = 0
    Default = 1
    Login = 2

class ScenarioBGType(IntEnum):
    None_ = 0
    Image = 1
    BlurRT = 2
    Spine = 3
    Hide = 4

class ScenarioType(IntEnum):
    None_ = 0
    Title = 1
    Place = 2

class ScenarioTypes(IntEnum):
    None_ = 0
    Title = 1
    Place = 2

class ScenarioCharacterAction(IntEnum):
    Idle = 0
    Shake = 1
    Greeting = 2
    FalldownLeft = 3
    FalldownRight = 4
    Stiff = 5
    Hophop = 6
    Jump = 7

class ScenarioCharacterBehaviors(IntEnum):
    None_ = 0
    Appear = 1
    Disappear = 2
    AppearToLeft = 3
    ApperToRight = 4
    DisappearToLeft = 5
    DisappearToRight = 6
    MoveToTarget = 7

class ScenarioCharacterShapes(IntEnum):
    None_ = 0
    Signal = 1
    BlackSilhouette = 2
    Closeup = 4
    Highlight = 8
    WhiteSilhouette = 16

class ScenarioBGScroll(IntEnum):
    None_ = 0
    Vertical = 1
    Horizontal = 2

class DialogCategory(IntEnum):
    Cafe = 0
    Echelon = 1
    CharacterSSRNew = 2
    CharacterGet = 3
    Birthday = 4
    Dating = 5
    Title = 6
    UILobby = 7
    UILobbySpecial = 8
    UIShop = 9
    UIGacha = 10
    UIRaidLobby = 11
    UIWork = 12
    UITitle = 13
    UIWeekDungeon = 14
    UIAcademyLobby = 15
    UIRaidLobbySeasonOff = 16
    UIRaidLobbySeasonOn = 17
    UIWorkAronaSit = 18
    UIWorkAronaSleep = 19
    UIWorkAronaWatch = 20
    UIGuideMission = 21
    UILobby2 = 22
    UIClanSearchList = 23
    UIAttendance = 24
    UIAttendanceEvent01 = 25
    UIEventLobby = 26
    UIEventShop = 27
    UIEventBoxGachaShop = 28
    UIAttendanceEvent02 = 29
    UIAttendanceEvent03 = 30
    UIEventCardShop = 31
    UISchoolDungeon = 32
    UIAttendanceEvent = 33
    UISpecialOperationLobby = 34
    WeaponGet = 35
    UIAttendanceEvent04 = 36
    UIEventFortuneGachaShop = 37
    UIAttendanceEvent05 = 38
    UIAttendanceEvent06 = 39
    UIMission = 40
    UIEventMission = 41
    UIAttendanceEvent08 = 42
    UIAttendanceEvent07 = 43
    UIEventMiniGameMission = 44
    UIAttendanceEvent09 = 45
    UIAttendanceEvent10 = 46
    UIAttendanceEvent11 = 47
    UIWorkPlanaSit = 48
    UIWorkPlanaUmbrella = 49
    UIWorkPlanaCabinet = 50
    UIWorkCoexist_AronaSleepSit = 51
    UIWorkCoexist_PlanaWatchSky = 52
    UIWorkCoexist_PlanaSitPeek = 53
    UIWorkCoexist_AronaSleepPeek = 54
    UIEventArchive = 55
    UIAttendanceEvent12 = 56
    UIAttendanceEvent13 = 57
    UIAttendanceEvent14 = 58
    Temp_1 = 59
    Temp_2 = 60
    Temp_3 = 61
    Temp_4 = 62
    Temp_5 = 63
    UIAttendanceEvent15 = 64
    UILobbySpecial2 = 65
    UIAttendanceEvent16 = 66
    UIEventTreasure = 67
    UIMultiFloorRaid = 68
    UIEventMiniGameDreamMaker = 69
    UIAttendanceEvent17 = 70
    UIAttendanceEvent18 = 71

class DialogCondition(IntEnum):
    Idle = 0
    Enter = 1
    Exit = 2
    Buy = 3
    SoldOut = 4
    BoxGachaNormal = 5
    BoxGachaPrize = 6
    Prize0 = 7
    Prize1 = 8
    Prize2 = 9
    Prize3 = 10
    Interaction = 11
    Luck0 = 12
    Luck1 = 13
    Luck2 = 14
    Luck3 = 15
    Luck4 = 16
    Luck5 = 17
    StoryOpen = 18
    CollectionOpen = 19
    BoxGachaFinish = 20
    FindTreasure = 21
    GetTreasure = 22
    RoundRenewal = 23
    MiniGameDreamMakerEnough01 = 24
    MiniGameDreamMakerEnough02 = 25
    MiniGameDreamMakerEnough03 = 26
    MiniGameDreamMakerEnough04 = 27
    MiniGameDreamMakerDefault = 28

class DialogConditionDetail(IntEnum):
    None_ = 0
    Day = 1
    Close = 2
    MiniGameDreamMakerDay = 3

class DialogType(IntEnum):
    Talk = 0
    Think = 1
    UITalk = 2

class Anniversary(IntEnum):
    None_ = 0
    UserBDay = 1
    StudentBDay = 2

class School(IntEnum):
    None_ = 0
    Hyakkiyako = 1
    RedWinter = 2
    Trinity = 3
    Gehenna = 4
    Abydos = 5
    Millennium = 6
    Arius = 7
    Shanhaijing = 8
    Valkyrie = 9
    WildHunt = 10
    SRT = 11
    SCHALE = 12
    ETC = 13
    Tokiwadai = 14
    Sakugawa = 15
    Highlander = 16

class EtcSchool(IntEnum):
    None_ = 0
    ETC = 1
    Tokiwadai = 2
    Sakugawa = 3
    Max = 4

class StoryCondition(IntEnum):
    Open = 0
    Locked = 1
    ComingSoon = 2
    Hide = 3

class EmojiEvent(IntEnum):
    EnterConver = 0
    EnterShelter = 1
    SignalLeader = 2
    Nice = 3
    Reload = 4
    Blind = 5
    Panic = 6
    Silence = 7
    NearyDead = 8
    Run = 9
    TerrainAdaptionS = 10
    TerrainAdaptionA = 11
    TerrainAdaptionB = 12
    TerrainAdaptionC = 13
    TerrainAdaptionD = 14
    TerrainAdaptionSS = 15
    Dot = 16
    Angry = 17
    Bulb = 18
    Exclaim = 19
    Surprise = 20
    Sad = 21
    Sigh = 22
    Steam = 23
    Upset = 24
    Respond = 25
    Question = 26
    Sweat = 27
    Music = 28
    Chat = 29
    Twinkle = 30
    Zzz = 31
    Tear = 32
    Heart = 33
    Shy = 34
    Think = 35

class ScenarioModeTypes(IntEnum):
    None_ = 0
    Main = 1
    Sub = 2
    Replay = 3
    Mini = 4
    SpecialOperation = 5
    Prologue = 6

class ScenarioModeSubTypes(IntEnum):
    None_ = 0
    Club = 1

class ScenarioModeReplayTypes(IntEnum):
    None_ = 0
    Event = 1
    Favor = 2
    Work = 3
    EventMeetup = 4

class ScenarioEffectDepth(IntEnum):
    None_ = 0
    AboveBg = 1
    AboveCharacter = 2
    AboveAll = 3

class ScenarioZoomAnchors(IntEnum):
    Center = 0
    LeftTop = 1
    LeftBottom = 2
    RightTop = 3
    RightBottom = 4

class ScenarioZoomType(IntEnum):
    Instant = 0
    Slide = 1

class ScenarioContentType(IntEnum):
    Prologue = 0
    WeekDungeon = 1
    Raid = 2
    Arena = 3
    Favor = 4
    Shop = 5
    EventContent = 6
    Craft = 7
    Chaser = 8
    EventContentMeetup = 9
    TimeAttack = 10
    Mission = 11
    EventContentPermanentPrologue = 12
    EventContentReturnSeason = 13
    MiniEvent = 14
    EliminateRaid = 15
    MultiFloorRaid = 16
    EventContentPermanent = 17

class MemoryLobbyCategory(IntEnum):
    None_ = 0
    UILobbySpecial = 1
    UILobbySpecial2 = 2

class PurchaseCountResetType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3

class ShopCategoryType(IntEnum):
    General = 0
    SecretStone = 1
    Raid = 2
    Gold = 3
    Ap = 4
    PickupGacha = 5
    NormalGacha = 6
    PointGacha = 7
    EventGacha = 8
    ArenaTicket = 9
    Arena = 10
    TutoGacha = 11
    RecruitSellection = 12
    EventContent_0 = 13
    EventContent_1 = 14
    EventContent_2 = 15
    EventContent_3 = 16
    EventContent_4 = 17
    _Obsolete = 18
    LimitedGacha = 19
    MasterCoin = 20
    SecretStoneGrowth = 21
    TicketGacha = 22
    DirectPayGacha = 23
    FesGacha = 24
    TimeAttack = 25
    Chaser = 26
    ChaserTicket = 27
    SchoolDungeonTicket = 28
    AcademyTicket = 29
    Special = 30
    Care = 31
    BeforehandGacha = 32
    EliminateRaid = 33
    GlobalSpecialGacha = 34

class PurchaseServerTag(IntEnum):
    Audit = 0
    PreAudit = 1
    Production = 2
    Hotfix = 3
    Standby2 = 4
    Standby1 = 5
    Major = 6
    Minor = 7
    Temp = 8
    Test = 9
    TestIn = 10

class PurchaseStatusCode(IntEnum):
    None_ = 0
    Start = 1
    PublishSuccess = 2
    End = 3
    Error = 4
    DuplicateOrder = 5
    Refund = 6

class StoreType(IntEnum):
    None_ = 0
    GooglePlay = 1
    AppStore = 2
    OneStore = 3
    MicrosoftStore = 4
    GalaxyStore = 5

class PurchasePeriodType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3

class PurchaseSourceType(IntEnum):
    None_ = 0
    Product = 1
    ProductMonthly = 2

class ProductCategory(IntEnum):
    None_ = 0
    Gem = 1
    Monthly = 2
    Package = 3
    GachaDirect = 4
    TimeLimit = 5

class ProductDisplayTag(IntEnum):
    None_ = 0
    New = 1
    Hot = 2
    Sale = 3
    Limited = 4

class ProductTagType(IntEnum):
    Monthly = 0
    Weekly = 1
    Biweekly = 2

class BillingTransactionEndType(IntEnum):
    None_ = 0
    Success = 1
    Cancel = 2

class GachaRewardType(IntEnum):
    None_ = 0
    Eligma = 1
    Eleph = 2

class ShopFreeRecruitType(IntEnum):
    None_ = 0
    Accumulation = 1
    Reset = 2

class GachaDisplayTag(IntEnum):
    None_ = 0
    Limited = 1
    TwoStar = 2
    ThreeStar = 3
    Free = 4
    New = 5
    Fes = 6
    SelectRecruit = 7

class ShopFilterType(IntEnum):
    GachaTicket = 0
    SecretStone = 1
    SecretStone_1 = 2
    SkillBook_Ultimate = 3
    ExSkill = 4
    SkillBook = 5
    Craft = 6
    AP = 7
    CharacterExpItem = 8
    Equip = 9
    Material = 10
    Creddit = 11
    Furniture = 12
    SelectItem = 13
    Currency = 14
    Hyakkiyako = 15
    RedWinter = 16
    Trinity = 17
    Gehenna = 18
    Abydos = 19
    Millennium = 20
    Arius = 21
    Shanhaijing = 22
    Valkyrie = 23
    SRT = 24
    Event = 25
    ChaserTotalTicket = 26
    SchoolTotalTicket = 27
    Highlander = 28
    ShopFilterDUMMY_2 = 29
    ShopFilterDUMMY_3 = 30
    ShopFilterDUMMY_4 = 31
    ShopFilterDUMMY_5 = 32
    ShopFilterDUMMY_6 = 33
    ShopFilterDUMMY_7 = 34
    ETC = 35
    Bundle = 36

class SocialMode(IntEnum):
    TITLE = 0
    LOBBY = 1
    FORMATION = 2
    STAGE_SELECT = 3
    BATTLE = 4
    POPUP = 5
    BATTLE_RESULT = 6
    BATTLE_RESULT_VICTORY = 7
    BATTLE_RESULT_DEFEAT = 8
    INVALID = 9
    TACTIC = 10
    STRATEGY = 11
    ACCONT = 12
    CAMPAIGN_STORY = 13
    CAMPAIGN_STAGE = 14
    TACTICREADY = 15

class AccountState(IntEnum):
    WaitingSignIn = 0
    Normal = 1
    Dormant = 2
    Comeback = 3
    Newbie = 4

class MessagePopupLayout(IntEnum):
    TextOnly = 0
    ImageBig = 1
    ImageSmall = 2
    UnlockCondition = 3

class MessagePopupImagePositionType(IntEnum):
    ImageFirst = 0
    TextFirst = 1

class MessagePopupButtonType(IntEnum):
    Accept = 0
    Cancel = 1
    Command = 2

class ToastType(IntEnum):
    None_ = 0
    Tactic_Left = 1
    Tactic_Right = 2
    Social_Center = 3
    Social_Mission = 4
    Social_Right = 5
    Notice_Center = 6

class StrategyAIType(IntEnum):
    None_ = 0
    Guard = 1
    Pursuit = 2

class StageDifficulty(IntEnum):
    None_ = 0
    Normal = 1
    Hard = 2
    VeryHard = 3
    VeryHard_Ex = 4

class HexaUnitGrade(IntEnum):
    Grade1 = 0
    Grade2 = 1
    Grade3 = 2
    Boss = 3

class TacticEnvironment(IntEnum):
    None_ = 0
    WarFog = 1

class StrategyObjectType(IntEnum):
    None_ = 0
    Start = 1
    Heal = 2
    Skill = 3
    StatBuff = 4
    Parcel = 5
    ParcelOneTimePerAccount = 6
    Portal = 7
    PortalOneWayEnterance = 8
    PortalOneWayExit = 9
    Observatory = 10
    Beacon = 11
    BeaconOneTime = 12
    EnemySpawn = 13
    SwitchToggle = 14
    SwitchMovableWhenToggleOff = 15
    SwitchMovableWhenToggleOn = 16
    FixedStart01 = 17
    FixedStart02 = 18
    FixedStart03 = 19
    FixedStart04 = 20

class StrategyEnvironment(IntEnum):
    None_ = 0
    MapFog = 1

class Tag(IntEnum):
    A = 0
    a = 1
    B = 2
    b = 3
    C = 4
    c = 5
    D = 6
    d = 7
    E = 8
    e = 9
    F = 10
    f = 11
    G = 12
    g = 13
    H = 14
    h = 15
    I = 16
    i = 17
    J = 18
    j = 19
    K = 20
    k = 21
    L = 22
    l = 23
    M = 24
    m = 25
    N = 26
    n = 27
    O = 28
    o = 29
    P = 30
    p = 31
    Q = 32
    q = 33
    R = 34
    r = 35
    S = 36
    s = 37
    T = 38
    t = 39
    U = 40
    u = 41
    V = 42
    v = 43
    W = 44
    w = 45
    X = 46
    x = 47
    Y = 48
    y = 49
    Z = 50
    z = 51
    aA = 52
    aa = 53
    aB = 54
    ab = 55
    aC = 56
    ac = 57
    aD = 58
    ad = 59
    aE = 60
    ae = 61
    aF = 62
    af = 63
    aG = 64
    ag = 65
    aH = 66
    ah = 67
    aI = 68
    ai = 69
    aJ = 70
    aj = 71
    aK = 72
    ak = 73
    aL = 74
    al = 75
    aM = 76
    am = 77
    aN = 78
    an = 79
    aO = 80
    ao = 81
    aP = 82
    ap = 83
    aQ = 84
    aq = 85
    aR = 86
    ar = 87
    aS = 88
    as_ = 89
    aT = 90
    at = 91
    aU = 92
    au = 93
    aV = 94
    av = 95
    aW = 96
    aw = 97
    aX = 98
    ax = 99
    aY = 100
    ay = 101
    aZ = 102
    az = 103
    BA = 104
    Ba = 105
    BB = 106
    Bb = 107
    BC = 108
    Bc = 109
    BD = 110
    Bd = 111
    BE = 112
    Be = 113
    BF = 114
    Bf = 115
    BG = 116
    Bg = 117
    BH = 118
    Bh = 119
    BI = 120
    Bi = 121
    BJ = 122
    Bj = 123
    BK = 124
    Bk = 125
    BL = 126
    Bl = 127
    BM = 128
    Bm = 129
    BN = 130
    Bn = 131
    BO = 132
    Bo = 133
    BP = 134
    Bp = 135
    BQ = 136
    Bq = 137
    BR = 138
    Br = 139
    BS = 140
    Bs = 141
    BT = 142
    Bt = 143
    BU = 144
    Bu = 145
    BV = 146
    Bv = 147
    BW = 148
    Bw = 149
    BX = 150
    Bx = 151
    BY = 152
    By = 153
    BZ = 154
    Bz = 155
    bA = 156
    ba = 157
    bB = 158
    bb = 159
    bC = 160
    bc = 161
    bD = 162
    bd = 163
    bE = 164
    be = 165
    bF = 166
    bf = 167
    bG = 168
    bg = 169
    bH = 170
    bh = 171
    bI = 172
    bi = 173
    bJ = 174
    bj = 175
    bK = 176
    bk = 177
    bL = 178
    bl = 179
    bM = 180
    bm = 181
    bN = 182
    bn = 183
    bO = 184
    bo = 185
    bP = 186
    bp = 187
    bQ = 188
    bq = 189
    bR = 190
    br = 191
    bS = 192
    bs = 193
    bT = 194
    bt = 195
    bU = 196
    bu = 197
    bV = 198
    bv = 199
    bW = 200
    bw = 201
    bX = 202
    bx = 203
    bY = 204
    by = 205
    bZ = 206
    bz = 207
    CA = 208
    Ca = 209
    CB = 210
    Cb = 211
    CC = 212
    Cc = 213
    CD = 214
    Cd = 215
    CE = 216
    Ce = 217
    CF = 218
    Cf = 219
    CG = 220
    Cg = 221
    CH = 222
    Ch = 223
    CI = 224
    Ci = 225
    CJ = 226
    Cj = 227
    CK = 228
    Ck = 229
    CL = 230
    Cl = 231
    CM = 232
    Cm = 233
    CN = 234
    Cn = 235
    CO = 236
    Co = 237
    CP = 238
    Cp = 239
    CQ = 240
    Cq = 241
    CR = 242
    Cr = 243
    CS = 244
    Cs = 245
    CT = 246
    Ct = 247
    CU = 248
    Cu = 249
    CV = 250
    Cv = 251
    CW = 252
    Cw = 253
    CX = 254
    Cx = 255
    CY = 256
    Cy = 257
    CZ = 258
    Cz = 259
    cA = 260
    ca = 261
    cB = 262
    cb = 263
    cC = 264
    cc = 265
    cD = 266
    cd = 267
    cE = 268
    ce = 269
    cF = 270
    cf = 271
    cG = 272
    cg = 273
    cH = 274
    ch = 275
    cI = 276
    ci = 277
    cJ = 278
    cj = 279
    cK = 280
    ck = 281
    cL = 282
    cl = 283
    cM = 284
    cm = 285
    cN = 286
    cn = 287
    cO = 288
    co = 289
    cP = 290
    cp = 291
    cQ = 292
    cq = 293
    cR = 294
    cr = 295
    cS = 296
    cs = 297
    cT = 298
    ct = 299
    cU = 300
    cu = 301
    cV = 302
    cv = 303
    cW = 304
    cw = 305
    cX = 306
    cx = 307
    cY = 308
    cy = 309
    cZ = 310
    cz = 311
    DA = 312
    Da = 313
    DB = 314
    Db = 315
    DC = 316
    Dc = 317
    DD = 318
    Dd = 319
    DE = 320
    De = 321
    DF = 322
    Df = 323
    DG = 324
    Dg = 325
    DH = 326
    Dh = 327
    DI = 328
    Di = 329
    DJ = 330
    Dj = 331
    DK = 332
    Dk = 333
    DL = 334
    Dl = 335
    DM = 336
    Dm = 337
    DN = 338
    Dn = 339
    DO = 340
    Do = 341
    DP = 342
    Dp = 343
    DQ = 344
    Dq = 345
    DR = 346
    Dr = 347
    DS = 348
    Ds = 349
    DT = 350
    Dt = 351
    DU = 352
    Du = 353
    DV = 354
    Dv = 355
    DW = 356
    Dw = 357
    DX = 358
    Dx = 359
    DY = 360
    Dy = 361
    DZ = 362
    Dz = 363
    dA = 364
    da = 365
    dB = 366
    db = 367
    dC = 368
    dc = 369
    dD = 370
    dd = 371
    dE = 372
    de = 373
    dF = 374
    df = 375
    dG = 376
    dg = 377
    dH = 378
    dh = 379
    dI = 380
    di = 381
    dJ = 382
    dj = 383
    dK = 384
    dk = 385
    dL = 386
    dl = 387
    dM = 388
    dm = 389
    dN = 390
    dn = 391
    dO = 392
    do = 393
    dP = 394
    dp = 395
    dQ = 396
    dq = 397
    dR = 398
    dr = 399
    dS = 400
    ds = 401
    dT = 402
    dt = 403
    dU = 404
    du = 405
    dV = 406
    dv = 407
    dW = 408
    dw = 409
    dX = 410
    dx = 411
    dY = 412
    dy = 413
    dZ = 414
    dz = 415
    EA = 416
    Ea = 417
    EB = 418
    Eb = 419
    EC = 420
    Ec = 421
    ED = 422
    Ed = 423
    EE = 424
    Ee = 425
    EF = 426
    Ef = 427
    EG = 428
    Eg = 429
    EH = 430
    Eh = 431
    EI = 432
    Ei = 433
    EJ = 434
    Ej = 435
    EK = 436
    Ek = 437
    EL = 438
    El = 439
    EM = 440
    Em = 441
    EN = 442
    En = 443
    EO = 444
    Eo = 445
    EP = 446
    Ep = 447
    EQ = 448
    Eq = 449
    ER = 450
    Er = 451
    ES = 452
    Es = 453
    ET = 454
    Et = 455
    EU = 456
    Eu = 457
    EV = 458
    Ev = 459
    EW = 460
    Ew = 461
    EX = 462
    Ex = 463
    EY = 464
    Ey = 465
    EZ = 466
    Ez = 467
    eA = 468
    ea = 469
    eB = 470
    eb = 471
    eC = 472
    ec = 473
    eD = 474
    ed = 475
    eE = 476
    ee = 477
    eF = 478
    ef = 479
    eG = 480
    eg = 481
    eH = 482
    eh = 483
    eI = 484
    ei = 485
    eJ = 486
    ej = 487
    eK = 488
    ek = 489
    eL = 490
    el = 491
    eM = 492
    em = 493
    eN = 494
    en = 495
    eO = 496
    eo = 497
    eP = 498
    ep = 499
    eQ = 500
    eq = 501
    eR = 502
    er = 503
    eS = 504
    es = 505
    eT = 506
    et = 507
    eU = 508
    eu = 509
    eV = 510
    ev = 511
    eW = 512
    ew = 513
    eX = 514
    ex = 515
    eY = 516
    ey = 517
    eZ = 518
    ez = 519
    FA = 520
    Fa = 521
    FB = 522
    Fb = 523
    FC = 524
    Fc = 525
    FD = 526
    Fd = 527
    FE = 528
    Fe = 529
    FF = 530
    Ff = 531
    FG = 532
    Fg = 533
    FH = 534
    Fh = 535
    FI = 536
    Fi = 537
    FJ = 538
    Fj = 539
    FK = 540
    Fk = 541
    FL = 542
    Fl = 543
    FM = 544
    Fm = 545
    FN = 546
    Fn = 547
    FO = 548
    Fo = 549
    FP = 550
    Fp = 551
    FQ = 552
    Fq = 553
    FR = 554
    Fr = 555
    FS = 556
    Fs = 557
    FT = 558
    Ft = 559
    FU = 560
    Fu = 561
    FV = 562
    Fv = 563
    FW = 564
    Fw = 565
    FX = 566
    Fx = 567
    FY = 568
    Fy = 569
    FZ = 570
    Fz = 571
    fA = 572
    fa = 573
    fB = 574
    fb = 575
    fC = 576
    fc = 577
    fD = 578
    fd = 579
    fE = 580
    fe = 581
    fF = 582
    ff = 583
    fG = 584
    fg = 585
    fH = 586
    fh = 587
    fI = 588
    fi = 589
    fJ = 590
    fj = 591
    fK = 592
    fk = 593
    fL = 594
    fl = 595
    fM = 596
    fm = 597
    fN = 598
    fn = 599
    fO = 600
    fo = 601
    fP = 602
    fp = 603
    fQ = 604
    fq = 605
    fR = 606
    fr = 607
    fS = 608
    fs = 609
    fT = 610
    ft = 611
    fU = 612
    fu = 613
    fV = 614
    fv = 615
    fW = 616
    fw = 617
    fX = 618
    fx = 619
    fY = 620
    fy = 621
    fZ = 622
    fz = 623
    GA = 624
    Ga = 625
    GB = 626
    Gb = 627
    GC = 628
    Gc = 629
    GD = 630
    Gd = 631
    GE = 632
    Ge = 633
    GF = 634
    Gf = 635
    GG = 636
    Gg = 637
    GH = 638
    Gh = 639
    GI = 640
    Gi = 641
    GJ = 642
    Gj = 643
    GK = 644
    Gk = 645
    GL = 646
    Gl = 647
    GM = 648
    Gm = 649
    GN = 650
    Gn = 651
    GO = 652
    Go = 653
    GP = 654
    Gp = 655
    GQ = 656
    Gq = 657
    GR = 658
    Gr = 659
    GS = 660
    Gs = 661
    GT = 662
    Gt = 663
    GU = 664
    Gu = 665
    GV = 666
    Gv = 667
    GW = 668
    Gw = 669
    GX = 670
    Gx = 671
    GY = 672
    Gy = 673
    GZ = 674
    Gz = 675
    gA = 676
    ga = 677
    gB = 678
    gb = 679
    gC = 680
    gc = 681
    gD = 682
    gd = 683
    gE = 684
    ge = 685
    gF = 686
    gf = 687
    gG = 688
    gg = 689
    gH = 690
    gh = 691
    gI = 692
    gi = 693
    gJ = 694
    gj = 695
    gK = 696
    gk = 697
    gL = 698
    gl = 699
    gM = 700
    gm = 701
    gN = 702
    gn = 703
    gO = 704
    go = 705
    gP = 706
    gp = 707
    gQ = 708
    gq = 709
    gR = 710
    gr = 711
    gS = 712
    gs = 713
    gT = 714
    gt = 715
    gU = 716
    gu = 717
    gV = 718
    gv = 719
    gW = 720
    gw = 721
    gX = 722
    gx = 723
    gY = 724
    gy = 725
    gZ = 726
    gz = 727
    HA = 728
    Ha = 729
    HB = 730
    Hb = 731
    HC = 732
    Hc = 733
    HD = 734
    Hd = 735
    HE = 736
    He = 737
    HF = 738
    Hf = 739
    HG = 740
    Hg = 741
    HH = 742
    Hh = 743
    HI = 744
    Hi = 745
    HJ = 746
    Hj = 747
    HK = 748
    Hk = 749
    HL = 750
    Hl = 751
    HM = 752
    Hm = 753
    HN = 754
    Hn = 755
    HO = 756
    Ho = 757
    HP = 758
    Hp = 759
    HQ = 760
    Hq = 761
    HR = 762
    Hr = 763
    HS = 764
    Hs = 765
    HT = 766
    Ht = 767
    HU = 768
    Hu = 769
    HV = 770
    Hv = 771
    HW = 772
    Hw = 773
    HX = 774
    Hx = 775
    HY = 776
    Hy = 777
    HZ = 778
    Hz = 779
    hA = 780
    ha = 781
    hB = 782
    hb = 783
    hC = 784
    hc = 785
    hD = 786
    hd = 787
    hE = 788
    he = 789
    hF = 790
    hf = 791
    hG = 792
    hg = 793
    hH = 794
    hh = 795
    hI = 796
    hi = 797
    hJ = 798
    hj = 799
    hK = 800
    hk = 801
    hL = 802
    hl = 803
    hM = 804
    hm = 805
    hN = 806
    hn = 807
    hO = 808
    ho = 809
    hP = 810
    hp = 811
    hQ = 812
    hq = 813
    hR = 814
    hr = 815
    hS = 816
    hs = 817
    hT = 818
    ht = 819
    hU = 820
    hu = 821
    hV = 822
    hv = 823
    hW = 824
    hw = 825
    hX = 826
    hx = 827
    hY = 828
    hy = 829
    hZ = 830
    hz = 831
    IA = 832
    Ia = 833
    IB = 834
    Ib = 835
    IC = 836
    Ic = 837
    ID = 838
    Id = 839
    IE = 840
    Ie = 841
    IF = 842
    If = 843
    IG = 844
    Ig = 845
    IH = 846
    Ih = 847
    II = 848
    Ii = 849
    IJ = 850
    Ij = 851
    IK = 852
    Ik = 853
    IL = 854
    Il = 855
    IM = 856
    Im = 857
    IN = 858
    In = 859
    IO = 860
    Io = 861
    IP = 862
    Ip = 863
    IQ = 864
    Iq = 865
    IR = 866
    Ir = 867
    IS = 868
    Is = 869
    IT = 870
    It = 871
    IU = 872
    Iu = 873
    IV = 874
    Iv = 875
    IW = 876
    Iw = 877
    IX = 878
    Ix = 879
    IY = 880
    Iy = 881
    IZ = 882
    Iz = 883
    iA = 884
    ia = 885
    iB = 886
    ib = 887
    iC = 888
    ic = 889
    iD = 890
    id = 891
    iE = 892
    ie = 893
    iF = 894
    if_ = 895
    iG = 896
    ig = 897
    iH = 898
    ih = 899
    iI = 900
    ii = 901
    iJ = 902
    ij = 903
    iK = 904
    ik = 905
    iL = 906
    il = 907
    iM = 908
    im = 909
    iN = 910
    in_ = 911
    iO = 912
    io = 913
    iP = 914
    ip = 915
    iQ = 916
    iq = 917
    iR = 918
    ir = 919
    iS = 920
    is_ = 921
    iT = 922
    it = 923
    iU = 924
    iu = 925
    iV = 926
    iv = 927
    iW = 928
    iw = 929
    iX = 930
    ix = 931
    iY = 932
    iy = 933
    iZ = 934
    iz = 935
    JA = 936
    Ja = 937
    JB = 938
    Jb = 939
    JC = 940
    Jc = 941
    JD = 942
    Jd = 943
    JE = 944
    Je = 945
    JF = 946
    Jf = 947
    JG = 948
    Jg = 949
    JH = 950
    Jh = 951
    JI = 952
    Ji = 953
    JJ = 954
    Jj = 955
    JK = 956
    Jk = 957
    JL = 958
    Jl = 959
    JM = 960
    Jm = 961
    JN = 962
    Jn = 963
    JO = 964
    Jo = 965
    JP = 966
    Jp = 967
    JQ = 968
    Jq = 969
    JR = 970
    Jr = 971
    JS = 972
    Js = 973
    JT = 974
    Jt = 975
    JU = 976
    Ju = 977
    JV = 978
    Jv = 979
    JW = 980
    Jw = 981
    JX = 982
    Jx = 983
    JY = 984
    Jy = 985
    JZ = 986
    Jz = 987
    jA = 988
    ja = 989
    jB = 990
    jb = 991
    jC = 992
    jc = 993
    jD = 994
    jd = 995
    jE = 996
    je = 997
    jF = 998
    jf = 999
    jG = 1000
    jg = 1001
    jH = 1002
    jh = 1003
    jI = 1004
    ji = 1005
    jJ = 1006
    jj = 1007
    jK = 1008
    jk = 1009
    jL = 1010
    jl = 1011
    jM = 1012
    jm = 1013
    jN = 1014
    jn = 1015
    jO = 1016
    jo = 1017
    jP = 1018
    jp = 1019
    jQ = 1020
    jq = 1021
    jR = 1022
    jr = 1023
    jS = 1024
    js = 1025
    jT = 1026
    jt = 1027
    jU = 1028
    ju = 1029
    jV = 1030
    jv = 1031
    jW = 1032
    jw = 1033
    jX = 1034
    jx = 1035
    jY = 1036
    jy = 1037
    jZ = 1038
    jz = 1039
    KA = 1040
    Ka = 1041
    KB = 1042
    Kb = 1043
    KC = 1044
    Kc = 1045
    KD = 1046
    Kd = 1047
    KE = 1048
    Ke = 1049
    KF = 1050
    Kf = 1051
    KG = 1052
    Kg = 1053
    KH = 1054
    Kh = 1055
    KI = 1056
    Ki = 1057
    KJ = 1058
    Kj = 1059
    KK = 1060
    Kk = 1061
    KL = 1062
    Kl = 1063
    KM = 1064
    Km = 1065
    KN = 1066
    Kn = 1067
    KO = 1068
    Ko = 1069
    KP = 1070
    Kp = 1071
    KQ = 1072
    Kq = 1073
    KR = 1074
    Kr = 1075
    KS = 1076
    Ks = 1077
    KT = 1078
    Kt = 1079
    KU = 1080
    Ku = 1081
    KV = 1082
    Kv = 1083
    KW = 1084
    Kw = 1085
    KX = 1086
    Kx = 1087
    KY = 1088
    Ky = 1089
    KZ = 1090
    Kz = 1091
    kA = 1092
    ka = 1093
    kB = 1094
    kb = 1095
    kC = 1096
    kc = 1097
    kD = 1098
    kd = 1099
    kE = 1100
    ke = 1101
    kF = 1102
    kf = 1103
    kG = 1104
    kg = 1105
    kH = 1106
    kh = 1107
    kI = 1108
    ki = 1109
    kJ = 1110
    kj = 1111
    kK = 1112
    kk = 1113
    kL = 1114
    kl = 1115
    kM = 1116
    km = 1117
    kN = 1118
    kn = 1119
    kO = 1120
    ko = 1121
    kP = 1122
    kp = 1123
    kQ = 1124
    kq = 1125
    kR = 1126
    kr = 1127
    kS = 1128
    ks = 1129
    kT = 1130
    kt = 1131
    kU = 1132
    ku = 1133
    kV = 1134
    kv = 1135
    kW = 1136
    kw = 1137
    kX = 1138
    kx = 1139
    kY = 1140
    ky = 1141
    kZ = 1142
    kz = 1143
    LA = 1144
    La = 1145
    LB = 1146
    Lb = 1147
    LC = 1148
    Lc = 1149
    LD = 1150
    Ld = 1151
    LE = 1152
    Le = 1153
    LF = 1154
    Lf = 1155
    LG = 1156
    Lg = 1157
    LH = 1158
    Lh = 1159
    LI = 1160
    Li = 1161
    LJ = 1162
    Lj = 1163
    LK = 1164
    Lk = 1165
    LL = 1166
    Ll = 1167
    LM = 1168
    Lm = 1169
    LN = 1170
    Ln = 1171
    LO = 1172
    Lo = 1173
    LP = 1174
    Lp = 1175
    LQ = 1176
    Lq = 1177
    LR = 1178
    Lr = 1179
    LS = 1180
    Ls = 1181
    LT = 1182
    Lt = 1183
    LU = 1184
    Lu = 1185
    LV = 1186
    Lv = 1187
    LW = 1188
    Lw = 1189
    LX = 1190
    Lx = 1191
    LY = 1192
    Ly = 1193
    LZ = 1194
    Lz = 1195
    lA = 1196
    la = 1197
    lB = 1198
    lb = 1199
    lC = 1200
    lc = 1201
    lD = 1202
    ld = 1203
    lE = 1204
    le = 1205
    lF = 1206
    lf = 1207
    lG = 1208
    lg = 1209
    lH = 1210
    lh = 1211
    lI = 1212
    li = 1213
    lJ = 1214
    lj = 1215
    lK = 1216
    lk = 1217
    lL = 1218
    ll = 1219
    lM = 1220
    lm = 1221
    lN = 1222
    ln = 1223
    lO = 1224
    lo = 1225
    lP = 1226
    lp = 1227
    lQ = 1228
    lq = 1229
    lR = 1230
    lr = 1231
    lS = 1232
    ls = 1233
    lT = 1234
    lt = 1235
    lU = 1236
    lu = 1237
    lV = 1238
    lv = 1239
    lW = 1240
    lw = 1241
    lX = 1242
    lx = 1243
    lY = 1244
    ly = 1245
    lZ = 1246
    lz = 1247
    MA = 1248
    Ma = 1249
    MB = 1250
    Mb = 1251
    MC = 1252
    Mc = 1253
    MD = 1254
    Md = 1255
    ME = 1256
    Me = 1257
    MF = 1258
    Mf = 1259
    MG = 1260
    Mg = 1261
    MH = 1262
    Mh = 1263
    MI = 1264
    Mi = 1265
    MJ = 1266
    Mj = 1267
    MK = 1268
    Mk = 1269
    ML = 1270
    Ml = 1271
    MM = 1272
    Mm = 1273
    MN = 1274
    Mn = 1275
    MO = 1276
    Mo = 1277
    MP = 1278
    Mp = 1279
    MQ = 1280
    Mq = 1281
    MR = 1282
    Mr = 1283
    MS = 1284
    Ms = 1285
    MT = 1286
    Mt = 1287
    MU = 1288
    Mu = 1289
    MV = 1290
    Mv = 1291
    MW = 1292
    Mw = 1293
    MX = 1294
    Mx = 1295
    MY = 1296
    My = 1297
    MZ = 1298
    Mz = 1299
    mA = 1300
    ma = 1301
    mB = 1302
    mb = 1303
    mC = 1304
    mc = 1305
    mD = 1306
    md = 1307
    mE = 1308
    me = 1309
    mF = 1310
    mf = 1311
    mG = 1312
    mg = 1313
    mH = 1314
    mh = 1315
    mI = 1316
    mi = 1317
    mJ = 1318
    mj = 1319
    mK = 1320
    mk = 1321
    mL = 1322
    ml = 1323
    mM = 1324
    mm = 1325
    mN = 1326
    mn = 1327
    mO = 1328
    mo = 1329
    mP = 1330
    mp = 1331
    mQ = 1332
    mq = 1333
    mR = 1334
    mr = 1335
    mS = 1336
    ms = 1337
    mT = 1338
    mt = 1339
    mU = 1340
    mu = 1341
    mV = 1342
    mv = 1343
    mW = 1344
    mw = 1345
    mX = 1346
    mx = 1347
    mY = 1348
    my = 1349
    mZ = 1350
    mz = 1351
    NA = 1352
    Na = 1353
    NB = 1354
    Nb = 1355
    NC = 1356
    Nc = 1357
    ND = 1358
    Nd = 1359
    NE = 1360
    Ne = 1361
    NF = 1362
    Nf = 1363
    NG = 1364
    Ng = 1365
    NH = 1366
    Nh = 1367
    NI = 1368
    Ni = 1369
    NJ = 1370
    Nj = 1371
    NK = 1372
    Nk = 1373
    NL = 1374
    Nl = 1375
    NM = 1376
    Nm = 1377
    NN = 1378
    Nn = 1379
    NO = 1380
    No = 1381
    NP = 1382
    Np = 1383
    NQ = 1384
    Nq = 1385
    NR = 1386
    Nr = 1387
    NS = 1388
    Ns = 1389
    NT = 1390
    Nt = 1391
    NU = 1392
    Nu = 1393
    NV = 1394
    Nv = 1395
    NW = 1396
    Nw = 1397
    NX = 1398
    Nx = 1399
    NY = 1400
    Ny = 1401
    NZ = 1402
    Nz = 1403
    nA = 1404
    na = 1405
    nB = 1406
    nb = 1407
    nC = 1408
    nc = 1409
    nD = 1410
    nd = 1411
    nE = 1412
    ne = 1413
    nF = 1414
    nf = 1415
    nG = 1416
    ng = 1417
    nH = 1418
    nh = 1419
    nI = 1420
    ni = 1421
    nJ = 1422
    nj = 1423
    nK = 1424
    nk = 1425
    nL = 1426
    nl = 1427
    nM = 1428
    nm = 1429
    nN = 1430
    nn = 1431
    nO = 1432
    no = 1433
    nP = 1434
    np = 1435
    nQ = 1436
    nq = 1437
    nR = 1438
    nr = 1439
    nS = 1440
    ns = 1441
    nT = 1442
    nt = 1443
    nU = 1444
    nu = 1445
    nV = 1446
    nv = 1447
    nW = 1448
    nw = 1449
    nX = 1450
    nx = 1451
    nY = 1452
    ny = 1453
    nZ = 1454
    nz = 1455
    OA = 1456
    Oa = 1457
    OB = 1458
    Ob = 1459
    OC = 1460
    Oc = 1461
    OD = 1462
    Od = 1463
    OE = 1464
    Oe = 1465
    OF = 1466
    Of = 1467
    OG = 1468
    Og = 1469
    OH = 1470
    Oh = 1471
    OI = 1472
    Oi = 1473
    OJ = 1474
    Oj = 1475
    OK = 1476
    Ok = 1477
    OL = 1478
    Ol = 1479
    OM = 1480
    Om = 1481
    ON = 1482
    On = 1483
    OO = 1484
    Oo = 1485
    OP = 1486
    Op = 1487
    OQ = 1488
    Oq = 1489
    OR = 1490
    Or = 1491
    OS = 1492
    Os = 1493
    OT = 1494
    Ot = 1495
    OU = 1496
    Ou = 1497
    OV = 1498
    Ov = 1499
    OW = 1500
    Ow = 1501
    OX = 1502
    Ox = 1503
    OY = 1504
    Oy = 1505
    OZ = 1506
    Oz = 1507
    oA = 1508
    oa = 1509
    oB = 1510
    ob = 1511
    oC = 1512
    oc = 1513
    oD = 1514
    od = 1515
    oE = 1516
    oe = 1517
    oF = 1518
    of = 1519
    oG = 1520
    og = 1521
    oH = 1522
    oh = 1523
    oI = 1524
    oi = 1525
    oJ = 1526
    oj = 1527
    oK = 1528
    ok = 1529
    oL = 1530
    ol = 1531
    oM = 1532
    om = 1533
    oN = 1534
    on = 1535
    oO = 1536
    oo = 1537
    oP = 1538
    op = 1539
    oQ = 1540
    oq = 1541
    oR = 1542
    or_ = 1543
    oS = 1544
    os = 1545
    oT = 1546
    ot = 1547
    oU = 1548
    ou = 1549
    oV = 1550
    ov = 1551
    oW = 1552
    ow = 1553
    oX = 1554
    ox = 1555
    oY = 1556
    oy = 1557
    oZ = 1558
    oz = 1559
    PA = 1560
    Pa = 1561
    PB = 1562
    Pb = 1563
    PC = 1564
    Pc = 1565
    PD = 1566
    Pd = 1567
    PE = 1568
    Pe = 1569
    PF = 1570
    Pf = 1571
    PG = 1572
    Pg = 1573
    PH = 1574
    Ph = 1575
    PI = 1576
    Pi = 1577
    PJ = 1578
    Pj = 1579
    PK = 1580
    Pk = 1581
    PL = 1582
    Pl = 1583
    PM = 1584
    Pm = 1585
    PN = 1586
    Pn = 1587
    PO = 1588
    Po = 1589
    PP = 1590
    Pp = 1591
    PQ = 1592
    Pq = 1593
    PR = 1594
    Pr = 1595
    PS = 1596
    Ps = 1597
    PT = 1598
    Pt = 1599
    PU = 1600
    Pu = 1601
    PV = 1602
    Pv = 1603
    PW = 1604
    Pw = 1605
    PX = 1606
    Px = 1607
    PY = 1608
    Py = 1609
    PZ = 1610
    Pz = 1611
    pA = 1612
    pa = 1613
    pB = 1614
    pb = 1615
    pC = 1616
    pc = 1617
    pD = 1618
    pd = 1619
    pE = 1620
    pe = 1621
    pF = 1622
    pf = 1623
    pG = 1624
    pg = 1625
    pH = 1626
    ph = 1627
    pI = 1628
    pi = 1629
    pJ = 1630
    pj = 1631
    pK = 1632
    pk = 1633
    pL = 1634
    pl = 1635
    pM = 1636
    pm = 1637
    pN = 1638
    pn = 1639
    pO = 1640
    po = 1641
    pP = 1642
    pp = 1643
    pQ = 1644
    pq = 1645
    pR = 1646
    pr = 1647
    pS = 1648
    ps = 1649
    pT = 1650
    pt = 1651
    pU = 1652
    pu = 1653
    pV = 1654
    pv = 1655
    pW = 1656
    pw = 1657
    pX = 1658
    px = 1659
    pY = 1660
    py = 1661
    pZ = 1662
    pz = 1663
    QA = 1664
    Qa = 1665
    QB = 1666
    Qb = 1667
    QC = 1668
    Qc = 1669
    QD = 1670
    Qd = 1671
    QE = 1672
    Qe = 1673
    QF = 1674
    Qf = 1675
    QG = 1676
    Qg = 1677
    QH = 1678
    Qh = 1679
    QI = 1680
    Qi = 1681
    QJ = 1682
    Qj = 1683
    QK = 1684
    Qk = 1685
    QL = 1686
    Ql = 1687
    QM = 1688
    Qm = 1689
    QN = 1690
    Qn = 1691
    QO = 1692
    Qo = 1693
    QP = 1694
    Qp = 1695
    QQ = 1696
    Qq = 1697
    QR = 1698
    Qr = 1699
    QS = 1700
    Qs = 1701
    QT = 1702
    Qt = 1703
    QU = 1704
    Qu = 1705
    QV = 1706
    Qv = 1707
    QW = 1708
    Qw = 1709
    QX = 1710
    Qx = 1711
    QY = 1712
    Qy = 1713
    QZ = 1714
    Qz = 1715
    qA = 1716
    qa = 1717
    qB = 1718
    qb = 1719
    qC = 1720
    qc = 1721
    qD = 1722
    qd = 1723
    qE = 1724
    qe = 1725
    qF = 1726
    qf = 1727
    qG = 1728
    qg = 1729
    qH = 1730
    qh = 1731
    qI = 1732
    qi = 1733
    qJ = 1734
    qj = 1735
    qK = 1736
    qk = 1737
    qL = 1738
    ql = 1739
    qM = 1740
    qm = 1741
    qN = 1742
    qn = 1743
    qO = 1744
    qo = 1745
    qP = 1746
    qp = 1747
    qQ = 1748
    qq = 1749
    qR = 1750
    qr = 1751
    qS = 1752
    qs = 1753
    qT = 1754
    qt = 1755
    qU = 1756
    qu = 1757
    qV = 1758
    qv = 1759
    qW = 1760
    qw = 1761
    qX = 1762
    qx = 1763
    qY = 1764
    qy = 1765
    qZ = 1766
    qz = 1767
    RA = 1768
    Ra = 1769
    RB = 1770
    Rb = 1771
    RC = 1772
    Rc = 1773
    RD = 1774
    Rd = 1775
    RE = 1776
    Re = 1777
    RF = 1778
    Rf = 1779
    RG = 1780
    Rg = 1781
    RH = 1782
    Rh = 1783
    RI = 1784
    Ri = 1785
    RJ = 1786
    Rj = 1787
    RK = 1788
    Rk = 1789
    RL = 1790
    Rl = 1791
    RM = 1792
    Rm = 1793
    RN = 1794
    Rn = 1795
    RO = 1796
    Ro = 1797
    RP = 1798
    Rp = 1799
    RQ = 1800
    Rq = 1801
    RR = 1802
    Rr = 1803
    RS = 1804
    Rs = 1805
    RT = 1806
    Rt = 1807
    RU = 1808
    Ru = 1809
    RV = 1810
    Rv = 1811
    RW = 1812
    Rw = 1813
    RX = 1814
    Rx = 1815
    RY = 1816
    Ry = 1817
    RZ = 1818
    Rz = 1819
    rA = 1820
    ra = 1821
    rB = 1822
    rb = 1823
    rC = 1824
    rc = 1825
    rD = 1826
    rd = 1827
    rE = 1828
    re = 1829
    rF = 1830
    rf = 1831
    rG = 1832
    rg = 1833
    rH = 1834
    rh = 1835
    rI = 1836
    ri = 1837
    rJ = 1838
    rj = 1839
    rK = 1840
    rk = 1841
    rL = 1842
    rl = 1843
    rM = 1844
    rm = 1845
    rN = 1846
    rn = 1847
    rO = 1848
    ro = 1849
    rP = 1850
    rp = 1851
    rQ = 1852
    rq = 1853
    rR = 1854
    rr = 1855
    rS = 1856
    rs = 1857
    rT = 1858
    rt = 1859
    rU = 1860
    ru = 1861
    rV = 1862
    rv = 1863
    rW = 1864
    rw = 1865
    rX = 1866
    rx = 1867
    rY = 1868
    ry = 1869
    rZ = 1870
    rz = 1871
    SA = 1872
    Sa = 1873
    SB = 1874
    Sb = 1875
    SC = 1876
    Sc = 1877
    SD = 1878
    Sd = 1879
    SE = 1880
    Se = 1881
    SF = 1882
    Sf = 1883
    SG = 1884
    Sg = 1885
    SH = 1886
    Sh = 1887
    SI = 1888
    Si = 1889
    SJ = 1890
    Sj = 1891
    SK = 1892
    Sk = 1893
    SL = 1894
    Sl = 1895
    SM = 1896
    Sm = 1897
    SN = 1898
    Sn = 1899
    SO = 1900
    So = 1901
    SP = 1902
    Sp = 1903
    SQ = 1904
    Sq = 1905
    SR = 1906
    Sr = 1907
    SS = 1908
    Ss = 1909
    ST = 1910
    St = 1911
    SU = 1912
    Su = 1913
    SV = 1914
    Sv = 1915
    SW = 1916
    Sw = 1917
    SX = 1918
    Sx = 1919
    SY = 1920
    Sy = 1921
    SZ = 1922
    Sz = 1923
    sA = 1924
    sa = 1925
    sB = 1926
    sb = 1927
    sC = 1928
    sc = 1929
    sD = 1930
    sd = 1931
    sE = 1932
    se = 1933
    sF = 1934
    sf = 1935
    sG = 1936
    sg = 1937
    sH = 1938
    sh = 1939
    sI = 1940
    si = 1941
    sJ = 1942
    sj = 1943
    sK = 1944
    sk = 1945
    sL = 1946
    sl = 1947
    sM = 1948
    sm = 1949
    sN = 1950
    sn = 1951
    sO = 1952
    so = 1953
    sP = 1954
    sp = 1955
    sQ = 1956
    sq = 1957
    sR = 1958
    sr = 1959
    sS = 1960
    ss = 1961
    sT = 1962
    st = 1963
    sU = 1964
    su = 1965
    sV = 1966
    sv = 1967
    sW = 1968
    sw = 1969
    sX = 1970
    sx = 1971
    sY = 1972
    sy = 1973
    sZ = 1974
    sz = 1975
    TA = 1976
    Ta = 1977
    TB = 1978
    Tb = 1979
    TC = 1980
    Tc = 1981
    TD = 1982
    Td = 1983
    TE = 1984
    Te = 1985
    TF = 1986
    Tf = 1987
    TG = 1988
    Tg = 1989
    TH = 1990
    Th = 1991
    TI = 1992
    Ti = 1993
    TJ = 1994
    Tj = 1995
    TK = 1996
    Tk = 1997
    TL = 1998
    Tl = 1999
    TM = 2000
    Tm = 2001
    TN = 2002
    Tn = 2003
    TO = 2004
    To = 2005
    TP = 2006
    Tp = 2007
    TQ = 2008
    Tq = 2009
    TR = 2010
    Tr = 2011
    TS = 2012
    Ts = 2013
    TT = 2014
    Tt = 2015
    TU = 2016
    Tu = 2017
    TV = 2018
    Tv = 2019
    TW = 2020
    Tw = 2021
    TX = 2022
    Tx = 2023
    TY = 2024
    Ty = 2025
    TZ = 2026
    Tz = 2027
    tA = 2028
    ta = 2029
    tB = 2030
    tb = 2031
    tC = 2032
    tc = 2033
    tD = 2034
    td = 2035
    tE = 2036
    te = 2037
    tF = 2038
    tf = 2039
    tG = 2040
    tg = 2041
    tH = 2042
    th = 2043
    tI = 2044
    ti = 2045
    tJ = 2046
    tj = 2047
    tK = 2048
    tk = 2049
    tL = 2050
    tl = 2051
    tM = 2052
    tm = 2053
    tN = 2054
    tn = 2055
    tO = 2056
    to = 2057
    tP = 2058
    tp = 2059
    tQ = 2060
    tq = 2061
    tR = 2062
    tr = 2063
    tS = 2064
    ts = 2065
    tT = 2066
    tt = 2067
    tU = 2068
    tu = 2069
    tV = 2070
    tv = 2071
    tW = 2072
    tw = 2073
    tX = 2074
    tx = 2075
    tY = 2076
    ty = 2077
    tZ = 2078
    tz = 2079
    UA = 2080
    Ua = 2081
    UB = 2082
    Ub = 2083
    UC = 2084
    Uc = 2085
    UD = 2086
    Ud = 2087
    UE = 2088
    Ue = 2089
    UF = 2090
    Uf = 2091
    UG = 2092
    Ug = 2093
    UH = 2094
    Uh = 2095
    UI = 2096
    Ui = 2097
    UJ = 2098
    Uj = 2099
    UK = 2100
    Uk = 2101
    UL = 2102
    Ul = 2103
    UM = 2104
    Um = 2105
    UN = 2106
    Un = 2107
    UO = 2108
    Uo = 2109
    UP = 2110
    Up = 2111
    UQ = 2112
    Uq = 2113
    UR = 2114
    Ur = 2115
    US = 2116
    Us = 2117
    UT = 2118
    Ut = 2119
    UU = 2120
    Uu = 2121
    UV = 2122
    Uv = 2123
    UW = 2124
    Uw = 2125
    UX = 2126
    Ux = 2127
    UY = 2128
    Uy = 2129
    UZ = 2130
    Uz = 2131
    uA = 2132
    ua = 2133
    uB = 2134
    ub = 2135
    uC = 2136
    uc = 2137
    uD = 2138
    ud = 2139
    uE = 2140
    ue = 2141
    uF = 2142
    uf = 2143
    uG = 2144
    ug = 2145
    uH = 2146
    uh = 2147
    uI = 2148
    ui = 2149
    uJ = 2150
    uj = 2151
    uK = 2152
    uk = 2153
    uL = 2154
    ul = 2155
    uM = 2156
    um = 2157
    uN = 2158
    un = 2159
    uO = 2160
    uo = 2161
    uP = 2162
    up = 2163
    uQ = 2164
    uq = 2165
    uR = 2166
    ur = 2167
    uS = 2168
    us = 2169
    uT = 2170
    ut = 2171
    uU = 2172
    uu = 2173
    uV = 2174
    uv = 2175
    uW = 2176
    uw = 2177
    uX = 2178
    ux = 2179
    uY = 2180
    uy = 2181
    uZ = 2182
    uz = 2183
    VA = 2184
    Va = 2185
    VB = 2186
    Vb = 2187
    VC = 2188
    Vc = 2189
    VD = 2190
    Vd = 2191
    VE = 2192
    Ve = 2193
    VF = 2194
    Vf = 2195
    VG = 2196
    Vg = 2197
    VH = 2198
    Vh = 2199
    VI = 2200
    Vi = 2201
    VJ = 2202
    Vj = 2203
    VK = 2204
    Vk = 2205
    VL = 2206
    Vl = 2207
    VM = 2208
    Vm = 2209
    VN = 2210
    Vn = 2211
    VO = 2212
    Vo = 2213
    VP = 2214
    Vp = 2215
    VQ = 2216
    Vq = 2217
    VR = 2218
    Vr = 2219
    VS = 2220
    Vs = 2221
    VT = 2222
    Vt = 2223
    VU = 2224
    Vu = 2225
    VV = 2226
    Vv = 2227
    VW = 2228
    Vw = 2229
    VX = 2230
    Vx = 2231
    VY = 2232
    Vy = 2233
    VZ = 2234
    Vz = 2235
    vA = 2236
    va = 2237
    vB = 2238
    vb = 2239
    vC = 2240
    vc = 2241
    vD = 2242
    vd = 2243
    vE = 2244
    ve = 2245
    vF = 2246
    vf = 2247
    vG = 2248
    vg = 2249
    vH = 2250
    vh = 2251
    vI = 2252
    vi = 2253
    vJ = 2254
    vj = 2255
    vK = 2256
    vk = 2257
    vL = 2258
    vl = 2259
    vM = 2260
    vm = 2261
    vN = 2262
    vn = 2263
    vO = 2264
    vo = 2265
    vP = 2266
    vp = 2267
    vQ = 2268
    vq = 2269
    vR = 2270
    vr = 2271
    vS = 2272
    vs = 2273
    vT = 2274
    vt = 2275
    vU = 2276
    vu = 2277
    vV = 2278
    vv = 2279
    vW = 2280
    vw = 2281
    vX = 2282
    vx = 2283
    vY = 2284
    vy = 2285
    vZ = 2286
    vz = 2287
    WA = 2288
    Wa = 2289
    WB = 2290
    Wb = 2291
    WC = 2292
    Wc = 2293
    WD = 2294
    Wd = 2295
    WE = 2296
    We = 2297
    WF = 2298
    Wf = 2299
    WG = 2300
    Wg = 2301
    WH = 2302
    Wh = 2303
    WI = 2304
    Wi = 2305
    WJ = 2306
    Wj = 2307
    WK = 2308
    Wk = 2309
    WL = 2310
    Wl = 2311
    WM = 2312
    Wm = 2313
    WN = 2314
    Wn = 2315
    WO = 2316
    Wo = 2317
    WP = 2318
    Wp = 2319
    WQ = 2320
    Wq = 2321
    WR = 2322
    Wr = 2323
    WS = 2324
    Ws = 2325
    WT = 2326
    Wt = 2327
    WU = 2328
    Wu = 2329
    WV = 2330
    Wv = 2331
    WW = 2332
    Ww = 2333
    WX = 2334
    Wx = 2335
    WY = 2336
    Wy = 2337
    WZ = 2338
    Wz = 2339
    wA = 2340
    wa = 2341
    wB = 2342
    wb = 2343
    wC = 2344
    wc = 2345
    wD = 2346
    wd = 2347
    wE = 2348
    we = 2349
    wF = 2350
    wf = 2351
    wG = 2352
    wg = 2353
    wH = 2354
    wh = 2355
    wI = 2356
    wi = 2357
    wJ = 2358
    wj = 2359
    wK = 2360
    wk = 2361
    wL = 2362
    wl = 2363
    wM = 2364
    wm = 2365
    wN = 2366
    wn = 2367
    wO = 2368
    wo = 2369
    wP = 2370
    wp = 2371
    wQ = 2372
    wq = 2373
    wR = 2374
    wr = 2375
    wS = 2376
    ws = 2377
    wT = 2378
    wt = 2379
    wU = 2380
    wu = 2381
    wV = 2382
    wv = 2383
    wW = 2384
    ww = 2385
    wX = 2386
    wx = 2387
    wY = 2388
    wy = 2389
    wZ = 2390
    wz = 2391
    XA = 2392
    Xa = 2393
    XB = 2394
    Xb = 2395
    XC = 2396
    Xc = 2397
    XD = 2398
    Xd = 2399
    XE = 2400
    Xe = 2401
    XF = 2402
    Xf = 2403
    XG = 2404
    Xg = 2405
    XH = 2406
    Xh = 2407
    XI = 2408
    Xi = 2409
    XJ = 2410
    Xj = 2411
    XK = 2412
    Xk = 2413
    XL = 2414
    Xl = 2415
    XM = 2416
    Xm = 2417
    XN = 2418
    Xn = 2419
    XO = 2420
    Xo = 2421
    XP = 2422
    Xp = 2423
    XQ = 2424
    Xq = 2425
    XR = 2426
    Xr = 2427
    XS = 2428
    Xs = 2429
    XT = 2430
    Xt = 2431
    XU = 2432
    Xu = 2433
    XV = 2434
    Xv = 2435
    XW = 2436
    Xw = 2437
    XX = 2438
    Xx = 2439
    XY = 2440
    Xy = 2441
    XZ = 2442
    Xz = 2443
    xA = 2444
    xa = 2445
    xB = 2446
    xb = 2447
    xC = 2448
    xc = 2449
    xD = 2450
    xd = 2451
    xE = 2452
    xe = 2453
    xF = 2454
    xf = 2455
    xG = 2456
    xg = 2457
    xH = 2458
    xh = 2459
    xI = 2460
    xi = 2461
    xJ = 2462
    xj = 2463
    xK = 2464
    xk = 2465
    xL = 2466
    xl = 2467
    xM = 2468
    xm = 2469
    xN = 2470
    xn = 2471
    xO = 2472
    xo = 2473
    xP = 2474
    xp = 2475
    xQ = 2476
    xq = 2477
    xR = 2478
    xr = 2479
    xS = 2480
    xs = 2481
    xT = 2482
    xt = 2483
    xU = 2484
    xu = 2485
    xV = 2486
    xv = 2487
    xW = 2488
    xw = 2489
    xX = 2490
    xx = 2491
    xY = 2492
    xy = 2493
    xZ = 2494
    xz = 2495
    YA = 2496
    Ya = 2497
    YB = 2498
    Yb = 2499
    YC = 2500
    Yc = 2501
    YD = 2502
    Yd = 2503
    YE = 2504
    Ye = 2505
    YF = 2506
    Yf = 2507
    YG = 2508
    Yg = 2509
    YH = 2510
    Yh = 2511
    YI = 2512
    Yi = 2513
    YJ = 2514
    Yj = 2515
    YK = 2516
    Yk = 2517
    YL = 2518
    Yl = 2519
    YM = 2520
    Ym = 2521
    YN = 2522
    Yn = 2523
    YO = 2524
    Yo = 2525
    YP = 2526
    Yp = 2527
    YQ = 2528
    Yq = 2529
    YR = 2530
    Yr = 2531
    YS = 2532
    Ys = 2533
    YT = 2534
    Yt = 2535
    YU = 2536
    Yu = 2537
    YV = 2538
    Yv = 2539
    YW = 2540
    Yw = 2541
    YX = 2542
    Yx = 2543
    YY = 2544
    Yy = 2545
    YZ = 2546
    Yz = 2547
    yA = 2548
    ya = 2549
    yB = 2550
    yb = 2551
    yC = 2552
    yc = 2553
    yD = 2554
    yd = 2555
    yE = 2556
    ye = 2557
    yF = 2558
    yf = 2559
    yG = 2560
    yg = 2561
    yH = 2562
    yh = 2563
    yI = 2564
    yi = 2565
    yJ = 2566
    yj = 2567
    yK = 2568
    yk = 2569
    yL = 2570
    yl = 2571
    yM = 2572
    ym = 2573
    yN = 2574
    yn = 2575
    yO = 2576
    yo = 2577
    yP = 2578
    yp = 2579
    yQ = 2580
    yq = 2581
    yR = 2582
    yr = 2583
    yS = 2584
    ys = 2585
    yT = 2586
    yt = 2587
    yU = 2588
    yu = 2589
    yV = 2590
    yv = 2591
    yW = 2592
    yw = 2593
    yX = 2594
    yx = 2595
    yY = 2596
    yy = 2597
    yZ = 2598
    yz = 2599
    ZA = 2600
    Za = 2601
    ZB = 2602
    Zb = 2603
    ZC = 2604
    Zc = 2605
    ZD = 2606
    Zd = 2607
    ZE = 2608
    Ze = 2609
    ZF = 2610
    Zf = 2611
    ZG = 2612
    Zg = 2613
    ZH = 2614
    Zh = 2615
    ZI = 2616
    Zi = 2617
    ZJ = 2618
    Zj = 2619
    ZK = 2620
    Zk = 2621
    ZL = 2622
    Zl = 2623
    ZM = 2624
    Zm = 2625
    ZN = 2626
    Zn = 2627
    ZO = 2628
    Zo = 2629
    ZP = 2630
    Zp = 2631
    ZQ = 2632
    Zq = 2633
    ZR = 2634
    Zr = 2635
    ZS = 2636
    Zs = 2637
    ZT = 2638
    Zt = 2639
    ZU = 2640
    Zu = 2641
    ZV = 2642
    Zv = 2643
    ZW = 2644
    Zw = 2645
    ZX = 2646
    Zx = 2647
    ZY = 2648
    Zy = 2649
    ZZ = 2650
    Zz = 2651
    zA = 2652
    za = 2653
    zB = 2654
    zb = 2655
    zC = 2656
    zc = 2657
    zD = 2658
    zd = 2659
    zE = 2660
    ze = 2661
    zF = 2662
    zf = 2663
    zG = 2664
    zg = 2665
    zH = 2666
    zh = 2667
    zI = 2668
    zi = 2669
    zJ = 2670
    zj = 2671
    zK = 2672
    zk = 2673
    zL = 2674
    zl = 2675
    zM = 2676
    zm = 2677
    zN = 2678
    zn = 2679
    zO = 2680
    zo = 2681
    zP = 2682
    zp = 2683
    zQ = 2684
    zq = 2685
    zR = 2686
    zr = 2687
    zS = 2688
    zs = 2689
    zT = 2690
    zt = 2691
    zU = 2692
    zu = 2693
    zV = 2694
    zv = 2695
    zW = 2696
    zw = 2697
    zX = 2698
    zx = 2699
    zY = 2700
    zy = 2701
    zZ = 2702
    zz = 2703
    aAA = 2704
    aAa = 2705
    aAB = 2706
    aAb = 2707
    aAC = 2708
    aAc = 2709
    aAD = 2710
    aAd = 2711
    aAE = 2712
    aAe = 2713
    aAF = 2714
    aAf = 2715
    aAG = 2716
    aAg = 2717
    aAH = 2718
    aAh = 2719
    aAI = 2720
    aAi = 2721
    aAJ = 2722
    aAj = 2723
    aAK = 2724
    aAk = 2725
    aAL = 2726
    aAl = 2727
    aAM = 2728
    aAm = 2729
    aAN = 2730
    aAn = 2731
    aAO = 2732
    aAo = 2733
    aAP = 2734
    aAp = 2735
    aAQ = 2736
    aAq = 2737
    aAR = 2738
    aAr = 2739
    aAS = 2740
    aAs = 2741
    aAT = 2742
    aAt = 2743
    aAU = 2744
    aAu = 2745
    aAV = 2746
    aAv = 2747
    aAW = 2748
    aAw = 2749
    aAX = 2750
    aAx = 2751
    aAY = 2752
    aAy = 2753
    aAZ = 2754
    aAz = 2755
    aaA = 2756
    aaa = 2757
    aaB = 2758
    aab = 2759
    aaC = 2760
    aac = 2761
    aaD = 2762
    aad = 2763
    aaE = 2764
    aae = 2765
    aaF = 2766
    aaf = 2767
    aaG = 2768
    aag = 2769
    aaH = 2770
    aah = 2771
    aaI = 2772
    aai = 2773
    aaJ = 2774
    aaj = 2775
    aaK = 2776
    aak = 2777
    aaL = 2778
    aal = 2779
    aaM = 2780
    aam = 2781
    aaN = 2782
    aan = 2783
    aaO = 2784
    aao = 2785
    aaP = 2786
    aap = 2787
    aaQ = 2788
    aaq = 2789
    aaR = 2790
    aar = 2791
    aaS = 2792
    aas = 2793
    aaT = 2794
    aat = 2795
    aaU = 2796
    aau = 2797
    aaV = 2798
    aav = 2799
    aaW = 2800
    aaw = 2801
    aaX = 2802
    aax = 2803
    aaY = 2804
    aay = 2805
    aaZ = 2806
    aaz = 2807
    aBA = 2808
    aBa = 2809
    aBB = 2810
    aBb = 2811
    aBC = 2812
    aBc = 2813
    aBD = 2814
    aBd = 2815
    aBE = 2816
    aBe = 2817
    aBF = 2818
    aBf = 2819
    aBG = 2820
    aBg = 2821
    aBH = 2822
    aBh = 2823
    aBI = 2824
    aBi = 2825
    aBJ = 2826
    aBj = 2827
    aBK = 2828
    aBk = 2829
    aBL = 2830
    aBl = 2831
    aBM = 2832
    aBm = 2833
    aBN = 2834
    aBn = 2835
    aBO = 2836
    aBo = 2837
    aBP = 2838
    aBp = 2839
    aBQ = 2840
    aBq = 2841
    aBR = 2842
    aBr = 2843
    aBS = 2844
    aBs = 2845
    aBT = 2846
    aBt = 2847
    aBU = 2848
    aBu = 2849
    aBV = 2850
    aBv = 2851
    aBW = 2852
    aBw = 2853
    aBX = 2854
    aBx = 2855
    aBY = 2856
    aBy = 2857
    aBZ = 2858
    aBz = 2859
    abA = 2860
    aba = 2861
    abB = 2862
    abb = 2863
    abC = 2864
    abc = 2865
    abD = 2866
    abd = 2867
    abE = 2868
    abe = 2869
    abF = 2870
    abf = 2871
    abG = 2872
    abg = 2873
    abH = 2874
    abh = 2875
    abI = 2876
    abi = 2877
    abJ = 2878
    abj = 2879
    abK = 2880
    abk = 2881
    abL = 2882
    abl = 2883
    abM = 2884
    abm = 2885
    abN = 2886
    abn = 2887
    abO = 2888
    abo = 2889
    abP = 2890
    abp = 2891
    abQ = 2892
    abq = 2893
    abR = 2894
    abr = 2895
    abS = 2896
    abs = 2897
    abT = 2898
    abt = 2899
    abU = 2900
    abu = 2901
    abV = 2902
    abv = 2903
    abW = 2904
    abw = 2905
    abX = 2906
    abx = 2907
    abY = 2908
    aby = 2909
    abZ = 2910
    abz = 2911
    aCA = 2912
    aCa = 2913
    aCB = 2914
    aCb = 2915
    aCC = 2916
    aCc = 2917
    aCD = 2918
    aCd = 2919
    aCE = 2920
    aCe = 2921
    aCF = 2922
    aCf = 2923
    aCG = 2924
    aCg = 2925
    aCH = 2926
    aCh = 2927
    aCI = 2928
    aCi = 2929
    aCJ = 2930
    aCj = 2931
    aCK = 2932
    aCk = 2933
    aCL = 2934
    aCl = 2935
    aCM = 2936
    aCm = 2937
    aCN = 2938
    aCn = 2939
    aCO = 2940
    aCo = 2941
    aCP = 2942
    aCp = 2943
    aCQ = 2944
    aCq = 2945
    aCR = 2946
    aCr = 2947
    aCS = 2948
    aCs = 2949
    aCT = 2950
    aCt = 2951
    aCU = 2952
    aCu = 2953
    aCV = 2954
    aCv = 2955
    aCW = 2956
    aCw = 2957
    aCX = 2958
    aCx = 2959
    aCY = 2960
    aCy = 2961
    aCZ = 2962
    aCz = 2963
    acA = 2964
    aca = 2965
    acB = 2966
    acb = 2967
    acC = 2968
    acc = 2969
    acD = 2970
    acd = 2971
    acE = 2972
    ace = 2973
    acF = 2974
    acf = 2975
    acG = 2976
    acg = 2977
    acH = 2978
    ach = 2979
    acI = 2980
    aci = 2981
    acJ = 2982
    acj = 2983
    acK = 2984
    ack = 2985
    acL = 2986
    acl = 2987
    acM = 2988
    acm = 2989
    acN = 2990
    acn = 2991
    acO = 2992
    aco = 2993
    acP = 2994
    acp = 2995
    acQ = 2996
    acq = 2997
    acR = 2998
    acr = 2999
    acS = 3000
    acs = 3001
    acT = 3002
    act = 3003

class Club(IntEnum):
    None_ = 0
    Engineer = 1
    CleanNClearing = 2
    KnightsHospitaller = 3
    IndeGEHENNA = 4
    IndeMILLENNIUM = 5
    IndeHyakkiyako = 6
    IndeShanhaijing = 7
    IndeTrinity = 8
    FoodService = 9
    Countermeasure = 10
    BookClub = 11
    MatsuriOffice = 12
    GourmetClub = 13
    HoukagoDessert = 14
    RedwinterSecretary = 15
    Schale = 16
    TheSeminar = 17
    AriusSqud = 18
    Justice = 19
    Fuuki = 20
    Kohshinjo68 = 21
    Meihuayuan = 22
    SisterHood = 23
    GameDev = 24
    anzenkyoku = 25
    RemedialClass = 26
    SPTF = 27
    TrinityVigilance = 28
    Veritas = 29
    TrainingClub = 30
    Onmyobu = 31
    Shugyobu = 32
    Endanbou = 33
    NinpoKenkyubu = 34
    Class227 = 35
    EmptyClub = 36
    Emergentology = 37
    RabbitPlatoon = 38
    PandemoniumSociety = 39
    HotSpringsDepartment = 40
    TeaParty = 41
    PublicPeaceBureau = 42
    Genryumon = 43
    BlackTortoisePromenade = 44
    LaborParty = 45
    KnowledgeLiberationFront = 46
    Hyakkayouran = 47
    ShinySparkleSociety = 48
    AbydosStudentCouncil = 49
    CentralControlCenter = 50
    FreightLogisticsDepartment = 51

class UnderCoverItemCategory(IntEnum):
    Consumable = 0
    Interaction = 1
    Skill = 2
    Collection = 3


def dump_GroundVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_AcademyFavorScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "ScheduleGroupId": convert_long(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_long(excel_instance.OrderInGroup(), password),
        "Location": convert_string(excel_instance.Location(), password),
        "LocalizeScenarioId": convert_uint(excel_instance.LocalizeScenarioId(), password),
        "FavorRank": convert_long(excel_instance.FavorRank(), password),
        "SecretStoneAmount": convert_long(excel_instance.SecretStoneAmount(), password),
        "ScenarioSriptGroupId": convert_long(excel_instance.ScenarioSriptGroupId(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_AcademyLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPath(), password),
        "IconImagePath": convert_string(excel_instance.IconImagePath(), password),
        "OpenCondition": [School(convert_int(excel_instance.OpenCondition(j), password)).name for j in range(excel_instance.OpenConditionLength())],
        "OpenConditionCount": [convert_long(excel_instance.OpenConditionCount(j), password) for j in range(excel_instance.OpenConditionCountLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "OpenTeacherRank": convert_long(excel_instance.OpenTeacherRank(), password),
    }

def dump_AcademyLocationRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Rank": convert_long(excel_instance.Rank(), password),
        "RankExp": convert_long(excel_instance.RankExp(), password),
        "TotalExp": convert_long(excel_instance.TotalExp(), password),
    }

def dump_AcademyMessanger1Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_long(excel_instance.MessageGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_long(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_long(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_long(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_long(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_long(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_long(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessanger2Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_long(excel_instance.MessageGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_long(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_long(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_long(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_long(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_long(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_long(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessanger3Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_long(excel_instance.MessageGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_long(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_long(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_long(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_long(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_long(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_long(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessangerExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_long(excel_instance.MessageGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_long(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_long(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_long(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_long(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_long(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_long(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.Location(), password),
        "ScheduleGroupId": convert_long(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_long(excel_instance.OrderInGroup(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTexture(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocationRank": convert_long(excel_instance.LocationRank(), password),
        "FavorExp": convert_long(excel_instance.FavorExp(), password),
        "SecretStoneAmount": convert_long(excel_instance.SecretStoneAmount(), password),
        "SecretStoneProb": convert_long(excel_instance.SecretStoneProb(), password),
        "ExtraFavorExp": convert_long(excel_instance.ExtraFavorExp(), password),
        "ExtraFavorExpProb": convert_long(excel_instance.ExtraFavorExpProb(), password),
        "ExtraRewardParcelType": [ParcelType(convert_int(excel_instance.ExtraRewardParcelType(j), password)).name for j in range(excel_instance.ExtraRewardParcelTypeLength())],
        "ExtraRewardParcelId": [convert_long(excel_instance.ExtraRewardParcelId(j), password) for j in range(excel_instance.ExtraRewardParcelIdLength())],
        "ExtraRewardAmount": [convert_long(excel_instance.ExtraRewardAmount(j), password) for j in range(excel_instance.ExtraRewardAmountLength())],
        "ExtraRewardProb": [convert_long(excel_instance.ExtraRewardProb(j), password) for j in range(excel_instance.ExtraRewardProbLength())],
        "IsExtraRewardDisplayed": [excel_instance.IsExtraRewardDisplayed(j) for j in range(excel_instance.IsExtraRewardDisplayedLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_AcademyTicketExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocationRankSum": convert_long(excel_instance.LocationRankSum(), password),
        "ScheduleTicktetMax": convert_long(excel_instance.ScheduleTicktetMax(), password),
    }

def dump_AcademyZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocationId": convert_long(excel_instance.LocationId(), password),
        "LocationRankForUnlock": convert_long(excel_instance.LocationRankForUnlock(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StudentVisitProb": [convert_long(excel_instance.StudentVisitProb(j), password) for j in range(excel_instance.StudentVisitProbLength())],
        "RewardGroupId": convert_long(excel_instance.RewardGroupId(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
    }

def dump_AnimationBlendTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BlendData(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BlendData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": convert_int(excel_instance.Type(), password),
        "InfoList": [dump_BlendInfo(excel_instance.InfoList(j), password) for j in range(excel_instance.InfoListLength())],
    }

def dump_BlendInfo(excel_instance, password: bytes = b"") -> dict:
    return {
        "From": convert_int(excel_instance.From(), password),
        "To": convert_int(excel_instance.To(), password),
        "Blend": convert_float(excel_instance.Blend(), password),
    }

def dump_AnimatorDataTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AnimatorData(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AnimatorData(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultStateName": convert_string(excel_instance.DefaultStateName(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "DataList": [dump_AniStateData(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AniStateData(excel_instance, password: bytes = b"") -> dict:
    return {
        "StateName": convert_string(excel_instance.StateName(), password),
        "StatePrefix": convert_string(excel_instance.StatePrefix(), password),
        "StateNameWithPrefix": convert_string(excel_instance.StateNameWithPrefix(), password),
        "Tag": convert_string(excel_instance.Tag(), password),
        "SpeedParameterName": convert_string(excel_instance.SpeedParameterName(), password),
        "SpeedParamter": convert_float(excel_instance.SpeedParamter(), password),
        "StateSpeed": convert_float(excel_instance.StateSpeed(), password),
        "ClipName": convert_string(excel_instance.ClipName(), password),
        "Length": convert_float(excel_instance.Length(), password),
        "FrameRate": convert_float(excel_instance.FrameRate(), password),
        "IsLooping": excel_instance.IsLooping(),
        "Events": [dump_AniEventData(excel_instance.Events(j), password) for j in range(excel_instance.EventsLength())],
    }

def dump_AniEventData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Time": convert_float(excel_instance.Time(), password),
        "IntParam": convert_int(excel_instance.IntParam(), password),
        "FloatParam": convert_float(excel_instance.FloatParam(), password),
        "StringParam": convert_string(excel_instance.StringParam(), password),
    }

def dump_ArenaLevelSectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ArenaSeasonId": convert_long(excel_instance.ArenaSeasonId(), password),
        "StartLevel": convert_long(excel_instance.StartLevel(), password),
        "LastLevel": convert_long(excel_instance.LastLevel(), password),
        "UserCount": convert_long(excel_instance.UserCount(), password),
    }

def dump_ArenaMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "TerrainType": convert_long(excel_instance.TerrainType(), password),
        "TerrainTypeLocalizeKey": convert_string(excel_instance.TerrainTypeLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "GroundGroupId": convert_long(excel_instance.GroundGroupId(), password),
        "GroundGroupNameLocalizeKey": convert_string(excel_instance.GroundGroupNameLocalizeKey(), password),
        "StartRank": convert_long(excel_instance.StartRank(), password),
        "EndRank": convert_long(excel_instance.EndRank(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
    }

def dump_ArenaNPCExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Rank": convert_long(excel_instance.Rank(), password),
        "NPCAccountLevel": convert_long(excel_instance.NPCAccountLevel(), password),
        "NPCLevel": convert_long(excel_instance.NPCLevel(), password),
        "NPCLevelDeviation": convert_long(excel_instance.NPCLevelDeviation(), password),
        "NPCStarGrade": convert_long(excel_instance.NPCStarGrade(), password),
        "ExceptionCharacterRarities": [Rarity(convert_int(excel_instance.ExceptionCharacterRarities(j), password)).name for j in range(excel_instance.ExceptionCharacterRaritiesLength())],
        "ExceptionMainCharacterIds": [convert_long(excel_instance.ExceptionMainCharacterIds(j), password) for j in range(excel_instance.ExceptionMainCharacterIdsLength())],
        "ExceptionSupportCharacterIds": [convert_long(excel_instance.ExceptionSupportCharacterIds(j), password) for j in range(excel_instance.ExceptionSupportCharacterIdsLength())],
        "ExceptionTSSIds": [convert_long(excel_instance.ExceptionTSSIds(j), password) for j in range(excel_instance.ExceptionTSSIdsLength())],
    }

def dump_ArenaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "ArenaRewardType": ArenaRewardType(convert_int(excel_instance.ArenaRewardType(), password)).name,
        "RankStart": convert_long(excel_instance.RankStart(), password),
        "RankEnd": convert_long(excel_instance.RankEnd(), password),
        "RankIconPath": convert_string(excel_instance.RankIconPath(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_long(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueName(j), password) for j in range(excel_instance.RewardParcelUniqueNameLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_ArenaSeasonCloseRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "RankStart": convert_long(excel_instance.RankStart(), password),
        "RankEnd": convert_long(excel_instance.RankEnd(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_long(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueName(j), password) for j in range(excel_instance.RewardParcelUniqueNameLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_ArenaSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDate(), password),
        "SeasonGroupLimit": convert_long(excel_instance.SeasonGroupLimit(), password),
        "PrevSeasonId": convert_long(excel_instance.PrevSeasonId(), password),
    }

def dump_BattleLevelFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "DamageRate": convert_long(excel_instance.DamageRate(), password),
    }

def dump_BossExternalBTExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ExternalBTId": convert_long(excel_instance.ExternalBTId(), password),
        "AIPhase": convert_long(excel_instance.AIPhase(), password),
        "ExternalBTNodeType": ExternalBTNodeType(convert_int(excel_instance.ExternalBTNodeType(), password)).name,
        "ExternalBTTrigger": ExternalBTTrigger(convert_int(excel_instance.ExternalBTTrigger(), password)).name,
        "TriggerArgument": convert_string(excel_instance.TriggerArgument(), password),
        "BehaviorRate": convert_long(excel_instance.BehaviorRate(), password),
        "ExternalBehavior": ExternalBehavior(convert_int(excel_instance.ExternalBehavior(), password)).name,
        "BehaviorArgument": convert_string(excel_instance.BehaviorArgument(), password),
    }

def dump_BossPhaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "AIPhase": convert_long(excel_instance.AIPhase(), password),
        "NormalAttackSkillUniqueName": convert_string(excel_instance.NormalAttackSkillUniqueName(), password),
        "UseExSkill": [excel_instance.UseExSkill(j) for j in range(excel_instance.UseExSkillLength())],
    }

def dump_BuffParticleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "UniqueName": convert_string(excel_instance.UniqueName(), password),
        "BuffType": convert_string(excel_instance.BuffType(), password),
        "BuffName": convert_string(excel_instance.BuffName(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_BulletArmorDamageFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupId(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorType(), password)).name,
        "DamageRate": convert_long(excel_instance.DamageRate(), password),
        "DamageAttribute": DamageAttribute(convert_int(excel_instance.DamageAttribute(), password)).name,
        "MinDamageRate": convert_long(excel_instance.MinDamageRate(), password),
        "MaxDamageRate": convert_long(excel_instance.MaxDamageRate(), password),
        "ShowHighlightFloater": excel_instance.ShowHighlightFloater(),
    }

def dump_CafeInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_long(excel_instance.CafeId(), password),
        "IsDefault": excel_instance.IsDefault(),
        "OpenConditionCafeId": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeId(), password)).name,
        "OpenConditionCafeInvite": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeInvite(), password)).name,
    }

def dump_CafeInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "IgnoreIfUnobtained": excel_instance.IgnoreIfUnobtained(),
        "IgnoreIfUnobtainedStartDate": convert_string(excel_instance.IgnoreIfUnobtainedStartDate(), password),
        "IgnoreIfUnobtainedEndDate": convert_string(excel_instance.IgnoreIfUnobtainedEndDate(), password),
        "BubbleType": [BubbleType(convert_int(excel_instance.BubbleType(j), password)).name for j in range(excel_instance.BubbleTypeLength())],
        "BubbleDuration": [convert_long(excel_instance.BubbleDuration(j), password) for j in range(excel_instance.BubbleDurationLength())],
        "FavorEmoticonRewardParcelType": ParcelType(convert_int(excel_instance.FavorEmoticonRewardParcelType(), password)).name,
        "FavorEmoticonRewardId": convert_long(excel_instance.FavorEmoticonRewardId(), password),
        "FavorEmoticonRewardAmount": convert_long(excel_instance.FavorEmoticonRewardAmount(), password),
        "CafeCharacterState": [convert_string(excel_instance.CafeCharacterState(j), password) for j in range(excel_instance.CafeCharacterStateLength())],
    }

def dump_CafeProductionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_long(excel_instance.CafeId(), password),
        "Rank": convert_long(excel_instance.Rank(), password),
        "CafeProductionParcelType": ParcelType(convert_int(excel_instance.CafeProductionParcelType(), password)).name,
        "CafeProductionParcelId": convert_long(excel_instance.CafeProductionParcelId(), password),
        "ParcelProductionCoefficient": convert_long(excel_instance.ParcelProductionCoefficient(), password),
        "ParcelProductionCorrectionValue": convert_long(excel_instance.ParcelProductionCorrectionValue(), password),
        "ParcelStorageMax": convert_long(excel_instance.ParcelStorageMax(), password),
    }

def dump_CafeRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_long(excel_instance.CafeId(), password),
        "Rank": convert_long(excel_instance.Rank(), password),
        "RecipeId": convert_long(excel_instance.RecipeId(), password),
        "ComfortMax": convert_long(excel_instance.ComfortMax(), password),
        "TagCountMax": convert_long(excel_instance.TagCountMax(), password),
        "CharacterVisitMin": convert_int(excel_instance.CharacterVisitMin(), password),
        "CharacterVisitMax": convert_int(excel_instance.CharacterVisitMax(), password),
        "CafeVisitWeightBase": convert_int(excel_instance.CafeVisitWeightBase(), password),
        "CafeVisitWeightTagBonusStep": [convert_int(excel_instance.CafeVisitWeightTagBonusStep(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusStepLength())],
        "CafeVisitWeightTagBonus": [convert_int(excel_instance.CafeVisitWeightTagBonus(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusLength())],
    }

def dump_CampaignChapterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "NormalImagePath": convert_string(excel_instance.NormalImagePath(), password),
        "HardImagePath": convert_string(excel_instance.HardImagePath(), password),
        "Order": convert_long(excel_instance.Order(), password),
        "PreChapterId": [convert_long(excel_instance.PreChapterId(j), password) for j in range(excel_instance.PreChapterIdLength())],
        "ChapterRewardId": convert_long(excel_instance.ChapterRewardId(), password),
        "ChapterHardRewardId": convert_long(excel_instance.ChapterHardRewardId(), password),
        "ChapterVeryHardRewardId": convert_long(excel_instance.ChapterVeryHardRewardId(), password),
        "NormalCampaignStageId": [convert_long(excel_instance.NormalCampaignStageId(j), password) for j in range(excel_instance.NormalCampaignStageIdLength())],
        "NormalExtraStageId": [convert_long(excel_instance.NormalExtraStageId(j), password) for j in range(excel_instance.NormalExtraStageIdLength())],
        "HardCampaignStageId": [convert_long(excel_instance.HardCampaignStageId(j), password) for j in range(excel_instance.HardCampaignStageIdLength())],
        "VeryHardCampaignStageId": [convert_long(excel_instance.VeryHardCampaignStageId(j), password) for j in range(excel_instance.VeryHardCampaignStageIdLength())],
        "IsTacticSkip": excel_instance.IsTacticSkip(),
    }

def dump_CampaignChapterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CampaignChapterStar": convert_long(excel_instance.CampaignChapterStar(), password),
        "ChapterRewardParcelType": [ParcelType(convert_int(excel_instance.ChapterRewardParcelType(j), password)).name for j in range(excel_instance.ChapterRewardParcelTypeLength())],
        "ChapterRewardId": [convert_long(excel_instance.ChapterRewardId(j), password) for j in range(excel_instance.ChapterRewardIdLength())],
        "ChapterRewardAmount": [convert_int(excel_instance.ChapterRewardAmount(j), password) for j in range(excel_instance.ChapterRewardAmountLength())],
    }

def dump_CampaignStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Deprecated": excel_instance.Deprecated(),
        "Name": convert_string(excel_instance.Name(), password),
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "CleardScenarioId": convert_long(excel_instance.CleardScenarioId(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_long(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_long(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_long(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_long(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "CampaignStageRewardId": convert_long(excel_instance.CampaignStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "RecommandLevelGapForGuide": convert_int(excel_instance.RecommandLevelGapForGuide(), password),
        "MinEquipmentTierForGuide": [convert_long(excel_instance.MinEquipmentTierForGuide(j), password) for j in range(excel_instance.MinEquipmentTierForGuideLength())],
        "MinSkillLevelForGuide": [convert_long(excel_instance.MinSkillLevelForGuide(j), password) for j in range(excel_instance.MinSkillLevelForGuideLength())],
        "BgmId": convert_string(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "StrategySkipGroundId": convert_int(excel_instance.StrategySkipGroundId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
        "TacticRewardExp": convert_long(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_CampaignStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "StageRewardProb": convert_int(excel_instance.StageRewardProb(), password),
        "StageRewardParcelType": ParcelType(convert_int(excel_instance.StageRewardParcelType(), password)).name,
        "StageRewardId": convert_long(excel_instance.StageRewardId(), password),
        "StageRewardAmount": convert_int(excel_instance.StageRewardAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_CampaignStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyObjectType": StrategyObjectType(convert_int(excel_instance.StrategyObjectType(), password)).name,
        "StrategyRewardParcelType": ParcelType(convert_int(excel_instance.StrategyRewardParcelType(), password)).name,
        "StrategyRewardID": convert_long(excel_instance.StrategyRewardID(), password),
        "StrategyRewardName": convert_string(excel_instance.StrategyRewardName(), password),
        "StrategyRewardAmount": convert_int(excel_instance.StrategyRewardAmount(), password),
        "StrategySightRange": convert_long(excel_instance.StrategySightRange(), password),
        "PortalId": convert_int(excel_instance.PortalId(), password),
        "HealValue": convert_int(excel_instance.HealValue(), password),
        "SwithId": convert_int(excel_instance.SwithId(), password),
        "BuffId": convert_int(excel_instance.BuffId(), password),
        "Disposable": excel_instance.Disposable(),
    }

def dump_CampaignUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabName(), password),
        "EnterScenarioGroupId": [convert_long(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_long(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "MoveRange": convert_int(excel_instance.MoveRange(), password),
        "AIMoveType": StrategyAIType(convert_int(excel_instance.AIMoveType(), password)).name,
        "Grade": HexaUnitGrade(convert_int(excel_instance.Grade(), password)).name,
        "EnvironmentType": TacticEnvironment(convert_int(excel_instance.EnvironmentType(), password)).name,
        "Scale": convert_float(excel_instance.Scale(), password),
        "IsTacticSkip": excel_instance.IsTacticSkip(),
    }

def dump_CharacterAcademyTagsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "FavorTags": [Tag(convert_int(excel_instance.FavorTags(j), password)).name for j in range(excel_instance.FavorTagsLength())],
        "FavorItemTags": [Tag(convert_int(excel_instance.FavorItemTags(j), password)).name for j in range(excel_instance.FavorItemTagsLength())],
        "FavorItemUniqueTags": [Tag(convert_int(excel_instance.FavorItemUniqueTags(j), password)).name for j in range(excel_instance.FavorItemUniqueTagsLength())],
        "ForbiddenTags": [Tag(convert_int(excel_instance.ForbiddenTags(j), password)).name for j in range(excel_instance.ForbiddenTagsLength())],
        "ZoneWhiteListTags": [Tag(convert_int(excel_instance.ZoneWhiteListTags(j), password)).name for j in range(excel_instance.ZoneWhiteListTagsLength())],
    }

def dump_CharacterAIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EngageType": EngageType(convert_int(excel_instance.EngageType(), password)).name,
        "Positioning": PositioningType(convert_int(excel_instance.Positioning(), password)).name,
        "CheckCanUseAutoSkill": excel_instance.CheckCanUseAutoSkill(),
        "DistanceReduceRatioObstaclePath": convert_long(excel_instance.DistanceReduceRatioObstaclePath(), password),
        "DistanceReduceObstaclePath": convert_long(excel_instance.DistanceReduceObstaclePath(), password),
        "DistanceReduceRatioFormationPath": convert_long(excel_instance.DistanceReduceRatioFormationPath(), password),
        "DistanceReduceFormationPath": convert_long(excel_instance.DistanceReduceFormationPath(), password),
        "MinimumPositionGap": convert_long(excel_instance.MinimumPositionGap(), password),
        "CanUseObstacleOfKneelMotion": excel_instance.CanUseObstacleOfKneelMotion(),
        "CanUseObstacleOfStandMotion": excel_instance.CanUseObstacleOfStandMotion(),
        "HasTargetSwitchingMotion": excel_instance.HasTargetSwitchingMotion(),
    }

def dump_CharacterCalculationLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "CalculationValue": BattleCalculationStat(convert_int(excel_instance.CalculationValue(), password)).name,
        "MinValue": convert_long(excel_instance.MinValue(), password),
        "MaxValue": convert_long(excel_instance.MaxValue(), password),
        "LimitStartValue": [convert_long(excel_instance.LimitStartValue(j), password) for j in range(excel_instance.LimitStartValueLength())],
        "DecreaseRate": [convert_long(excel_instance.DecreaseRate(j), password) for j in range(excel_instance.DecreaseRateLength())],
    }

def dump_CharacterCombatSkinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": convert_string(excel_instance.DialogType(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "HideUI": excel_instance.HideUI(),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterDialogFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "Phase": convert_int(excel_instance.Phase(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": FieldDialogType(convert_int(excel_instance.DialogType(), password)).name,
        "Duration": convert_long(excel_instance.Duration(), password),
        "MotionName": convert_string(excel_instance.MotionName(), password),
        "IsInteractionDialog": excel_instance.IsInteractionDialog(),
        "HideUI": excel_instance.HideUI(),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostumeGroupId": convert_long(excel_instance.CostumeGroupId(), password),
        "IsPlayable": excel_instance.IsPlayable(),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "CollectionVisible": excel_instance.CollectionVisible(),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "IsPlayableCharacter": excel_instance.IsPlayableCharacter(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "IsNPC": excel_instance.IsNPC(),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "CanSurvive": excel_instance.CanSurvive(),
        "IsDummy": excel_instance.IsDummy(),
        "SubPartsCount": convert_int(excel_instance.SubPartsCount(), password),
        "TacticRole": TacticRole(convert_int(excel_instance.TacticRole(), password)).name,
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "TacticRange": TacticRange(convert_int(excel_instance.TacticRange(), password)).name,
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorType(), password)).name,
        "AimIKType": AimIKType(convert_int(excel_instance.AimIKType(), password)).name,
        "School": School(convert_int(excel_instance.School(), password)).name,
        "Club": Club(convert_int(excel_instance.Club(), password)).name,
        "DefaultStarGrade": convert_int(excel_instance.DefaultStarGrade(), password),
        "MaxStarGrade": convert_int(excel_instance.MaxStarGrade(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "SquadType": SquadType(convert_int(excel_instance.SquadType(), password)).name,
        "Jumpable": excel_instance.Jumpable(),
        "PersonalityId": convert_long(excel_instance.PersonalityId(), password),
        "CharacterAIId": convert_long(excel_instance.CharacterAIId(), password),
        "ExternalBTId": convert_long(excel_instance.ExternalBTId(), password),
        "MainCombatStyleId": convert_long(excel_instance.MainCombatStyleId(), password),
        "CombatStyleIndex": convert_int(excel_instance.CombatStyleIndex(), password),
        "ScenarioCharacter": convert_string(excel_instance.ScenarioCharacter(), password),
        "SpawnTemplateId": convert_uint(excel_instance.SpawnTemplateId(), password),
        "FavorLevelupType": convert_int(excel_instance.FavorLevelupType(), password),
        "EquipmentSlot": [EquipmentCategory(convert_int(excel_instance.EquipmentSlot(j), password)).name for j in range(excel_instance.EquipmentSlotLength())],
        "WeaponLocalizeId": convert_uint(excel_instance.WeaponLocalizeId(), password),
        "DisplayEnemyInfo": excel_instance.DisplayEnemyInfo(),
        "BodyRadius": convert_long(excel_instance.BodyRadius(), password),
        "RandomEffectRadius": convert_long(excel_instance.RandomEffectRadius(), password),
        "HPBarHide": excel_instance.HPBarHide(),
        "HpBarHeight": convert_float(excel_instance.HpBarHeight(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeight(), password),
        "EmojiOffsetX": convert_float(excel_instance.EmojiOffsetX(), password),
        "EmojiOffsetY": convert_float(excel_instance.EmojiOffsetY(), password),
        "MoveStartFrame": convert_int(excel_instance.MoveStartFrame(), password),
        "MoveEndFrame": convert_int(excel_instance.MoveEndFrame(), password),
        "JumpMotionFrame": convert_int(excel_instance.JumpMotionFrame(), password),
        "AppearFrame": convert_int(excel_instance.AppearFrame(), password),
        "CanMove": excel_instance.CanMove(),
        "CanFix": excel_instance.CanFix(),
        "CanCrowdControl": excel_instance.CanCrowdControl(),
        "CanBattleItemMove": excel_instance.CanBattleItemMove(),
        "IgnoreObstacle": excel_instance.IgnoreObstacle(),
        "IsAirUnit": excel_instance.IsAirUnit(),
        "AirUnitHeight": convert_long(excel_instance.AirUnitHeight(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
        "SecretStoneItemId": convert_long(excel_instance.SecretStoneItemId(), password),
        "SecretStoneItemAmount": convert_int(excel_instance.SecretStoneItemAmount(), password),
        "CharacterPieceItemId": convert_long(excel_instance.CharacterPieceItemId(), password),
        "CharacterPieceItemAmount": convert_int(excel_instance.CharacterPieceItemAmount(), password),
        "CombineRecipeId": convert_long(excel_instance.CombineRecipeId(), password),
    }

def dump_CharacterIllustCoordinateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterBodyCenterX": convert_float(excel_instance.CharacterBodyCenterX(), password),
        "CharacterBodyCenterY": convert_float(excel_instance.CharacterBodyCenterY(), password),
        "DefaultScale": convert_float(excel_instance.DefaultScale(), password),
        "MinScale": convert_float(excel_instance.MinScale(), password),
        "MaxScale": convert_float(excel_instance.MaxScale(), password),
    }

def dump_CharacterLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_long(excel_instance.Exp(), password),
        "TotalExp": convert_long(excel_instance.TotalExp(), password),
    }

def dump_CharacterLevelStatFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_long(excel_instance.Level(), password),
        "CriticalFactor": convert_long(excel_instance.CriticalFactor(), password),
        "StabilityFactor": convert_long(excel_instance.StabilityFactor(), password),
        "DefenceFactor": convert_long(excel_instance.DefenceFactor(), password),
        "AccuracyFactor": convert_long(excel_instance.AccuracyFactor(), password),
    }

def dump_CharacterSkillListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterSkillListGroupId": convert_long(excel_instance.CharacterSkillListGroupId(), password),
        "MinimumGradeCharacterWeapon": convert_int(excel_instance.MinimumGradeCharacterWeapon(), password),
        "MinimumTierCharacterGear": convert_int(excel_instance.MinimumTierCharacterGear(), password),
        "FormIndex": convert_int(excel_instance.FormIndex(), password),
        "IsRootMotion": excel_instance.IsRootMotion(),
        "IsMoveLeftRight": excel_instance.IsMoveLeftRight(),
        "UseRandomExSkillTimeline": excel_instance.UseRandomExSkillTimeline(),
        "TSAInteractionId": convert_long(excel_instance.TSAInteractionId(), password),
        "NormalSkillGroupId": [convert_string(excel_instance.NormalSkillGroupId(j), password) for j in range(excel_instance.NormalSkillGroupIdLength())],
        "NormalSkillTimeLineIndex": [convert_int(excel_instance.NormalSkillTimeLineIndex(j), password) for j in range(excel_instance.NormalSkillTimeLineIndexLength())],
        "ExSkillGroupId": [convert_string(excel_instance.ExSkillGroupId(j), password) for j in range(excel_instance.ExSkillGroupIdLength())],
        "ExSkillCutInTimeLineIndex": [convert_string(excel_instance.ExSkillCutInTimeLineIndex(j), password) for j in range(excel_instance.ExSkillCutInTimeLineIndexLength())],
        "ExSkillLevelTimeLineIndex": [convert_string(excel_instance.ExSkillLevelTimeLineIndex(j), password) for j in range(excel_instance.ExSkillLevelTimeLineIndexLength())],
        "PublicSkillGroupId": [convert_string(excel_instance.PublicSkillGroupId(j), password) for j in range(excel_instance.PublicSkillGroupIdLength())],
        "PublicSkillTimeLineIndex": [convert_int(excel_instance.PublicSkillTimeLineIndex(j), password) for j in range(excel_instance.PublicSkillTimeLineIndexLength())],
        "PassiveSkillGroupId": [convert_string(excel_instance.PassiveSkillGroupId(j), password) for j in range(excel_instance.PassiveSkillGroupIdLength())],
        "LeaderSkillGroupId": [convert_string(excel_instance.LeaderSkillGroupId(j), password) for j in range(excel_instance.LeaderSkillGroupIdLength())],
        "ExtraPassiveSkillGroupId": [convert_string(excel_instance.ExtraPassiveSkillGroupId(j), password) for j in range(excel_instance.ExtraPassiveSkillGroupIdLength())],
        "HiddenPassiveSkillGroupId": [convert_string(excel_instance.HiddenPassiveSkillGroupId(j), password) for j in range(excel_instance.HiddenPassiveSkillGroupIdLength())],
    }

def dump_CharacterStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "StabilityRate": convert_long(excel_instance.StabilityRate(), password),
        "StabilityPoint": convert_long(excel_instance.StabilityPoint(), password),
        "AttackPower1": convert_long(excel_instance.AttackPower1(), password),
        "AttackPower100": convert_long(excel_instance.AttackPower100(), password),
        "MaxHP1": convert_long(excel_instance.MaxHP1(), password),
        "MaxHP100": convert_long(excel_instance.MaxHP100(), password),
        "DefensePower1": convert_long(excel_instance.DefensePower1(), password),
        "DefensePower100": convert_long(excel_instance.DefensePower100(), password),
        "HealPower1": convert_long(excel_instance.HealPower1(), password),
        "HealPower100": convert_long(excel_instance.HealPower100(), password),
        "DodgePoint": convert_long(excel_instance.DodgePoint(), password),
        "AccuracyPoint": convert_long(excel_instance.AccuracyPoint(), password),
        "CriticalPoint": convert_long(excel_instance.CriticalPoint(), password),
        "CriticalResistPoint": convert_long(excel_instance.CriticalResistPoint(), password),
        "CriticalDamageRate": convert_long(excel_instance.CriticalDamageRate(), password),
        "CriticalDamageResistRate": convert_long(excel_instance.CriticalDamageResistRate(), password),
        "BlockRate": convert_long(excel_instance.BlockRate(), password),
        "HealEffectivenessRate": convert_long(excel_instance.HealEffectivenessRate(), password),
        "OppressionPower": convert_long(excel_instance.OppressionPower(), password),
        "OppressionResist": convert_long(excel_instance.OppressionResist(), password),
        "DefensePenetration1": convert_long(excel_instance.DefensePenetration1(), password),
        "DefensePenetration100": convert_long(excel_instance.DefensePenetration100(), password),
        "DefensePenetrationResist1": convert_long(excel_instance.DefensePenetrationResist1(), password),
        "DefensePenetrationResist100": convert_long(excel_instance.DefensePenetrationResist100(), password),
        "EnhanceExplosionRate": convert_long(excel_instance.EnhanceExplosionRate(), password),
        "EnhancePierceRate": convert_long(excel_instance.EnhancePierceRate(), password),
        "EnhanceMysticRate": convert_long(excel_instance.EnhanceMysticRate(), password),
        "EnhanceSonicRate": convert_long(excel_instance.EnhanceSonicRate(), password),
        "EnhanceSiegeRate": convert_long(excel_instance.EnhanceSiegeRate(), password),
        "EnhanceNormalRate": convert_long(excel_instance.EnhanceNormalRate(), password),
        "EnhanceLightArmorRate": convert_long(excel_instance.EnhanceLightArmorRate(), password),
        "EnhanceHeavyArmorRate": convert_long(excel_instance.EnhanceHeavyArmorRate(), password),
        "EnhanceUnarmedRate": convert_long(excel_instance.EnhanceUnarmedRate(), password),
        "EnhanceElasticArmorRate": convert_long(excel_instance.EnhanceElasticArmorRate(), password),
        "EnhanceStructureRate": convert_long(excel_instance.EnhanceStructureRate(), password),
        "EnhanceNormalArmorRate": convert_long(excel_instance.EnhanceNormalArmorRate(), password),
        "ExtendBuffDuration": convert_long(excel_instance.ExtendBuffDuration(), password),
        "ExtendDebuffDuration": convert_long(excel_instance.ExtendDebuffDuration(), password),
        "ExtendCrowdControlDuration": convert_long(excel_instance.ExtendCrowdControlDuration(), password),
        "AmmoCount": convert_long(excel_instance.AmmoCount(), password),
        "AmmoCost": convert_long(excel_instance.AmmoCost(), password),
        "IgnoreDelayCount": convert_long(excel_instance.IgnoreDelayCount(), password),
        "NormalAttackSpeed": convert_long(excel_instance.NormalAttackSpeed(), password),
        "Range": convert_long(excel_instance.Range(), password),
        "InitialRangeRate": convert_long(excel_instance.InitialRangeRate(), password),
        "MoveSpeed": convert_long(excel_instance.MoveSpeed(), password),
        "SightPoint": convert_long(excel_instance.SightPoint(), password),
        "ActiveGauge": convert_long(excel_instance.ActiveGauge(), password),
        "GroggyGauge": convert_int(excel_instance.GroggyGauge(), password),
        "GroggyTime": convert_int(excel_instance.GroggyTime(), password),
        "StrategyMobility": convert_long(excel_instance.StrategyMobility(), password),
        "ActionCount": convert_long(excel_instance.ActionCount(), password),
        "StrategySightRange": convert_long(excel_instance.StrategySightRange(), password),
        "DamageRatio": convert_long(excel_instance.DamageRatio(), password),
        "DamagedRatio": convert_long(excel_instance.DamagedRatio(), password),
        "DamageRatio2Increase": convert_long(excel_instance.DamageRatio2Increase(), password),
        "DamageRatio2Decrease": convert_long(excel_instance.DamageRatio2Decrease(), password),
        "DamagedRatio2Increase": convert_long(excel_instance.DamagedRatio2Increase(), password),
        "DamagedRatio2Decrease": convert_long(excel_instance.DamagedRatio2Decrease(), password),
        "ExDamagedRatioIncrease": convert_long(excel_instance.ExDamagedRatioIncrease(), password),
        "ExDamagedRatioDecrease": convert_long(excel_instance.ExDamagedRatioDecrease(), password),
        "EnhanceExDamageRate": convert_long(excel_instance.EnhanceExDamageRate(), password),
        "ReduceExDamagedRate": convert_long(excel_instance.ReduceExDamagedRate(), password),
        "HealRate": convert_long(excel_instance.HealRate(), password),
        "HealLightArmorRate": convert_long(excel_instance.HealLightArmorRate(), password),
        "HealHeavyArmorRate": convert_long(excel_instance.HealHeavyArmorRate(), password),
        "HealUnarmedRate": convert_long(excel_instance.HealUnarmedRate(), password),
        "HealElasticArmorRate": convert_long(excel_instance.HealElasticArmorRate(), password),
        "HealNormalArmorRate": convert_long(excel_instance.HealNormalArmorRate(), password),
        "HealedExplosionRate": convert_long(excel_instance.HealedExplosionRate(), password),
        "HealedPierceRate": convert_long(excel_instance.HealedPierceRate(), password),
        "HealedMysticRate": convert_long(excel_instance.HealedMysticRate(), password),
        "HealedSonicRate": convert_long(excel_instance.HealedSonicRate(), password),
        "HealedNormalRate": convert_long(excel_instance.HealedNormalRate(), password),
        "StreetBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.StreetBattleAdaptation(), password)).name,
        "OutdoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OutdoorBattleAdaptation(), password)).name,
        "IndoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.IndoorBattleAdaptation(), password)).name,
        "RegenCost": convert_long(excel_instance.RegenCost(), password),
    }

def dump_CharacterStatLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "StatType": StatType(convert_int(excel_instance.StatType(), password)).name,
        "StatMinValue": convert_long(excel_instance.StatMinValue(), password),
        "StatMaxValue": convert_long(excel_instance.StatMaxValue(), password),
        "StatRatioMinValue": convert_long(excel_instance.StatRatioMinValue(), password),
        "StatRatioMaxValue": convert_long(excel_instance.StatRatioMaxValue(), password),
    }

def dump_CharacterStatsDetailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DetailShowStats": [StatType(convert_int(excel_instance.DetailShowStats(j), password)).name for j in range(excel_instance.DetailShowStatsLength())],
        "IsStatsPercent": [excel_instance.IsStatsPercent(j) for j in range(excel_instance.IsStatsPercentLength())],
    }

def dump_CharacterStatsTransExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TransSupportStats": StatType(convert_int(excel_instance.TransSupportStats(), password)).name,
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "TransSupportStatsFactor": convert_int(excel_instance.TransSupportStatsFactor(), password),
        "StatTransType": StatTransType(convert_int(excel_instance.StatTransType(), password)).name,
    }

def dump_CharacterTranscendenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "MaxFavorLevel": [convert_int(excel_instance.MaxFavorLevel(j), password) for j in range(excel_instance.MaxFavorLevelLength())],
        "StatBonusRateAttack": [convert_long(excel_instance.StatBonusRateAttack(j), password) for j in range(excel_instance.StatBonusRateAttackLength())],
        "StatBonusRateHP": [convert_long(excel_instance.StatBonusRateHP(j), password) for j in range(excel_instance.StatBonusRateHPLength())],
        "StatBonusRateHeal": [convert_long(excel_instance.StatBonusRateHeal(j), password) for j in range(excel_instance.StatBonusRateHealLength())],
        "RecipeId": [convert_long(excel_instance.RecipeId(j), password) for j in range(excel_instance.RecipeIdLength())],
        "SkillSlotA": [convert_string(excel_instance.SkillSlotA(j), password) for j in range(excel_instance.SkillSlotALength())],
        "SkillSlotB": [convert_string(excel_instance.SkillSlotB(j), password) for j in range(excel_instance.SkillSlotBLength())],
        "SkillSlotC": [convert_string(excel_instance.SkillSlotC(j), password) for j in range(excel_instance.SkillSlotCLength())],
        "MaxlevelStar": [convert_int(excel_instance.MaxlevelStar(j), password) for j in range(excel_instance.MaxlevelStarLength())],
    }

def dump_CharacterVictoryInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "InteractionId": convert_long(excel_instance.InteractionId(), password),
        "CostumeId01": convert_long(excel_instance.CostumeId01(), password),
        "PositionIndex01": convert_int(excel_instance.PositionIndex01(), password),
        "VictoryStartAnimationPath01": convert_string(excel_instance.VictoryStartAnimationPath01(), password),
        "VictoryEndAnimationPath01": convert_string(excel_instance.VictoryEndAnimationPath01(), password),
        "VoiceEvent01": VoiceEvent(convert_int(excel_instance.VoiceEvent01(), password)).name,
        "CostumeId02": convert_long(excel_instance.CostumeId02(), password),
        "PositionIndex02": convert_int(excel_instance.PositionIndex02(), password),
        "VictoryStartAnimationPath02": convert_string(excel_instance.VictoryStartAnimationPath02(), password),
        "VictoryEndAnimationPath02": convert_string(excel_instance.VictoryEndAnimationPath02(), password),
        "VoiceEvent02": VoiceEvent(convert_int(excel_instance.VoiceEvent02(), password)).name,
        "CostumeId03": convert_long(excel_instance.CostumeId03(), password),
        "PositionIndex03": convert_int(excel_instance.PositionIndex03(), password),
        "VictoryStartAnimationPath03": convert_string(excel_instance.VictoryStartAnimationPath03(), password),
        "VictoryEndAnimationPath03": convert_string(excel_instance.VictoryEndAnimationPath03(), password),
        "VoiceEvent03": VoiceEvent(convert_int(excel_instance.VoiceEvent03(), password)).name,
        "CostumeId04": convert_long(excel_instance.CostumeId04(), password),
        "PositionIndex04": convert_int(excel_instance.PositionIndex04(), password),
        "VictoryStartAnimationPath04": convert_string(excel_instance.VictoryStartAnimationPath04(), password),
        "VictoryEndAnimationPath04": convert_string(excel_instance.VictoryEndAnimationPath04(), password),
        "VoiceEvent04": VoiceEvent(convert_int(excel_instance.VoiceEvent04(), password)).name,
        "CostumeId05": convert_long(excel_instance.CostumeId05(), password),
        "PositionIndex05": convert_int(excel_instance.PositionIndex05(), password),
        "VictoryStartAnimationPath05": convert_string(excel_instance.VictoryStartAnimationPath05(), password),
        "VictoryEndAnimationPath05": convert_string(excel_instance.VictoryEndAnimationPath05(), password),
        "VoiceEvent05": VoiceEvent(convert_int(excel_instance.VoiceEvent05(), password)).name,
        "CostumeId06": convert_long(excel_instance.CostumeId06(), password),
        "PositionIndex06": convert_int(excel_instance.PositionIndex06(), password),
        "VictoryStartAnimationPath06": convert_string(excel_instance.VictoryStartAnimationPath06(), password),
        "VictoryEndAnimationPath06": convert_string(excel_instance.VictoryEndAnimationPath06(), password),
        "VoiceEvent06": VoiceEvent(convert_int(excel_instance.VoiceEvent06(), password)).name,
    }

def dump_CharacterWeaponExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "SetRecipe": convert_long(excel_instance.SetRecipe(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "AttackPower": convert_long(excel_instance.AttackPower(), password),
        "AttackPower100": convert_long(excel_instance.AttackPower100(), password),
        "MaxHP": convert_long(excel_instance.MaxHP(), password),
        "MaxHP100": convert_long(excel_instance.MaxHP100(), password),
        "HealPower": convert_long(excel_instance.HealPower(), password),
        "HealPower100": convert_long(excel_instance.HealPower100(), password),
        "Unlock": [excel_instance.Unlock(j) for j in range(excel_instance.UnlockLength())],
        "RecipeId": [convert_long(excel_instance.RecipeId(j), password) for j in range(excel_instance.RecipeIdLength())],
        "MaxLevel": [convert_int(excel_instance.MaxLevel(j), password) for j in range(excel_instance.MaxLevelLength())],
        "LearnSkillSlot": [convert_string(excel_instance.LearnSkillSlot(j), password) for j in range(excel_instance.LearnSkillSlotLength())],
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatType(j), password)).name for j in range(excel_instance.StatTypeLength())],
        "StatValue": [convert_long(excel_instance.StatValue(j), password) for j in range(excel_instance.StatValueLength())],
    }

def dump_CharacterWeaponExpBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "WeaponExpGrowthA": convert_int(excel_instance.WeaponExpGrowthA(), password),
        "WeaponExpGrowthB": convert_int(excel_instance.WeaponExpGrowthB(), password),
        "WeaponExpGrowthC": convert_int(excel_instance.WeaponExpGrowthC(), password),
        "WeaponExpGrowthZ": convert_int(excel_instance.WeaponExpGrowthZ(), password),
    }

def dump_CharacterWeaponLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_long(excel_instance.Exp(), password),
        "TotalExp": convert_long(excel_instance.TotalExp(), password),
    }

def dump_ClearDeckRuleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "SizeLimit": convert_long(excel_instance.SizeLimit(), password),
    }

def dump_ConquestCalculateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CalculateConditionParcelType": ParcelType(convert_int(excel_instance.CalculateConditionParcelType(), password)).name,
        "CalculateConditionParcelUniqueId": convert_long(excel_instance.CalculateConditionParcelUniqueId(), password),
        "CalculateConditionParcelAmount": convert_long(excel_instance.CalculateConditionParcelAmount(), password),
    }

def dump_ConquestCameraSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeft(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRight(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTop(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottom(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetX(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
    }

def dump_ConquestErosionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "ErosionType": ConquestErosionType(convert_int(excel_instance.ErosionType(), password)).name,
        "Phase": convert_int(excel_instance.Phase(), password),
        "PhaseAlarm": excel_instance.PhaseAlarm(),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "PhaseStartConditionType": [ConquestConditionType(convert_int(excel_instance.PhaseStartConditionType(j), password)).name for j in range(excel_instance.PhaseStartConditionTypeLength())],
        "PhaseStartConditionParameter": [convert_string(excel_instance.PhaseStartConditionParameter(j), password) for j in range(excel_instance.PhaseStartConditionParameterLength())],
        "PhaseBeforeExposeConditionType": [ConquestConditionType(convert_int(excel_instance.PhaseBeforeExposeConditionType(j), password)).name for j in range(excel_instance.PhaseBeforeExposeConditionTypeLength())],
        "PhaseBeforeExposeConditionParameter": [convert_string(excel_instance.PhaseBeforeExposeConditionParameter(j), password) for j in range(excel_instance.PhaseBeforeExposeConditionParameterLength())],
        "ErosionBattleConditionParcelType": ParcelType(convert_int(excel_instance.ErosionBattleConditionParcelType(), password)).name,
        "ErosionBattleConditionParcelUniqueId": convert_long(excel_instance.ErosionBattleConditionParcelUniqueId(), password),
        "ErosionBattleConditionParcelAmount": convert_long(excel_instance.ErosionBattleConditionParcelAmount(), password),
        "ConquestRewardId": convert_long(excel_instance.ConquestRewardId(), password),
    }

def dump_ConquestErosionUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TilePrefabId": convert_long(excel_instance.TilePrefabId(), password),
        "MassErosionUnitId": convert_long(excel_instance.MassErosionUnitId(), password),
        "MassErosionUnitRotationY": convert_float(excel_instance.MassErosionUnitRotationY(), password),
        "IndividualErosionUnitId": convert_long(excel_instance.IndividualErosionUnitId(), password),
        "IndividualErosionUnitRotationY": convert_float(excel_instance.IndividualErosionUnitRotationY(), password),
    }

def dump_ConquestEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "MainStoryEventContentId": convert_long(excel_instance.MainStoryEventContentId(), password),
        "ConquestEventType": ConquestEventType(convert_int(excel_instance.ConquestEventType(), password)).name,
        "UseErosion": excel_instance.UseErosion(),
        "UseUnexpectedEvent": excel_instance.UseUnexpectedEvent(),
        "UseCalculate": excel_instance.UseCalculate(),
        "UseConquestObject": excel_instance.UseConquestObject(),
        "EvnetMapGoalLocalize": convert_string(excel_instance.EvnetMapGoalLocalize(), password),
        "EvnetMapNameLocalize": convert_string(excel_instance.EvnetMapNameLocalize(), password),
        "MapEnterScenarioGroupId": convert_long(excel_instance.MapEnterScenarioGroupId(), password),
        "EvnetScenarioBG": convert_string(excel_instance.EvnetScenarioBG(), password),
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChange(), password),
        "AssistCount": convert_int(excel_instance.AssistCount(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMin(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMax(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelay(), password),
        "LocalizeUnexpected": convert_string(excel_instance.LocalizeUnexpected(), password),
        "LocalizeErosions": convert_string(excel_instance.LocalizeErosions(), password),
        "LocalizeStep": convert_string(excel_instance.LocalizeStep(), password),
        "LocalizeTile": convert_string(excel_instance.LocalizeTile(), password),
        "LocalizeMapInfo": convert_string(excel_instance.LocalizeMapInfo(), password),
        "LocalizeManage": convert_string(excel_instance.LocalizeManage(), password),
        "LocalizeUpgrade": convert_string(excel_instance.LocalizeUpgrade(), password),
        "LocalizeTreasureBox": convert_string(excel_instance.LocalizeTreasureBox(), password),
        "IndividualErosionDailyCount": convert_long(excel_instance.IndividualErosionDailyCount(), password),
    }

def dump_ConquestGroupBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBonusId": convert_long(excel_instance.ConquestBonusId(), password),
        "School": [School(convert_int(excel_instance.School(j), password)).name for j in range(excel_instance.SchoolLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "BonusParcelType": [ParcelType(convert_int(excel_instance.BonusParcelType(j), password)).name for j in range(excel_instance.BonusParcelTypeLength())],
        "BonusId": [convert_long(excel_instance.BonusId(j), password) for j in range(excel_instance.BonusIdLength())],
        "BonusCharacterCount1": [convert_int(excel_instance.BonusCharacterCount1(j), password) for j in range(excel_instance.BonusCharacterCount1Length())],
        "BonusPercentage1": [convert_long(excel_instance.BonusPercentage1(j), password) for j in range(excel_instance.BonusPercentage1Length())],
        "BonusCharacterCount2": [convert_int(excel_instance.BonusCharacterCount2(j), password) for j in range(excel_instance.BonusCharacterCount2Length())],
        "BonusPercentage2": [convert_long(excel_instance.BonusPercentage2(j), password) for j in range(excel_instance.BonusPercentage2Length())],
        "BonusCharacterCount3": [convert_int(excel_instance.BonusCharacterCount3(j), password) for j in range(excel_instance.BonusCharacterCount3Length())],
        "BonusPercentage3": [convert_long(excel_instance.BonusPercentage3(j), password) for j in range(excel_instance.BonusPercentage3Length())],
    }

def dump_ConquestGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBuffId": convert_long(excel_instance.ConquestBuffId(), password),
        "School": [School(convert_int(excel_instance.School(j), password)).name for j in range(excel_instance.SchoolLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_ConquestMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "ConquestMap": convert_string(excel_instance.ConquestMap(), password),
        "StepEnterScenarioGroupId": convert_long(excel_instance.StepEnterScenarioGroupId(), password),
        "StepOpenConditionType": [ConquestConditionType(convert_int(excel_instance.StepOpenConditionType(j), password)).name for j in range(excel_instance.StepOpenConditionTypeLength())],
        "StepOpenConditionParameter": [convert_string(excel_instance.StepOpenConditionParameter(j), password) for j in range(excel_instance.StepOpenConditionParameterLength())],
        "MapGoalLocalize": convert_string(excel_instance.MapGoalLocalize(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalize(), password),
        "StepNameLocalize": convert_string(excel_instance.StepNameLocalize(), password),
        "ConquestMapBG": convert_string(excel_instance.ConquestMapBG(), password),
        "CameraSettingId": convert_long(excel_instance.CameraSettingId(), password),
    }

def dump_ConquestObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ConquestObjectType": ConquestObjectType(convert_int(excel_instance.ConquestObjectType(), password)).name,
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ConquestRewardParcelType": ParcelType(convert_int(excel_instance.ConquestRewardParcelType(), password)).name,
        "ConquestRewardID": convert_long(excel_instance.ConquestRewardID(), password),
        "ConquestRewardAmount": convert_int(excel_instance.ConquestRewardAmount(), password),
        "Disposable": excel_instance.Disposable(),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "StepObjectCount": convert_int(excel_instance.StepObjectCount(), password),
    }

def dump_ConquestPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_ConquestProgressResourceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Group": ConquestProgressType(convert_int(excel_instance.Group(), password)).name,
        "ProgressResource": convert_string(excel_instance.ProgressResource(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "ProgressLocalizeCode": convert_string(excel_instance.ProgressLocalizeCode(), password),
    }

def dump_ConquestRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_ConquestStepExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "Step": convert_int(excel_instance.Step(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalize(), password),
        "StepEnterScenarioGroupId": convert_long(excel_instance.StepEnterScenarioGroupId(), password),
        "StepEnterItemType": ParcelType(convert_int(excel_instance.StepEnterItemType(), password)).name,
        "StepEnterItemUniqueId": convert_long(excel_instance.StepEnterItemUniqueId(), password),
        "StepEnterItemAmount": convert_long(excel_instance.StepEnterItemAmount(), password),
        "UnexpectedEventUnitId": [convert_long(excel_instance.UnexpectedEventUnitId(j), password) for j in range(excel_instance.UnexpectedEventUnitIdLength())],
        "UnexpectedEventPrefab": convert_string(excel_instance.UnexpectedEventPrefab(), password),
        "TreasureBoxObjectId": convert_long(excel_instance.TreasureBoxObjectId(), password),
        "TreasureBoxCountPerStepOpen": convert_int(excel_instance.TreasureBoxCountPerStepOpen(), password),
    }

def dump_ConquestTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventId": convert_long(excel_instance.EventId(), password),
        "Step": convert_int(excel_instance.Step(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "TileNameLocalize": convert_string(excel_instance.TileNameLocalize(), password),
        "TileImageName": convert_string(excel_instance.TileImageName(), password),
        "Playable": excel_instance.Playable(),
        "TileType": ConquestTileType(convert_int(excel_instance.TileType(), password)).name,
        "NotMapFog": excel_instance.NotMapFog(),
        "GroupBonusId": convert_long(excel_instance.GroupBonusId(), password),
        "ConquestCostType": ParcelType(convert_int(excel_instance.ConquestCostType(), password)).name,
        "ConquestCostId": convert_long(excel_instance.ConquestCostId(), password),
        "ConquestCostAmount": convert_int(excel_instance.ConquestCostAmount(), password),
        "ManageCostType": ParcelType(convert_int(excel_instance.ManageCostType(), password)).name,
        "ManageCostId": convert_long(excel_instance.ManageCostId(), password),
        "ManageCostAmount": convert_int(excel_instance.ManageCostAmount(), password),
        "ConquestRewardId": convert_long(excel_instance.ConquestRewardId(), password),
        "MassErosionId": convert_long(excel_instance.MassErosionId(), password),
        "Upgrade2CostType": ParcelType(convert_int(excel_instance.Upgrade2CostType(), password)).name,
        "Upgrade2CostId": convert_long(excel_instance.Upgrade2CostId(), password),
        "Upgrade2CostAmount": convert_int(excel_instance.Upgrade2CostAmount(), password),
        "Upgrade3CostType": ParcelType(convert_int(excel_instance.Upgrade3CostType(), password)).name,
        "Upgrade3CostId": convert_long(excel_instance.Upgrade3CostId(), password),
        "Upgrade3CostAmount": convert_int(excel_instance.Upgrade3CostAmount(), password),
    }

def dump_ConquestUnexpectedEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UnexpectedEventConditionType": ParcelType(convert_int(excel_instance.UnexpectedEventConditionType(), password)).name,
        "UnexpectedEventConditionUniqueId": convert_long(excel_instance.UnexpectedEventConditionUniqueId(), password),
        "UnexpectedEventConditionAmount": convert_long(excel_instance.UnexpectedEventConditionAmount(), password),
        "UnexpectedEventOccurDailyLimitCount": convert_int(excel_instance.UnexpectedEventOccurDailyLimitCount(), password),
        "UnitCountPerStep": convert_int(excel_instance.UnitCountPerStep(), password),
        "UnexpectedEventPrefab": [convert_string(excel_instance.UnexpectedEventPrefab(j), password) for j in range(excel_instance.UnexpectedEventPrefabLength())],
        "UnexpectedEventUnitId": [convert_long(excel_instance.UnexpectedEventUnitId(j), password) for j in range(excel_instance.UnexpectedEventUnitIdLength())],
    }

def dump_ConquestUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabName(), password),
        "Scale": convert_float(excel_instance.Scale(), password),
        "ShieldEffectScale": convert_float(excel_instance.ShieldEffectScale(), password),
        "UnitFxPrefabName": convert_string(excel_instance.UnitFxPrefabName(), password),
        "PointAnimation": convert_string(excel_instance.PointAnimation(), password),
        "EnemyType": ConquestEnemyType(convert_int(excel_instance.EnemyType(), password)).name,
        "Team": ConquestTeamType(convert_int(excel_instance.Team(), password)).name,
        "UnitGroup": convert_long(excel_instance.UnitGroup(), password),
        "PrevUnitGroup": convert_long(excel_instance.PrevUnitGroup(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "GroupBuffId": convert_long(excel_instance.GroupBuffId(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "ManageEchelonStageEnterCostType": ParcelType(convert_int(excel_instance.ManageEchelonStageEnterCostType(), password)).name,
        "ManageEchelonStageEnterCostId": convert_long(excel_instance.ManageEchelonStageEnterCostId(), password),
        "ManageEchelonStageEnterCostAmount": convert_int(excel_instance.ManageEchelonStageEnterCostAmount(), password),
        "EnterScenarioGroupId": convert_long(excel_instance.EnterScenarioGroupId(), password),
        "ClearScenarioGroupId": convert_long(excel_instance.ClearScenarioGroupId(), password),
        "ConquestRewardId": convert_long(excel_instance.ConquestRewardId(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "TacticRewardExp": convert_long(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_ConstArenaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttackCoolTime": convert_long(excel_instance.AttackCoolTime(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "DefenseCoolTime": convert_long(excel_instance.DefenseCoolTime(), password),
        "TSSStartCoolTime": convert_long(excel_instance.TSSStartCoolTime(), password),
        "EndAlarm": convert_long(excel_instance.EndAlarm(), password),
        "TimeRewardMaxAmount": convert_long(excel_instance.TimeRewardMaxAmount(), password),
        "EnterCostType": ParcelType(convert_int(excel_instance.EnterCostType(), password)).name,
        "EnterCostId": convert_long(excel_instance.EnterCostId(), password),
        "TicketCost": convert_long(excel_instance.TicketCost(), password),
        "DailyRewardResetTime": convert_string(excel_instance.DailyRewardResetTime(), password),
        "OpenScenarioId": convert_string(excel_instance.OpenScenarioId(), password),
        "CharacterSlotHideRank": [convert_long(excel_instance.CharacterSlotHideRank(j), password) for j in range(excel_instance.CharacterSlotHideRankLength())],
        "MapSlotHideRank": convert_long(excel_instance.MapSlotHideRank(), password),
        "RelativeOpponentRankStart": [convert_long(excel_instance.RelativeOpponentRankStart(j), password) for j in range(excel_instance.RelativeOpponentRankStartLength())],
        "RelativeOpponentRankEnd": [convert_long(excel_instance.RelativeOpponentRankEnd(j), password) for j in range(excel_instance.RelativeOpponentRankEndLength())],
        "ModifiedStatType": [StatType(convert_int(excel_instance.ModifiedStatType(j), password)).name for j in range(excel_instance.ModifiedStatTypeLength())],
        "StatMulFactor": [convert_long(excel_instance.StatMulFactor(j), password) for j in range(excel_instance.StatMulFactorLength())],
        "StatSumFactor": [convert_long(excel_instance.StatSumFactor(j), password) for j in range(excel_instance.StatSumFactorLength())],
        "NPCName": [convert_string(excel_instance.NPCName(j), password) for j in range(excel_instance.NPCNameLength())],
        "NPCMainCharacterCount": convert_long(excel_instance.NPCMainCharacterCount(), password),
        "NPCSupportCharacterCount": convert_long(excel_instance.NPCSupportCharacterCount(), password),
        "NPCCharacterSkillLevel": convert_long(excel_instance.NPCCharacterSkillLevel(), password),
        "TimeSpanInDaysForBattleHistory": convert_long(excel_instance.TimeSpanInDaysForBattleHistory(), password),
        "HiddenCharacterImagePath": convert_string(excel_instance.HiddenCharacterImagePath(), password),
        "DefenseVictoryRewardMaxCount": convert_long(excel_instance.DefenseVictoryRewardMaxCount(), password),
        "TopRankerCountLimit": convert_long(excel_instance.TopRankerCountLimit(), password),
        "AutoRefreshIntervalMilliSeconds": convert_long(excel_instance.AutoRefreshIntervalMilliSeconds(), password),
        "EchelonSettingIntervalMilliSeconds": convert_long(excel_instance.EchelonSettingIntervalMilliSeconds(), password),
        "SkipAllowedTimeMilliSeconds": convert_long(excel_instance.SkipAllowedTimeMilliSeconds(), password),
        "ShowSeasonChangeInfoStartTime": convert_string(excel_instance.ShowSeasonChangeInfoStartTime(), password),
        "ShowSeasonChangeInfoEndTime": convert_string(excel_instance.ShowSeasonChangeInfoEndTime(), password),
        "ShowSeasonId": convert_long(excel_instance.ShowSeasonId(), password),
        "ArenaHistoryQueryLimitDays": convert_int(excel_instance.ArenaHistoryQueryLimitDays(), password),
    }

def dump_ConstAudioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultSnapShotName": convert_string(excel_instance.DefaultSnapShotName(), password),
        "BattleSnapShotName": convert_string(excel_instance.BattleSnapShotName(), password),
        "RaidSnapShotName": convert_string(excel_instance.RaidSnapShotName(), password),
        "ExSkillCutInSnapShotName": convert_string(excel_instance.ExSkillCutInSnapShotName(), password),
    }

def dump_ConstCombatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SkillHandCount": convert_int(excel_instance.SkillHandCount(), password),
        "DyingTime": convert_int(excel_instance.DyingTime(), password),
        "BuffIconBlinkTime": convert_int(excel_instance.BuffIconBlinkTime(), password),
        "ShowBufficonEXSkill": excel_instance.ShowBufficonEXSkill(),
        "ShowBufficonPassiveSkill": excel_instance.ShowBufficonPassiveSkill(),
        "ShowBufficonExtraPassiveSkill": excel_instance.ShowBufficonExtraPassiveSkill(),
        "ShowBufficonLeaderSkill": excel_instance.ShowBufficonLeaderSkill(),
        "ShowBufficonGroundPassiveSkill": excel_instance.ShowBufficonGroundPassiveSkill(),
        "SuppliesConditionStringId": convert_string(excel_instance.SuppliesConditionStringId(), password),
        "PublicSpeechBubbleOffsetX": convert_float(excel_instance.PublicSpeechBubbleOffsetX(), password),
        "PublicSpeechBubbleOffsetY": convert_float(excel_instance.PublicSpeechBubbleOffsetY(), password),
        "PublicSpeechBubbleOffsetZ": convert_float(excel_instance.PublicSpeechBubbleOffsetZ(), password),
        "ShowRaidListCount": convert_int(excel_instance.ShowRaidListCount(), password),
        "MaxRaidTicketCount": convert_long(excel_instance.MaxRaidTicketCount(), password),
        "MaxRaidBossSkillSlot": convert_long(excel_instance.MaxRaidBossSkillSlot(), password),
        "EngageTimelinePath": convert_string(excel_instance.EngageTimelinePath(), password),
        "EngageWithSupporterTimelinePath": convert_string(excel_instance.EngageWithSupporterTimelinePath(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "TimeLimitAlarm": convert_long(excel_instance.TimeLimitAlarm(), password),
        "EchelonMaxCommonCost": convert_int(excel_instance.EchelonMaxCommonCost(), password),
        "EchelonInitCommonCost": convert_int(excel_instance.EchelonInitCommonCost(), password),
        "SkillSlotCoolTime": convert_long(excel_instance.SkillSlotCoolTime(), password),
        "EnemyRegenCost": convert_long(excel_instance.EnemyRegenCost(), password),
        "ChampionRegenCost": convert_long(excel_instance.ChampionRegenCost(), password),
        "PlayerRegenCostDelay": convert_long(excel_instance.PlayerRegenCostDelay(), password),
        "CrowdControlFactor": convert_long(excel_instance.CrowdControlFactor(), password),
        "RaidOpenScenarioId": convert_string(excel_instance.RaidOpenScenarioId(), password),
        "EliminateRaidOpenScenarioId": convert_string(excel_instance.EliminateRaidOpenScenarioId(), password),
        "DefenceConstA": convert_long(excel_instance.DefenceConstA(), password),
        "DefenceConstB": convert_long(excel_instance.DefenceConstB(), password),
        "DefenceConstC": convert_long(excel_instance.DefenceConstC(), password),
        "DefenceConstD": convert_long(excel_instance.DefenceConstD(), password),
        "AccuracyConstA": convert_long(excel_instance.AccuracyConstA(), password),
        "AccuracyConstB": convert_long(excel_instance.AccuracyConstB(), password),
        "AccuracyConstC": convert_long(excel_instance.AccuracyConstC(), password),
        "AccuracyConstD": convert_long(excel_instance.AccuracyConstD(), password),
        "CriticalConstA": convert_long(excel_instance.CriticalConstA(), password),
        "CriticalConstB": convert_long(excel_instance.CriticalConstB(), password),
        "CriticalConstC": convert_long(excel_instance.CriticalConstC(), password),
        "CriticalConstD": convert_long(excel_instance.CriticalConstD(), password),
        "MaxGroupBuffLevel": convert_int(excel_instance.MaxGroupBuffLevel(), password),
        "EmojiDefaultTime": convert_int(excel_instance.EmojiDefaultTime(), password),
        "TimeLineActionRotateSpeed": convert_long(excel_instance.TimeLineActionRotateSpeed(), password),
        "BodyRotateSpeed": convert_long(excel_instance.BodyRotateSpeed(), password),
        "NormalTimeScale": convert_long(excel_instance.NormalTimeScale(), password),
        "FastTimeScale": convert_long(excel_instance.FastTimeScale(), password),
        "BulletTimeScale": convert_long(excel_instance.BulletTimeScale(), password),
        "UIDisplayDelayAfterSkillCutIn": convert_long(excel_instance.UIDisplayDelayAfterSkillCutIn(), password),
        "UseInitialRangeForCoverMove": excel_instance.UseInitialRangeForCoverMove(),
        "SlowTimeScale": convert_long(excel_instance.SlowTimeScale(), password),
        "AimIKMinDegree": convert_float(excel_instance.AimIKMinDegree(), password),
        "AimIKMaxDegree": convert_float(excel_instance.AimIKMaxDegree(), password),
        "MinimumClearTime": convert_int(excel_instance.MinimumClearTime(), password),
        "MinimumClearLevelGap": convert_int(excel_instance.MinimumClearLevelGap(), password),
        "CheckCheaterMaxUseCostNonArena": convert_int(excel_instance.CheckCheaterMaxUseCostNonArena(), password),
        "CheckCheaterMaxUseCostArena": convert_int(excel_instance.CheckCheaterMaxUseCostArena(), password),
        "AllowedMaxTimeScale": convert_long(excel_instance.AllowedMaxTimeScale(), password),
        "RandomAnimationOutput": convert_long(excel_instance.RandomAnimationOutput(), password),
        "SummonedTeleportDistance": convert_long(excel_instance.SummonedTeleportDistance(), password),
        "ArenaMinimumClearTime": convert_int(excel_instance.ArenaMinimumClearTime(), password),
        "WORLDBOSSBATTLELITTLE": convert_long(excel_instance.WORLDBOSSBATTLELITTLE(), password),
        "WORLDBOSSBATTLEMIDDLE": convert_long(excel_instance.WORLDBOSSBATTLEMIDDLE(), password),
        "WORLDBOSSBATTLEHIGH": convert_long(excel_instance.WORLDBOSSBATTLEHIGH(), password),
        "WORLDBOSSBATTLEVERYHIGH": convert_long(excel_instance.WORLDBOSSBATTLEVERYHIGH(), password),
        "WorldRaidAutoSyncTermSecond": convert_long(excel_instance.WorldRaidAutoSyncTermSecond(), password),
        "WorldRaidBossHpDecreaseTerm": convert_long(excel_instance.WorldRaidBossHpDecreaseTerm(), password),
        "WorldRaidBossParcelReactionDelay": convert_long(excel_instance.WorldRaidBossParcelReactionDelay(), password),
        "RaidRankingJumpMinimumWaitingTime": convert_long(excel_instance.RaidRankingJumpMinimumWaitingTime(), password),
        "EffectTeleportDistance": convert_float(excel_instance.EffectTeleportDistance(), password),
        "AuraExitThresholdMargin": convert_long(excel_instance.AuraExitThresholdMargin(), password),
        "TSAInteractionDamageFactor": convert_long(excel_instance.TSAInteractionDamageFactor(), password),
        "VictoryInteractionRate": convert_long(excel_instance.VictoryInteractionRate(), password),
        "EchelonExtensionEngageTimelinePath": convert_string(excel_instance.EchelonExtensionEngageTimelinePath(), password),
        "EchelonExtensionEngageWithSupporterTimelinePath": convert_string(excel_instance.EchelonExtensionEngageWithSupporterTimelinePath(), password),
        "EchelonExtensionVictoryTimelinePath": convert_string(excel_instance.EchelonExtensionVictoryTimelinePath(), password),
        "EchelonExtensionEchelonMaxCommonCost": convert_int(excel_instance.EchelonExtensionEchelonMaxCommonCost(), password),
        "EchelonExtensionEchelonInitCommonCost": convert_int(excel_instance.EchelonExtensionEchelonInitCommonCost(), password),
        "EchelonExtensionCostRegenRatio": convert_long(excel_instance.EchelonExtensionCostRegenRatio(), password),
        "CheckCheaterMaxUseCostMultiFloorRaid": convert_int(excel_instance.CheckCheaterMaxUseCostMultiFloorRaid(), password),
        "ExcessiveTouchCheckTime": convert_float(excel_instance.ExcessiveTouchCheckTime(), password),
        "ExcessiveTouchCheckCount": convert_int(excel_instance.ExcessiveTouchCheckCount(), password),
        "CampaignAlertPopupLevelGap": convert_int(excel_instance.CampaignAlertPopupLevelGap(), password),
    }

def dump_ConstCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CampaignMainStageMaxRank": convert_int(excel_instance.CampaignMainStageMaxRank(), password),
        "CampaignMainStageBestRecord": convert_int(excel_instance.CampaignMainStageBestRecord(), password),
        "HardAdventurePlayCountRecoverDailyNumber": convert_int(excel_instance.HardAdventurePlayCountRecoverDailyNumber(), password),
        "HardStageCount": convert_int(excel_instance.HardStageCount(), password),
        "TacticRankClearTime": convert_int(excel_instance.TacticRankClearTime(), password),
        "BaseTimeScale": convert_long(excel_instance.BaseTimeScale(), password),
        "GachaPercentage": convert_int(excel_instance.GachaPercentage(), password),
        "AcademyFavorZoneId": convert_long(excel_instance.AcademyFavorZoneId(), password),
        "CafePresetSlotCount": convert_int(excel_instance.CafePresetSlotCount(), password),
        "CafeMonologueIntervalMillisec": convert_long(excel_instance.CafeMonologueIntervalMillisec(), password),
        "CafeMonologueDefaultDuration": convert_long(excel_instance.CafeMonologueDefaultDuration(), password),
        "CafeBubbleIdleDurationMilliSec": convert_long(excel_instance.CafeBubbleIdleDurationMilliSec(), password),
        "FindGiftTimeLimit": convert_int(excel_instance.FindGiftTimeLimit(), password),
        "CafeAutoChargePeriodInMsc": convert_int(excel_instance.CafeAutoChargePeriodInMsc(), password),
        "CafeProductionDecimalPosition": convert_int(excel_instance.CafeProductionDecimalPosition(), password),
        "CafeSetGroupApplyCount": convert_int(excel_instance.CafeSetGroupApplyCount(), password),
        "WeekDungeonFindGiftRewardLimitCount": convert_int(excel_instance.WeekDungeonFindGiftRewardLimitCount(), password),
        "StageFailedCurrencyRefundRate": convert_int(excel_instance.StageFailedCurrencyRefundRate(), password),
        "EnterDeposit": convert_int(excel_instance.EnterDeposit(), password),
        "AccountMaxLevel": convert_int(excel_instance.AccountMaxLevel(), password),
        "MainSquadExpBonus": convert_int(excel_instance.MainSquadExpBonus(), password),
        "SupportSquadExpBonus": convert_int(excel_instance.SupportSquadExpBonus(), password),
        "AccountExpRatio": convert_int(excel_instance.AccountExpRatio(), password),
        "MissionToastLifeTime": convert_int(excel_instance.MissionToastLifeTime(), password),
        "ExpItemInsertLimit": convert_int(excel_instance.ExpItemInsertLimit(), password),
        "ExpItemInsertAccelTime": convert_int(excel_instance.ExpItemInsertAccelTime(), password),
        "CharacterLvUpCoefficient": convert_int(excel_instance.CharacterLvUpCoefficient(), password),
        "EquipmentLvUpCoefficient": convert_int(excel_instance.EquipmentLvUpCoefficient(), password),
        "ExpEquipInsertLimit": convert_int(excel_instance.ExpEquipInsertLimit(), password),
        "EquipLvUpCoefficient": convert_int(excel_instance.EquipLvUpCoefficient(), password),
        "NicknameLength": convert_int(excel_instance.NicknameLength(), password),
        "CraftDuration": [convert_int(excel_instance.CraftDuration(j), password) for j in range(excel_instance.CraftDurationLength())],
        "CraftLimitTime": convert_int(excel_instance.CraftLimitTime(), password),
        "ShiftingCraftDuration": [convert_int(excel_instance.ShiftingCraftDuration(j), password) for j in range(excel_instance.ShiftingCraftDurationLength())],
        "ShiftingCraftTicketConsumeAmount": convert_int(excel_instance.ShiftingCraftTicketConsumeAmount(), password),
        "ShiftingCraftSlotMaxCapacity": convert_int(excel_instance.ShiftingCraftSlotMaxCapacity(), password),
        "CraftTicketItemUniqueId": convert_int(excel_instance.CraftTicketItemUniqueId(), password),
        "CraftTicketConsumeAmount": convert_int(excel_instance.CraftTicketConsumeAmount(), password),
        "AcademyEnterCostType": ParcelType(convert_int(excel_instance.AcademyEnterCostType(), password)).name,
        "AcademyEnterCostId": convert_long(excel_instance.AcademyEnterCostId(), password),
        "AcademyTicketCost": convert_int(excel_instance.AcademyTicketCost(), password),
        "MassangerMessageExpireDay": convert_int(excel_instance.MassangerMessageExpireDay(), password),
        "CraftLeafNodeGenerateLv1Count": convert_int(excel_instance.CraftLeafNodeGenerateLv1Count(), password),
        "CraftLeafNodeGenerateLv2Count": convert_int(excel_instance.CraftLeafNodeGenerateLv2Count(), password),
        "TutorialGachaShopId": convert_int(excel_instance.TutorialGachaShopId(), password),
        "BeforehandGachaShopId": convert_int(excel_instance.BeforehandGachaShopId(), password),
        "TutorialGachaGoodsId": convert_int(excel_instance.TutorialGachaGoodsId(), password),
        "EquipmentSlotOpenLevel": [convert_int(excel_instance.EquipmentSlotOpenLevel(j), password) for j in range(excel_instance.EquipmentSlotOpenLevelLength())],
        "ScenarioAutoDelayMillisec": convert_float(excel_instance.ScenarioAutoDelayMillisec(), password),
        "JoinOrCreateClanCoolTimeFromHour": convert_long(excel_instance.JoinOrCreateClanCoolTimeFromHour(), password),
        "ClanMaxMember": convert_long(excel_instance.ClanMaxMember(), password),
        "ClanSearchResultCount": convert_long(excel_instance.ClanSearchResultCount(), password),
        "ClanMaxApplicant": convert_long(excel_instance.ClanMaxApplicant(), password),
        "ClanRejoinCoolTimeFromSecond": convert_long(excel_instance.ClanRejoinCoolTimeFromSecond(), password),
        "ClanWordBalloonMaxCharacter": convert_int(excel_instance.ClanWordBalloonMaxCharacter(), password),
        "CallNameRenameCoolTimeFromHour": convert_long(excel_instance.CallNameRenameCoolTimeFromHour(), password),
        "CallNameMinimumLength": convert_long(excel_instance.CallNameMinimumLength(), password),
        "CallNameMaximumLength": convert_long(excel_instance.CallNameMaximumLength(), password),
        "LobbyToScreenModeWaitTime": convert_long(excel_instance.LobbyToScreenModeWaitTime(), password),
        "ScreenshotToLobbyButtonHideDelay": convert_long(excel_instance.ScreenshotToLobbyButtonHideDelay(), password),
        "PrologueScenarioID01": convert_long(excel_instance.PrologueScenarioID01(), password),
        "PrologueScenarioID02": convert_long(excel_instance.PrologueScenarioID02(), password),
        "TutorialHardStage11": convert_long(excel_instance.TutorialHardStage11(), password),
        "TutorialSpeedButtonStage": convert_long(excel_instance.TutorialSpeedButtonStage(), password),
        "TutorialCharacterDefaultCount": convert_long(excel_instance.TutorialCharacterDefaultCount(), password),
        "TutorialShopCategoryType": ShopCategoryType(convert_int(excel_instance.TutorialShopCategoryType(), password)).name,
        "AdventureStrategyPlayTimeLimitInSeconds": convert_long(excel_instance.AdventureStrategyPlayTimeLimitInSeconds(), password),
        "WeekDungoenTacticPlayTimeLimitInSeconds": convert_long(excel_instance.WeekDungoenTacticPlayTimeLimitInSeconds(), password),
        "RaidTacticPlayTimeLimitInSeconds": convert_long(excel_instance.RaidTacticPlayTimeLimitInSeconds(), password),
        "RaidOpponentListAmount": convert_long(excel_instance.RaidOpponentListAmount(), password),
        "CraftBaseGoldRequired": [convert_long(excel_instance.CraftBaseGoldRequired(j), password) for j in range(excel_instance.CraftBaseGoldRequiredLength())],
        "PostExpiredDayAttendance": convert_int(excel_instance.PostExpiredDayAttendance(), password),
        "PostExpiredDayInventoryOverflow": convert_int(excel_instance.PostExpiredDayInventoryOverflow(), password),
        "PostExpiredDayGameManager": convert_int(excel_instance.PostExpiredDayGameManager(), password),
        "UILabelCharacterWrap": convert_string(excel_instance.UILabelCharacterWrap(), password),
        "RequestTimeOut": convert_float(excel_instance.RequestTimeOut(), password),
        "MailStorageSoftCap": convert_int(excel_instance.MailStorageSoftCap(), password),
        "MailStorageHardCap": convert_int(excel_instance.MailStorageHardCap(), password),
        "ClearDeckStorageSize": convert_int(excel_instance.ClearDeckStorageSize(), password),
        "ClearDeckNoStarViewCount": convert_int(excel_instance.ClearDeckNoStarViewCount(), password),
        "ClearDeck1StarViewCount": convert_int(excel_instance.ClearDeck1StarViewCount(), password),
        "ClearDeck2StarViewCount": convert_int(excel_instance.ClearDeck2StarViewCount(), password),
        "ClearDeck3StarViewCount": convert_int(excel_instance.ClearDeck3StarViewCount(), password),
        "ExSkillLevelMax": convert_int(excel_instance.ExSkillLevelMax(), password),
        "PublicSkillLevelMax": convert_int(excel_instance.PublicSkillLevelMax(), password),
        "PassiveSkillLevelMax": convert_int(excel_instance.PassiveSkillLevelMax(), password),
        "ExtraPassiveSkillLevelMax": convert_int(excel_instance.ExtraPassiveSkillLevelMax(), password),
        "AccountCommentMaxLength": convert_int(excel_instance.AccountCommentMaxLength(), password),
        "CafeSummonCoolTimeFromHour": convert_int(excel_instance.CafeSummonCoolTimeFromHour(), password),
        "LimitedStageDailyClearCount": convert_long(excel_instance.LimitedStageDailyClearCount(), password),
        "LimitedStageEntryTimeLimit": convert_long(excel_instance.LimitedStageEntryTimeLimit(), password),
        "LimitedStageEntryTimeBuffer": convert_long(excel_instance.LimitedStageEntryTimeBuffer(), password),
        "LimitedStagePointAmount": convert_long(excel_instance.LimitedStagePointAmount(), password),
        "LimitedStagePointPerApMin": convert_long(excel_instance.LimitedStagePointPerApMin(), password),
        "LimitedStagePointPerApMax": convert_long(excel_instance.LimitedStagePointPerApMax(), password),
        "AccountLinkReward": convert_int(excel_instance.AccountLinkReward(), password),
        "MonthlyProductCheckDays": convert_int(excel_instance.MonthlyProductCheckDays(), password),
        "WeaponLvUpCoefficient": convert_int(excel_instance.WeaponLvUpCoefficient(), password),
        "ShowRaidMyListCount": convert_int(excel_instance.ShowRaidMyListCount(), password),
        "MaxLevelExpMasterCoinRatio": convert_int(excel_instance.MaxLevelExpMasterCoinRatio(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostType(), password)).name,
        "RaidEnterCostId": convert_long(excel_instance.RaidEnterCostId(), password),
        "RaidTicketCost": convert_long(excel_instance.RaidTicketCost(), password),
        "TimeAttackDungeonScenarioId": convert_string(excel_instance.TimeAttackDungeonScenarioId(), password),
        "TimeAttackDungoenPlayCountPerTicket": convert_int(excel_instance.TimeAttackDungoenPlayCountPerTicket(), password),
        "TimeAttackDungeonEnterCostType": ParcelType(convert_int(excel_instance.TimeAttackDungeonEnterCostType(), password)).name,
        "TimeAttackDungeonEnterCostId": convert_long(excel_instance.TimeAttackDungeonEnterCostId(), password),
        "TimeAttackDungeonEnterCost": convert_long(excel_instance.TimeAttackDungeonEnterCost(), password),
        "ClanLeaderTransferLastLoginLimit": convert_long(excel_instance.ClanLeaderTransferLastLoginLimit(), password),
        "MonthlyProductRepurchasePopupLimit": convert_int(excel_instance.MonthlyProductRepurchasePopupLimit(), password),
        "CommonFavorItemTags": [Tag(convert_int(excel_instance.CommonFavorItemTags(j), password)).name for j in range(excel_instance.CommonFavorItemTagsLength())],
        "MaxApMasterCoinPerWeek": convert_long(excel_instance.MaxApMasterCoinPerWeek(), password),
        "CraftOpenExpTier1": convert_long(excel_instance.CraftOpenExpTier1(), password),
        "CraftOpenExpTier2": convert_long(excel_instance.CraftOpenExpTier2(), password),
        "CraftOpenExpTier3": convert_long(excel_instance.CraftOpenExpTier3(), password),
        "CharacterEquipmentGearSlot": convert_long(excel_instance.CharacterEquipmentGearSlot(), password),
        "BirthDayDDay": convert_int(excel_instance.BirthDayDDay(), password),
        "RecommendedFriendsLvDifferenceLimit": convert_int(excel_instance.RecommendedFriendsLvDifferenceLimit(), password),
        "DDosDetectCount": convert_int(excel_instance.DDosDetectCount(), password),
        "DDosCheckIntervalInSeconds": convert_int(excel_instance.DDosCheckIntervalInSeconds(), password),
        "MaxFriendsCount": convert_int(excel_instance.MaxFriendsCount(), password),
        "MaxFriendsRequest": convert_int(excel_instance.MaxFriendsRequest(), password),
        "FriendsSearchRequestCount": convert_int(excel_instance.FriendsSearchRequestCount(), password),
        "FriendsMaxApplicant": convert_int(excel_instance.FriendsMaxApplicant(), password),
        "IdCardDefaultCharacterId": convert_long(excel_instance.IdCardDefaultCharacterId(), password),
        "IdCardDefaultBgId": convert_long(excel_instance.IdCardDefaultBgId(), password),
        "WorldRaidGemEnterCost": convert_long(excel_instance.WorldRaidGemEnterCost(), password),
        "WorldRaidGemEnterAmout": convert_long(excel_instance.WorldRaidGemEnterAmout(), password),
        "FriendIdCardCommentMaxLength": convert_long(excel_instance.FriendIdCardCommentMaxLength(), password),
        "FormationPresetNumberOfEchelonTab": convert_int(excel_instance.FormationPresetNumberOfEchelonTab(), password),
        "FormationPresetNumberOfEchelon": convert_int(excel_instance.FormationPresetNumberOfEchelon(), password),
        "FormationPresetRecentNumberOfEchelon": convert_int(excel_instance.FormationPresetRecentNumberOfEchelon(), password),
        "FormationPresetEchelonTabTextLength": convert_int(excel_instance.FormationPresetEchelonTabTextLength(), password),
        "FormationPresetEchelonSlotTextLength": convert_int(excel_instance.FormationPresetEchelonSlotTextLength(), password),
        "CharProfileRowIntervalKr": convert_int(excel_instance.CharProfileRowIntervalKr(), password),
        "CharProfileRowIntervalJp": convert_int(excel_instance.CharProfileRowIntervalJp(), password),
        "CharProfilePopupRowIntervalKr": convert_int(excel_instance.CharProfilePopupRowIntervalKr(), password),
        "CharProfilePopupRowIntervalJp": convert_int(excel_instance.CharProfilePopupRowIntervalJp(), password),
        "BeforehandGachaCount": convert_int(excel_instance.BeforehandGachaCount(), password),
        "BeforehandGachaGroupId": convert_int(excel_instance.BeforehandGachaGroupId(), password),
        "RenewalDisplayOrderDay": convert_int(excel_instance.RenewalDisplayOrderDay(), password),
        "EmblemDefaultId": convert_long(excel_instance.EmblemDefaultId(), password),
        "BirthdayMailStartDate": convert_string(excel_instance.BirthdayMailStartDate(), password),
        "BirthdayMailRemainDate": convert_int(excel_instance.BirthdayMailRemainDate(), password),
        "BirthdayMailParcelType": ParcelType(convert_int(excel_instance.BirthdayMailParcelType(), password)).name,
        "BirthdayMailParcelId": convert_long(excel_instance.BirthdayMailParcelId(), password),
        "BirthdayMailParcelAmount": convert_int(excel_instance.BirthdayMailParcelAmount(), password),
        "ClearDeckAverageDeckCount": convert_int(excel_instance.ClearDeckAverageDeckCount(), password),
        "ClearDeckWorldRaidSaveConditionCoefficient": convert_int(excel_instance.ClearDeckWorldRaidSaveConditionCoefficient(), password),
        "ClearDeckShowCount": convert_int(excel_instance.ClearDeckShowCount(), password),
        "CharacterMaxLevel": convert_int(excel_instance.CharacterMaxLevel(), password),
        "PotentialBonusStatMaxLevelMaxHP": convert_int(excel_instance.PotentialBonusStatMaxLevelMaxHP(), password),
        "PotentialBonusStatMaxLevelAttackPower": convert_int(excel_instance.PotentialBonusStatMaxLevelAttackPower(), password),
        "PotentialBonusStatMaxLevelHealPower": convert_int(excel_instance.PotentialBonusStatMaxLevelHealPower(), password),
        "PotentialOpenConditionCharacterLevel": convert_int(excel_instance.PotentialOpenConditionCharacterLevel(), password),
        "AssistStrangerMinLevel": convert_int(excel_instance.AssistStrangerMinLevel(), password),
        "AssistStrangerMaxLevel": convert_int(excel_instance.AssistStrangerMaxLevel(), password),
        "MaxBlockedUserCount": convert_int(excel_instance.MaxBlockedUserCount(), password),
        "CafeRandomVisitMinComfortBonus": convert_long(excel_instance.CafeRandomVisitMinComfortBonus(), password),
        "CafeRandomVisitMinLastLogin": convert_int(excel_instance.CafeRandomVisitMinLastLogin(), password),
        "CafeTravelSyncIntervalByMillisec": convert_int(excel_instance.CafeTravelSyncIntervalByMillisec(), password),
    }

def dump_ConstConquestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChange(), password),
        "AssistCount": convert_int(excel_instance.AssistCount(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMin(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMax(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelay(), password),
    }

def dump_ConstEventCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentHardStageCount": convert_int(excel_instance.EventContentHardStageCount(), password),
        "EventStrategyPlayTimeLimitInSeconds": convert_long(excel_instance.EventStrategyPlayTimeLimitInSeconds(), password),
        "SubEventChangeLimitSeconds": convert_long(excel_instance.SubEventChangeLimitSeconds(), password),
        "SubEventInstantClear": excel_instance.SubEventInstantClear(),
        "CardShopProbWeightCount": convert_long(excel_instance.CardShopProbWeightCount(), password),
        "CardShopProbWeightRarity": Rarity(convert_int(excel_instance.CardShopProbWeightRarity(), password)).name,
        "MeetupScenarioReplayResource": convert_string(excel_instance.MeetupScenarioReplayResource(), password),
        "MeetupScenarioReplayTitleLocalize": convert_string(excel_instance.MeetupScenarioReplayTitleLocalize(), password),
        "SpecialOperactionCollectionGroupId": convert_long(excel_instance.SpecialOperactionCollectionGroupId(), password),
        "TreasureNormalVariationAmount": convert_int(excel_instance.TreasureNormalVariationAmount(), password),
        "TreasureLoopVariationAmount": convert_int(excel_instance.TreasureLoopVariationAmount(), password),
        "TreasureLimitVariationLoopCount": convert_int(excel_instance.TreasureLimitVariationLoopCount(), password),
        "TreasureLimitVariationClearLoopCount": convert_int(excel_instance.TreasureLimitVariationClearLoopCount(), password),
        "EventStoryReplayHideEventContentId": convert_int(excel_instance.EventStoryReplayHideEventContentId(), password),
    }

def dump_ConstFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DialogSmoothTime": convert_int(excel_instance.DialogSmoothTime(), password),
        "TalkDialogDurationDefault": convert_int(excel_instance.TalkDialogDurationDefault(), password),
        "ThinkDialogDurationDefault": convert_int(excel_instance.ThinkDialogDurationDefault(), password),
        "IdleThinkDelayMin": convert_int(excel_instance.IdleThinkDelayMin(), password),
        "IdleThinkDelayMax": convert_int(excel_instance.IdleThinkDelayMax(), password),
    }

def dump_ConstMinigameRoadPuzzleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RoadPuzzleMapBoundaryOffsetLeft": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetLeft(), password),
        "RoadPuzzleMapBoundaryOffsetRight": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetRight(), password),
        "RoadPuzzleMapBoundaryOffsetTop": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetTop(), password),
        "RoadPuzzleMapBoundaryOffsetBottom": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetBottom(), password),
        "RoadPuzzleMapCenterOffsetX": convert_float(excel_instance.RoadPuzzleMapCenterOffsetX(), password),
        "RoadPuzzleMapCenterOffsetY": convert_float(excel_instance.RoadPuzzleMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "StageLoadingProgressTime": convert_float(excel_instance.StageLoadingProgressTime(), password),
        "TileRotationDegree": convert_int(excel_instance.TileRotationDegree(), password),
        "StartStageIndex": convert_int(excel_instance.StartStageIndex(), password),
        "LoopStageIndex": convert_int(excel_instance.LoopStageIndex(), password),
    }

def dump_ConstMiniGameShootingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NormalStageId": convert_long(excel_instance.NormalStageId(), password),
        "NormalSectionCount": convert_int(excel_instance.NormalSectionCount(), password),
        "HardStageId": convert_long(excel_instance.HardStageId(), password),
        "HardSectionCount": convert_int(excel_instance.HardSectionCount(), password),
        "FreeStageId": convert_long(excel_instance.FreeStageId(), password),
        "FreeSectionCount": convert_int(excel_instance.FreeSectionCount(), password),
        "PlayerCharacterId": [convert_long(excel_instance.PlayerCharacterId(j), password) for j in range(excel_instance.PlayerCharacterIdLength())],
        "HiddenPlayerCharacterId": convert_long(excel_instance.HiddenPlayerCharacterId(), password),
        "CameraSmoothTime": convert_float(excel_instance.CameraSmoothTime(), password),
        "SpawnEffectPath": convert_string(excel_instance.SpawnEffectPath(), password),
        "WaitTimeAfterSpawn": convert_float(excel_instance.WaitTimeAfterSpawn(), password),
        "FreeGearInterval": convert_int(excel_instance.FreeGearInterval(), password),
    }

def dump_ConstMinigameTBGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeft(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRight(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTop(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottom(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetX(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "ThemaLoadingProgressTime": convert_float(excel_instance.ThemaLoadingProgressTime(), password),
        "MapAllyRotation": convert_float(excel_instance.MapAllyRotation(), password),
        "AniAllyBattleAttack": convert_string(excel_instance.AniAllyBattleAttack(), password),
        "EffectAllyBattleAttack": convert_string(excel_instance.EffectAllyBattleAttack(), password),
        "EffectAllyBattleDamage": convert_string(excel_instance.EffectAllyBattleDamage(), password),
        "AniEnemyBattleAttack": convert_string(excel_instance.AniEnemyBattleAttack(), password),
        "EffectEnemyBattleAttack": convert_string(excel_instance.EffectEnemyBattleAttack(), password),
        "EffectEnemyBattleDamage": convert_string(excel_instance.EffectEnemyBattleDamage(), password),
        "EncounterAllyRotation": convert_float(excel_instance.EncounterAllyRotation(), password),
        "EncounterEnemyRotation": convert_float(excel_instance.EncounterEnemyRotation(), password),
        "EncounterRewardReceiveIndex": convert_int(excel_instance.EncounterRewardReceiveIndex(), password),
    }

def dump_ConstNewbieContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NewbieGachaReleaseDate": convert_string(excel_instance.NewbieGachaReleaseDate(), password),
        "NewbieGachaCheckDays": convert_int(excel_instance.NewbieGachaCheckDays(), password),
        "NewbieGachaTokenGraceTime": convert_int(excel_instance.NewbieGachaTokenGraceTime(), password),
        "NewbieAttendanceReleaseDate": convert_string(excel_instance.NewbieAttendanceReleaseDate(), password),
        "NewbieAttendanceStartableEndDay": convert_int(excel_instance.NewbieAttendanceStartableEndDay(), password),
        "NewbieAttendanceEndDay": convert_int(excel_instance.NewbieAttendanceEndDay(), password),
    }

def dump_ConstStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "HexaMapBoundaryOffset": convert_float(excel_instance.HexaMapBoundaryOffset(), password),
        "HexaMapStartCameraOffset": convert_float(excel_instance.HexaMapStartCameraOffset(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "HealCostType": CurrencyTypes(convert_int(excel_instance.HealCostType(), password)).name,
        "HealCostAmount": [convert_long(excel_instance.HealCostAmount(j), password) for j in range(excel_instance.HealCostAmountLength())],
        "CanHealHpRate": convert_int(excel_instance.CanHealHpRate(), password),
        "PlayTimeLimitInSeconds": convert_long(excel_instance.PlayTimeLimitInSeconds(), password),
        "AdventureEchelonCount": convert_int(excel_instance.AdventureEchelonCount(), password),
        "RaidEchelonCount": convert_int(excel_instance.RaidEchelonCount(), password),
        "DefaultEchelonCount": convert_int(excel_instance.DefaultEchelonCount(), password),
        "EventContentEchelonCount": convert_int(excel_instance.EventContentEchelonCount(), password),
        "TimeAttackDungeonEchelonCount": convert_int(excel_instance.TimeAttackDungeonEchelonCount(), password),
        "WorldRaidEchelonCount": convert_int(excel_instance.WorldRaidEchelonCount(), password),
        "TacticSkipClearTimeSeconds": convert_int(excel_instance.TacticSkipClearTimeSeconds(), password),
        "TacticSkipFramePerSecond": convert_int(excel_instance.TacticSkipFramePerSecond(), password),
        "ConquestEchelonCount": convert_int(excel_instance.ConquestEchelonCount(), password),
        "StoryEchelonCount": convert_int(excel_instance.StoryEchelonCount(), password),
        "MultiSweepPresetCount": convert_int(excel_instance.MultiSweepPresetCount(), password),
        "MultiSweepPresetNameMaxLength": convert_int(excel_instance.MultiSweepPresetNameMaxLength(), password),
        "MultiSweepPresetSelectStageMaxCount": convert_int(excel_instance.MultiSweepPresetSelectStageMaxCount(), password),
        "MultiSweepPresetMaxSweepCount": convert_int(excel_instance.MultiSweepPresetMaxSweepCount(), password),
        "MultiSweepPresetSelectParcelMaxCount": convert_int(excel_instance.MultiSweepPresetSelectParcelMaxCount(), password),
    }

def dump_ContentsFeverExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConditionContent": FeverBattleType(convert_int(excel_instance.ConditionContent(), password)).name,
        "SkillFeverCheckCondition": SkillPriorityCheckTarget(convert_int(excel_instance.SkillFeverCheckCondition(), password)).name,
        "SkillCostFever": convert_long(excel_instance.SkillCostFever(), password),
        "FeverStartTime": convert_long(excel_instance.FeverStartTime(), password),
        "FeverDurationTime": convert_long(excel_instance.FeverDurationTime(), password),
    }

def dump_CostumeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeGroupId": convert_long(excel_instance.CostumeGroupId(), password),
        "CostumeUniqueId": convert_long(excel_instance.CostumeUniqueId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "IsDefault": excel_instance.IsDefault(),
        "CollectionVisible": excel_instance.CollectionVisible(),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "CharacterSkillListGroupId": convert_long(excel_instance.CharacterSkillListGroupId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "SpineResourceNameDiorama": convert_string(excel_instance.SpineResourceNameDiorama(), password),
        "SpineResourceNameDioramaForFormConversion": [convert_string(excel_instance.SpineResourceNameDioramaForFormConversion(j), password) for j in range(excel_instance.SpineResourceNameDioramaForFormConversionLength())],
        "EntityMaterialType": EntityMaterialType(convert_int(excel_instance.EntityMaterialType(), password)).name,
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "CafeModelPrefabName": convert_string(excel_instance.CafeModelPrefabName(), password),
        "EchelonModelPrefabName": convert_string(excel_instance.EchelonModelPrefabName(), password),
        "StrategyModelPrefabName": convert_string(excel_instance.StrategyModelPrefabName(), password),
        "TextureDir": convert_string(excel_instance.TextureDir(), password),
        "CollectionTexturePath": convert_string(excel_instance.CollectionTexturePath(), password),
        "CollectionBGTexturePath": convert_string(excel_instance.CollectionBGTexturePath(), password),
        "CombatStyleTexturePath": convert_string(excel_instance.CombatStyleTexturePath(), password),
        "UseObjectHPBAR": excel_instance.UseObjectHPBAR(),
        "TextureBoss": convert_string(excel_instance.TextureBoss(), password),
        "TextureSkillCard": [convert_string(excel_instance.TextureSkillCard(j), password) for j in range(excel_instance.TextureSkillCardLength())],
        "InformationPacel": convert_string(excel_instance.InformationPacel(), password),
        "AnimationSSR": convert_string(excel_instance.AnimationSSR(), password),
        "EnterStrategyAnimationName": convert_string(excel_instance.EnterStrategyAnimationName(), password),
        "AnimationValidator": excel_instance.AnimationValidator(),
        "CharacterVoiceGroupId": convert_long(excel_instance.CharacterVoiceGroupId(), password),
        "ShowObjectHpStatus": excel_instance.ShowObjectHpStatus(),
    }

def dump_CouponStuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StuffId": convert_long(excel_instance.StuffId(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_long(excel_instance.ParcelId(), password),
        "LimitAmount": convert_int(excel_instance.LimitAmount(), password),
        "CouponStuffNameLocalizeKey": convert_string(excel_instance.CouponStuffNameLocalizeKey(), password),
    }

def dump_DefaultCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "FavoriteCharacter": excel_instance.FavoriteCharacter(),
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "FavorRank": convert_int(excel_instance.FavorRank(), password),
        "StarGrade": convert_int(excel_instance.StarGrade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevel(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevel(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevel(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevel(), password),
    }

def dump_DefaultEchelonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EchlonId": convert_int(excel_instance.EchlonId(), password),
        "LeaderId": convert_long(excel_instance.LeaderId(), password),
        "MainId": [convert_long(excel_instance.MainId(j), password) for j in range(excel_instance.MainIdLength())],
        "SupportId": [convert_long(excel_instance.SupportId(j), password) for j in range(excel_instance.SupportIdLength())],
        "TssId": convert_long(excel_instance.TssId(), password),
    }

def dump_DefaultFurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.Location(), password)).name,
        "PositionX": convert_float(excel_instance.PositionX(), password),
        "PositionY": convert_float(excel_instance.PositionY(), password),
        "Rotation": convert_float(excel_instance.Rotation(), password),
    }

def dump_DefaultMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "MailSendPeriodFrom": convert_string(excel_instance.MailSendPeriodFrom(), password),
        "MailSendPeriodTo": convert_string(excel_instance.MailSendPeriodTo(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_DefaultParcelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_long(excel_instance.ParcelId(), password),
        "ParcelAmount": convert_long(excel_instance.ParcelAmount(), password),
    }

def dump_EchelonConstraintExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "IsWhiteList": excel_instance.IsWhiteList(),
        "CharacterId": [convert_long(excel_instance.CharacterId(j), password) for j in range(excel_instance.CharacterIdLength())],
        "PersonalityId": [convert_long(excel_instance.PersonalityId(j), password) for j in range(excel_instance.PersonalityIdLength())],
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "School": School(convert_int(excel_instance.School(), password)).name,
        "Club": Club(convert_int(excel_instance.Club(), password)).name,
        "Role": TacticRole(convert_int(excel_instance.Role(), password)).name,
    }

def dump_EliminateRaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_long(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "RankStart": convert_long(excel_instance.RankStart(), password),
        "RankEnd": convert_long(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_long(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_long(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_long(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueName(j), password) for j in range(excel_instance.RewardParcelUniqueNameLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EliminateRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_long(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "LobbyTableBGPath": convert_string(excel_instance.LobbyTableBGPath(), password),
        "LobbyScreenBGPath": convert_string(excel_instance.LobbyScreenBGPath(), password),
        "OpenRaidBossGroup01": convert_string(excel_instance.OpenRaidBossGroup01(), password),
        "OpenRaidBossGroup02": convert_string(excel_instance.OpenRaidBossGroup02(), password),
        "OpenRaidBossGroup03": convert_string(excel_instance.OpenRaidBossGroup03(), password),
        "RankingRewardGroupId": convert_long(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGauge": [convert_long(excel_instance.StackedSeasonRewardGauge(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeLength())],
        "SeasonRewardId": [convert_long(excel_instance.SeasonRewardId(j), password) for j in range(excel_instance.SeasonRewardIdLength())],
        "LimitedRewardIdNormal": convert_long(excel_instance.LimitedRewardIdNormal(), password),
        "LimitedRewardIdHard": convert_long(excel_instance.LimitedRewardIdHard(), password),
        "LimitedRewardIdVeryhard": convert_long(excel_instance.LimitedRewardIdVeryhard(), password),
        "LimitedRewardIdHardcore": convert_long(excel_instance.LimitedRewardIdHardcore(), password),
        "LimitedRewardIdExtreme": convert_long(excel_instance.LimitedRewardIdExtreme(), password),
        "LimitedRewardIdInsane": convert_long(excel_instance.LimitedRewardIdInsane(), password),
        "LimitedRewardIdTorment": convert_long(excel_instance.LimitedRewardIdTorment(), password),
    }

def dump_EliminateRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "UseBossIndex": excel_instance.UseBossIndex(),
        "UseBossAIPhaseSync": excel_instance.UseBossAIPhaseSync(),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroup(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostType(), password)).name,
        "RaidEnterCostId": convert_long(excel_instance.RaidEnterCostId(), password),
        "RaidEnterCostAmount": convert_int(excel_instance.RaidEnterCostAmount(), password),
        "BossSpinePath": convert_string(excel_instance.BossSpinePath(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_long(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_long(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "IsOpen": excel_instance.IsOpen(),
        "MaxPlayerCount": convert_long(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "GroundDevName": convert_string(excel_instance.GroundDevName(), password),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironment(), password)).name,
        "DefaultClearScore": convert_long(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_long(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_long(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_long(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_long(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_long(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_long(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_long(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": excel_instance.ShowSkillCard(),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_EliminateRaidStageLimitedRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LimitedRewardId": convert_long(excel_instance.LimitedRewardId(), password),
        "LimitedRewardParcelType": [ParcelType(convert_int(excel_instance.LimitedRewardParcelType(j), password)).name for j in range(excel_instance.LimitedRewardParcelTypeLength())],
        "LimitedRewardParcelUniqueId": [convert_long(excel_instance.LimitedRewardParcelUniqueId(j), password) for j in range(excel_instance.LimitedRewardParcelUniqueIdLength())],
        "LimitedRewardAmount": [convert_long(excel_instance.LimitedRewardAmount(j), password) for j in range(excel_instance.LimitedRewardAmountLength())],
    }

def dump_EliminateRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": excel_instance.IsClearStageRewardHideInfo(),
        "ClearStageRewardProb": convert_long(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_long(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_long(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_EliminateRaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_long(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelType": [ParcelType(convert_int(excel_instance.SeasonRewardParcelType(j), password)).name for j in range(excel_instance.SeasonRewardParcelTypeLength())],
        "SeasonRewardParcelUniqueId": [convert_long(excel_instance.SeasonRewardParcelUniqueId(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdLength())],
        "SeasonRewardParcelUniqueName": [convert_string(excel_instance.SeasonRewardParcelUniqueName(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueNameLength())],
        "SeasonRewardAmount": [convert_long(excel_instance.SeasonRewardAmount(j), password) for j in range(excel_instance.SeasonRewardAmountLength())],
    }

def dump_EmoticonSpecialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "CharacterUniqueId": convert_long(excel_instance.CharacterUniqueId(), password),
        "Random": convert_string(excel_instance.Random(), password),
    }

def dump_EventContentArchiveBannerOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "OffsetX": convert_float(excel_instance.OffsetX(), password),
        "OffsetY": convert_float(excel_instance.OffsetY(), password),
        "ScaleX": convert_float(excel_instance.ScaleX(), password),
        "ScaleY": convert_float(excel_instance.ScaleY(), password),
    }

def dump_EventContentBoxGachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "Round": convert_long(excel_instance.Round(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
    }

def dump_EventContentBoxGachaManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Round": convert_long(excel_instance.Round(), password),
        "GoodsId": convert_long(excel_instance.GoodsId(), password),
        "IsLoop": excel_instance.IsLoop(),
    }

def dump_EventContentBoxGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "GroupElementAmount": convert_long(excel_instance.GroupElementAmount(), password),
        "Round": convert_long(excel_instance.Round(), password),
        "IsLegacy": excel_instance.IsLegacy(),
        "IsPrize": excel_instance.IsPrize(),
        "GoodsId": [convert_long(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
    }

def dump_EventContentBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentBuffId": convert_long(excel_instance.EventContentBuffId(), password),
        "IsBuff": excel_instance.IsBuff(),
        "CharacterTag": Tag(convert_int(excel_instance.CharacterTag(), password)).name,
        "EnumType": EventContentBuffFindRule(convert_int(excel_instance.EnumType(), password)).name,
        "EnumTypeValue": [convert_string(excel_instance.EnumTypeValue(j), password) for j in range(excel_instance.EnumTypeValueLength())],
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "BuffDescriptionLocalizeCodeId": convert_string(excel_instance.BuffDescriptionLocalizeCodeId(), password),
    }

def dump_EventContentBuffGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "BuffContentId": convert_long(excel_instance.BuffContentId(), password),
        "BuffGroupId": convert_long(excel_instance.BuffGroupId(), password),
        "BuffGroupNameLocalizeCodeId": convert_string(excel_instance.BuffGroupNameLocalizeCodeId(), password),
        "EventContentBuffId1": convert_long(excel_instance.EventContentBuffId1(), password),
        "BuffNameLocalizeCodeId1": convert_string(excel_instance.BuffNameLocalizeCodeId1(), password),
        "BuffDescriptionIconPath1": convert_string(excel_instance.BuffDescriptionIconPath1(), password),
        "EventContentBuffId2": convert_long(excel_instance.EventContentBuffId2(), password),
        "BuffNameLocalizeCodeId2": convert_string(excel_instance.BuffNameLocalizeCodeId2(), password),
        "BuffDescriptionIconPath2": convert_string(excel_instance.BuffDescriptionIconPath2(), password),
        "EventContentDebuffId": convert_long(excel_instance.EventContentDebuffId(), password),
        "DebuffNameLocalizeCodeId": convert_string(excel_instance.DebuffNameLocalizeCodeId(), password),
        "DeBuffDescriptionIconPath": convert_string(excel_instance.DeBuffDescriptionIconPath(), password),
        "BuffGroupProb": convert_long(excel_instance.BuffGroupProb(), password),
    }

def dump_EventContentCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CardGroupId": convert_int(excel_instance.CardGroupId(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "BackIconPath": convert_string(excel_instance.BackIconPath(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
    }

def dump_EventContentCardShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "CostGoodsId": convert_long(excel_instance.CostGoodsId(), password),
        "CardGroupId": convert_int(excel_instance.CardGroupId(), password),
        "IsLegacy": excel_instance.IsLegacy(),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbWeight1": convert_int(excel_instance.ProbWeight1(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ChangeCount": convert_long(excel_instance.ChangeCount(), password),
        "IsLast": excel_instance.IsLast(),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "ChangeCostType": ParcelType(convert_int(excel_instance.ChangeCostType(), password)).name,
        "ChangeCostId": convert_long(excel_instance.ChangeCostId(), password),
        "ChangeCostAmount": convert_int(excel_instance.ChangeCostAmount(), password),
    }

def dump_EventContentChangeScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ChangeType": EventChangeType(convert_int(excel_instance.ChangeType(), password)).name,
        "ChangeCount": convert_long(excel_instance.ChangeCount(), password),
        "ScenarioGroupId": convert_long(excel_instance.ScenarioGroupId(), password),
    }

def dump_EventContentCharacterBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "EventContentItemType": [EventContentItemType(convert_int(excel_instance.EventContentItemType(j), password)).name for j in range(excel_instance.EventContentItemTypeLength())],
        "BonusPercentage": [convert_long(excel_instance.BonusPercentage(j), password) for j in range(excel_instance.BonusPercentageLength())],
    }

def dump_EventContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionType(), password)).name,
        "UnlockConditionParameter": [convert_long(excel_instance.UnlockConditionParameter(j), password) for j in range(excel_instance.UnlockConditionParameterLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "UnlockConditionCount": convert_long(excel_instance.UnlockConditionCount(), password),
        "IsObject": excel_instance.IsObject(),
        "IsObjectOnFullResource": excel_instance.IsObjectOnFullResource(),
        "IsHorizon": excel_instance.IsHorizon(),
        "EmblemResource": convert_string(excel_instance.EmblemResource(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResource(), password),
        "FullResource": convert_string(excel_instance.FullResource(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeId(), password),
    }

def dump_EventContentCurrencyItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemType(), password)).name,
        "ItemUniqueId": convert_long(excel_instance.ItemUniqueId(), password),
        "UseShortCutContentType": convert_string(excel_instance.UseShortCutContentType(), password),
    }

def dump_EventContentDebuffRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventStageId": convert_long(excel_instance.EventStageId(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemType(), password)).name,
        "RewardPercentage": convert_long(excel_instance.RewardPercentage(), password),
    }

def dump_EventContentDiceRaceEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultType(), password)).name,
        "IsDiceResult": excel_instance.IsDiceResult(),
        "AniClip": convert_string(excel_instance.AniClip(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
    }

def dump_EventContentDiceRaceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DiceCostGoodsId": convert_long(excel_instance.DiceCostGoodsId(), password),
        "SkipableLap": convert_int(excel_instance.SkipableLap(), password),
        "DiceRacePawnPrefab": convert_string(excel_instance.DiceRacePawnPrefab(), password),
        "IsUsingFixedDice": excel_instance.IsUsingFixedDice(),
        "DiceRaceEventType": [convert_string(excel_instance.DiceRaceEventType(j), password) for j in range(excel_instance.DiceRaceEventTypeLength())],
    }

def dump_EventContentDiceRaceNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "NodeId": convert_long(excel_instance.NodeId(), password),
        "EventContentDiceRaceNodeType": EventContentDiceRaceNodeType(convert_int(excel_instance.EventContentDiceRaceNodeType(), password)).name,
        "MoveForwardTypeArg": convert_int(excel_instance.MoveForwardTypeArg(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentDiceRaceProbExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultType(), password)).name,
        "CostItemId": convert_long(excel_instance.CostItemId(), password),
        "CostItemAmount": convert_int(excel_instance.CostItemAmount(), password),
        "DiceResult": convert_int(excel_instance.DiceResult(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
    }

def dump_EventContentDiceRaceTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "RewardID": convert_long(excel_instance.RewardID(), password),
        "RequiredLapFinishCount": convert_int(excel_instance.RequiredLapFinishCount(), password),
        "DisplayLapFinishCount": convert_int(excel_instance.DisplayLapFinishCount(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "BgImagePath": convert_string(excel_instance.BgImagePath(), password),
    }

def dump_EventContentFortuneGachaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "NameImagePath": convert_string(excel_instance.NameImagePath(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_EventContentFortuneGachaModifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TargetGrade": convert_int(excel_instance.TargetGrade(), password),
        "ProbModifyStartCount": convert_int(excel_instance.ProbModifyStartCount(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
        "BucketImagePath": convert_string(excel_instance.BucketImagePath(), password),
        "ShopBgImagePath": convert_string(excel_instance.ShopBgImagePath(), password),
        "TitleLocalizeKey": convert_string(excel_instance.TitleLocalizeKey(), password),
    }

def dump_EventContentFortuneGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "Grade": convert_int(excel_instance.Grade(), password),
        "CostGoodsId": convert_long(excel_instance.CostGoodsId(), password),
        "IsLegacy": excel_instance.IsLegacy(),
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupId(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbModifyValue": convert_int(excel_instance.ProbModifyValue(), password),
        "ProbModifyLimit": convert_int(excel_instance.ProbModifyLimit(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentLobbyMenuExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "IconSpriteName": convert_string(excel_instance.IconSpriteName(), password),
        "ButtonText": convert_string(excel_instance.ButtonText(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "IconOffsetX": convert_float(excel_instance.IconOffsetX(), password),
        "IconOffsetY": convert_float(excel_instance.IconOffsetY(), password),
        "ReddotSpriteName": convert_string(excel_instance.ReddotSpriteName(), password),
    }

def dump_EventContentLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPath(), password),
        "LocationResetScheduleCount": convert_int(excel_instance.LocationResetScheduleCount(), password),
        "ScheduleEventPointCostParcelType": ParcelType(convert_int(excel_instance.ScheduleEventPointCostParcelType(), password)).name,
        "ScheduleEventPointCostParcelId": convert_long(excel_instance.ScheduleEventPointCostParcelId(), password),
        "ScheduleEventPointCostParcelAmount": convert_long(excel_instance.ScheduleEventPointCostParcelAmount(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "InformationGroupId": convert_long(excel_instance.InformationGroupId(), password),
    }

def dump_EventContentLocationRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.Location(), password),
        "ScheduleGroupId": convert_long(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_long(excel_instance.OrderInGroup(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTexture(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocationRank": convert_long(excel_instance.LocationRank(), password),
        "FavorExp": convert_long(excel_instance.FavorExp(), password),
        "SecretStoneAmount": convert_long(excel_instance.SecretStoneAmount(), password),
        "SecretStoneProb": convert_long(excel_instance.SecretStoneProb(), password),
        "ExtraFavorExp": convert_long(excel_instance.ExtraFavorExp(), password),
        "ExtraFavorExpProb": convert_long(excel_instance.ExtraFavorExpProb(), password),
        "ExtraRewardParcelType": [ParcelType(convert_int(excel_instance.ExtraRewardParcelType(j), password)).name for j in range(excel_instance.ExtraRewardParcelTypeLength())],
        "ExtraRewardParcelId": [convert_long(excel_instance.ExtraRewardParcelId(j), password) for j in range(excel_instance.ExtraRewardParcelIdLength())],
        "ExtraRewardAmount": [convert_long(excel_instance.ExtraRewardAmount(j), password) for j in range(excel_instance.ExtraRewardAmountLength())],
        "ExtraRewardProb": [convert_long(excel_instance.ExtraRewardProb(j), password) for j in range(excel_instance.ExtraRewardProbLength())],
        "IsExtraRewardDisplayed": [excel_instance.IsExtraRewardDisplayed(j) for j in range(excel_instance.IsExtraRewardDisplayedLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentMeetupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "ConditionScenarioGroupId": convert_long(excel_instance.ConditionScenarioGroupId(), password),
        "ConditionType": MeetupConditionType(convert_int(excel_instance.ConditionType(), password)).name,
        "ConditionParameter": [convert_long(excel_instance.ConditionParameter(j), password) for j in range(excel_instance.ConditionParameterLength())],
        "ConditionPrintType": MeetupConditionPrintType(convert_int(excel_instance.ConditionPrintType(), password)).name,
    }

def dump_EventContentMeetupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CostParcelType": ParcelType(convert_int(excel_instance.CostParcelType(), password)).name,
        "CostId": convert_long(excel_instance.CostId(), password),
        "CostAmount": convert_int(excel_instance.CostAmount(), password),
    }

def dump_EventContentMiniEventShortCutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ShorcutContentType": EventTargetType(convert_int(excel_instance.ShorcutContentType(), password)).name,
        "ShortcutUI": convert_string(excel_instance.ShortcutUI(), password),
    }

def dump_EventContentMiniEventTokenExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ItemUniqueId": convert_long(excel_instance.ItemUniqueId(), password),
        "MaximumAmount": convert_long(excel_instance.MaximumAmount(), password),
    }

def dump_EventContentMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "GroupName": convert_string(excel_instance.GroupName(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": excel_instance.ViewFlag(),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_long(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_long(excel_instance.AccountLevel(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "ChallengeStageShortcut": convert_long(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "IsCompleteExtensionTime": excel_instance.IsCompleteExtensionTime(),
        "CompleteConditionCount": convert_long(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_long(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTag(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "CompleteConditionMissionId": [convert_long(excel_instance.CompleteConditionMissionId(j), password) for j in range(excel_instance.CompleteConditionMissionIdLength())],
        "CompleteConditionMissionCount": convert_long(excel_instance.CompleteConditionMissionCount(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelType(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_long(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
        "ConditionRewardParcelType": [ParcelType(convert_int(excel_instance.ConditionRewardParcelType(j), password)).name for j in range(excel_instance.ConditionRewardParcelTypeLength())],
        "ConditionRewardParcelId": [convert_long(excel_instance.ConditionRewardParcelId(j), password) for j in range(excel_instance.ConditionRewardParcelIdLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmount(j), password) for j in range(excel_instance.ConditionRewardAmountLength())],
    }

def dump_EventContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_EventContentScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ReplayDisplayGroup": convert_int(excel_instance.ReplayDisplayGroup(), password),
        "Order": convert_long(excel_instance.Order(), password),
        "RecollectionNumber": convert_long(excel_instance.RecollectionNumber(), password),
        "IsRecollection": excel_instance.IsRecollection(),
        "IsMeetup": excel_instance.IsMeetup(),
        "IsOmnibus": excel_instance.IsOmnibus(),
        "ScenarioGroupId": [convert_long(excel_instance.ScenarioGroupId(j), password) for j in range(excel_instance.ScenarioGroupIdLength())],
        "ScenarioConditionType": EventContentScenarioConditionType(convert_int(excel_instance.ScenarioConditionType(), password)).name,
        "ConditionAmount": convert_long(excel_instance.ConditionAmount(), password),
        "ConditionEventContentId": convert_long(excel_instance.ConditionEventContentId(), password),
        "ClearedScenarioGroupId": convert_long(excel_instance.ClearedScenarioGroupId(), password),
        "RecollectionSummaryLocalizeScenarioId": convert_uint(excel_instance.RecollectionSummaryLocalizeScenarioId(), password),
        "RecollectionResource": convert_string(excel_instance.RecollectionResource(), password),
        "IsRecollectionHorizon": excel_instance.IsRecollectionHorizon(),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_long(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "OriginalEventContentId": convert_long(excel_instance.OriginalEventContentId(), password),
        "IsReturn": excel_instance.IsReturn(),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContent(), password)).name,
        "EventDisplay": excel_instance.EventDisplay(),
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "SubEventType": SubEventType(convert_int(excel_instance.SubEventType(), password)).name,
        "SubEvent": excel_instance.SubEvent(),
        "EventItemId": convert_long(excel_instance.EventItemId(), password),
        "MainEventId": convert_long(excel_instance.MainEventId(), password),
        "EventChangeOpenCondition": convert_long(excel_instance.EventChangeOpenCondition(), password),
        "BeforehandExposedTime": convert_string(excel_instance.BeforehandExposedTime(), password),
        "EventContentOpenTime": convert_string(excel_instance.EventContentOpenTime(), password),
        "EventContentCloseTime": convert_string(excel_instance.EventContentCloseTime(), password),
        "ExtensionTime": convert_string(excel_instance.ExtensionTime(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPath(), password),
        "SubIconParcelPath": convert_string(excel_instance.SubIconParcelPath(), password),
        "BeforehandBgImagePath": convert_string(excel_instance.BeforehandBgImagePath(), password),
        "MinigamePrologScenarioGroupId": convert_long(excel_instance.MinigamePrologScenarioGroupId(), password),
        "BeforehandScenarioGroupId": [convert_long(excel_instance.BeforehandScenarioGroupId(j), password) for j in range(excel_instance.BeforehandScenarioGroupIdLength())],
        "MainBannerImagePath": convert_string(excel_instance.MainBannerImagePath(), password),
        "MainBgImagePath": convert_string(excel_instance.MainBgImagePath(), password),
        "ShiftTriggerStageId": convert_long(excel_instance.ShiftTriggerStageId(), password),
        "ShiftMainBgImagePath": convert_string(excel_instance.ShiftMainBgImagePath(), password),
        "MinigameLobbyPrefabName": convert_string(excel_instance.MinigameLobbyPrefabName(), password),
        "MinigameVictoryPrefabName": convert_string(excel_instance.MinigameVictoryPrefabName(), password),
        "MinigameMissionBgPrefabName": convert_string(excel_instance.MinigameMissionBgPrefabName(), password),
        "MinigameMissionBgImagePath": convert_string(excel_instance.MinigameMissionBgImagePath(), password),
        "CardBgImagePath": convert_string(excel_instance.CardBgImagePath(), password),
        "EventAssist": excel_instance.EventAssist(),
        "EventContentReleaseType": EventContentReleaseType(convert_int(excel_instance.EventContentReleaseType(), password)).name,
        "EventContentStageRewardIdPermanent": convert_long(excel_instance.EventContentStageRewardIdPermanent(), password),
        "RewardTagPermanent": RewardTag(convert_int(excel_instance.RewardTagPermanent(), password)).name,
        "MiniEventShortCutScenarioModeId": convert_long(excel_instance.MiniEventShortCutScenarioModeId(), password),
        "ScenarioContentCollectionGroupId": convert_long(excel_instance.ScenarioContentCollectionGroupId(), password),
    }

def dump_EventContentShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "IsLegacy": excel_instance.IsLegacy(),
        "GoodsId": [convert_long(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_long(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_long(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": excel_instance.RestrictBuyWhenInventoryFull(),
    }

def dump_EventContentShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelType(j), password)).name for j in range(excel_instance.CostParcelTypeLength())],
        "CostParcelId": [convert_long(excel_instance.CostParcelId(j), password) for j in range(excel_instance.CostParcelIdLength())],
        "IsRefresh": excel_instance.IsRefresh(),
        "IsSoldOutDimmed": excel_instance.IsSoldOutDimmed(),
        "AutoRefreshCoolTime": convert_long(excel_instance.AutoRefreshCoolTime(), password),
        "RefreshAbleCount": convert_long(excel_instance.RefreshAbleCount(), password),
        "GoodsId": [convert_long(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFrom(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodTo(), password),
        "ShopProductUpdateDate": convert_string(excel_instance.ShopProductUpdateDate(), password),
    }

def dump_EventContentShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IsLegacy": excel_instance.IsLegacy(),
        "GoodsId": convert_long(excel_instance.GoodsId(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
    }

def dump_EventContentSpecialOperationsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "PointItemId": convert_long(excel_instance.PointItemId(), password),
    }

def dump_EventContentSpineDialogOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "CostumeUniqueId": convert_long(excel_instance.CostumeUniqueId(), password),
        "SpineOffsetX": convert_float(excel_instance.SpineOffsetX(), password),
        "SpineOffsetY": convert_float(excel_instance.SpineOffsetY(), password),
        "DialogOffsetX": convert_float(excel_instance.DialogOffsetX(), password),
        "DialogOffsetY": convert_float(excel_instance.DialogOffsetY(), password),
    }

def dump_EventContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "OpenDate": convert_long(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_long(excel_instance.OpenEventPoint(), password),
        "OpenConditionScenarioPermanentSubEventId": convert_long(excel_instance.OpenConditionScenarioPermanentSubEventId(), password),
        "PrevStageSubEventId": convert_long(excel_instance.PrevStageSubEventId(), password),
        "OpenConditionScenarioId": convert_long(excel_instance.OpenConditionScenarioId(), password),
        "OpenConditionContentType": EventContentType(convert_int(excel_instance.OpenConditionContentType(), password)).name,
        "OpenConditionContentId": convert_long(excel_instance.OpenConditionContentId(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_long(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_long(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_long(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_long(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "EventContentStageRewardId": convert_long(excel_instance.EventContentStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_string(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundID": convert_long(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "InstantClear": excel_instance.InstantClear(),
        "BuffContentId": convert_long(excel_instance.BuffContentId(), password),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "ChallengeDisplay": excel_instance.ChallengeDisplay(),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "IsDefeatBattle": excel_instance.IsDefeatBattle(),
        "StageHint": convert_uint(excel_instance.StageHint(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_EventContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_EventContentStageTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "RequiredEventItemAmount": convert_long(excel_instance.RequiredEventItemAmount(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "OriginalZoneId": convert_long(excel_instance.OriginalZoneId(), password),
        "LocationId": convert_long(excel_instance.LocationId(), password),
        "LocationRank": convert_long(excel_instance.LocationRank(), password),
        "EventPointForLocationRank": convert_long(excel_instance.EventPointForLocationRank(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StudentVisitProb": [convert_long(excel_instance.StudentVisitProb(j), password) for j in range(excel_instance.StudentVisitProbLength())],
        "RewardGroupId": convert_long(excel_instance.RewardGroupId(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
        "WhiteListTags": [Tag(convert_int(excel_instance.WhiteListTags(j), password)).name for j in range(excel_instance.WhiteListTagsLength())],
    }

def dump_EventContentZoneVisitRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentLocationId": convert_long(excel_instance.EventContentLocationId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "CharacterDevName": convert_string(excel_instance.CharacterDevName(), password),
        "VisitRewardParcelType": [ParcelType(convert_int(excel_instance.VisitRewardParcelType(j), password)).name for j in range(excel_instance.VisitRewardParcelTypeLength())],
        "VisitRewardParcelId": [convert_long(excel_instance.VisitRewardParcelId(j), password) for j in range(excel_instance.VisitRewardParcelIdLength())],
        "VisitRewardAmount": [convert_long(excel_instance.VisitRewardAmount(j), password) for j in range(excel_instance.VisitRewardAmountLength())],
        "VisitRewardProb": [convert_long(excel_instance.VisitRewardProb(j), password) for j in range(excel_instance.VisitRewardProbLength())],
    }

def dump_FieldContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "AreaId": convert_long(excel_instance.AreaId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_long(excel_instance.GroundID(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "InstantClear": excel_instance.InstantClear(),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": excel_instance.SkipFormationSettings(),
        "DailyLastPlay": excel_instance.DailyLastPlay(),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
    }

def dump_FieldContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_FieldCurtainCallFreeModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "OpenDate": convert_long(excel_instance.OpenDate(), password),
        "SetFieldDateID": convert_long(excel_instance.SetFieldDateID(), password),
        "SetFieldQuestOpenDate": convert_long(excel_instance.SetFieldQuestOpenDate(), password),
    }

def dump_FieldDateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "OpenDate": convert_long(excel_instance.OpenDate(), password),
        "DateLocalizeKey": convert_string(excel_instance.DateLocalizeKey(), password),
        "EntrySceneId": convert_long(excel_instance.EntrySceneId(), password),
        "StartConditionType": FieldConditionType(convert_int(excel_instance.StartConditionType(), password)).name,
        "StartConditionId": convert_long(excel_instance.StartConditionId(), password),
        "EndConditionType": FieldConditionType(convert_int(excel_instance.EndConditionType(), password)).name,
        "EndConditionId": convert_long(excel_instance.EndConditionId(), password),
        "EndReadyConditionType": FieldConditionType(convert_int(excel_instance.EndReadyConditionType(), password)).name,
        "EndReadyConditionId": convert_long(excel_instance.EndReadyConditionId(), password),
        "OpenConditionStage": convert_long(excel_instance.OpenConditionStage(), password),
        "CharacterIconPath": convert_string(excel_instance.CharacterIconPath(), password),
        "DateResultBGPath": convert_string(excel_instance.DateResultBGPath(), password),
        "DateResultSpinePath": convert_string(excel_instance.DateResultSpinePath(), password),
        "DateResultSpineOffsetX": convert_float(excel_instance.DateResultSpineOffsetX(), password),
    }

def dump_FieldEvidenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKey(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKey(), password),
        "DetailLocalizeKey": convert_string(excel_instance.DetailLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_FieldInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_long(excel_instance.FieldSeasonId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "FieldDateId": convert_long(excel_instance.FieldDateId(), password),
        "ShowEmoji": excel_instance.ShowEmoji(),
        "KeywordLocalize": convert_string(excel_instance.KeywordLocalize(), password),
        "InteractionType": [FieldInteractionType(convert_int(excel_instance.InteractionType(j), password)).name for j in range(excel_instance.InteractionTypeLength())],
        "InteractionId": [convert_long(excel_instance.InteractionId(j), password) for j in range(excel_instance.InteractionIdLength())],
        "ConditionClass": FieldConditionClass(convert_int(excel_instance.ConditionClass(), password)).name,
        "ConditionClassParameters": [convert_long(excel_instance.ConditionClassParameters(j), password) for j in range(excel_instance.ConditionClassParametersLength())],
        "OnceOnly": excel_instance.OnceOnly(),
        "ConditionIndex": [convert_long(excel_instance.ConditionIndex(j), password) for j in range(excel_instance.ConditionIndexLength())],
        "ConditionType": [FieldConditionType(convert_int(excel_instance.ConditionType(j), password)).name for j in range(excel_instance.ConditionTypeLength())],
        "ConditionId": [convert_long(excel_instance.ConditionId(j), password) for j in range(excel_instance.ConditionIdLength())],
        "NegateCondition": [excel_instance.NegateCondition(j) for j in range(excel_instance.NegateConditionLength())],
    }

def dump_FieldKeywordExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKey(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_FieldMasteryExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "ExpAmount": convert_long(excel_instance.ExpAmount(), password),
        "TokenType": ParcelType(convert_int(excel_instance.TokenType(), password)).name,
        "TokenId": convert_long(excel_instance.TokenId(), password),
        "TokenRequirement": convert_long(excel_instance.TokenRequirement(), password),
        "AccomplishmentConditionType": FieldConditionType(convert_int(excel_instance.AccomplishmentConditionType(), password)).name,
        "AccomplishmentConditionId": convert_long(excel_instance.AccomplishmentConditionId(), password),
    }

def dump_FieldMasteryLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Id": [convert_long(excel_instance.Id(j), password) for j in range(excel_instance.IdLength())],
        "Exp": [convert_long(excel_instance.Exp(j), password) for j in range(excel_instance.ExpLength())],
        "TotalExp": [convert_long(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
        "RewardId": [convert_long(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
    }

def dump_FieldMasteryManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeason": convert_long(excel_instance.FieldSeason(), password),
        "LocalizeEtc": convert_uint(excel_instance.LocalizeEtc(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "LevelId": convert_long(excel_instance.LevelId(), password),
    }

def dump_FieldQuestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_long(excel_instance.FieldSeasonId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "IsDaily": excel_instance.IsDaily(),
        "FieldDateId": convert_long(excel_instance.FieldDateId(), password),
        "Opendate": convert_long(excel_instance.Opendate(), password),
        "AssetPath": convert_string(excel_instance.AssetPath(), password),
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "QuestNamKey": convert_uint(excel_instance.QuestNamKey(), password),
        "QuestDescKey": convert_uint(excel_instance.QuestDescKey(), password),
    }

def dump_FieldRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_FieldSceneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "DateId": convert_long(excel_instance.DateId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPath(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPath(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "ConditionalBGMQuestId": [convert_long(excel_instance.ConditionalBGMQuestId(j), password) for j in range(excel_instance.ConditionalBGMQuestIdLength())],
        "BeginConditionalBGMScenarioGroupId": [convert_long(excel_instance.BeginConditionalBGMScenarioGroupId(j), password) for j in range(excel_instance.BeginConditionalBGMScenarioGroupIdLength())],
        "BeginConditionalBGMInteractionId": [convert_long(excel_instance.BeginConditionalBGMInteractionId(j), password) for j in range(excel_instance.BeginConditionalBGMInteractionIdLength())],
        "EndConditionalBGMScenarioGroupId": [convert_long(excel_instance.EndConditionalBGMScenarioGroupId(j), password) for j in range(excel_instance.EndConditionalBGMScenarioGroupIdLength())],
        "EndConditionalBGMInteractionId": [convert_long(excel_instance.EndConditionalBGMInteractionId(j), password) for j in range(excel_instance.EndConditionalBGMInteractionIdLength())],
        "ConditionalBGMId": [convert_long(excel_instance.ConditionalBGMId(j), password) for j in range(excel_instance.ConditionalBGMIdLength())],
    }

def dump_FieldSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EntryDateId": convert_long(excel_instance.EntryDateId(), password),
        "InstantEntryDateId": convert_long(excel_instance.InstantEntryDateId(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "LobbyBGMChangeStageId": convert_long(excel_instance.LobbyBGMChangeStageId(), password),
        "FieldPrefabControlID": convert_long(excel_instance.FieldPrefabControlID(), password),
        "FieldGetKeywordCallDialogEnum": FieldDialogType(convert_int(excel_instance.FieldGetKeywordCallDialogEnum(), password)).name,
        "MasteryImagePath": convert_string(excel_instance.MasteryImagePath(), password),
        "FieldLobbyTitleImagePath": convert_string(excel_instance.FieldLobbyTitleImagePath(), password),
        "KeywordLogoImagePath": convert_string(excel_instance.KeywordLogoImagePath(), password),
    }

def dump_FieldStoryStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_long(excel_instance.GroundID(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": excel_instance.SkipFormationSettings(),
    }

def dump_FieldTutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "TutorialType": [FieldTutorialType(convert_int(excel_instance.TutorialType(j), password)).name for j in range(excel_instance.TutorialTypeLength())],
        "ConditionType": [FieldConditionType(convert_int(excel_instance.ConditionType(j), password)).name for j in range(excel_instance.ConditionTypeLength())],
        "ConditionId": [convert_long(excel_instance.ConditionId(j), password) for j in range(excel_instance.ConditionIdLength())],
    }

def dump_FieldWorldMapZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Date": convert_int(excel_instance.Date(), password),
        "OpenConditionType": FieldConditionType(convert_int(excel_instance.OpenConditionType(), password)).name,
        "OpenConditionId": convert_long(excel_instance.OpenConditionId(), password),
        "CloseConditionType": FieldConditionType(convert_int(excel_instance.CloseConditionType(), password)).name,
        "CloseConditionId": convert_long(excel_instance.CloseConditionId(), password),
        "ResultFieldScene": convert_long(excel_instance.ResultFieldScene(), password),
        "FieldStageInteractionId": convert_long(excel_instance.FieldStageInteractionId(), password),
        "WorldMapButtonType": FieldWorldMapButtonType(convert_int(excel_instance.WorldMapButtonType(), password)).name,
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "NewTagDisplay": excel_instance.NewTagDisplay(),
    }

def dump_FixedStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StageEnterEchelon01FixedEchelonId": convert_long(excel_instance.StageEnterEchelon01FixedEchelonId(), password),
        "StageEnterEchelon01Starttile": convert_long(excel_instance.StageEnterEchelon01Starttile(), password),
        "StageEnterEchelon02FixedEchelonId": convert_long(excel_instance.StageEnterEchelon02FixedEchelonId(), password),
        "StageEnterEchelon02Starttile": convert_long(excel_instance.StageEnterEchelon02Starttile(), password),
        "StageEnterEchelon03FixedEchelonId": convert_long(excel_instance.StageEnterEchelon03FixedEchelonId(), password),
        "StageEnterEchelon03Starttile": convert_long(excel_instance.StageEnterEchelon03Starttile(), password),
        "StageEnterEchelon04FixedEchelonId": convert_long(excel_instance.StageEnterEchelon04FixedEchelonId(), password),
        "StageEnterEchelon04Starttile": convert_long(excel_instance.StageEnterEchelon04Starttile(), password),
    }

def dump_FloaterCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "FloaterOffsetPosX": convert_int(excel_instance.FloaterOffsetPosX(), password),
        "FloaterOffsetPosY": convert_int(excel_instance.FloaterOffsetPosY(), password),
        "FloaterRandomPosRangeX": convert_int(excel_instance.FloaterRandomPosRangeX(), password),
        "FloaterRandomPosRangeY": convert_int(excel_instance.FloaterRandomPosRangeY(), password),
    }

def dump_FurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "Category": FurnitureCategory(convert_int(excel_instance.Category(), password)).name,
        "SubCategory": FurnitureSubCategory(convert_int(excel_instance.SubCategory(), password)).name,
        "CheckFloorDecoration": excel_instance.CheckFloorDecoration(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StarGradeInit": convert_int(excel_instance.StarGradeInit(), password),
        "Tier": convert_long(excel_instance.Tier(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "SizeWidth": convert_int(excel_instance.SizeWidth(), password),
        "SizeHeight": convert_int(excel_instance.SizeHeight(), password),
        "OtherSize": convert_int(excel_instance.OtherSize(), password),
        "ExpandWidth": convert_int(excel_instance.ExpandWidth(), password),
        "Enable": excel_instance.Enable(),
        "ReverseRotation": excel_instance.ReverseRotation(),
        "Prefab": convert_string(excel_instance.Prefab(), password),
        "PrefabExpand": convert_string(excel_instance.PrefabExpand(), password),
        "SubPrefab": convert_string(excel_instance.SubPrefab(), password),
        "SubExpandPrefab": convert_string(excel_instance.SubExpandPrefab(), password),
        "CornerPrefab": convert_string(excel_instance.CornerPrefab(), password),
        "StackableMax": convert_long(excel_instance.StackableMax(), password),
        "RecipeCraftId": convert_long(excel_instance.RecipeCraftId(), password),
        "SetGroudpId": convert_long(excel_instance.SetGroudpId(), password),
        "ComfortBonus": convert_long(excel_instance.ComfortBonus(), password),
        "VisitOperationType": convert_long(excel_instance.VisitOperationType(), password),
        "VisitBonusOperationType": convert_long(excel_instance.VisitBonusOperationType(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
        "CraftQualityTier0": convert_long(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_long(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_long(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_long(excel_instance.ShiftingCraftQuality(), password),
        "FurnitureFunctionType": FurnitureFunctionType(convert_int(excel_instance.FurnitureFunctionType(), password)).name,
        "FurnitureFunctionParameter": [convert_long(excel_instance.FurnitureFunctionParameter(j), password) for j in range(excel_instance.FurnitureFunctionParameterLength())],
        "VideoId": convert_long(excel_instance.VideoId(), password),
        "EventCollectionId": convert_long(excel_instance.EventCollectionId(), password),
        "FurnitureBubbleOffsetX": convert_long(excel_instance.FurnitureBubbleOffsetX(), password),
        "FurnitureBubbleOffsetY": convert_long(excel_instance.FurnitureBubbleOffsetY(), password),
        "CafeCharacterStateReq": [convert_string(excel_instance.CafeCharacterStateReq(j), password) for j in range(excel_instance.CafeCharacterStateReqLength())],
        "CafeCharacterStateAdd": [convert_string(excel_instance.CafeCharacterStateAdd(j), password) for j in range(excel_instance.CafeCharacterStateAddLength())],
        "CafeCharacterStateMake": [convert_string(excel_instance.CafeCharacterStateMake(j), password) for j in range(excel_instance.CafeCharacterStateMakeLength())],
        "CafeCharacterStateOnly": [convert_string(excel_instance.CafeCharacterStateOnly(j), password) for j in range(excel_instance.CafeCharacterStateOnlyLength())],
    }

def dump_FurnitureGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "GroupNameLocalize": convert_uint(excel_instance.GroupNameLocalize(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "RequiredFurnitureCount": [convert_int(excel_instance.RequiredFurnitureCount(j), password) for j in range(excel_instance.RequiredFurnitureCountLength())],
        "ComfortBonus": [convert_long(excel_instance.ComfortBonus(j), password) for j in range(excel_instance.ComfortBonusLength())],
    }

def dump_FurnitureTemplateElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_long(excel_instance.FurnitureTemplateId(), password),
        "FurnitureId": convert_long(excel_instance.FurnitureId(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.Location(), password)).name,
        "PositionX": convert_float(excel_instance.PositionX(), password),
        "PositionY": convert_float(excel_instance.PositionY(), password),
        "Rotation": convert_float(excel_instance.Rotation(), password),
        "Order": convert_long(excel_instance.Order(), password),
    }

def dump_FurnitureTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_long(excel_instance.FurnitureTemplateId(), password),
        "FunitureTemplateTitle": convert_uint(excel_instance.FunitureTemplateTitle(), password),
        "ThumbnailImagePath": convert_string(excel_instance.ThumbnailImagePath(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_GachaCraftNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "Tier": convert_long(excel_instance.Tier(), password),
        "QuickCraftNodeDisplayOrder": convert_int(excel_instance.QuickCraftNodeDisplayOrder(), password),
        "NodeQuality": convert_long(excel_instance.NodeQuality(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "LocalizeKey": convert_uint(excel_instance.LocalizeKey(), password),
        "Property": convert_long(excel_instance.Property(), password),
    }

def dump_GachaCraftNodeGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeId": convert_long(excel_instance.NodeId(), password),
        "GachaGroupId": convert_long(excel_instance.GachaGroupId(), password),
        "ProbWeight": convert_long(excel_instance.ProbWeight(), password),
    }

def dump_GachaCraftOpenTagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeTier": CraftNodeTier(convert_int(excel_instance.NodeTier(), password)).name,
        "Tag": [Tag(convert_int(excel_instance.Tag(j), password)).name for j in range(excel_instance.TagLength())],
    }

def dump_GroundGridFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "StartX": convert_float(excel_instance.StartX(), password),
        "StartY": convert_float(excel_instance.StartY(), password),
        "Gap": convert_float(excel_instance.Gap(), password),
        "Nodes": [dump_GroundNodeFlat(excel_instance.Nodes(j), password) for j in range(excel_instance.NodesLength())],
        "Version": convert_string(excel_instance.Version(), password),
    }

def dump_GroundNodeFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "IsCanNotUseSkill": excel_instance.IsCanNotUseSkill(),
        "Position": dump_GroundVector3(excel_instance.Position(), password),
        "NodeType": GroundNodeType(convert_int(excel_instance.NodeType(), password)).name,
        "OriginalNodeType": GroundNodeType(convert_int(excel_instance.OriginalNodeType(), password)).name,
    }

def dump_GroundNodeLayerFlat(excel_instance, password: bytes = b"") -> dict:
    return {
            }

def dump_HpBarAbbreviationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MonsterLv": convert_int(excel_instance.MonsterLv(), password),
        "StandardHpBar": convert_int(excel_instance.StandardHpBar(), password),
        "RaidBossHpBar": convert_int(excel_instance.RaidBossHpBar(), password),
    }

def dump_InformationStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StageId": convert_long(excel_instance.StageId(), password),
        "PageName": convert_string(excel_instance.PageName(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
    }

def dump_KnockBackExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_long(excel_instance.Index(), password),
        "Dist": convert_float(excel_instance.Dist(), password),
        "Speed": convert_float(excel_instance.Speed(), password),
    }

def dump_LimitedStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "OpenDate": convert_long(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_long(excel_instance.OpenEventPoint(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_long(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_long(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_long(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_long(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "StageRewardId": convert_long(excel_instance.StageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_string(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundID": convert_long(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "InstantClear": excel_instance.InstantClear(),
        "BuffContentId": convert_long(excel_instance.BuffContentId(), password),
        "ChallengeDisplay": excel_instance.ChallengeDisplay(),
    }

def dump_LimitedStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_LimitedStageSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "TypeACount": convert_long(excel_instance.TypeACount(), password),
        "TypeBCount": convert_long(excel_instance.TypeBCount(), password),
        "TypeCCount": convert_long(excel_instance.TypeCCount(), password),
    }

def dump_LocalizeCharProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "StatusMessageKr": convert_string(excel_instance.StatusMessageKr(), password),
        "StatusMessageJp": convert_string(excel_instance.StatusMessageJp(), password),
        "FullNameKr": convert_string(excel_instance.FullNameKr(), password),
        "FullNameJp": convert_string(excel_instance.FullNameJp(), password),
        "FamilyNameKr": convert_string(excel_instance.FamilyNameKr(), password),
        "FamilyNameRubyKr": convert_string(excel_instance.FamilyNameRubyKr(), password),
        "PersonalNameKr": convert_string(excel_instance.PersonalNameKr(), password),
        "PersonalNameRubyKr": convert_string(excel_instance.PersonalNameRubyKr(), password),
        "FamilyNameJp": convert_string(excel_instance.FamilyNameJp(), password),
        "FamilyNameRubyJp": convert_string(excel_instance.FamilyNameRubyJp(), password),
        "PersonalNameJp": convert_string(excel_instance.PersonalNameJp(), password),
        "PersonalNameRubyJp": convert_string(excel_instance.PersonalNameRubyJp(), password),
        "SchoolYearKr": convert_string(excel_instance.SchoolYearKr(), password),
        "SchoolYearJp": convert_string(excel_instance.SchoolYearJp(), password),
        "CharacterAgeKr": convert_string(excel_instance.CharacterAgeKr(), password),
        "CharacterAgeJp": convert_string(excel_instance.CharacterAgeJp(), password),
        "BirthDay": convert_string(excel_instance.BirthDay(), password),
        "BirthdayKr": convert_string(excel_instance.BirthdayKr(), password),
        "BirthdayJp": convert_string(excel_instance.BirthdayJp(), password),
        "CharHeightKr": convert_string(excel_instance.CharHeightKr(), password),
        "CharHeightJp": convert_string(excel_instance.CharHeightJp(), password),
        "DesignerNameKr": convert_string(excel_instance.DesignerNameKr(), password),
        "DesignerNameJp": convert_string(excel_instance.DesignerNameJp(), password),
        "IllustratorNameKr": convert_string(excel_instance.IllustratorNameKr(), password),
        "IllustratorNameJp": convert_string(excel_instance.IllustratorNameJp(), password),
        "CharacterVoiceKr": convert_string(excel_instance.CharacterVoiceKr(), password),
        "CharacterVoiceJp": convert_string(excel_instance.CharacterVoiceJp(), password),
        "HobbyKr": convert_string(excel_instance.HobbyKr(), password),
        "HobbyJp": convert_string(excel_instance.HobbyJp(), password),
        "WeaponNameKr": convert_string(excel_instance.WeaponNameKr(), password),
        "WeaponDescKr": convert_string(excel_instance.WeaponDescKr(), password),
        "WeaponNameJp": convert_string(excel_instance.WeaponNameJp(), password),
        "WeaponDescJp": convert_string(excel_instance.WeaponDescJp(), password),
        "ProfileIntroductionKr": convert_string(excel_instance.ProfileIntroductionKr(), password),
        "ProfileIntroductionJp": convert_string(excel_instance.ProfileIntroductionJp(), password),
        "CharacterSSRNewKr": convert_string(excel_instance.CharacterSSRNewKr(), password),
        "CharacterSSRNewJp": convert_string(excel_instance.CharacterSSRNewJp(), password),
    }

def dump_LocalizeFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LogicEffectCommonVisualExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringID(), password),
        "IconSpriteName": convert_string(excel_instance.IconSpriteName(), password),
        "IconDispelColor": [convert_float(excel_instance.IconDispelColor(j), password) for j in range(excel_instance.IconDispelColorLength())],
        "ParticleEnterPath": convert_string(excel_instance.ParticleEnterPath(), password),
        "ParticleEnterSocket": EffectBone(convert_int(excel_instance.ParticleEnterSocket(), password)).name,
        "ParticleLoopPath": convert_string(excel_instance.ParticleLoopPath(), password),
        "ParticleLoopSocket": EffectBone(convert_int(excel_instance.ParticleLoopSocket(), password)).name,
        "ParticleEndPath": convert_string(excel_instance.ParticleEndPath(), password),
        "ParticleEndSocket": EffectBone(convert_int(excel_instance.ParticleEndSocket(), password)).name,
        "ParticleApplyPath": convert_string(excel_instance.ParticleApplyPath(), password),
        "ParticleApplySocket": EffectBone(convert_int(excel_instance.ParticleApplySocket(), password)).name,
        "ParticleRemovedPath": convert_string(excel_instance.ParticleRemovedPath(), password),
        "ParticleRemovedSocket": EffectBone(convert_int(excel_instance.ParticleRemovedSocket(), password)).name,
    }

def dump_MiniGameAudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHash(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefix(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHash(), password),
        "StateName": convert_string(excel_instance.StateName(), password),
        "IgnoreInterruptDelay": excel_instance.IgnoreInterruptDelay(),
        "IgnoreInterruptPlay": excel_instance.IgnoreInterruptPlay(),
        "Volume": convert_float(excel_instance.Volume(), password),
        "Delay": convert_float(excel_instance.Delay(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriority(), password),
        "AudioClipPath": [convert_string(excel_instance.AudioClipPath(j), password) for j in range(excel_instance.AudioClipPathLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_MiniGameMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "GroupName": convert_string(excel_instance.GroupName(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": excel_instance.ViewFlag(),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_long(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_long(excel_instance.AccountLevel(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "IsCompleteExtensionTime": excel_instance.IsCompleteExtensionTime(),
        "CompleteConditionCount": convert_long(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_long(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTag(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "CompleteConditionMissionId": [convert_long(excel_instance.CompleteConditionMissionId(j), password) for j in range(excel_instance.CompleteConditionMissionIdLength())],
        "CompleteConditionMissionCount": convert_long(excel_instance.CompleteConditionMissionCount(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelType(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_long(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
        "ConditionRewardParcelType": [ParcelType(convert_int(excel_instance.ConditionRewardParcelType(j), password)).name for j in range(excel_instance.ConditionRewardParcelTypeLength())],
        "ConditionRewardParcelId": [convert_long(excel_instance.ConditionRewardParcelId(j), password) for j in range(excel_instance.ConditionRewardParcelIdLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmount(j), password) for j in range(excel_instance.ConditionRewardAmountLength())],
    }

def dump_MiniGamePlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_MiniGameRhythmBgmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RhythmBgmId": convert_long(excel_instance.RhythmBgmId(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "StageSelectImagePath": convert_string(excel_instance.StageSelectImagePath(), password),
        "Bpm": convert_long(excel_instance.Bpm(), password),
        "Bgm": convert_long(excel_instance.Bgm(), password),
        "BgmNameText": convert_string(excel_instance.BgmNameText(), password),
        "BgmArtistText": convert_string(excel_instance.BgmArtistText(), password),
        "HasLyricist": excel_instance.HasLyricist(),
        "BgmComposerText": convert_string(excel_instance.BgmComposerText(), password),
        "BgmLength": convert_int(excel_instance.BgmLength(), password),
    }

def dump_MiniGameRhythmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "RhythmBgmId": convert_long(excel_instance.RhythmBgmId(), password),
        "PresetName": convert_string(excel_instance.PresetName(), password),
        "StageDifficulty": Difficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "IsSpecial": excel_instance.IsSpecial(),
        "OpenStageScoreAmount": convert_long(excel_instance.OpenStageScoreAmount(), password),
        "MaxHp": convert_long(excel_instance.MaxHp(), password),
        "MissDamage": convert_long(excel_instance.MissDamage(), password),
        "CriticalHPRestoreValue": convert_long(excel_instance.CriticalHPRestoreValue(), password),
        "MaxScore": convert_long(excel_instance.MaxScore(), password),
        "FeverScoreRate": convert_long(excel_instance.FeverScoreRate(), password),
        "NoteScoreRate": convert_long(excel_instance.NoteScoreRate(), password),
        "ComboScoreRate": convert_long(excel_instance.ComboScoreRate(), password),
        "AttackScoreRate": convert_long(excel_instance.AttackScoreRate(), password),
        "FeverCriticalRate": convert_float(excel_instance.FeverCriticalRate(), password),
        "FeverAttackRate": convert_float(excel_instance.FeverAttackRate(), password),
        "MaxHpScore": convert_long(excel_instance.MaxHpScore(), password),
        "RhythmFileName": convert_string(excel_instance.RhythmFileName(), password),
        "ArtLevelSceneName": convert_string(excel_instance.ArtLevelSceneName(), password),
        "ComboImagePath": convert_string(excel_instance.ComboImagePath(), password),
    }

def dump_MinigameRoadExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [RoadPuzzleMapTileType(convert_int(excel_instance.None_(j), password)).name for j in range(excel_instance.None_Length())],
    }

def dump_MiniGameShootingCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "BodyRadius": convert_float(excel_instance.BodyRadius(), password),
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "NormalAttackSkillData": convert_string(excel_instance.NormalAttackSkillData(), password),
        "PublicSkillData": [convert_string(excel_instance.PublicSkillData(j), password) for j in range(excel_instance.PublicSkillDataLength())],
        "DeathSkillData": convert_string(excel_instance.DeathSkillData(), password),
        "MaxHP": convert_long(excel_instance.MaxHP(), password),
        "AttackPower": convert_long(excel_instance.AttackPower(), password),
        "DefensePower": convert_long(excel_instance.DefensePower(), password),
        "CriticalRate": convert_long(excel_instance.CriticalRate(), password),
        "CriticalDamageRate": convert_long(excel_instance.CriticalDamageRate(), password),
        "AttackRange": convert_long(excel_instance.AttackRange(), password),
        "MoveSpeed": convert_long(excel_instance.MoveSpeed(), password),
        "ShotTime": convert_long(excel_instance.ShotTime(), password),
        "IsBoss": excel_instance.IsBoss(),
        "Scale": convert_float(excel_instance.Scale(), password),
        "IgnoreObstacleCheck": excel_instance.IgnoreObstacleCheck(),
        "CharacterVoiceGroupId": convert_long(excel_instance.CharacterVoiceGroupId(), password),
    }

def dump_MiniGameShootingGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "GeasType": Geas(convert_int(excel_instance.GeasType(), password)).name,
        "Icon": convert_string(excel_instance.Icon(), password),
        "Probability": convert_long(excel_instance.Probability(), password),
        "MaxOverlapCount": convert_int(excel_instance.MaxOverlapCount(), password),
        "GeasData": convert_string(excel_instance.GeasData(), password),
        "NeedGeasId": convert_long(excel_instance.NeedGeasId(), password),
        "HideInPausePopup": excel_instance.HideInPausePopup(),
    }

def dump_MiniGameShootingStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "BgmId": [convert_long(excel_instance.BgmId(j), password) for j in range(excel_instance.BgmIdLength())],
        "CostGoodsId": convert_long(excel_instance.CostGoodsId(), password),
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "DesignLevel": convert_string(excel_instance.DesignLevel(), password),
        "ArtLevel": convert_string(excel_instance.ArtLevel(), password),
        "StartBattleDuration": convert_long(excel_instance.StartBattleDuration(), password),
        "DefaultBattleDuration": convert_long(excel_instance.DefaultBattleDuration(), password),
        "DefaultLogicEffect": convert_string(excel_instance.DefaultLogicEffect(), password),
        "CameraSizeRate": convert_float(excel_instance.CameraSizeRate(), password),
        "EventContentStageRewardId": convert_long(excel_instance.EventContentStageRewardId(), password),
    }

def dump_MiniGameShootingStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "ClearSection": convert_long(excel_instance.ClearSection(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameTBGDiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "DiceGroup": convert_int(excel_instance.DiceGroup(), password),
        "DiceResult": convert_int(excel_instance.DiceResult(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbModifyCondition": [TBGProbModifyCondition(convert_int(excel_instance.ProbModifyCondition(j), password)).name for j in range(excel_instance.ProbModifyConditionLength())],
        "ProbModifyValue": [convert_int(excel_instance.ProbModifyValue(j), password) for j in range(excel_instance.ProbModifyValueLength())],
        "ProbModifyLimit": [convert_int(excel_instance.ProbModifyLimit(j), password) for j in range(excel_instance.ProbModifyLimitLength())],
    }

def dump_MinigameTBGEncounterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "AllThema": excel_instance.AllThema(),
        "ThemaIndex": convert_int(excel_instance.ThemaIndex(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaType(), password)).name,
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectType(), password)).name,
        "EnemyImagePath": convert_string(excel_instance.EnemyImagePath(), password),
        "EnemyPrefabName": convert_string(excel_instance.EnemyPrefabName(), password),
        "EnemyNameLocalize": convert_string(excel_instance.EnemyNameLocalize(), password),
        "OptionGroupId": convert_long(excel_instance.OptionGroupId(), password),
        "RewardHide": excel_instance.RewardHide(),
        "EncounterTitleLocalize": convert_string(excel_instance.EncounterTitleLocalize(), password),
        "StoryImagePath": convert_string(excel_instance.StoryImagePath(), password),
        "BeforeStoryLocalize": convert_string(excel_instance.BeforeStoryLocalize(), password),
        "BeforeStoryOption1Localize": convert_string(excel_instance.BeforeStoryOption1Localize(), password),
        "BeforeStoryOption2Localize": convert_string(excel_instance.BeforeStoryOption2Localize(), password),
        "BeforeStoryOption3Localize": convert_string(excel_instance.BeforeStoryOption3Localize(), password),
        "AllyAttackLocalize": convert_string(excel_instance.AllyAttackLocalize(), password),
        "EnemyAttackLocalize": convert_string(excel_instance.EnemyAttackLocalize(), password),
        "AttackDefenceLocalize": convert_string(excel_instance.AttackDefenceLocalize(), password),
        "ClearStoryLocalize": convert_string(excel_instance.ClearStoryLocalize(), password),
        "DefeatStoryLocalize": convert_string(excel_instance.DefeatStoryLocalize(), password),
        "RunawayStoryLocalize": convert_string(excel_instance.RunawayStoryLocalize(), password),
    }

def dump_MinigameTBGEncounterOptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OptionGroupId": convert_long(excel_instance.OptionGroupId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "SlotIndex": convert_int(excel_instance.SlotIndex(), password),
        "OptionTitleLocalize": convert_string(excel_instance.OptionTitleLocalize(), password),
        "OptionSuccessLocalize": convert_string(excel_instance.OptionSuccessLocalize(), password),
        "OptionSuccessRewardGroupId": convert_long(excel_instance.OptionSuccessRewardGroupId(), password),
        "OptionSuccessOrHigherDiceCount": convert_int(excel_instance.OptionSuccessOrHigherDiceCount(), password),
        "OptionGreatSuccessOrHigherDiceCount": convert_int(excel_instance.OptionGreatSuccessOrHigherDiceCount(), password),
        "OptionFailLocalize": convert_string(excel_instance.OptionFailLocalize(), password),
        "OptionFailLessDiceCount": convert_int(excel_instance.OptionFailLessDiceCount(), password),
        "RunawayOrHigherDiceCount": convert_int(excel_instance.RunawayOrHigherDiceCount(), password),
        "RewardHide": excel_instance.RewardHide(),
    }

def dump_MinigameTBGEncounterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "TBGOptionSuccessType": TBGOptionSuccessType(convert_int(excel_instance.TBGOptionSuccessType(), password)).name,
        "Paremeter": convert_long(excel_instance.Paremeter(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_long(excel_instance.ParcelId(), password),
        "Amount": convert_long(excel_instance.Amount(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
    }

def dump_MinigameTBGItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "ItemType": TBGItemType(convert_int(excel_instance.ItemType(), password)).name,
        "TBGItemEffectType": TBGItemEffectType(convert_int(excel_instance.TBGItemEffectType(), password)).name,
        "ItemParameter": convert_int(excel_instance.ItemParameter(), password),
        "LocalizeETCId": convert_string(excel_instance.LocalizeETCId(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "BuffIcon": convert_string(excel_instance.BuffIcon(), password),
        "EncounterCount": convert_int(excel_instance.EncounterCount(), password),
        "DiceEffectAniClip": convert_string(excel_instance.DiceEffectAniClip(), password),
        "BuffIconHUDVisible": excel_instance.BuffIconHUDVisible(),
    }

def dump_MinigameTBGObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Key": convert_string(excel_instance.Key(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectType(), password)).name,
        "ObjectCostType": ParcelType(convert_int(excel_instance.ObjectCostType(), password)).name,
        "ObjectCostId": convert_long(excel_instance.ObjectCostId(), password),
        "ObjectCostAmount": convert_int(excel_instance.ObjectCostAmount(), password),
        "Disposable": excel_instance.Disposable(),
        "ReEncounterCost": excel_instance.ReEncounterCost(),
    }

def dump_MinigameTBGSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ItemSlot": convert_int(excel_instance.ItemSlot(), password),
        "DefaultEchelonHp": convert_int(excel_instance.DefaultEchelonHp(), password),
        "DefaultItemDiceId": convert_long(excel_instance.DefaultItemDiceId(), password),
        "EchelonSlot1CharacterId": convert_long(excel_instance.EchelonSlot1CharacterId(), password),
        "EchelonSlot2CharacterId": convert_long(excel_instance.EchelonSlot2CharacterId(), password),
        "EchelonSlot3CharacterId": convert_long(excel_instance.EchelonSlot3CharacterId(), password),
        "EchelonSlot4CharacterId": convert_long(excel_instance.EchelonSlot4CharacterId(), password),
        "EchelonSlot1Portrait": convert_string(excel_instance.EchelonSlot1Portrait(), password),
        "EchelonSlot2Portrait": convert_string(excel_instance.EchelonSlot2Portrait(), password),
        "EchelonSlot3Portrait": convert_string(excel_instance.EchelonSlot3Portrait(), password),
        "EchelonSlot4Portrait": convert_string(excel_instance.EchelonSlot4Portrait(), password),
        "EventUseCostType": ParcelType(convert_int(excel_instance.EventUseCostType(), password)).name,
        "EventUseCostId": convert_long(excel_instance.EventUseCostId(), password),
        "EchelonRevivalCostType": ParcelType(convert_int(excel_instance.EchelonRevivalCostType(), password)).name,
        "EchelonRevivalCostId": convert_long(excel_instance.EchelonRevivalCostId(), password),
        "EchelonRevivalCostAmount": convert_int(excel_instance.EchelonRevivalCostAmount(), password),
        "EnemyBossHP": convert_int(excel_instance.EnemyBossHP(), password),
        "EnemyMinionHP": convert_int(excel_instance.EnemyMinionHP(), password),
        "AttackDamage": convert_int(excel_instance.AttackDamage(), password),
        "CriticalAttackDamage": convert_int(excel_instance.CriticalAttackDamage(), password),
        "RoundItemSelectLimit": convert_int(excel_instance.RoundItemSelectLimit(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRound(), password),
        "MaxHp": convert_int(excel_instance.MaxHp(), password),
        "MapImagePath": convert_string(excel_instance.MapImagePath(), password),
        "MapNameLocalize": convert_string(excel_instance.MapNameLocalize(), password),
        "StartThemaIndex": convert_int(excel_instance.StartThemaIndex(), password),
        "LoopThemaIndex": convert_int(excel_instance.LoopThemaIndex(), password),
        "MaxDicePlus": convert_int(excel_instance.MaxDicePlus(), password),
    }

def dump_MinigameTBGThemaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "ThemaIndex": convert_int(excel_instance.ThemaIndex(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaType(), password)).name,
        "ThemaMap": convert_string(excel_instance.ThemaMap(), password),
        "ThemaMapBG": convert_string(excel_instance.ThemaMapBG(), password),
        "PortalCondition": [TBGPortalCondition(convert_int(excel_instance.PortalCondition(j), password)).name for j in range(excel_instance.PortalConditionLength())],
        "PortalConditionParameter": [convert_string(excel_instance.PortalConditionParameter(j), password) for j in range(excel_instance.PortalConditionParameterLength())],
        "ThemaNameLocalize": convert_string(excel_instance.ThemaNameLocalize(), password),
        "ThemaLoadingImage": convert_string(excel_instance.ThemaLoadingImage(), password),
        "ThemaPlayerPrefab": convert_string(excel_instance.ThemaPlayerPrefab(), password),
        "ThemaLeaderId": convert_long(excel_instance.ThemaLeaderId(), password),
        "ThemaGoalLocalize": convert_string(excel_instance.ThemaGoalLocalize(), password),
        "InstantClearCostAmount": convert_long(excel_instance.InstantClearCostAmount(), password),
        "IsTutorial": excel_instance.IsTutorial(),
    }

def dump_MiniGameTBGThemaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ThemaRound": convert_int(excel_instance.ThemaRound(), password),
        "ThemaUniqueId": convert_int(excel_instance.ThemaUniqueId(), password),
        "IsLoop": excel_instance.IsLoop(),
        "MiniGameTBGThemaRewardType": MiniGameTBGThemaRewardType(convert_int(excel_instance.MiniGameTBGThemaRewardType(), password)).name,
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameTBGVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "VoiceCondition": TBGVoiceCondition(convert_int(excel_instance.VoiceCondition(), password)).name,
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_NormalSkillTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_long(excel_instance.Index(), password),
        "FirstCoolTime": convert_float(excel_instance.FirstCoolTime(), password),
        "CoolTime": convert_float(excel_instance.CoolTime(), password),
        "MultiAni": excel_instance.MultiAni(),
    }

def dump_ObstacleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_long(excel_instance.Index(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "JumpAble": excel_instance.JumpAble(),
        "SubOffset": [convert_float(excel_instance.SubOffset(j), password) for j in range(excel_instance.SubOffsetLength())],
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
        "Hp": convert_long(excel_instance.Hp(), password),
        "MaxHp": convert_long(excel_instance.MaxHp(), password),
        "BlockRate": convert_int(excel_instance.BlockRate(), password),
        "EvasionRate": convert_int(excel_instance.EvasionRate(), password),
        "DestroyType": ObstacleDestroyType(convert_int(excel_instance.DestroyType(), password)).name,
        "Point1Offeset": [convert_float(excel_instance.Point1Offeset(j), password) for j in range(excel_instance.Point1OffesetLength())],
        "EnemyPoint1Osset": [convert_float(excel_instance.EnemyPoint1Osset(j), password) for j in range(excel_instance.EnemyPoint1OssetLength())],
        "Point2Offeset": [convert_float(excel_instance.Point2Offeset(j), password) for j in range(excel_instance.Point2OffesetLength())],
        "EnemyPoint2Osset": [convert_float(excel_instance.EnemyPoint2Osset(j), password) for j in range(excel_instance.EnemyPoint2OssetLength())],
        "SubObstacleID": [convert_long(excel_instance.SubObstacleID(j), password) for j in range(excel_instance.SubObstacleIDLength())],
    }

def dump_ObstacleFireLineCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MyObstacleFireLineCheck": excel_instance.MyObstacleFireLineCheck(),
        "AllyObstacleFireLineCheck": excel_instance.AllyObstacleFireLineCheck(),
        "EnemyObstacleFireLineCheck": excel_instance.EnemyObstacleFireLineCheck(),
        "EmptyObstacleFireLineCheck": excel_instance.EmptyObstacleFireLineCheck(),
    }

def dump_PersonalityExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
    }

def dump_PropVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_PropMotion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Positions": [dump_PropVector3(excel_instance.Positions(j), password) for j in range(excel_instance.PositionsLength())],
        "Rotations": [dump_PropVector3(excel_instance.Rotations(j), password) for j in range(excel_instance.RotationsLength())],
    }

def dump_PropRootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "RootMotions": [dump_PropMotion(excel_instance.RootMotions(j), password) for j in range(excel_instance.RootMotionsLength())],
    }

def dump_ProtocolSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Protocol": convert_string(excel_instance.Protocol(), password),
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContent(), password)).name,
        "Currency": excel_instance.Currency(),
        "Inventory": excel_instance.Inventory(),
        "Mail": excel_instance.Mail(),
    }

def dump_RaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_long(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "RankStart": convert_long(excel_instance.RankStart(), password),
        "RankEnd": convert_long(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_long(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_long(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_long(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueName(j), password) for j in range(excel_instance.RewardParcelUniqueNameLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_RaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_long(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "OpenRaidBossGroup": [convert_string(excel_instance.OpenRaidBossGroup(j), password) for j in range(excel_instance.OpenRaidBossGroupLength())],
        "RankingRewardGroupId": convert_long(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGauge": [convert_long(excel_instance.StackedSeasonRewardGauge(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeLength())],
        "SeasonRewardId": [convert_long(excel_instance.SeasonRewardId(j), password) for j in range(excel_instance.SeasonRewardIdLength())],
    }

def dump_RaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "UseBossIndex": excel_instance.UseBossIndex(),
        "UseBossAIPhaseSync": excel_instance.UseBossAIPhaseSync(),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroup(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_long(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_long(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "DifficultyOpenCondition": excel_instance.DifficultyOpenCondition(),
        "MaxPlayerCount": convert_long(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "GroundDevName": convert_string(excel_instance.GroundDevName(), password),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironment(), password)).name,
        "DefaultClearScore": convert_long(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_long(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_long(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_long(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_long(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_long(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_long(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_long(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": excel_instance.ShowSkillCard(),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_RaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": excel_instance.IsClearStageRewardHideInfo(),
        "ClearStageRewardProb": convert_long(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_long(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_long(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_RaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_long(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelType": [ParcelType(convert_int(excel_instance.SeasonRewardParcelType(j), password)).name for j in range(excel_instance.SeasonRewardParcelTypeLength())],
        "SeasonRewardParcelUniqueId": [convert_long(excel_instance.SeasonRewardParcelUniqueId(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdLength())],
        "SeasonRewardParcelUniqueName": [convert_string(excel_instance.SeasonRewardParcelUniqueName(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueNameLength())],
        "SeasonRewardAmount": [convert_long(excel_instance.SeasonRewardAmount(j), password) for j in range(excel_instance.SeasonRewardAmountLength())],
    }

def dump_RecipeCraftExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "RecipeIngredientId": convert_long(excel_instance.RecipeIngredientId(), password),
        "RecipeIngredientDevName": convert_string(excel_instance.RecipeIngredientDevName(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelDevName": [convert_string(excel_instance.ParcelDevName(j), password) for j in range(excel_instance.ParcelDevNameLength())],
        "ResultAmountMin": [convert_long(excel_instance.ResultAmountMin(j), password) for j in range(excel_instance.ResultAmountMinLength())],
        "ResultAmountMax": [convert_long(excel_instance.ResultAmountMax(j), password) for j in range(excel_instance.ResultAmountMaxLength())],
    }

def dump_RecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "RecipeIngredientId": convert_long(excel_instance.RecipeIngredientId(), password),
        "RecipeSelectionGroupId": convert_long(excel_instance.RecipeSelectionGroupId(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ResultAmountMin": [convert_long(excel_instance.ResultAmountMin(j), password) for j in range(excel_instance.ResultAmountMinLength())],
        "ResultAmountMax": [convert_long(excel_instance.ResultAmountMax(j), password) for j in range(excel_instance.ResultAmountMaxLength())],
    }

def dump_RecipeIngredientExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelType(j), password)).name for j in range(excel_instance.CostParcelTypeLength())],
        "CostId": [convert_long(excel_instance.CostId(j), password) for j in range(excel_instance.CostIdLength())],
        "CostAmount": [convert_long(excel_instance.CostAmount(j), password) for j in range(excel_instance.CostAmountLength())],
        "IngredientParcelType": [ParcelType(convert_int(excel_instance.IngredientParcelType(j), password)).name for j in range(excel_instance.IngredientParcelTypeLength())],
        "IngredientId": [convert_long(excel_instance.IngredientId(j), password) for j in range(excel_instance.IngredientIdLength())],
        "IngredientAmount": [convert_long(excel_instance.IngredientAmount(j), password) for j in range(excel_instance.IngredientAmountLength())],
        "CostTimeInSecond": convert_long(excel_instance.CostTimeInSecond(), password),
    }

def dump_RecipeSelectionAutoUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "TargetItemId": convert_long(excel_instance.TargetItemId(), password),
        "Priority": [convert_long(excel_instance.Priority(j), password) for j in range(excel_instance.PriorityLength())],
    }

def dump_RecipeSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RecipeSelectionGroupId": convert_long(excel_instance.RecipeSelectionGroupId(), password),
        "RecipeSelectionGroupComponentId": convert_long(excel_instance.RecipeSelectionGroupComponentId(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_long(excel_instance.ParcelId(), password),
        "ResultAmountMin": convert_long(excel_instance.ResultAmountMin(), password),
        "ResultAmountMax": convert_long(excel_instance.ResultAmountMax(), password),
    }

def dump_Position(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_Motion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Positions": [dump_Position(excel_instance.Positions(j), password) for j in range(excel_instance.PositionsLength())],
    }

def dump_MoveEnd(excel_instance, password: bytes = b"") -> dict:
    return {
        "Normal": dump_Motion(excel_instance.Normal(), password),
        "Stand": dump_Motion(excel_instance.Stand(), password),
        "Kneel": dump_Motion(excel_instance.Kneel(), password),
    }

def dump_Form(excel_instance, password: bytes = b"") -> dict:
    return {
        "MoveEnd": dump_MoveEnd(excel_instance.MoveEnd(), password),
        "PublicSkill": dump_Motion(excel_instance.PublicSkill(), password),
    }

def dump_RootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "Forms": [dump_Form(excel_instance.Forms(j), password) for j in range(excel_instance.FormsLength())],
        "ExSkills": [dump_Motion(excel_instance.ExSkills(j), password) for j in range(excel_instance.ExSkillsLength())],
        "MoveLeft": dump_Motion(excel_instance.MoveLeft(), password),
        "MoveRight": dump_Motion(excel_instance.MoveRight(), password),
    }

def dump_ScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [ScenarioBGType(convert_int(excel_instance.None_(j), password)).name for j in range(excel_instance.None_Length())],
        "Idle": [ScenarioCharacterAction(convert_int(excel_instance.Idle(j), password)).name for j in range(excel_instance.IdleLength())],
        "Cafe": DialogCategory(convert_int(excel_instance.Cafe(), password)).name,
        "Talk": DialogType(convert_int(excel_instance.Talk(), password)).name,
        "Open": StoryCondition(convert_int(excel_instance.Open(), password)).name,
        "EnterConver": EmojiEvent(convert_int(excel_instance.EnterConver(), password)).name,
        "Center": ScenarioZoomAnchors(convert_int(excel_instance.Center(), password)).name,
        "Instant": ScenarioZoomType(convert_int(excel_instance.Instant(), password)).name,
        "Prologue": ScenarioContentType(convert_int(excel_instance.Prologue(), password)).name,
    }

def dump_ScenarioReplayExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_long(excel_instance.ModeId(), password),
        "VolumeId": convert_long(excel_instance.VolumeId(), password),
        "ReplayType": ScenarioModeReplayTypes(convert_int(excel_instance.ReplayType(), password)).name,
        "ChapterId": convert_long(excel_instance.ChapterId(), password),
        "EpisodeId": convert_long(excel_instance.EpisodeId(), password),
        "FrontScenarioGroupId": [convert_long(excel_instance.FrontScenarioGroupId(j), password) for j in range(excel_instance.FrontScenarioGroupIdLength())],
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "BackScenarioGroupId": [convert_long(excel_instance.BackScenarioGroupId(j), password) for j in range(excel_instance.BackScenarioGroupIdLength())],
    }

def dump_ScenarioScriptField1Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "SelectionGroup": convert_long(excel_instance.SelectionGroup(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "Sound": convert_string(excel_instance.Sound(), password),
        "Transition": convert_uint(excel_instance.Transition(), password),
        "BGName": convert_uint(excel_instance.BGName(), password),
        "BGEffect": convert_uint(excel_instance.BGEffect(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileName(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKr(), password),
        "TextJp": convert_string(excel_instance.TextJp(), password),
        "VoiceJp": convert_string(excel_instance.VoiceJp(), password),
    }

def dump_ShiftingCraftRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "NotificationId": convert_int(excel_instance.NotificationId(), password),
        "ResultParcel": ParcelType(convert_int(excel_instance.ResultParcel(), password)).name,
        "ResultId": convert_long(excel_instance.ResultId(), password),
        "ResultAmount": convert_long(excel_instance.ResultAmount(), password),
        "RequireItemId": convert_long(excel_instance.RequireItemId(), password),
        "RequireItemAmount": convert_long(excel_instance.RequireItemAmount(), password),
        "RequireGold": convert_long(excel_instance.RequireGold(), password),
        "IngredientTag": [Tag(convert_int(excel_instance.IngredientTag(j), password)).name for j in range(excel_instance.IngredientTagLength())],
        "IngredientExp": convert_long(excel_instance.IngredientExp(), password),
    }

def dump_SkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeSkillId": convert_uint(excel_instance.LocalizeSkillId(), password),
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "SkillDataKey": convert_string(excel_instance.SkillDataKey(), password),
        "VisualDataKey": convert_string(excel_instance.VisualDataKey(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "SkillCost": convert_int(excel_instance.SkillCost(), password),
        "ExtraSkillCost": convert_int(excel_instance.ExtraSkillCost(), password),
        "EnemySkillCost": convert_int(excel_instance.EnemySkillCost(), password),
        "ExtraEnemySkillCost": convert_int(excel_instance.ExtraEnemySkillCost(), password),
        "NPCSkillCost": convert_int(excel_instance.NPCSkillCost(), password),
        "ExtraNPCSkillCost": convert_int(excel_instance.ExtraNPCSkillCost(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "StartCoolTime": convert_int(excel_instance.StartCoolTime(), password),
        "CoolTime": convert_int(excel_instance.CoolTime(), password),
        "EnemyStartCoolTime": convert_int(excel_instance.EnemyStartCoolTime(), password),
        "EnemyCoolTime": convert_int(excel_instance.EnemyCoolTime(), password),
        "NPCStartCoolTime": convert_int(excel_instance.NPCStartCoolTime(), password),
        "NPCCoolTime": convert_int(excel_instance.NPCCoolTime(), password),
        "UseAtg": convert_int(excel_instance.UseAtg(), password),
        "RequireCharacterLevel": convert_int(excel_instance.RequireCharacterLevel(), password),
        "RequireLevelUpMaterial": convert_long(excel_instance.RequireLevelUpMaterial(), password),
        "IconName": convert_string(excel_instance.IconName(), password),
        "IsShowInfo": excel_instance.IsShowInfo(),
        "IsShowSpeechbubble": excel_instance.IsShowSpeechbubble(),
        "PublicSpeechDuration": convert_int(excel_instance.PublicSpeechDuration(), password),
        "AdditionalToolTipId": convert_long(excel_instance.AdditionalToolTipId(), password),
        "TextureSkillCardForFormConversion": convert_string(excel_instance.TextureSkillCardForFormConversion(), password),
        "SkillCardLabelPath": convert_string(excel_instance.SkillCardLabelPath(), password),
    }

def dump_SpecialLobbyIllustExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CharacterCostumeUniqueId": convert_long(excel_instance.CharacterCostumeUniqueId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "SlotTextureName": convert_string(excel_instance.SlotTextureName(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureName(), password),
    }

def dump_StrategyObjectBuffDefineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StrategyObjectBuffID": convert_long(excel_instance.StrategyObjectBuffID(), password),
        "StrategyObjectTurn": convert_int(excel_instance.StrategyObjectTurn(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_StringTestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "String": [convert_string(excel_instance.String(j), password) for j in range(excel_instance.StringLength())],
        "Sentence1": convert_string(excel_instance.Sentence1(), password),
        "Script": convert_string(excel_instance.Script(), password),
    }

def dump_SystemMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "ExpiredDay": convert_long(excel_instance.ExpiredDay(), password),
        "Sender": convert_string(excel_instance.Sender(), password),
        "Comment": convert_string(excel_instance.Comment(), password),
    }

def dump_TacticalSupportSystemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "SummonedTime": convert_long(excel_instance.SummonedTime(), password),
        "DefaultPersonalityId": convert_long(excel_instance.DefaultPersonalityId(), password),
        "CanTargeting": excel_instance.CanTargeting(),
        "CanCover": excel_instance.CanCover(),
        "ObstacleUniqueName": convert_string(excel_instance.ObstacleUniqueName(), password),
        "ObstacleCoverRange": convert_long(excel_instance.ObstacleCoverRange(), password),
        "SummonSkilllGroupId": convert_string(excel_instance.SummonSkilllGroupId(), password),
        "CrashObstacleOBBWidth": convert_long(excel_instance.CrashObstacleOBBWidth(), password),
        "CrashObstacleOBBHeight": convert_long(excel_instance.CrashObstacleOBBHeight(), password),
        "IsTSSBlockedNodeCheck": excel_instance.IsTSSBlockedNodeCheck(),
        "NumberOfUses": convert_int(excel_instance.NumberOfUses(), password),
        "InventoryOffsetX": convert_float(excel_instance.InventoryOffsetX(), password),
        "InventoryOffsetY": convert_float(excel_instance.InventoryOffsetY(), password),
        "InventoryOffsetZ": convert_float(excel_instance.InventoryOffsetZ(), password),
        "InteractionChar": convert_long(excel_instance.InteractionChar(), password),
        "CharacterInteractionStartDelay": convert_long(excel_instance.CharacterInteractionStartDelay(), password),
        "GetOnStartEffectPath": convert_string(excel_instance.GetOnStartEffectPath(), password),
        "GetOnEndEffectPath": convert_string(excel_instance.GetOnEndEffectPath(), password),
        "SummonerCharacterId": convert_long(excel_instance.SummonerCharacterId(), password),
        "InteractionFrame": convert_int(excel_instance.InteractionFrame(), password),
        "TSAInteractionAddDuration": convert_long(excel_instance.TSAInteractionAddDuration(), password),
        "InteractionStudentExSkillGroupId": convert_string(excel_instance.InteractionStudentExSkillGroupId(), password),
        "InteractionSkillCardTexture": convert_string(excel_instance.InteractionSkillCardTexture(), password),
        "InteractionSkillSpine": convert_string(excel_instance.InteractionSkillSpine(), password),
        "RetreatFrame": convert_int(excel_instance.RetreatFrame(), password),
        "DestroyFrame": convert_int(excel_instance.DestroyFrame(), password),
    }

def dump_TacticArenaSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_long(excel_instance.Order(), password),
        "Repeat": convert_long(excel_instance.Repeat(), password),
        "AttackerFrom": ArenaSimulatorServer(convert_int(excel_instance.AttackerFrom(), password)).name,
        "AttackerUserArenaGroup": convert_long(excel_instance.AttackerUserArenaGroup(), password),
        "AttackerUserArenaRank": convert_long(excel_instance.AttackerUserArenaRank(), password),
        "AttackerPresetGroupId": convert_long(excel_instance.AttackerPresetGroupId(), password),
        "AttackerStrikerNum": convert_long(excel_instance.AttackerStrikerNum(), password),
        "AttackerSpecialNum": convert_long(excel_instance.AttackerSpecialNum(), password),
        "DefenderFrom": ArenaSimulatorServer(convert_int(excel_instance.DefenderFrom(), password)).name,
        "DefenderUserArenaGroup": convert_long(excel_instance.DefenderUserArenaGroup(), password),
        "DefenderUserArenaRank": convert_long(excel_instance.DefenderUserArenaRank(), password),
        "DefenderPresetGroupId": convert_long(excel_instance.DefenderPresetGroupId(), password),
        "DefenderStrikerNum": convert_long(excel_instance.DefenderStrikerNum(), password),
        "DefenderSpecialNum": convert_long(excel_instance.DefenderSpecialNum(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
    }

def dump_TacticDamageSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.Order(), password),
        "Repeat": convert_int(excel_instance.Repeat(), password),
        "TestPreset": convert_long(excel_instance.TestPreset(), password),
        "TestBattleTime": convert_long(excel_instance.TestBattleTime(), password),
        "StrikerSquard": convert_long(excel_instance.StrikerSquard(), password),
        "SpecialSquard": convert_long(excel_instance.SpecialSquard(), password),
        "ReplaceCharacterCostRegen": excel_instance.ReplaceCharacterCostRegen(),
        "ReplaceCostRegenValue": convert_int(excel_instance.ReplaceCostRegenValue(), password),
        "UseAutoSkill": excel_instance.UseAutoSkill(),
        "OverrideStreetAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideStreetAdaptation(), password)).name,
        "OverrideOutdoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideOutdoorAdaptation(), password)).name,
        "OverrideIndoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideIndoorAdaptation(), password)).name,
        "ApplyOverrideAdaptation": excel_instance.ApplyOverrideAdaptation(),
        "OverrideFavorLevel": convert_int(excel_instance.OverrideFavorLevel(), password),
        "ApplyOverrideFavorLevel": excel_instance.ApplyOverrideFavorLevel(),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "FixedCharacter": [convert_long(excel_instance.FixedCharacter(j), password) for j in range(excel_instance.FixedCharacterLength())],
    }

def dump_TacticEntityEffectFilterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetEffectName": convert_string(excel_instance.TargetEffectName(), password),
        "ShowEffectToVehicle": excel_instance.ShowEffectToVehicle(),
        "ShowEffectToBoss": excel_instance.ShowEffectToBoss(),
    }

def dump_TacticSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
    }

def dump_TacticSkipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "HPResult": convert_long(excel_instance.HPResult(), password),
    }

def dump_TacticTimeAttackSimulatorConfigExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_long(excel_instance.Order(), password),
        "Repeat": convert_long(excel_instance.Repeat(), password),
        "PresetGroupId": convert_long(excel_instance.PresetGroupId(), password),
        "AttackStrikerNum": convert_long(excel_instance.AttackStrikerNum(), password),
        "AttackSpecialNum": convert_long(excel_instance.AttackSpecialNum(), password),
        "GeasId": convert_long(excel_instance.GeasId(), password),
    }

def dump_TagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Furniture": Tag(convert_int(excel_instance.Furniture(), password)).name,
        "None_": Club(convert_int(excel_instance.None_(), password)).name,
    }

def dump_TerrainAdaptationFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TerrainAdaptation": StageTopography(convert_int(excel_instance.TerrainAdaptation(), password)).name,
        "TerrainAdaptationStat": TerrainAdaptationStat(convert_int(excel_instance.TerrainAdaptationStat(), password)).name,
        "ShotFactor": convert_long(excel_instance.ShotFactor(), password),
        "BlockFactor": convert_long(excel_instance.BlockFactor(), password),
        "AccuracyFactor": convert_long(excel_instance.AccuracyFactor(), password),
        "DodgeFactor": convert_long(excel_instance.DodgeFactor(), password),
        "AttackPowerFactor": convert_long(excel_instance.AttackPowerFactor(), password),
    }

def dump_TranscendenceRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostCurrencyType": CurrencyTypes(convert_int(excel_instance.CostCurrencyType(), password)).name,
        "CostCurrencyAmount": convert_long(excel_instance.CostCurrencyAmount(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_TrophyCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "FurnitureId": [convert_long(excel_instance.FurnitureId(j), password) for j in range(excel_instance.FurnitureIdLength())],
    }

def dump_WeekDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_long(excel_instance.StageId(), password),
        "WeekDungeonType": WeekDungeonType(convert_int(excel_instance.WeekDungeonType(), password)).name,
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "StageEnterCostType": [ParcelType(convert_int(excel_instance.StageEnterCostType(j), password)).name for j in range(excel_instance.StageEnterCostTypeLength())],
        "StageEnterCostId": [convert_long(excel_instance.StageEnterCostId(j), password) for j in range(excel_instance.StageEnterCostIdLength())],
        "StageEnterCostAmount": [convert_int(excel_instance.StageEnterCostAmount(j), password) for j in range(excel_instance.StageEnterCostAmountLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_long(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_long(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_long(excel_instance.PlayTimeLimitInSeconds(), password),
        "BattleRewardExp": convert_long(excel_instance.BattleRewardExp(), password),
        "BattleRewardPlayerExp": convert_long(excel_instance.BattleRewardPlayerExp(), password),
        "GroupBuffID": [convert_long(excel_instance.GroupBuffID(j), password) for j in range(excel_instance.GroupBuffIDLength())],
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_WeekDungeonFindGiftRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageRewardId": convert_long(excel_instance.StageRewardId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
        "RewardParcelProbability": [convert_long(excel_instance.RewardParcelProbability(j), password) for j in range(excel_instance.RewardParcelProbabilityLength())],
        "DropItemModelPrefabPath": [convert_string(excel_instance.DropItemModelPrefabPath(j), password) for j in range(excel_instance.DropItemModelPrefabPathLength())],
    }

def dump_WeekDungeonGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDungeonBuffId": convert_long(excel_instance.WeekDungeonBuffId(), password),
        "School": School(convert_int(excel_instance.School(), password)).name,
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "FormationLocalizeEtcId": convert_uint(excel_instance.FormationLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_WeekDungeonOpenScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDay": WeekDay(convert_int(excel_instance.WeekDay(), password)).name,
        "Open": [WeekDungeonType(convert_int(excel_instance.Open(j), password)).name for j in range(excel_instance.OpenLength())],
    }

def dump_WeekDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "DungeonType": WeekDungeonType(convert_int(excel_instance.DungeonType(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_long(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_AccountLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Level": convert_long(excel_instance.Level(), password),
        "Exp": convert_long(excel_instance.Exp(), password),
        "NewbieExpRatio": convert_int(excel_instance.NewbieExpRatio(), password),
        "CloseInterval": convert_int(excel_instance.CloseInterval(), password),
        "APAutoChargeMax": convert_long(excel_instance.APAutoChargeMax(), password),
        "NeedReportEvent": excel_instance.NeedReportEvent(),
    }

def dump_AssistEchelonTypeConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Contents": EchelonType(convert_int(excel_instance.Contents(), password)).name,
        "ConvertTo": EchelonType(convert_int(excel_instance.ConvertTo(), password)).name,
    }

def dump_AttendanceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Type": AttendanceType(convert_int(excel_instance.Type(), password)).name,
        "CountdownPrefab": convert_string(excel_instance.CountdownPrefab(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevelLimit": convert_long(excel_instance.AccountLevelLimit(), password),
        "Title": convert_string(excel_instance.Title(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCode(), password),
        "CountRule": AttendanceCountRule(convert_int(excel_instance.CountRule(), password)).name,
        "CountReset": AttendanceResetType(convert_int(excel_instance.CountReset(), password)).name,
        "BookSize": convert_long(excel_instance.BookSize(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "ExpiryDate": convert_long(excel_instance.ExpiryDate(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "TitleImagePath": convert_string(excel_instance.TitleImagePath(), password),
        "DecorationImagePath": convert_string(excel_instance.DecorationImagePath(), password),
        "DecorationGarlandImagePath": convert_string(excel_instance.DecorationGarlandImagePath(), password),
    }

def dump_AttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttendanceId": convert_long(excel_instance.AttendanceId(), password),
        "Day": convert_long(excel_instance.Day(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_long(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_AudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHash(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefix(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHash(), password),
        "StateName": convert_string(excel_instance.StateName(), password),
        "IgnoreInterruptDelay": excel_instance.IgnoreInterruptDelay(),
        "IgnoreInterruptPlay": excel_instance.IgnoreInterruptPlay(),
        "Volume": convert_float(excel_instance.Volume(), password),
        "Delay": convert_float(excel_instance.Delay(), password),
        "RandomPitchMin": convert_int(excel_instance.RandomPitchMin(), password),
        "RandomPitchMax": convert_int(excel_instance.RandomPitchMax(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriority(), password),
        "AudioClipPath": [convert_string(excel_instance.AudioClipPath(j), password) for j in range(excel_instance.AudioClipPathLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_BGMExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
        "LoopStartTime": [convert_float(excel_instance.LoopStartTime(j), password) for j in range(excel_instance.LoopStartTimeLength())],
        "LoopEndTime": [convert_float(excel_instance.LoopEndTime(j), password) for j in range(excel_instance.LoopEndTimeLength())],
        "LoopTranstionTime": [convert_float(excel_instance.LoopTranstionTime(j), password) for j in range(excel_instance.LoopTranstionTimeLength())],
        "LoopOffsetTime": [convert_float(excel_instance.LoopOffsetTime(j), password) for j in range(excel_instance.LoopOffsetTimeLength())],
    }

def dump_BGMRaidExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_long(excel_instance.StageId(), password),
        "PhaseIndex": convert_long(excel_instance.PhaseIndex(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
    }

def dump_BGMUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UIPrefab": convert_uint(excel_instance.UIPrefab(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "BGMId2nd": convert_long(excel_instance.BGMId2nd(), password),
        "BGMId3rd": convert_long(excel_instance.BGMId3rd(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
    }

def dump_CameraExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "MinDistance": convert_float(excel_instance.MinDistance(), password),
        "MaxDistance": convert_float(excel_instance.MaxDistance(), password),
        "RotationX": convert_float(excel_instance.RotationX(), password),
        "RotationY": convert_float(excel_instance.RotationY(), password),
        "MoveInstantly": excel_instance.MoveInstantly(),
        "MoveInstantlyRotationSave": excel_instance.MoveInstantlyRotationSave(),
        "LeftMargin": convert_float(excel_instance.LeftMargin(), password),
        "BottomMargin": convert_float(excel_instance.BottomMargin(), password),
        "IgnoreEnemies": excel_instance.IgnoreEnemies(),
        "UseRailPointCompensation": excel_instance.UseRailPointCompensation(),
    }

def dump_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": convert_string(excel_instance.DialogType(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "HideUI": excel_instance.HideUI(),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterDialogEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_long(excel_instance.CostumeUniqueId(), password),
        "OriginalCharacterId": convert_long(excel_instance.OriginalCharacterId(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "EventID": convert_long(excel_instance.EventID(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogCondition(), password)).name,
        "DialogConditionDetail": DialogConditionDetail(convert_int(excel_instance.DialogConditionDetail(), password)).name,
        "DialogConditionDetailValue": convert_long(excel_instance.DialogConditionDetailValue(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogType(), password)).name,
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "CollectionVisible": excel_instance.CollectionVisible(),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "CVUnlockScenarioType": CVUnlockScenarioType(convert_int(excel_instance.CVUnlockScenarioType(), password)).name,
        "UnlockEventSeason": convert_long(excel_instance.UnlockEventSeason(), password),
        "ScenarioGroupId": convert_long(excel_instance.ScenarioGroupId(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
    }

def dump_CharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "CostumeUniqueId": convert_long(excel_instance.CostumeUniqueId(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogCondition(), password)).name,
        "Anniversary": Anniversary(convert_int(excel_instance.Anniversary(), password)).name,
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogType(), password)).name,
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "ApplyPosition": excel_instance.ApplyPosition(),
        "PosX": convert_float(excel_instance.PosX(), password),
        "PosY": convert_float(excel_instance.PosY(), password),
        "CollectionVisible": excel_instance.CollectionVisible(),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "UnlockFavorRank": convert_long(excel_instance.UnlockFavorRank(), password),
        "UnlockEquipWeapon": excel_instance.UnlockEquipWeapon(),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
    }

def dump_CharacterDialogSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "Separate": excel_instance.Separate(),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterGearExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "Tier": convert_long(excel_instance.Tier(), password),
        "NextTierEquipment": convert_long(excel_instance.NextTierEquipment(), password),
        "RecipeId": convert_long(excel_instance.RecipeId(), password),
        "OpenFavorLevel": convert_long(excel_instance.OpenFavorLevel(), password),
        "MaxLevel": convert_long(excel_instance.MaxLevel(), password),
        "LearnSkillSlot": convert_string(excel_instance.LearnSkillSlot(), password),
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatType(j), password)).name for j in range(excel_instance.StatTypeLength())],
        "MinStatValue": [convert_long(excel_instance.MinStatValue(j), password) for j in range(excel_instance.MinStatValueLength())],
        "MaxStatValue": [convert_long(excel_instance.MaxStatValue(j), password) for j in range(excel_instance.MaxStatValueLength())],
        "Icon": convert_string(excel_instance.Icon(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
    }

def dump_CharacterGearLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExp": [convert_long(excel_instance.TierLevelExp(j), password) for j in range(excel_instance.TierLevelExpLength())],
        "TotalExp": [convert_long(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
    }

def dump_CharacterPotentialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "PotentialStatGroupId": convert_long(excel_instance.PotentialStatGroupId(), password),
        "PotentialStatBonusRateType": PotentialStatBonusRateType(convert_int(excel_instance.PotentialStatBonusRateType(), password)).name,
        "IsUnnecessaryStat": excel_instance.IsUnnecessaryStat(),
    }

def dump_CharacterPotentialRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "RequirePotentialStatType": [PotentialStatBonusRateType(convert_int(excel_instance.RequirePotentialStatType(j), password)).name for j in range(excel_instance.RequirePotentialStatTypeLength())],
        "RequirePotentialStatLevel": [convert_long(excel_instance.RequirePotentialStatLevel(j), password) for j in range(excel_instance.RequirePotentialStatLevelLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_CharacterPotentialStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PotentialStatGroupId": convert_long(excel_instance.PotentialStatGroupId(), password),
        "PotentialLevel": convert_int(excel_instance.PotentialLevel(), password),
        "RecipeId": convert_long(excel_instance.RecipeId(), password),
        "StatBonusRate": convert_long(excel_instance.StatBonusRate(), password),
    }

def dump_CharacterVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterVoiceUniqueId": convert_long(excel_instance.CharacterVoiceUniqueId(), password),
        "CharacterVoiceGroupId": convert_long(excel_instance.CharacterVoiceGroupId(), password),
        "VoiceHash": convert_uint(excel_instance.VoiceHash(), password),
        "OnlyOne": excel_instance.OnlyOne(),
        "Priority": convert_int(excel_instance.Priority(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "CollectionVisible": excel_instance.CollectionVisible(),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "UnlockFavorRank": convert_long(excel_instance.UnlockFavorRank(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
        "Delay": [convert_float(excel_instance.Delay(j), password) for j in range(excel_instance.DelayLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
    }

def dump_CharacterVoiceSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterVoiceGroupId": convert_long(excel_instance.CharacterVoiceGroupId(), password),
        "Duration": convert_long(excel_instance.Duration(), password),
        "Separate": excel_instance.Separate(),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CheatCodeListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CheatCode": [convert_string(excel_instance.CheatCode(j), password) for j in range(excel_instance.CheatCodeLength())],
        "InputTitle": [convert_string(excel_instance.InputTitle(j), password) for j in range(excel_instance.InputTitleLength())],
        "Desc": convert_string(excel_instance.Desc(), password),
    }

def dump_ClanAssistSlotExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SlotId": convert_long(excel_instance.SlotId(), password),
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonType(), password)).name,
        "SlotNumber": convert_long(excel_instance.SlotNumber(), password),
        "AssistTermRewardPeriodFromSec": convert_long(excel_instance.AssistTermRewardPeriodFromSec(), password),
        "AssistRewardLimit": convert_long(excel_instance.AssistRewardLimit(), password),
        "AssistRentRewardDailyMaxCount": convert_long(excel_instance.AssistRentRewardDailyMaxCount(), password),
        "AssistRentalFeeAmount": convert_long(excel_instance.AssistRentalFeeAmount(), password),
        "AssistRentalFeeAmountStranger": convert_long(excel_instance.AssistRentalFeeAmountStranger(), password),
    }

def dump_ClanChattingEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TabGroupId": convert_int(excel_instance.TabGroupId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
    }

def dump_ClanRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ClanRewardType": ClanRewardType(convert_int(excel_instance.ClanRewardType(), password)).name,
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonType(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
    }

def dump_CombatEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "EmojiEvent": EmojiEvent(convert_int(excel_instance.EmojiEvent(), password)).name,
        "OrderOfPriority": convert_int(excel_instance.OrderOfPriority(), password),
        "EmojiDuration": excel_instance.EmojiDuration(),
        "EmojiReversal": excel_instance.EmojiReversal(),
        "EmojiTurnOn": excel_instance.EmojiTurnOn(),
        "ShowEmojiDelay": convert_int(excel_instance.ShowEmojiDelay(), password),
        "ShowDefaultBG": excel_instance.ShowDefaultBG(),
    }

def dump_ContentEnterCostReduceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EnterCostReduceGroupId": convert_long(excel_instance.EnterCostReduceGroupId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "StageId": convert_long(excel_instance.StageId(), password),
        "ReduceEnterCostType": ParcelType(convert_int(excel_instance.ReduceEnterCostType(), password)).name,
        "ReduceEnterCostId": convert_long(excel_instance.ReduceEnterCostId(), password),
        "ReduceAmount": convert_long(excel_instance.ReduceAmount(), password),
    }

def dump_ContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "SpoilerPopupTitle": convert_string(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_string(excel_instance.SpoilerPopupDescription(), password),
        "IsWarningPopUp": excel_instance.IsWarningPopUp(),
        "ConditionScenarioModeId": convert_long(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_ContentsScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ScenarioContentType": ScenarioContentType(convert_int(excel_instance.ScenarioContentType(), password)).name,
        "ScenarioGroupId": [convert_long(excel_instance.ScenarioGroupId(j), password) for j in range(excel_instance.ScenarioGroupIdLength())],
    }

def dump_ContentsShortcutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ScenarioModeVolume": convert_long(excel_instance.ScenarioModeVolume(), password),
        "ScenarioModeChapter": convert_long(excel_instance.ScenarioModeChapter(), password),
        "ShortcutOpenTime": convert_string(excel_instance.ShortcutOpenTime(), password),
        "ShortcutCloseTime": convert_string(excel_instance.ShortcutCloseTime(), password),
        "ConditionContentId": convert_long(excel_instance.ConditionContentId(), password),
        "ConquestMapDifficulty": StageDifficulty(convert_int(excel_instance.ConquestMapDifficulty(), password)).name,
        "ConquestStepIndex": convert_int(excel_instance.ConquestStepIndex(), password),
        "ShortcutContentId": convert_long(excel_instance.ShortcutContentId(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUIName(j), password) for j in range(excel_instance.ShortcutUINameLength())],
        "Localize": convert_string(excel_instance.Localize(), password),
    }

def dump_CurrencyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CurrencyType": CurrencyTypes(convert_int(excel_instance.CurrencyType(), password)).name,
        "CurrencyName": convert_string(excel_instance.CurrencyName(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "AutoChargeMsc": convert_int(excel_instance.AutoChargeMsc(), password),
        "AutoChargeAmount": convert_int(excel_instance.AutoChargeAmount(), password),
        "CurrencyOverChargeType": CurrencyOverChargeType(convert_int(excel_instance.CurrencyOverChargeType(), password)).name,
        "CurrencyAdditionalChargeType": CurrencyAdditionalChargeType(convert_int(excel_instance.CurrencyAdditionalChargeType(), password)).name,
        "ChargeLimit": convert_long(excel_instance.ChargeLimit(), password),
        "OverChargeLimit": convert_long(excel_instance.OverChargeLimit(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "DailyRefillType": DailyRefillType(convert_int(excel_instance.DailyRefillType(), password)).name,
        "DailyRefillAmount": convert_long(excel_instance.DailyRefillAmount(), password),
        "DailyRefillTime": [convert_long(excel_instance.DailyRefillTime(j), password) for j in range(excel_instance.DailyRefillTimeLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelType(), password)).name,
        "ExpiryChangeId": convert_long(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_long(excel_instance.ExpiryChangeAmount(), password),
    }

def dump_DuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategory(), password)).name,
        "ItemId": convert_long(excel_instance.ItemId(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
    }

def dump_EmblemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Category": EmblemCategory(convert_int(excel_instance.Category(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "UseAtLocalizeId": convert_long(excel_instance.UseAtLocalizeId(), password),
        "EmblemTextVisible": excel_instance.EmblemTextVisible(),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EmblemIconPath": convert_string(excel_instance.EmblemIconPath(), password),
        "EmblemIconNumControl": convert_int(excel_instance.EmblemIconNumControl(), password),
        "EmblemIconBGPath": convert_string(excel_instance.EmblemIconBGPath(), password),
        "EmblemBGPathJp": convert_string(excel_instance.EmblemBGPathJp(), password),
        "EmblemBGPathKr": convert_string(excel_instance.EmblemBGPathKr(), password),
        "DisplayType": EmblemDisplayType(convert_int(excel_instance.DisplayType(), password)).name,
        "DisplayStartDate": convert_string(excel_instance.DisplayStartDate(), password),
        "DisplayEndDate": convert_string(excel_instance.DisplayEndDate(), password),
        "DislpayFavorLevel": convert_int(excel_instance.DislpayFavorLevel(), password),
        "CheckPassType": EmblemCheckPassType(convert_int(excel_instance.CheckPassType(), password)).name,
        "EmblemParameter": convert_long(excel_instance.EmblemParameter(), password),
        "CheckPassCount": convert_long(excel_instance.CheckPassCount(), password),
    }

def dump_EquipmentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategory(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Wear": excel_instance.Wear(),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "TierInit": convert_long(excel_instance.TierInit(), password),
        "NextTierEquipment": convert_long(excel_instance.NextTierEquipment(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "ImageName": convert_string(excel_instance.ImageName(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
        "CraftQualityTier0": convert_long(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_long(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_long(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_long(excel_instance.ShiftingCraftQuality(), password),
        "ShopCategory": [ShopCategoryType(convert_int(excel_instance.ShopCategory(j), password)).name for j in range(excel_instance.ShopCategoryLength())],
        "ShortcutTypeId": convert_long(excel_instance.ShortcutTypeId(), password),
    }

def dump_EquipmentLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExp": [convert_long(excel_instance.TierLevelExp(j), password) for j in range(excel_instance.TierLevelExpLength())],
        "TotalExp": [convert_long(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
    }

def dump_EquipmentStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_long(excel_instance.EquipmentId(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatType(j), password)).name for j in range(excel_instance.StatTypeLength())],
        "MinStat": [convert_long(excel_instance.MinStat(j), password) for j in range(excel_instance.MinStatLength())],
        "MaxStat": [convert_long(excel_instance.MaxStat(j), password) for j in range(excel_instance.MaxStatLength())],
        "LevelUpInsertLimit": convert_int(excel_instance.LevelUpInsertLimit(), password),
        "LevelUpFeedExp": convert_long(excel_instance.LevelUpFeedExp(), password),
        "LevelUpFeedCostCurrency": CurrencyTypes(convert_int(excel_instance.LevelUpFeedCostCurrency(), password)).name,
        "LevelUpFeedCostAmount": convert_long(excel_instance.LevelUpFeedCostAmount(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategory(), password)).name,
        "LevelUpFeedAddExp": convert_long(excel_instance.LevelUpFeedAddExp(), password),
        "DefaultMaxLevel": convert_int(excel_instance.DefaultMaxLevel(), password),
        "TranscendenceMax": convert_int(excel_instance.TranscendenceMax(), password),
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupId(), password),
    }

def dump_EventContentNotifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EventNotifyType": EventNotifyType(convert_int(excel_instance.EventNotifyType(), password)).name,
        "EventTargetType": EventTargetType(convert_int(excel_instance.EventTargetType(), password)).name,
        "ShortcutEventTargetType": EventTargetType(convert_int(excel_instance.ShortcutEventTargetType(), password)).name,
        "IsShortcutEnable": excel_instance.IsShortcutEnable(),
    }

def dump_EventContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "SpoilerPopupTitle": convert_string(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_string(excel_instance.SpoilerPopupDescription(), password),
        "IsWarningPopUp": excel_instance.IsWarningPopUp(),
        "ConditionScenarioModeId": convert_long(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_EventContentTreasureCellRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeID(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentTreasureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "TitleLocalize": convert_string(excel_instance.TitleLocalize(), password),
        "LoopRound": convert_int(excel_instance.LoopRound(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
        "TreasureBGImagePath": convert_string(excel_instance.TreasureBGImagePath(), password),
    }

def dump_EventContentTreasureRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeID(), password),
        "CellUnderImageWidth": convert_int(excel_instance.CellUnderImageWidth(), password),
        "CellUnderImageHeight": convert_int(excel_instance.CellUnderImageHeight(), password),
        "HiddenImage": excel_instance.HiddenImage(),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
        "CellUnderImagePath": convert_string(excel_instance.CellUnderImagePath(), password),
        "TreasureSmallImagePath": convert_string(excel_instance.TreasureSmallImagePath(), password),
        "TreasureSizeIconPath": convert_string(excel_instance.TreasureSizeIconPath(), password),
    }

def dump_EventContentTreasureRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "TreasureRound": convert_int(excel_instance.TreasureRound(), password),
        "TreasureRoundSize": [convert_int(excel_instance.TreasureRoundSize(j), password) for j in range(excel_instance.TreasureRoundSizeLength())],
        "CellVisualSortUnstructed": excel_instance.CellVisualSortUnstructed(),
        "CellCheckGoodsId": convert_long(excel_instance.CellCheckGoodsId(), password),
        "CellRewardId": convert_long(excel_instance.CellRewardId(), password),
        "RewardID": [convert_long(excel_instance.RewardID(j), password) for j in range(excel_instance.RewardIDLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
        "TreasureCellImagePath": convert_string(excel_instance.TreasureCellImagePath(), password),
    }

def dump_FarmingDungeonLocationManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FarmingDungeonLocationId": convert_long(excel_instance.FarmingDungeonLocationId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "WeekDungeonType": WeekDungeonType(convert_int(excel_instance.WeekDungeonType(), password)).name,
        "SchoolDungeonType": SchoolDungeonType(convert_int(excel_instance.SchoolDungeonType(), password)).name,
        "Order": convert_long(excel_instance.Order(), password),
        "OpenStartDateTime": convert_string(excel_instance.OpenStartDateTime(), password),
        "OpenEndDateTime": convert_string(excel_instance.OpenEndDateTime(), password),
        "LocationButtonImagePath": convert_string(excel_instance.LocationButtonImagePath(), password),
        "LocalizeCodeTitle": convert_uint(excel_instance.LocalizeCodeTitle(), password),
        "LocalizeCodeInfo": convert_uint(excel_instance.LocalizeCodeInfo(), password),
    }

def dump_FavorLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_long(excel_instance.Level(), password),
        "ExpType": [convert_long(excel_instance.ExpType(j), password) for j in range(excel_instance.ExpTypeLength())],
    }

def dump_FavorLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "FavorLevel": convert_long(excel_instance.FavorLevel(), password),
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatType(j), password)).name for j in range(excel_instance.StatTypeLength())],
        "StatValue": [convert_long(excel_instance.StatValue(j), password) for j in range(excel_instance.StatValueLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_long(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_FixedEchelonSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FixedEchelonID": convert_long(excel_instance.FixedEchelonID(), password),
        "EchelonSceneSkip": excel_instance.EchelonSceneSkip(),
        "MainLeaderSlot": convert_int(excel_instance.MainLeaderSlot(), password),
        "MainCharacterID": [convert_long(excel_instance.MainCharacterID(j), password) for j in range(excel_instance.MainCharacterIDLength())],
        "MainLevel": [convert_int(excel_instance.MainLevel(j), password) for j in range(excel_instance.MainLevelLength())],
        "MainGrade": [convert_int(excel_instance.MainGrade(j), password) for j in range(excel_instance.MainGradeLength())],
        "MainExSkillLevel": [convert_int(excel_instance.MainExSkillLevel(j), password) for j in range(excel_instance.MainExSkillLevelLength())],
        "MainNoneExSkillLevel": [convert_int(excel_instance.MainNoneExSkillLevel(j), password) for j in range(excel_instance.MainNoneExSkillLevelLength())],
        "MainEquipment1Tier": [convert_int(excel_instance.MainEquipment1Tier(j), password) for j in range(excel_instance.MainEquipment1TierLength())],
        "MainEquipment1Level": [convert_int(excel_instance.MainEquipment1Level(j), password) for j in range(excel_instance.MainEquipment1LevelLength())],
        "MainEquipment2Tier": [convert_int(excel_instance.MainEquipment2Tier(j), password) for j in range(excel_instance.MainEquipment2TierLength())],
        "MainEquipment2Level": [convert_int(excel_instance.MainEquipment2Level(j), password) for j in range(excel_instance.MainEquipment2LevelLength())],
        "MainEquipment3Tier": [convert_int(excel_instance.MainEquipment3Tier(j), password) for j in range(excel_instance.MainEquipment3TierLength())],
        "MainEquipment3Level": [convert_int(excel_instance.MainEquipment3Level(j), password) for j in range(excel_instance.MainEquipment3LevelLength())],
        "MainCharacterWeaponGrade": [convert_int(excel_instance.MainCharacterWeaponGrade(j), password) for j in range(excel_instance.MainCharacterWeaponGradeLength())],
        "MainCharacterWeaponLevel": [convert_int(excel_instance.MainCharacterWeaponLevel(j), password) for j in range(excel_instance.MainCharacterWeaponLevelLength())],
        "MainCharacterGearTier": [convert_int(excel_instance.MainCharacterGearTier(j), password) for j in range(excel_instance.MainCharacterGearTierLength())],
        "MainCharacterGearLevel": [convert_int(excel_instance.MainCharacterGearLevel(j), password) for j in range(excel_instance.MainCharacterGearLevelLength())],
        "SupportCharacterID": [convert_long(excel_instance.SupportCharacterID(j), password) for j in range(excel_instance.SupportCharacterIDLength())],
        "SupportLevel": [convert_int(excel_instance.SupportLevel(j), password) for j in range(excel_instance.SupportLevelLength())],
        "SupportGrade": [convert_int(excel_instance.SupportGrade(j), password) for j in range(excel_instance.SupportGradeLength())],
        "SupportExSkillLevel": [convert_int(excel_instance.SupportExSkillLevel(j), password) for j in range(excel_instance.SupportExSkillLevelLength())],
        "SupportNoneExSkillLevel": [convert_int(excel_instance.SupportNoneExSkillLevel(j), password) for j in range(excel_instance.SupportNoneExSkillLevelLength())],
        "SupportEquipment1Tier": [convert_int(excel_instance.SupportEquipment1Tier(j), password) for j in range(excel_instance.SupportEquipment1TierLength())],
        "SupportEquipment1Level": [convert_int(excel_instance.SupportEquipment1Level(j), password) for j in range(excel_instance.SupportEquipment1LevelLength())],
        "SupportEquipment2Tier": [convert_int(excel_instance.SupportEquipment2Tier(j), password) for j in range(excel_instance.SupportEquipment2TierLength())],
        "SupportEquipment2Level": [convert_int(excel_instance.SupportEquipment2Level(j), password) for j in range(excel_instance.SupportEquipment2LevelLength())],
        "SupportEquipment3Tier": [convert_int(excel_instance.SupportEquipment3Tier(j), password) for j in range(excel_instance.SupportEquipment3TierLength())],
        "SupportEquipment3Level": [convert_int(excel_instance.SupportEquipment3Level(j), password) for j in range(excel_instance.SupportEquipment3LevelLength())],
        "SupportCharacterWeaponGrade": [convert_int(excel_instance.SupportCharacterWeaponGrade(j), password) for j in range(excel_instance.SupportCharacterWeaponGradeLength())],
        "SupportCharacterWeaponLevel": [convert_int(excel_instance.SupportCharacterWeaponLevel(j), password) for j in range(excel_instance.SupportCharacterWeaponLevelLength())],
        "SupportCharacterGearTier": [convert_int(excel_instance.SupportCharacterGearTier(j), password) for j in range(excel_instance.SupportCharacterGearTierLength())],
        "SupportCharacterGearLevel": [convert_int(excel_instance.SupportCharacterGearLevel(j), password) for j in range(excel_instance.SupportCharacterGearLevelLength())],
        "InteractionTSCharacterId": convert_long(excel_instance.InteractionTSCharacterId(), password),
    }

def dump_FormationLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "GroupID": convert_long(excel_instance.GroupID(), password),
        "SlotZ": [convert_float(excel_instance.SlotZ(j), password) for j in range(excel_instance.SlotZLength())],
        "SlotX": [convert_float(excel_instance.SlotX(j), password) for j in range(excel_instance.SlotXLength())],
    }

def dump_GachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "GachaGroupID": convert_long(excel_instance.GachaGroupID(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelID": convert_long(excel_instance.ParcelID(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMin(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMax(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "State": convert_int(excel_instance.State(), password),
    }

def dump_GachaElementRecursiveExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "GachaGroupID": convert_long(excel_instance.GachaGroupID(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelID": convert_long(excel_instance.ParcelID(), password),
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMin(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMax(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "State": convert_int(excel_instance.State(), password),
    }

def dump_GachaGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "IsRecursive": excel_instance.IsRecursive(),
        "GroupType": GachaGroupType(convert_int(excel_instance.GroupType(), password)).name,
    }

def dump_GoodsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Type": convert_int(excel_instance.Type(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "ConsumeParcelType": [ParcelType(convert_int(excel_instance.ConsumeParcelType(j), password)).name for j in range(excel_instance.ConsumeParcelTypeLength())],
        "ConsumeParcelId": [convert_long(excel_instance.ConsumeParcelId(j), password) for j in range(excel_instance.ConsumeParcelIdLength())],
        "ConsumeParcelAmount": [convert_long(excel_instance.ConsumeParcelAmount(j), password) for j in range(excel_instance.ConsumeParcelAmountLength())],
        "ConsumeCondition": [ConsumeCondition(convert_int(excel_instance.ConsumeCondition(j), password)).name for j in range(excel_instance.ConsumeConditionLength())],
        "ConsumeGachaTicketType": GachaTicketType(convert_int(excel_instance.ConsumeGachaTicketType(), password)).name,
        "ConsumeGachaTicketTypeAmount": convert_long(excel_instance.ConsumeGachaTicketTypeAmount(), password),
        "ProductIdAOS": convert_long(excel_instance.ProductIdAOS(), password),
        "ProductIdiOS": convert_long(excel_instance.ProductIdiOS(), password),
        "ConsumeExtraStep": [convert_long(excel_instance.ConsumeExtraStep(j), password) for j in range(excel_instance.ConsumeExtraStepLength())],
        "ConsumeExtraAmount": [convert_long(excel_instance.ConsumeExtraAmount(j), password) for j in range(excel_instance.ConsumeExtraAmountLength())],
        "State": convert_int(excel_instance.State(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_long(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_GroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StageFileName": [convert_string(excel_instance.StageFileName(j), password) for j in range(excel_instance.StageFileNameLength())],
        "GroundSceneName": convert_string(excel_instance.GroundSceneName(), password),
        "FormationGroupId": convert_long(excel_instance.FormationGroupId(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "EnemyBulletType": BulletType(convert_int(excel_instance.EnemyBulletType(), password)).name,
        "EnemyArmorType": ArmorType(convert_int(excel_instance.EnemyArmorType(), password)).name,
        "LevelNPC": convert_long(excel_instance.LevelNPC(), password),
        "LevelMinion": convert_long(excel_instance.LevelMinion(), password),
        "LevelElite": convert_long(excel_instance.LevelElite(), password),
        "LevelChampion": convert_long(excel_instance.LevelChampion(), password),
        "LevelBoss": convert_long(excel_instance.LevelBoss(), password),
        "ObstacleLevel": convert_long(excel_instance.ObstacleLevel(), password),
        "GradeNPC": convert_long(excel_instance.GradeNPC(), password),
        "GradeMinion": convert_long(excel_instance.GradeMinion(), password),
        "GradeElite": convert_long(excel_instance.GradeElite(), password),
        "GradeChampion": convert_long(excel_instance.GradeChampion(), password),
        "GradeBoss": convert_long(excel_instance.GradeBoss(), password),
        "PlayerSightPointAdd": convert_long(excel_instance.PlayerSightPointAdd(), password),
        "PlayerSightPointRate": convert_long(excel_instance.PlayerSightPointRate(), password),
        "PlayerAttackRangeAdd": convert_long(excel_instance.PlayerAttackRangeAdd(), password),
        "PlayerAttackRangeRate": convert_long(excel_instance.PlayerAttackRangeRate(), password),
        "EnemySightPointAdd": convert_long(excel_instance.EnemySightPointAdd(), password),
        "EnemySightPointRate": convert_long(excel_instance.EnemySightPointRate(), password),
        "EnemyAttackRangeAdd": convert_long(excel_instance.EnemyAttackRangeAdd(), password),
        "EnemyAttackRangeRate": convert_long(excel_instance.EnemyAttackRangeRate(), password),
        "PlayerSkillRangeAdd": convert_long(excel_instance.PlayerSkillRangeAdd(), password),
        "PlayerSkillRangeRate": convert_long(excel_instance.PlayerSkillRangeRate(), password),
        "EnemySkillRangeAdd": convert_long(excel_instance.EnemySkillRangeAdd(), password),
        "EnemySkillRangeRate": convert_long(excel_instance.EnemySkillRangeRate(), password),
        "PlayerMinimumPositionGapRate": convert_long(excel_instance.PlayerMinimumPositionGapRate(), password),
        "EnemyMinimumPositionGapRate": convert_long(excel_instance.EnemyMinimumPositionGapRate(), password),
        "PlayerSightRangeMax": excel_instance.PlayerSightRangeMax(),
        "EnemySightRangeMax": excel_instance.EnemySightRangeMax(),
        "TSSAirUnitHeight": convert_long(excel_instance.TSSAirUnitHeight(), password),
        "IsPhaseBGM": excel_instance.IsPhaseBGM(),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "WarningUI": excel_instance.WarningUI(),
        "TSSHatchOpen": excel_instance.TSSHatchOpen(),
        "ForcedTacticSpeed": TacticSpeed(convert_int(excel_instance.ForcedTacticSpeed(), password)).name,
        "ForcedSkillUse": TacticSkillUse(convert_int(excel_instance.ForcedSkillUse(), password)).name,
        "ShowNPCSkillCutIn": ShowSkillCutIn(convert_int(excel_instance.ShowNPCSkillCutIn(), password)).name,
        "ImmuneHitBeforeTimeOutEnd": excel_instance.ImmuneHitBeforeTimeOutEnd(),
        "UIBattleHideFromScratch": excel_instance.UIBattleHideFromScratch(),
        "BattleReadyTimelinePath": convert_string(excel_instance.BattleReadyTimelinePath(), password),
        "BeforeVictoryTimelinePath": convert_string(excel_instance.BeforeVictoryTimelinePath(), password),
        "SkipBattleEnd": excel_instance.SkipBattleEnd(),
        "HideNPCWhenBattleEnd": excel_instance.HideNPCWhenBattleEnd(),
        "CoverPointOff": excel_instance.CoverPointOff(),
        "UIHpScale": convert_float(excel_instance.UIHpScale(), password),
        "UIEmojiScale": convert_float(excel_instance.UIEmojiScale(), password),
        "UISkillMainLogScale": convert_float(excel_instance.UISkillMainLogScale(), password),
        "EffectCountLimit": convert_int(excel_instance.EffectCountLimit(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillId(j), password) for j in range(excel_instance.AllyPassiveSkillIdLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillId(j), password) for j in range(excel_instance.EnemyPassiveSkillIdLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevel(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelLength())],
    }

def dump_GroundModuleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_uint(excel_instance.GroupId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_long(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_GuideMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "Id": convert_long(excel_instance.Id(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "IsLegacy": excel_instance.IsLegacy(),
        "TabNumber": convert_long(excel_instance.TabNumber(), password),
        "PreMissionId": [convert_long(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "Description": convert_uint(excel_instance.Description(), password),
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "CompleteConditionCount": convert_long(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_long(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTag(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "IsAutoClearForScenario": excel_instance.IsAutoClearForScenario(),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelType(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_long(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
    }

def dump_GuideMissionOpenStageConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "OrderNumber": convert_long(excel_instance.OrderNumber(), password),
        "TabLocalizeCode": convert_string(excel_instance.TabLocalizeCode(), password),
        "ClearScenarioModeId": convert_long(excel_instance.ClearScenarioModeId(), password),
        "LockScenarioTextLocailzeCode": convert_string(excel_instance.LockScenarioTextLocailzeCode(), password),
        "ShortcutScenarioUI": convert_string(excel_instance.ShortcutScenarioUI(), password),
        "ClearStageId": convert_long(excel_instance.ClearStageId(), password),
        "LockStageTextLocailzeCode": convert_string(excel_instance.LockStageTextLocailzeCode(), password),
        "ShortcutStageUI": convert_string(excel_instance.ShortcutStageUI(), password),
    }

def dump_GuideMissionSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TitleLocalizeCode": convert_string(excel_instance.TitleLocalizeCode(), password),
        "PermanentInfomationLocalizeCode": convert_string(excel_instance.PermanentInfomationLocalizeCode(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCode(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "Enabled": excel_instance.Enabled(),
        "BannerOpenDate": convert_string(excel_instance.BannerOpenDate(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "CloseBannerAfterCompletion": excel_instance.CloseBannerAfterCompletion(),
        "MaximumLoginCount": convert_long(excel_instance.MaximumLoginCount(), password),
        "ExpiryDate": convert_long(excel_instance.ExpiryDate(), password),
        "SpineCharacterId": convert_long(excel_instance.SpineCharacterId(), password),
        "RequirementParcelImage": convert_string(excel_instance.RequirementParcelImage(), password),
        "RewardImage": convert_string(excel_instance.RewardImage(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImage(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImage(), password),
        "TitleImage": convert_string(excel_instance.TitleImage(), password),
        "RequirementParcelType": ParcelType(convert_int(excel_instance.RequirementParcelType(), password)).name,
        "RequirementParcelId": convert_long(excel_instance.RequirementParcelId(), password),
        "RequirementParcelAmount": convert_int(excel_instance.RequirementParcelAmount(), password),
        "TabType": GuideMissionTabType(convert_int(excel_instance.TabType(), password)).name,
        "IsPermanent": excel_instance.IsPermanent(),
        "PreSeasonId": convert_long(excel_instance.PreSeasonId(), password),
    }

def dump_IdCardBackgroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "CollectionVisible": excel_instance.CollectionVisible(),
        "IsDefault": excel_instance.IsDefault(),
        "BgPath": convert_string(excel_instance.BgPath(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
    }

def dump_InformationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupID": convert_long(excel_instance.GroupID(), password),
        "PageName": convert_string(excel_instance.PageName(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
        "TutorialParentName": [convert_string(excel_instance.TutorialParentName(j), password) for j in range(excel_instance.TutorialParentNameLength())],
        "UIName": [convert_string(excel_instance.UIName(j), password) for j in range(excel_instance.UINameLength())],
    }

def dump_ItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategory(), password)).name,
        "Quality": convert_long(excel_instance.Quality(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "StackableFunction": convert_int(excel_instance.StackableFunction(), password),
        "ImmediateUse": excel_instance.ImmediateUse(),
        "UsingResultParcelType": ParcelType(convert_int(excel_instance.UsingResultParcelType(), password)).name,
        "UsingResultId": convert_long(excel_instance.UsingResultId(), password),
        "UsingResultAmount": convert_long(excel_instance.UsingResultAmount(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelType(), password)).name,
        "ExpiryChangeId": convert_long(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_long(excel_instance.ExpiryChangeAmount(), password),
        "CanTierUpgrade": excel_instance.CanTierUpgrade(),
        "TierUpgradeRecipeCraftId": convert_long(excel_instance.TierUpgradeRecipeCraftId(), password),
        "Tags": [Tag(convert_int(excel_instance.Tags(j), password)).name for j in range(excel_instance.TagsLength())],
        "CraftQualityTier0": convert_long(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_long(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_long(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_long(excel_instance.ShiftingCraftQuality(), password),
        "MaxGiftTags": convert_int(excel_instance.MaxGiftTags(), password),
        "ShopCategory": [ShopCategoryType(convert_int(excel_instance.ShopCategory(j), password)).name for j in range(excel_instance.ShopCategoryLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "ShortcutTypeId": convert_long(excel_instance.ShortcutTypeId(), password),
        "GachaTicket": GachaTicketType(convert_int(excel_instance.GachaTicket(), password)).name,
    }

def dump_LoadingImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
        "DisplayWeight": convert_int(excel_instance.DisplayWeight(), password),
    }

def dump_LocalizeCharProfileChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "ScenarioModeId": convert_long(excel_instance.ScenarioModeId(), password),
        "ChangeCharacterID": convert_long(excel_instance.ChangeCharacterID(), password),
    }

def dump_LocalizeCodeInBuildExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeErrorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "ErrorLevel": WebAPIErrorLevel(convert_int(excel_instance.ErrorLevel(), password)).name,
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeEtcExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKr(), password),
        "NameJp": convert_string(excel_instance.NameJp(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJp(), password),
    }

def dump_LocalizeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GachaShopId": convert_long(excel_instance.GachaShopId(), password),
        "TabNameKr": convert_string(excel_instance.TabNameKr(), password),
        "TabNameJp": convert_string(excel_instance.TabNameJp(), password),
        "TitleNameKr": convert_string(excel_instance.TitleNameKr(), password),
        "TitleNameJp": convert_string(excel_instance.TitleNameJp(), password),
        "SubTitleKr": convert_string(excel_instance.SubTitleKr(), password),
        "SubTitleJp": convert_string(excel_instance.SubTitleJp(), password),
        "GachaDescriptionKr": convert_string(excel_instance.GachaDescriptionKr(), password),
        "GachaDescriptionJp": convert_string(excel_instance.GachaDescriptionJp(), password),
    }

def dump_LocalizeSkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKr(), password),
        "SkillInvokeLocalizeKr": convert_string(excel_instance.SkillInvokeLocalizeKr(), password),
        "NameJp": convert_string(excel_instance.NameJp(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJp(), password),
        "SkillInvokeLocalizeJp": convert_string(excel_instance.SkillInvokeLocalizeJp(), password),
    }

def dump_MemoryLobbyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "MemoryLobbyCategory": MemoryLobbyCategory(convert_int(excel_instance.MemoryLobbyCategory(), password)).name,
        "SlotTextureName": convert_string(excel_instance.SlotTextureName(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureName(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "AudioClipJp": convert_string(excel_instance.AudioClipJp(), password),
        "AudioClipKr": convert_string(excel_instance.AudioClipKr(), password),
    }

def dump_MessagePopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringId": convert_uint(excel_instance.StringId(), password),
        "MessagePopupLayout": MessagePopupLayout(convert_int(excel_instance.MessagePopupLayout(), password)).name,
        "OrderType": MessagePopupImagePositionType(convert_int(excel_instance.OrderType(), password)).name,
        "Image": convert_string(excel_instance.Image(), password),
        "TitleText": convert_uint(excel_instance.TitleText(), password),
        "SubTitleText": convert_uint(excel_instance.SubTitleText(), password),
        "MessageText": convert_uint(excel_instance.MessageText(), password),
        "ConditionText": [convert_uint(excel_instance.ConditionText(j), password) for j in range(excel_instance.ConditionTextLength())],
        "DisplayXButton": excel_instance.DisplayXButton(),
        "Button": [MessagePopupButtonType(convert_int(excel_instance.Button(j), password)).name for j in range(excel_instance.ButtonLength())],
        "ButtonText": [convert_uint(excel_instance.ButtonText(j), password) for j in range(excel_instance.ButtonTextLength())],
        "ButtonCommand": [convert_string(excel_instance.ButtonCommand(j), password) for j in range(excel_instance.ButtonCommandLength())],
        "ButtonParameter": [convert_string(excel_instance.ButtonParameter(j), password) for j in range(excel_instance.ButtonParameterLength())],
    }

def dump_MiniGameDefenseCharacterBanExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
    }

def dump_MiniGameDefenseFixedStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MinigameDefenseFixedStatId": convert_long(excel_instance.MinigameDefenseFixedStatId(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "Grade": convert_int(excel_instance.Grade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "NoneExSkillLevel": convert_int(excel_instance.NoneExSkillLevel(), password),
        "Equipment1Tier": convert_int(excel_instance.Equipment1Tier(), password),
        "Equipment1Level": convert_int(excel_instance.Equipment1Level(), password),
        "Equipment2Tier": convert_int(excel_instance.Equipment2Tier(), password),
        "Equipment2Level": convert_int(excel_instance.Equipment2Level(), password),
        "Equipment3Tier": convert_int(excel_instance.Equipment3Tier(), password),
        "Equipment3Level": convert_int(excel_instance.Equipment3Level(), password),
        "CharacterWeaponGrade": convert_int(excel_instance.CharacterWeaponGrade(), password),
        "CharacterWeaponLevel": convert_int(excel_instance.CharacterWeaponLevel(), password),
        "CharacterGearTier": convert_int(excel_instance.CharacterGearTier(), password),
        "CharacterGearLevel": convert_int(excel_instance.CharacterGearLevel(), password),
    }

def dump_MiniGameDefenseInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DefenseBattleParcelType": ParcelType(convert_int(excel_instance.DefenseBattleParcelType(), password)).name,
        "DefenseBattleParcelId": convert_long(excel_instance.DefenseBattleParcelId(), password),
        "DefenseBattleMultiplierMax": convert_long(excel_instance.DefenseBattleMultiplierMax(), password),
        "DisableRootMotion": excel_instance.DisableRootMotion(),
    }

def dump_MiniGameDefenseStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageDifficultyLocalize": convert_uint(excel_instance.StageDifficultyLocalize(), password),
        "StageNumber": convert_int(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_long(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "EventContentStageRewardId": convert_long(excel_instance.EventContentStageRewardId(), password),
        "EnterScenarioGroupId": [convert_long(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_long(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_long(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "DefenseFormationBGPrefab": convert_string(excel_instance.DefenseFormationBGPrefab(), password),
        "DefenseFormationBGPrefabScale": convert_float(excel_instance.DefenseFormationBGPrefabScale(), password),
        "FixedEchelon": convert_long(excel_instance.FixedEchelon(), password),
        "MininageDefenseFixedStatId": convert_long(excel_instance.MininageDefenseFixedStatId(), password),
        "StageHint": convert_uint(excel_instance.StageHint(), password),
    }

def dump_MiniGameDreamCollectionScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "IsSkip": excel_instance.IsSkip(),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "Parameter": [DreamMakerParameterType(convert_int(excel_instance.Parameter(j), password)).name for j in range(excel_instance.ParameterLength())],
        "ParameterAmount": [convert_long(excel_instance.ParameterAmount(j), password) for j in range(excel_instance.ParameterAmountLength())],
        "ScenarioGroupId": convert_long(excel_instance.ScenarioGroupId(), password),
    }

def dump_MiniGameDreamDailyPointExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "TotalParameterMin": convert_long(excel_instance.TotalParameterMin(), password),
        "TotalParameterMax": convert_long(excel_instance.TotalParameterMax(), password),
        "DailyPointCoefficient": convert_long(excel_instance.DailyPointCoefficient(), password),
        "DailyPointCorrectionValue": convert_long(excel_instance.DailyPointCorrectionValue(), password),
    }

def dump_MiniGameDreamEndingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EndingId": convert_long(excel_instance.EndingId(), password),
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingType(), password)).name,
        "Order": convert_int(excel_instance.Order(), password),
        "ScenarioGroupId": convert_long(excel_instance.ScenarioGroupId(), password),
        "EndingCondition": [DreamMakerEndingCondition(convert_int(excel_instance.EndingCondition(j), password)).name for j in range(excel_instance.EndingConditionLength())],
        "EndingConditionValue": [convert_long(excel_instance.EndingConditionValue(j), password) for j in range(excel_instance.EndingConditionValueLength())],
    }

def dump_MiniGameDreamEndingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EndingId": convert_long(excel_instance.EndingId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "DreamMakerEndingRewardType": DreamMakerEndingRewardType(convert_int(excel_instance.DreamMakerEndingRewardType(), password)).name,
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingType(), password)).name,
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MiniGameDreamInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DreamMakerMultiplierCondition": DreamMakerMultiplierCondition(convert_int(excel_instance.DreamMakerMultiplierCondition(), password)).name,
        "DreamMakerMultiplierConditionValue": convert_long(excel_instance.DreamMakerMultiplierConditionValue(), password),
        "DreamMakerMultiplierMax": convert_long(excel_instance.DreamMakerMultiplierMax(), password),
        "DreamMakerDays": convert_long(excel_instance.DreamMakerDays(), password),
        "DreamMakerActionPoint": convert_long(excel_instance.DreamMakerActionPoint(), password),
        "DreamMakerParcelType": ParcelType(convert_int(excel_instance.DreamMakerParcelType(), password)).name,
        "DreamMakerParcelId": convert_long(excel_instance.DreamMakerParcelId(), password),
        "DreamMakerDailyPointParcelType": ParcelType(convert_int(excel_instance.DreamMakerDailyPointParcelType(), password)).name,
        "DreamMakerDailyPointId": convert_long(excel_instance.DreamMakerDailyPointId(), password),
        "DreamMakerParameterTransfer": convert_long(excel_instance.DreamMakerParameterTransfer(), password),
        "ScheduleCostGoodsId": convert_long(excel_instance.ScheduleCostGoodsId(), password),
        "LobbyBGMChangeScenarioId": convert_long(excel_instance.LobbyBGMChangeScenarioId(), password),
    }

def dump_MiniGameDreamParameterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ParameterType": DreamMakerParameterType(convert_int(excel_instance.ParameterType(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "ParameterBase": convert_long(excel_instance.ParameterBase(), password),
        "ParameterBaseMax": convert_long(excel_instance.ParameterBaseMax(), password),
        "ParameterMin": convert_long(excel_instance.ParameterMin(), password),
        "ParameterMax": convert_long(excel_instance.ParameterMax(), password),
    }

def dump_MiniGameDreamReplayScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "ScenarioGroupId": convert_long(excel_instance.ScenarioGroupId(), password),
        "Order": convert_long(excel_instance.Order(), password),
        "ReplaySummaryTitleLocalize": convert_uint(excel_instance.ReplaySummaryTitleLocalize(), password),
        "ReplaySummaryLocalizeScenarioId": convert_uint(excel_instance.ReplaySummaryLocalizeScenarioId(), password),
        "ReplayScenarioResource": convert_string(excel_instance.ReplayScenarioResource(), password),
        "IsReplayScenarioHorizon": excel_instance.IsReplayScenarioHorizon(),
    }

def dump_MiniGameDreamScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DreamMakerScheduleGroupId": convert_long(excel_instance.DreamMakerScheduleGroupId(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "LoadingResource01": convert_string(excel_instance.LoadingResource01(), password),
        "LoadingResource02": convert_string(excel_instance.LoadingResource02(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
    }

def dump_MiniGameDreamScheduleResultExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "DreamMakerResult": DreamMakerResult(convert_int(excel_instance.DreamMakerResult(), password)).name,
        "DreamMakerScheduleGroup": convert_long(excel_instance.DreamMakerScheduleGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "RewardParameter": [DreamMakerParameterType(convert_int(excel_instance.RewardParameter(j), password)).name for j in range(excel_instance.RewardParameterLength())],
        "RewardParameterOperationType": [DreamMakerParamOperationType(convert_int(excel_instance.RewardParameterOperationType(j), password)).name for j in range(excel_instance.RewardParameterOperationTypeLength())],
        "RewardParameterAmount": [convert_long(excel_instance.RewardParameterAmount(j), password) for j in range(excel_instance.RewardParameterAmountLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
    }

def dump_MiniGameDreamTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "DreamMakerDays": convert_long(excel_instance.DreamMakerDays(), password),
        "DreamMakerActionPoint": convert_long(excel_instance.DreamMakerActionPoint(), password),
        "EnterScenarioGroupId": convert_long(excel_instance.EnterScenarioGroupId(), password),
        "Bgm": convert_long(excel_instance.Bgm(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPath(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPath(), password),
    }

def dump_MinigameDreamVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "VoiceCondition": DreamMakerVoiceCondition(convert_int(excel_instance.VoiceCondition(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
    }

def dump_MiniGameRoadPuzzleInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventUseCostType": ParcelType(convert_int(excel_instance.EventUseCostType(), password)).name,
        "EventUseCostId": convert_long(excel_instance.EventUseCostId(), password),
        "CostGoodsId": convert_long(excel_instance.CostGoodsId(), password),
        "RailSetRewardId": convert_long(excel_instance.RailSetRewardId(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRound(), password),
    }

def dump_MinigameRoadPuzzleMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "MapGroupId": convert_long(excel_instance.MapGroupId(), password),
        "Map": convert_string(excel_instance.Map(), password),
        "MapBG": convert_string(excel_instance.MapBG(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "AvailableRailTile": [convert_long(excel_instance.AvailableRailTile(j), password) for j in range(excel_instance.AvailableRailTileLength())],
        "AvailableRailTileAmount": [convert_long(excel_instance.AvailableRailTileAmount(j), password) for j in range(excel_instance.AvailableRailTileAmountLength())],
        "OriginalTileCount": [convert_long(excel_instance.OriginalTileCount(j), password) for j in range(excel_instance.OriginalTileCountLength())],
        "TrainSpeed": convert_float(excel_instance.TrainSpeed(), password),
    }

def dump_MinigameRoadPuzzleMapTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "MapTileType": RoadPuzzleMapTileType(convert_int(excel_instance.MapTileType(), password)).name,
    }

def dump_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "LocalizePrefabID": convert_string(excel_instance.LocalizePrefabID(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameRoadPuzzleRailTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "OriginalTile": excel_instance.OriginalTile(),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "RailTileType": RoadPuzzleRailTileType(convert_int(excel_instance.RailTileType(), password)).name,
    }

def dump_MiniGameRoadPuzzleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_long(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameRoadPuzzleRoadRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "IsLoop": excel_instance.IsLoop(),
        "EnterScenarioGroupId": convert_long(excel_instance.EnterScenarioGroupId(), password),
        "EndScenarioGroupId": convert_long(excel_instance.EndScenarioGroupId(), password),
        "MapGroupId": convert_long(excel_instance.MapGroupId(), password),
        "RoundReward": convert_long(excel_instance.RoundReward(), password),
        "AdditionalRewardID": [convert_long(excel_instance.AdditionalRewardID(j), password) for j in range(excel_instance.AdditionalRewardIDLength())],
        "AdditionalRewardAmount": [convert_int(excel_instance.AdditionalRewardAmount(j), password) for j in range(excel_instance.AdditionalRewardAmountLength())],
    }

def dump_MiniGameRoadPuzzleVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "VoiceCondition": RoadPuzzleVoiceCondition(convert_int(excel_instance.VoiceCondition(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_MissionEmergencyCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MissionId": convert_long(excel_instance.MissionId(), password),
        "EmergencyComplete": excel_instance.EmergencyComplete(),
    }

def dump_MissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": excel_instance.ViewFlag(),
        "Limit": excel_instance.Limit(),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "EndDay": convert_long(excel_instance.EndDay(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "DateAutoRefer": ContentType(convert_int(excel_instance.DateAutoRefer(), password)).name,
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_long(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_long(excel_instance.AccountLevel(), password),
        "ContentTags": [SuddenMissionContentType(convert_int(excel_instance.ContentTags(j), password)).name for j in range(excel_instance.ContentTagsLength())],
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "ChallengeStageShortcut": convert_long(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "CompleteConditionCount": convert_long(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_long(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTag(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelType(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_long(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
    }

def dump_MultiFloorRaidRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardGroupId": convert_long(excel_instance.RewardGroupId(), password),
        "ClearStageRewardProb": convert_long(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_long(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_long(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_MultiFloorRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "LobbyEnterScenario": convert_uint(excel_instance.LobbyEnterScenario(), password),
        "ShowLobbyBanner": excel_instance.ShowLobbyBanner(),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDate(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "OpenRaidBossGroupId": convert_string(excel_instance.OpenRaidBossGroupId(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "LobbyImgPath": convert_string(excel_instance.LobbyImgPath(), password),
        "LevelImgPath": convert_string(excel_instance.LevelImgPath(), password),
        "PlayTip": convert_string(excel_instance.PlayTip(), password),
    }

def dump_MultiFloorRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "BossGroupId": convert_string(excel_instance.BossGroupId(), password),
        "AssistSlot": convert_int(excel_instance.AssistSlot(), password),
        "StageOpenCondition": convert_long(excel_instance.StageOpenCondition(), password),
        "FloorListSection": excel_instance.FloorListSection(),
        "FloorListSectionOpenCondition": convert_long(excel_instance.FloorListSectionOpenCondition(), password),
        "FloorListSectionLabel": convert_uint(excel_instance.FloorListSectionLabel(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "UseBossIndex": excel_instance.UseBossIndex(),
        "UseBossAIPhaseSync": excel_instance.UseBossAIPhaseSync(),
        "FloorListImgPath": convert_string(excel_instance.FloorListImgPath(), password),
        "FloorImgPath": convert_string(excel_instance.FloorImgPath(), password),
        "RaidCharacterId": convert_long(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_long(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "StatChangeId": [convert_long(excel_instance.StatChangeId(j), password) for j in range(excel_instance.StatChangeIdLength())],
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "RecommendLevel": convert_long(excel_instance.RecommendLevel(), password),
        "RewardGroupId": convert_long(excel_instance.RewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "ShowSkillCard": excel_instance.ShowSkillCard(),
    }

def dump_MultiFloorRaidStatChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StatChangeId": convert_long(excel_instance.StatChangeId(), password),
        "StatType": [StatType(convert_int(excel_instance.StatType(j), password)).name for j in range(excel_instance.StatTypeLength())],
        "StatAdd": [convert_long(excel_instance.StatAdd(j), password) for j in range(excel_instance.StatAddLength())],
        "StatMultiply": [convert_long(excel_instance.StatMultiply(j), password) for j in range(excel_instance.StatMultiplyLength())],
        "ApplyCharacterId": [convert_long(excel_instance.ApplyCharacterId(j), password) for j in range(excel_instance.ApplyCharacterIdLength())],
    }

def dump_ObstacleStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringID(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "MaxHP1": convert_long(excel_instance.MaxHP1(), password),
        "MaxHP100": convert_long(excel_instance.MaxHP100(), password),
        "BlockRate": convert_long(excel_instance.BlockRate(), password),
        "Dodge": convert_long(excel_instance.Dodge(), password),
        "CanNotStandRange": convert_long(excel_instance.CanNotStandRange(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeight(), password),
        "EnhanceLightArmorRate": convert_long(excel_instance.EnhanceLightArmorRate(), password),
        "EnhanceHeavyArmorRate": convert_long(excel_instance.EnhanceHeavyArmorRate(), password),
        "EnhanceUnarmedRate": convert_long(excel_instance.EnhanceUnarmedRate(), password),
        "EnhanceElasticArmorRate": convert_long(excel_instance.EnhanceElasticArmorRate(), password),
        "EnhanceStructureRate": convert_long(excel_instance.EnhanceStructureRate(), password),
        "EnhanceNormalArmorRate": convert_long(excel_instance.EnhanceNormalArmorRate(), password),
        "ReduceExDamagedRate": convert_long(excel_instance.ReduceExDamagedRate(), password),
    }

def dump_OpenConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OpenConditionContentType": OpenConditionContent(convert_int(excel_instance.OpenConditionContentType(), password)).name,
        "LockUI": [convert_string(excel_instance.LockUI(j), password) for j in range(excel_instance.LockUILength())],
        "ShortcutPopupPriority": convert_long(excel_instance.ShortcutPopupPriority(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUIName(j), password) for j in range(excel_instance.ShortcutUINameLength())],
        "ShortcutParam": convert_int(excel_instance.ShortcutParam(), password),
        "Scene": convert_string(excel_instance.Scene(), password),
        "HideWhenLocked": excel_instance.HideWhenLocked(),
        "AccountLevel": convert_long(excel_instance.AccountLevel(), password),
        "ScenarioModeId": convert_long(excel_instance.ScenarioModeId(), password),
        "CampaignStageId": convert_long(excel_instance.CampaignStageId(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "OpenDayOfWeek": WeekDay(convert_int(excel_instance.OpenDayOfWeek(), password)).name,
        "OpenHour": convert_long(excel_instance.OpenHour(), password),
        "CloseDayOfWeek": WeekDay(convert_int(excel_instance.CloseDayOfWeek(), password)).name,
        "CloseHour": convert_long(excel_instance.CloseHour(), password),
        "OpenedCafeId": convert_long(excel_instance.OpenedCafeId(), password),
        "CafeIdforCafeRank": convert_long(excel_instance.CafeIdforCafeRank(), password),
        "CafeRank": convert_long(excel_instance.CafeRank(), password),
        "ContentsOpenShow": excel_instance.ContentsOpenShow(),
        "ContentsOpenShortcutUI": convert_string(excel_instance.ContentsOpenShortcutUI(), password),
    }

def dump_OperatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "OperatorCondition": OperatorCondition(convert_int(excel_instance.OperatorCondition(), password)).name,
        "OutputSequence": convert_int(excel_instance.OutputSequence(), password),
        "RandomWeight": convert_int(excel_instance.RandomWeight(), password),
        "OutputDelay": convert_int(excel_instance.OutputDelay(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "OperatorOutputPriority": convert_int(excel_instance.OperatorOutputPriority(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "TextLocalizeKey": convert_string(excel_instance.TextLocalizeKey(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "OperatorWaitQueue": excel_instance.OperatorWaitQueue(),
    }

def dump_ParcelAutoSynthExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RequireParcelType": ParcelType(convert_int(excel_instance.RequireParcelType(), password)).name,
        "RequireParcelId": convert_long(excel_instance.RequireParcelId(), password),
        "RequireParcelAmount": convert_long(excel_instance.RequireParcelAmount(), password),
        "SynthStartAmount": convert_long(excel_instance.SynthStartAmount(), password),
        "SynthEndAmount": convert_long(excel_instance.SynthEndAmount(), password),
        "SynthMaxItem": excel_instance.SynthMaxItem(),
        "ResultParcelType": ParcelType(convert_int(excel_instance.ResultParcelType(), password)).name,
        "ResultParcelId": convert_long(excel_instance.ResultParcelId(), password),
        "ResultParcelAmount": convert_long(excel_instance.ResultParcelAmount(), password),
    }

def dump_PickupDuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ShopCategoryType": ShopCategoryType(convert_int(excel_instance.ShopCategoryType(), password)).name,
        "ShopId": convert_long(excel_instance.ShopId(), password),
        "PickupCharacterId": convert_long(excel_instance.PickupCharacterId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
    }

def dump_PossessionCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "DefaultParcelType": ParcelType(convert_int(excel_instance.DefaultParcelType(), password)).name,
        "DefaultParcelId": convert_long(excel_instance.DefaultParcelId(), password),
        "DefaultParcelAmount": convert_int(excel_instance.DefaultParcelAmount(), password),
        "ReplaceParcelType": ParcelType(convert_int(excel_instance.ReplaceParcelType(), password)).name,
        "ReplaceParcelId": convert_long(excel_instance.ReplaceParcelId(), password),
        "ReplaceParcelAmount": convert_int(excel_instance.ReplaceParcelAmount(), password),
    }

def dump_PresetCharacterGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PresetCharacterGroupId": convert_long(excel_instance.PresetCharacterGroupId(), password),
        "GetPresetType": convert_string(excel_instance.GetPresetType(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "FavorRank": convert_int(excel_instance.FavorRank(), password),
        "StarGrade": convert_int(excel_instance.StarGrade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevel(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevel(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevel(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevel(), password),
        "EquipSlot01": excel_instance.EquipSlot01(),
        "EquipSlotTier01": convert_int(excel_instance.EquipSlotTier01(), password),
        "EquipSlotLevel01": convert_int(excel_instance.EquipSlotLevel01(), password),
        "EquipSlot02": excel_instance.EquipSlot02(),
        "EquipSlotTier02": convert_int(excel_instance.EquipSlotTier02(), password),
        "EquipSlotLevel02": convert_int(excel_instance.EquipSlotLevel02(), password),
        "EquipSlot03": excel_instance.EquipSlot03(),
        "EquipSlotTier03": convert_int(excel_instance.EquipSlotTier03(), password),
        "EquipSlotLevel03": convert_int(excel_instance.EquipSlotLevel03(), password),
        "EquipCharacterWeapon": excel_instance.EquipCharacterWeapon(),
        "EquipCharacterWeaponTier": convert_int(excel_instance.EquipCharacterWeaponTier(), password),
        "EquipCharacterWeaponLevel": convert_int(excel_instance.EquipCharacterWeaponLevel(), password),
        "EquipCharacterGear": excel_instance.EquipCharacterGear(),
        "EquipCharacterGearTier": convert_int(excel_instance.EquipCharacterGearTier(), password),
        "EquipCharacterGearLevel": convert_int(excel_instance.EquipCharacterGearLevel(), password),
        "PotentialType01": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType01(), password)).name,
        "PotentialLevel01": convert_int(excel_instance.PotentialLevel01(), password),
        "PotentialType02": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType02(), password)).name,
        "PotentialLevel02": convert_int(excel_instance.PotentialLevel02(), password),
        "PotentialType03": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType03(), password)).name,
        "PotentialLevel03": convert_int(excel_instance.PotentialLevel03(), password),
    }

def dump_PresetCharacterGroupSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_long(excel_instance.CharacterId(), password),
        "ArenaSimulatorFixed": excel_instance.ArenaSimulatorFixed(),
        "PresetType": [convert_string(excel_instance.PresetType(j), password) for j in range(excel_instance.PresetTypeLength())],
    }

def dump_PresetParcelsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_long(excel_instance.ParcelId(), password),
        "PresetGroupId": convert_long(excel_instance.PresetGroupId(), password),
        "ParcelAmount": convert_long(excel_instance.ParcelAmount(), password),
    }

def dump_ProductExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreType(), password)).name,
        "Price": convert_long(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "PurchasePeriodType": PurchasePeriodType(convert_int(excel_instance.PurchasePeriodType(), password)).name,
        "PurchasePeriodLimit": convert_long(excel_instance.PurchasePeriodLimit(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_long(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_ProductMonthlyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreType(), password)).name,
        "Price": convert_long(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "ProductTagType": ProductTagType(convert_int(excel_instance.ProductTagType(), password)).name,
        "MonthlyDays": convert_long(excel_instance.MonthlyDays(), password),
        "UseMonthlyProductCheck": excel_instance.UseMonthlyProductCheck(),
        "PurchaseCountLimit": convert_long(excel_instance.PurchaseCountLimit(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelType(j), password)).name for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_long(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_long(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
        "EnterCostReduceGroupId": convert_long(excel_instance.EnterCostReduceGroupId(), password),
        "DailyParcelType": [ParcelType(convert_int(excel_instance.DailyParcelType(j), password)).name for j in range(excel_instance.DailyParcelTypeLength())],
        "DailyParcelId": [convert_long(excel_instance.DailyParcelId(j), password) for j in range(excel_instance.DailyParcelIdLength())],
        "DailyParcelAmount": [convert_long(excel_instance.DailyParcelAmount(j), password) for j in range(excel_instance.DailyParcelAmountLength())],
    }

def dump_ScenarioBGEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "Effect": convert_string(excel_instance.Effect(), password),
        "Effect2": convert_string(excel_instance.Effect2(), password),
        "Scroll": ScenarioBGScroll(convert_int(excel_instance.Scroll(), password)).name,
        "ScrollTime": convert_long(excel_instance.ScrollTime(), password),
        "ScrollFrom": convert_long(excel_instance.ScrollFrom(), password),
        "ScrollTo": convert_long(excel_instance.ScrollTo(), password),
    }

def dump_ScenarioBGNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "BGFileName": convert_string(excel_instance.BGFileName(), password),
        "BGType": ScenarioBGType(convert_int(excel_instance.BGType(), password)).name,
        "AnimationRoot": convert_string(excel_instance.AnimationRoot(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "SpineScale": convert_float(excel_instance.SpineScale(), password),
        "SpineLocalPosX": convert_int(excel_instance.SpineLocalPosX(), password),
        "SpineLocalPosY": convert_int(excel_instance.SpineLocalPosY(), password),
    }

def dump_ScenarioCharacterEmotionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EmoticonName": convert_string(excel_instance.EmoticonName(), password),
        "Name": convert_uint(excel_instance.Name(), password),
    }

def dump_ScenarioCharacterNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterName": convert_uint(excel_instance.CharacterName(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "NameKR": convert_string(excel_instance.NameKR(), password),
        "NicknameKR": convert_string(excel_instance.NicknameKR(), password),
        "NameJP": convert_string(excel_instance.NameJP(), password),
        "NicknameJP": convert_string(excel_instance.NicknameJP(), password),
        "Shape": ScenarioCharacterShapes(convert_int(excel_instance.Shape(), password)).name,
        "SpinePrefabName": convert_string(excel_instance.SpinePrefabName(), password),
        "SmallPortrait": convert_string(excel_instance.SmallPortrait(), password),
    }

def dump_ScenarioCharacterSituationSetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "Face": convert_string(excel_instance.Face(), password),
        "Behavior": convert_string(excel_instance.Behavior(), password),
        "Action": convert_string(excel_instance.Action(), password),
        "Shape": convert_string(excel_instance.Shape(), password),
        "Effect": convert_uint(excel_instance.Effect(), password),
        "Emotion": convert_uint(excel_instance.Emotion(), password),
    }

def dump_ScenarioContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionType(), password)).name,
        "UnlockConditionParameter": [convert_long(excel_instance.UnlockConditionParameter(j), password) for j in range(excel_instance.UnlockConditionParameterLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "UnlockConditionCount": convert_long(excel_instance.UnlockConditionCount(), password),
        "IsObject": excel_instance.IsObject(),
        "IsHorizon": excel_instance.IsHorizon(),
        "EmblemResource": convert_string(excel_instance.EmblemResource(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResource(), password),
        "FullResource": convert_string(excel_instance.FullResource(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeId(), password),
    }

def dump_ScenarioEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EffectName": convert_string(excel_instance.EffectName(), password),
        "Name": convert_uint(excel_instance.Name(), password),
    }

def dump_ScenarioModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_long(excel_instance.ModeId(), password),
        "ModeType": ScenarioModeTypes(convert_int(excel_instance.ModeType(), password)).name,
        "SubType": ScenarioModeSubTypes(convert_int(excel_instance.SubType(), password)).name,
        "VolumeId": convert_long(excel_instance.VolumeId(), password),
        "ChapterId": convert_long(excel_instance.ChapterId(), password),
        "EpisodeId": convert_long(excel_instance.EpisodeId(), password),
        "ExposedTime": convert_string(excel_instance.ExposedTime(), password),
        "Hide": excel_instance.Hide(),
        "Open": excel_instance.Open(),
        "IsContinue": excel_instance.IsContinue(),
        "EpisodeContinueModeId": convert_long(excel_instance.EpisodeContinueModeId(), password),
        "FrontScenarioGroupId": [convert_long(excel_instance.FrontScenarioGroupId(j), password) for j in range(excel_instance.FrontScenarioGroupIdLength())],
        "StrategyId": convert_long(excel_instance.StrategyId(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "IsDefeatBattle": excel_instance.IsDefeatBattle(),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "BackScenarioGroupId": [convert_long(excel_instance.BackScenarioGroupId(j), password) for j in range(excel_instance.BackScenarioGroupIdLength())],
        "ClearedModeId": [convert_long(excel_instance.ClearedModeId(j), password) for j in range(excel_instance.ClearedModeIdLength())],
        "ScenarioModeRewardId": convert_long(excel_instance.ScenarioModeRewardId(), password),
        "IsScenarioSpecialReward": excel_instance.IsScenarioSpecialReward(),
        "AccountLevelLimit": convert_long(excel_instance.AccountLevelLimit(), password),
        "ClearedStageId": convert_long(excel_instance.ClearedStageId(), password),
        "NeedClub": Club(convert_int(excel_instance.NeedClub(), password)).name,
        "NeedClubStudentCount": convert_int(excel_instance.NeedClubStudentCount(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "EventContentCondition": convert_long(excel_instance.EventContentCondition(), password),
        "EventContentConditionGroup": convert_long(excel_instance.EventContentConditionGroup(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevel(), password),
        "EventIconParcelPath": convert_string(excel_instance.EventIconParcelPath(), password),
        "EventBannerTitle": convert_uint(excel_instance.EventBannerTitle(), password),
        "Lof": excel_instance.Lof(),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "CompleteReportEventName": convert_string(excel_instance.CompleteReportEventName(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "CollectionGroupId": convert_long(excel_instance.CollectionGroupId(), password),
    }

def dump_ScenarioModeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioModeRewardId": convert_long(excel_instance.ScenarioModeRewardId(), password),
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_ScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "ScenarioModeId": convert_long(excel_instance.ScenarioModeId(), password),
        "PriorityOrder": convert_long(excel_instance.PriorityOrder(), password),
        "PVDisplayOrder": convert_long(excel_instance.PVDisplayOrder(), password),
        "VideoId": convert_long(excel_instance.VideoId(), password),
        "BgmId": convert_long(excel_instance.BgmId(), password),
        "AudioName": convert_string(excel_instance.AudioName(), password),
        "SpinePath": convert_string(excel_instance.SpinePath(), password),
        "Ratio": convert_int(excel_instance.Ratio(), password),
        "LobbyAniPath": convert_string(excel_instance.LobbyAniPath(), password),
        "MovieCGPath": convert_string(excel_instance.MovieCGPath(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
    }

def dump_ScenarioScriptExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "SelectionGroup": convert_long(excel_instance.SelectionGroup(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "Sound": convert_string(excel_instance.Sound(), password),
        "Transition": convert_uint(excel_instance.Transition(), password),
        "BGName": convert_uint(excel_instance.BGName(), password),
        "BGEffect": convert_uint(excel_instance.BGEffect(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileName(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKr(), password),
        "TextJp": convert_string(excel_instance.TextJp(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_ScenarioTransitionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "TransitionOut": convert_string(excel_instance.TransitionOut(), password),
        "TransitionOutDuration": convert_long(excel_instance.TransitionOutDuration(), password),
        "TransitionOutResource": convert_string(excel_instance.TransitionOutResource(), password),
        "TransitionIn": convert_string(excel_instance.TransitionIn(), password),
        "TransitionInDuration": convert_long(excel_instance.TransitionInDuration(), password),
        "TransitionInResource": convert_string(excel_instance.TransitionInResource(), password),
    }

def dump_SchoolDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonType(), password)).name,
        "RewardTag": RewardTag(convert_int(excel_instance.RewardTag(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_long(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_long(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_long(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": excel_instance.IsDisplayed(),
    }

def dump_SchoolDungeonStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_long(excel_instance.StageId(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonType(), password)).name,
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_long(excel_instance.PrevStageId(), password),
        "StageEnterCostType": [ParcelType(convert_int(excel_instance.StageEnterCostType(j), password)).name for j in range(excel_instance.StageEnterCostTypeLength())],
        "StageEnterCostId": [convert_long(excel_instance.StageEnterCostId(j), password) for j in range(excel_instance.StageEnterCostIdLength())],
        "StageEnterCostAmount": [convert_long(excel_instance.StageEnterCostAmount(j), password) for j in range(excel_instance.StageEnterCostAmountLength())],
        "StageEnterCostMinimumAmount": [convert_long(excel_instance.StageEnterCostMinimumAmount(j), password) for j in range(excel_instance.StageEnterCostMinimumAmountLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoal(j), password)).name for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_long(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_long(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_long(excel_instance.PlayTimeLimitInSeconds(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_ServiceActionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ServiceActionType": ServiceActionType(convert_int(excel_instance.ServiceActionType(), password)).name,
        "IsLegacy": excel_instance.IsLegacy(),
        "GoodsId": convert_long(excel_instance.GoodsId(), password),
    }

def dump_ShopCashExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CashProductId": convert_long(excel_instance.CashProductId(), password),
        "PackageType": PurchaseSourceType(convert_int(excel_instance.PackageType(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "RenewalDisplayOrder": convert_long(excel_instance.RenewalDisplayOrder(), password),
        "CategoryType": ProductCategory(convert_int(excel_instance.CategoryType(), password)).name,
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PeriodTag": excel_instance.PeriodTag(),
        "AccountLevelLimit": convert_long(excel_instance.AccountLevelLimit(), password),
        "AccountLevelHide": excel_instance.AccountLevelHide(),
        "ClearMissionLimit": convert_long(excel_instance.ClearMissionLimit(), password),
        "ClearMissionHide": excel_instance.ClearMissionHide(),
        "PurchaseReportEventName": convert_string(excel_instance.PurchaseReportEventName(), password),
    }

def dump_ShopCashScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioResrouceInfoId": convert_long(excel_instance.ScenarioResrouceInfoId(), password),
        "ShopCashId": convert_long(excel_instance.ShopCashId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_ShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "IsLegacy": excel_instance.IsLegacy(),
        "GoodsId": [convert_long(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_long(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_long(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": excel_instance.RestrictBuyWhenInventoryFull(),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "ShopUpdateGroupId": convert_int(excel_instance.ShopUpdateGroupId(), password),
    }

def dump_ShopFilterClassifiedExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "ConsumeParcelType": ParcelType(convert_int(excel_instance.ConsumeParcelType(), password)).name,
        "ConsumeParcelId": convert_long(excel_instance.ConsumeParcelId(), password),
        "ShopFilterType": ShopFilterType(convert_int(excel_instance.ShopFilterType(), password)).name,
        "GoodsId": convert_long(excel_instance.GoodsId(), password),
    }

def dump_ShopFreeRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "FreeRecruitPeriodFrom": convert_string(excel_instance.FreeRecruitPeriodFrom(), password),
        "FreeRecruitPeriodTo": convert_string(excel_instance.FreeRecruitPeriodTo(), password),
        "FreeRecruitType": ShopFreeRecruitType(convert_int(excel_instance.FreeRecruitType(), password)).name,
        "FreeRecruitDecorationImagePath": convert_string(excel_instance.FreeRecruitDecorationImagePath(), password),
        "ShopRecruitId": [convert_long(excel_instance.ShopRecruitId(j), password) for j in range(excel_instance.ShopRecruitIdLength())],
    }

def dump_ShopFreeRecruitPeriodExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ShopFreeRecruitId": convert_long(excel_instance.ShopFreeRecruitId(), password),
        "ShopFreeRecruitIntervalId": convert_long(excel_instance.ShopFreeRecruitIntervalId(), password),
        "IntervalDate": convert_string(excel_instance.IntervalDate(), password),
        "FreeRecruitCount": convert_int(excel_instance.FreeRecruitCount(), password),
    }

def dump_ShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "IsRefresh": excel_instance.IsRefresh(),
        "IsSoldOutDimmed": excel_instance.IsSoldOutDimmed(),
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelType(j), password)).name for j in range(excel_instance.CostParcelTypeLength())],
        "CostParcelId": [convert_long(excel_instance.CostParcelId(j), password) for j in range(excel_instance.CostParcelIdLength())],
        "AutoRefreshCoolTime": convert_long(excel_instance.AutoRefreshCoolTime(), password),
        "RefreshAbleCount": convert_long(excel_instance.RefreshAbleCount(), password),
        "GoodsId": [convert_long(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFrom(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodTo(), password),
        "ShopProductUpdateTime": convert_string(excel_instance.ShopProductUpdateTime(), password),
        "DisplayParcelType": ParcelType(convert_int(excel_instance.DisplayParcelType(), password)).name,
        "DisplayParcelId": convert_long(excel_instance.DisplayParcelId(), password),
        "IsShopVisible": excel_instance.IsShopVisible(),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ShopUpdateDate": convert_int(excel_instance.ShopUpdateDate(), password),
        "ShopUpdateGroupId1": convert_int(excel_instance.ShopUpdateGroupId1(), password),
        "ShopUpdateGroupId2": convert_int(excel_instance.ShopUpdateGroupId2(), password),
        "ShopUpdateGroupId3": convert_int(excel_instance.ShopUpdateGroupId3(), password),
        "ShopUpdateGroupId4": convert_int(excel_instance.ShopUpdateGroupId4(), password),
        "ShopUpdateGroupId5": convert_int(excel_instance.ShopUpdateGroupId5(), password),
        "ShopUpdateGroupId6": convert_int(excel_instance.ShopUpdateGroupId6(), password),
        "ShopUpdateGroupId7": convert_int(excel_instance.ShopUpdateGroupId7(), password),
        "ShopUpdateGroupId8": convert_int(excel_instance.ShopUpdateGroupId8(), password),
        "ShopUpdateGroupId9": convert_int(excel_instance.ShopUpdateGroupId9(), password),
        "ShopUpdateGroupId10": convert_int(excel_instance.ShopUpdateGroupId10(), password),
        "ShopUpdateGroupId11": convert_int(excel_instance.ShopUpdateGroupId11(), password),
        "ShopUpdateGroupId12": convert_int(excel_instance.ShopUpdateGroupId12(), password),
    }

def dump_ShopRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "IsLegacy": excel_instance.IsLegacy(),
        "OneGachaGoodsId": convert_long(excel_instance.OneGachaGoodsId(), password),
        "TenGachaGoodsId": convert_long(excel_instance.TenGachaGoodsId(), password),
        "GoodsDevName": convert_string(excel_instance.GoodsDevName(), password),
        "DisplayTag": GachaDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "GachaBannerPath": convert_string(excel_instance.GachaBannerPath(), password),
        "VideoId": [convert_long(excel_instance.VideoId(j), password) for j in range(excel_instance.VideoIdLength())],
        "LinkedRobbyBannerId": convert_long(excel_instance.LinkedRobbyBannerId(), password),
        "InfoCharacterId": [convert_long(excel_instance.InfoCharacterId(j), password) for j in range(excel_instance.InfoCharacterIdLength())],
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "RecruitCoinId": convert_long(excel_instance.RecruitCoinId(), password),
        "RecruitSellectionShopId": convert_long(excel_instance.RecruitSellectionShopId(), password),
        "PurchaseCooltimeMin": convert_long(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_long(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "IsNewbie": excel_instance.IsNewbie(),
        "IsSelectRecruit": excel_instance.IsSelectRecruit(),
        "DirectPayInvisibleTokenId": convert_long(excel_instance.DirectPayInvisibleTokenId(), password),
        "DirectPayAndroidShopCashId": convert_long(excel_instance.DirectPayAndroidShopCashId(), password),
        "DirectPayAppleShopCashId": convert_long(excel_instance.DirectPayAppleShopCashId(), password),
    }

def dump_ShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IsLegacy": excel_instance.IsLegacy(),
        "GoodsId": convert_long(excel_instance.GoodsId(), password),
        "IsBundle": excel_instance.IsBundle(),
        "VisibleAmount": convert_long(excel_instance.VisibleAmount(), password),
        "DisplayOrder": convert_long(excel_instance.DisplayOrder(), password),
        "CategoryType": ShopCategoryType(convert_int(excel_instance.CategoryType(), password)).name,
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
    }

def dump_ShortcutTypeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "IsAscending": excel_instance.IsAscending(),
        "ContentType": [ShortcutContentType(convert_int(excel_instance.ContentType(j), password)).name for j in range(excel_instance.ContentTypeLength())],
    }

def dump_SkillAdditionalTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "AdditionalSkillGroupId": convert_string(excel_instance.AdditionalSkillGroupId(), password),
        "ShowSkillSlot": convert_string(excel_instance.ShowSkillSlot(), password),
    }

def dump_SoundUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "SoundUniqueId": convert_string(excel_instance.SoundUniqueId(), password),
        "Path": convert_string(excel_instance.Path(), password),
    }

def dump_SpineLipsyncExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
        "AnimJson": convert_string(excel_instance.AnimJson(), password),
    }

def dump_StatLevelInterpolationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_long(excel_instance.Level(), password),
        "StatTypeIndex": [convert_long(excel_instance.StatTypeIndex(j), password) for j in range(excel_instance.StatTypeIndexLength())],
    }

def dump_StickerGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Layout": convert_string(excel_instance.Layout(), password),
        "UniqueLayoutPath": convert_string(excel_instance.UniqueLayoutPath(), password),
        "StickerGroupIconpath": convert_string(excel_instance.StickerGroupIconpath(), password),
        "PageCompleteSlot": convert_long(excel_instance.PageCompleteSlot(), password),
        "PageCompleteRewardParcelType": ParcelType(convert_int(excel_instance.PageCompleteRewardParcelType(), password)).name,
        "PageCompleteRewardParcelId": convert_long(excel_instance.PageCompleteRewardParcelId(), password),
        "PageCompleteRewardAmount": convert_int(excel_instance.PageCompleteRewardAmount(), password),
        "LocalizeTitle": convert_uint(excel_instance.LocalizeTitle(), password),
        "LocalizeDescription": convert_uint(excel_instance.LocalizeDescription(), password),
        "StickerGroupCoverpath": convert_string(excel_instance.StickerGroupCoverpath(), password),
    }

def dump_StickerPageContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StickerGroupId": convert_long(excel_instance.StickerGroupId(), password),
        "StickerPageId": convert_long(excel_instance.StickerPageId(), password),
        "StickerSlot": convert_long(excel_instance.StickerSlot(), password),
        "StickerGetConditionType": StickerGetConditionType(convert_int(excel_instance.StickerGetConditionType(), password)).name,
        "StickerCheckPassType": StickerCheckPassType(convert_int(excel_instance.StickerCheckPassType(), password)).name,
        "GetStickerConditionType": GetStickerConditionType(convert_int(excel_instance.GetStickerConditionType(), password)).name,
        "StickerGetConditionCount": convert_long(excel_instance.StickerGetConditionCount(), password),
        "StickerGetConditionParameter": [convert_long(excel_instance.StickerGetConditionParameter(j), password) for j in range(excel_instance.StickerGetConditionParameterLength())],
        "StickerGetConditionParameterTag": [Tag(convert_int(excel_instance.StickerGetConditionParameterTag(j), password)).name for j in range(excel_instance.StickerGetConditionParameterTagLength())],
        "PackedStickerIconLocalizeEtcId": convert_uint(excel_instance.PackedStickerIconLocalizeEtcId(), password),
        "PackedStickerIconPath": convert_string(excel_instance.PackedStickerIconPath(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "StickerDetailPath": convert_string(excel_instance.StickerDetailPath(), password),
    }

def dump_StoryStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "Localize": convert_string(excel_instance.Localize(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "WhiteListId": convert_long(excel_instance.WhiteListId(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
    }

def dump_TimeAttackDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonType(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "InformationGroupID": convert_long(excel_instance.InformationGroupID(), password),
    }

def dump_TimeAttackDungeonGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonType(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "ClearDefaultPoint": convert_long(excel_instance.ClearDefaultPoint(), password),
        "ClearTimeWeightPoint": convert_long(excel_instance.ClearTimeWeightPoint(), password),
        "TimeWeightConst": convert_long(excel_instance.TimeWeightConst(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillId(j), password) for j in range(excel_instance.AllyPassiveSkillIdLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillId(j), password) for j in range(excel_instance.EnemyPassiveSkillIdLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevel(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelLength())],
        "GeasIconPath": [convert_string(excel_instance.GeasIconPath(j), password) for j in range(excel_instance.GeasIconPathLength())],
        "GeasLocalizeEtcKey": [convert_uint(excel_instance.GeasLocalizeEtcKey(j), password) for j in range(excel_instance.GeasLocalizeEtcKeyLength())],
    }

def dump_TimeAttackDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "RewardMaxPoint": convert_long(excel_instance.RewardMaxPoint(), password),
        "RewardType": [TimeAttackDungeonRewardType(convert_int(excel_instance.RewardType(j), password)).name for j in range(excel_instance.RewardTypeLength())],
        "RewardMinPoint": [convert_long(excel_instance.RewardMinPoint(j), password) for j in range(excel_instance.RewardMinPointLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelType(j), password)).name for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_long(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelDefaultAmount": [convert_long(excel_instance.RewardParcelDefaultAmount(j), password) for j in range(excel_instance.RewardParcelDefaultAmountLength())],
        "RewardParcelMaxAmount": [convert_long(excel_instance.RewardParcelMaxAmount(j), password) for j in range(excel_instance.RewardParcelMaxAmountLength())],
    }

def dump_TimeAttackDungeonSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "UISlot": convert_long(excel_instance.UISlot(), password),
        "DungeonId": convert_long(excel_instance.DungeonId(), password),
        "DifficultyGeas": [convert_long(excel_instance.DifficultyGeas(j), password) for j in range(excel_instance.DifficultyGeasLength())],
        "TimeAttackDungeonRewardId": convert_long(excel_instance.TimeAttackDungeonRewardId(), password),
        "RoomLifeTimeInSeconds": convert_long(excel_instance.RoomLifeTimeInSeconds(), password),
    }

def dump_ToastExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "ToastType": ToastType(convert_int(excel_instance.ToastType(), password)).name,
        "MissionId": convert_uint(excel_instance.MissionId(), password),
        "TextId": convert_uint(excel_instance.TextId(), password),
        "LifeTime": convert_long(excel_instance.LifeTime(), password),
    }

def dump_TutorialCharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TalkId": convert_long(excel_instance.TalkId(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_TutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_long(excel_instance.ID(), password),
        "CompletionReportEventName": convert_string(excel_instance.CompletionReportEventName(), password),
        "CompulsoryTutorial": excel_instance.CompulsoryTutorial(),
        "DescriptionTutorial": excel_instance.DescriptionTutorial(),
        "TutorialStageId": convert_long(excel_instance.TutorialStageId(), password),
        "UIName": [convert_string(excel_instance.UIName(j), password) for j in range(excel_instance.UINameLength())],
        "TutorialParentName": [convert_string(excel_instance.TutorialParentName(j), password) for j in range(excel_instance.TutorialParentNameLength())],
    }

def dump_TutorialFailureImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Contents": TutorialFailureContentType(convert_int(excel_instance.Contents(), password)).name,
        "Type": convert_string(excel_instance.Type(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
    }

def dump_UnderCoverStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "StageNameFile": convert_string(excel_instance.StageNameFile(), password),
        "StageTryCount": convert_int(excel_instance.StageTryCount(), password),
        "ApplySkip": excel_instance.ApplySkip(),
        "SkipCount": convert_int(excel_instance.SkipCount(), password),
        "ShowClearScene": excel_instance.ShowClearScene(),
        "StageTips": convert_uint(excel_instance.StageTips(), password),
        "StageName": convert_uint(excel_instance.StageName(), password),
    }

def dump_VideoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "VideoPath": [convert_string(excel_instance.VideoPath(j), password) for j in range(excel_instance.VideoPathLength())],
        "SoundPath": [convert_string(excel_instance.SoundPath(j), password) for j in range(excel_instance.SoundPathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_VoiceCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceEvent": VoiceEvent(convert_int(excel_instance.VoiceEvent(), password)).name,
        "Rate": convert_long(excel_instance.Rate(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_VoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
    }

def dump_VoiceLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LogicEffectNameHash": convert_uint(excel_instance.LogicEffectNameHash(), password),
        "Self": excel_instance.Self(),
        "Priority": convert_int(excel_instance.Priority(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_VoiceRoomExceptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_long(excel_instance.CostumeUniqueId(), password),
        "LinkedCharacterVoicePrintType": CVPrintType(convert_int(excel_instance.LinkedCharacterVoicePrintType(), password)).name,
        "LinkedCostumeUniqueId": convert_long(excel_instance.LinkedCostumeUniqueId(), password),
    }

def dump_VoiceSpineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_VoiceTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [Nation(convert_int(excel_instance.Nation(j), password)).name for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_WorldRaidBossGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "WorldRaidBossGroupId": convert_long(excel_instance.WorldRaidBossGroupId(), password),
        "WorldBossName": convert_string(excel_instance.WorldBossName(), password),
        "WorldBossPopupPortrait": convert_string(excel_instance.WorldBossPopupPortrait(), password),
        "WorldBossPopupBG": convert_string(excel_instance.WorldBossPopupBG(), password),
        "WorldBossParcelPortrait": convert_string(excel_instance.WorldBossParcelPortrait(), password),
        "WorldBossListParcel": convert_string(excel_instance.WorldBossListParcel(), password),
        "WorldBossHP": convert_long(excel_instance.WorldBossHP(), password),
        "UIHideBeforeSpawn": excel_instance.UIHideBeforeSpawn(),
        "HideAnotherBossKilled": excel_instance.HideAnotherBossKilled(),
        "WorldBossClearRewardGroupId": convert_long(excel_instance.WorldBossClearRewardGroupId(), password),
        "AnotherBossKilled": [convert_long(excel_instance.AnotherBossKilled(j), password) for j in range(excel_instance.AnotherBossKilledLength())],
        "EchelonConstraintGroupId": convert_long(excel_instance.EchelonConstraintGroupId(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawn(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKill(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattle(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamaged(), password),
        "BossGroupOpenCondition": convert_long(excel_instance.BossGroupOpenCondition(), password),
    }

def dump_WorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "LockUI": [convert_string(excel_instance.LockUI(j), password) for j in range(excel_instance.LockUILength())],
        "HideWhenLocked": excel_instance.HideWhenLocked(),
        "AccountLevel": convert_long(excel_instance.AccountLevel(), password),
        "ScenarioModeId": [convert_long(excel_instance.ScenarioModeId(j), password) for j in range(excel_instance.ScenarioModeIdLength())],
        "CampaignStageID": [convert_long(excel_instance.CampaignStageID(j), password) for j in range(excel_instance.CampaignStageIDLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "AfterWhenDate": convert_string(excel_instance.AfterWhenDate(), password),
        "WorldRaidBossKill": [convert_long(excel_instance.WorldRaidBossKill(j), password) for j in range(excel_instance.WorldRaidBossKillLength())],
    }

def dump_WorldRaidFavorBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WorldRaidFavorRank": convert_long(excel_instance.WorldRaidFavorRank(), password),
        "WorldRaidFavorRankBonus": convert_long(excel_instance.WorldRaidFavorRankBonus(), password),
    }

def dump_WorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_long(excel_instance.SeasonId(), password),
        "EventContentId": convert_long(excel_instance.EventContentId(), password),
        "EnterTicket": CurrencyTypes(convert_int(excel_instance.EnterTicket(), password)).name,
        "WorldRaidLobbyScene": convert_string(excel_instance.WorldRaidLobbyScene(), password),
        "WorldRaidLobbyBanner": convert_string(excel_instance.WorldRaidLobbyBanner(), password),
        "WorldRaidLobbyBG": convert_string(excel_instance.WorldRaidLobbyBG(), password),
        "WorldRaidLobbyBannerShow": excel_instance.WorldRaidLobbyBannerShow(),
        "SeasonOpenCondition": convert_long(excel_instance.SeasonOpenCondition(), password),
        "WorldRaidLobbyEnterScenario": convert_long(excel_instance.WorldRaidLobbyEnterScenario(), password),
        "CanPlayNotSeasonTime": excel_instance.CanPlayNotSeasonTime(),
        "WorldRaidUniqueThemeLobbyUI": excel_instance.WorldRaidUniqueThemeLobbyUI(),
        "WorldRaidUniqueThemeName": convert_string(excel_instance.WorldRaidUniqueThemeName(), password),
        "CanWorldRaidGemEnter": excel_instance.CanWorldRaidGemEnter(),
        "HideWorldRaidTicketUI": excel_instance.HideWorldRaidTicketUI(),
        "HideWorldRaidBossCompleteRewardUI": excel_instance.HideWorldRaidBossCompleteRewardUI(),
        "UseWorldRaidCommonToast": excel_instance.UseWorldRaidCommonToast(),
        "OpenRaidBossGroupId": [convert_long(excel_instance.OpenRaidBossGroupId(j), password) for j in range(excel_instance.OpenRaidBossGroupIdLength())],
        "BossSpawnTime": [convert_string(excel_instance.BossSpawnTime(j), password) for j in range(excel_instance.BossSpawnTimeLength())],
        "EliminateTime": [convert_string(excel_instance.EliminateTime(j), password) for j in range(excel_instance.EliminateTimeLength())],
        "ScenarioOutputConditionId": [convert_long(excel_instance.ScenarioOutputConditionId(j), password) for j in range(excel_instance.ScenarioOutputConditionIdLength())],
        "ConditionScenarioGroupid": [convert_long(excel_instance.ConditionScenarioGroupid(j), password) for j in range(excel_instance.ConditionScenarioGroupidLength())],
        "WorldRaidMapEnterOperator": convert_string(excel_instance.WorldRaidMapEnterOperator(), password),
        "UseFavorRankBuff": excel_instance.UseFavorRankBuff(),
    }

def dump_WorldRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_long(excel_instance.Id(), password),
        "UseBossIndex": excel_instance.UseBossIndex(),
        "UseBossAIPhaseSync": excel_instance.UseBossAIPhaseSync(),
        "WorldRaidBossGroupId": convert_long(excel_instance.WorldRaidBossGroupId(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_long(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_long(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "AssistCharacterLimitCount": convert_long(excel_instance.AssistCharacterLimitCount(), password),
        "WorldRaidDifficulty": WorldRaidDifficulty(convert_int(excel_instance.WorldRaidDifficulty(), password)).name,
        "DifficultyOpenCondition": excel_instance.DifficultyOpenCondition(),
        "RaidEnterAmount": convert_long(excel_instance.RaidEnterAmount(), password),
        "ReEnterAmount": convert_long(excel_instance.ReEnterAmount(), password),
        "BattleDuration": convert_long(excel_instance.BattleDuration(), password),
        "GroundId": convert_long(excel_instance.GroundId(), password),
        "RaidBattleEndRewardGroupId": convert_long(excel_instance.RaidBattleEndRewardGroupId(), password),
        "RaidRewardGroupId": convert_long(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_long(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_long(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_long(excel_instance.ClearScenarioKey(), password),
        "UseFixedEchelon": excel_instance.UseFixedEchelon(),
        "FixedEchelonId": convert_long(excel_instance.FixedEchelonId(), password),
        "IsRaidScenarioBattle": excel_instance.IsRaidScenarioBattle(),
        "ShowSkillCard": excel_instance.ShowSkillCard(),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "DamageToWorldBoss": convert_long(excel_instance.DamageToWorldBoss(), password),
        "AllyPassiveSkill": [convert_string(excel_instance.AllyPassiveSkill(j), password) for j in range(excel_instance.AllyPassiveSkillLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "SaveCurrentLocalBossHP": excel_instance.SaveCurrentLocalBossHP(),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_WorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": excel_instance.IsClearStageRewardHideInfo(),
        "ClearStageRewardProb": convert_long(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_long(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_long(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_AcademyFavorScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyFavorScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyLocationRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyLocationRankExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger1ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger1Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger2ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger2Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger3ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger3Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessangerExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessangerExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyTicketExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyTicketExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaLevelSectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaLevelSectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaNPCExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaNPCExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaSeasonCloseRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaSeasonCloseRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattleLevelFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattleLevelFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossExternalBTExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossExternalBTExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossPhaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossPhaseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BuffParticleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BuffParticleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BulletArmorDamageFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BulletArmorDamageFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeProductionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeProductionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeRankExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignChapterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignChapterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignChapterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignChapterRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStrategyObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterAcademyTagsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterAcademyTagsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterAIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterAIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterCalculationLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterCalculationLimitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterCombatSkinExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterCombatSkinExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterIllustCoordinateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterIllustCoordinateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterLevelStatFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterLevelStatFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterSkillListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterSkillListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatLimitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatsDetailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatsDetailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatsTransExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatsTransExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterTranscendenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterTranscendenceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVictoryInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVictoryInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponExpBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponExpBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClearDeckRuleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClearDeckRuleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestCalculateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestCalculateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestCameraSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestCameraSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestErosionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestErosionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestErosionUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestErosionUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestGroupBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestGroupBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestGroupBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestPlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestProgressResourceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestProgressResourceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestStepExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestStepExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestUnexpectedEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestUnexpectedEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstArenaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstArenaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstAudioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstAudioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstCombatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstCombatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstConquestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstConquestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstEventCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstEventCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMinigameRoadPuzzleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMinigameRoadPuzzleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMiniGameShootingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMiniGameShootingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMinigameTBGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMinigameTBGExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstNewbieContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstNewbieContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsFeverExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsFeverExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CostumeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CostumeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CouponStuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CouponStuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultEchelonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultEchelonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultFurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultFurnitureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultMailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultParcelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultParcelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EchelonConstraintExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EchelonConstraintExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidRankingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageLimitedRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageLimitedRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageSeasonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EmoticonSpecialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmoticonSpecialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentArchiveBannerOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentArchiveBannerOffsetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBuffGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBuffGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCardShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCardShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentChangeScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentChangeScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCharacterBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCharacterBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCurrencyItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCurrencyItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDebuffRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDebuffRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceNodeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceProbExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceProbExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceTotalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaModifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaModifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLobbyMenuExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLobbyMenuExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLocationRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLocationRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMeetupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMeetupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMeetupInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMeetupInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMiniEventShortCutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMiniEventShortCutExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMiniEventTokenExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMiniEventTokenExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentPlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopRefreshExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpecialOperationsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpecialOperationsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpineDialogOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpineDialogOffsetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageTotalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentZoneVisitRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneVisitRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldContentStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldContentStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldCurtainCallFreeModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldCurtainCallFreeModeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldDateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldDateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldEvidenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldEvidenceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldKeywordExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldKeywordExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldQuestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldQuestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSceneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSceneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldStoryStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldStoryStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldTutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldTutorialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldWorldMapZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldWorldMapZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FloaterCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FloaterCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureTemplateElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureTemplateElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureTemplateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftNodeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftNodeGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftNodeGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftOpenTagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftOpenTagExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_HpBarAbbreviationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_HpBarAbbreviationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationStrategyObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KnockBackExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KnockBackExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LogicEffectCommonVisualExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LogicEffectCommonVisualExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameAudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameAudioAnimatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGamePlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGamePlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRhythmBgmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRhythmBgmExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRhythmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRhythmExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingGeasExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGDiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGDiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterOptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterOptionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGThemaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGThemaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameTBGThemaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameTBGThemaRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_NormalSkillTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_NormalSkillTemplateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleFireLineCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleFireLineCheckExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PersonalityExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PersonalityExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProtocolSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProtocolSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidRankingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageSeasonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeCraftExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeCraftExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeIngredientExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeIngredientExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeSelectionAutoUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeSelectionAutoUseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeSelectionGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioReplayExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioReplayExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptField1ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptField1Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShiftingCraftRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShiftingCraftRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpecialLobbyIllustExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpecialLobbyIllustExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StrategyObjectBuffDefineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StrategyObjectBuffDefineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StringTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StringTestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SystemMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SystemMailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticalSupportSystemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticalSupportSystemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticArenaSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticArenaSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticDamageSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticDamageSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticEntityEffectFilterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticEntityEffectFilterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSkipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSkipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticTimeAttackSimulatorConfigExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticTimeAttackSimulatorConfigExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TagExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TerrainAdaptationFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TerrainAdaptationFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TranscendenceRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TranscendenceRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TrophyCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TrophyCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonFindGiftRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonFindGiftRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonGroupBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonOpenScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonOpenScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AccountLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AccountLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AssistEchelonTypeConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AssistEchelonTypeConvertExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AttendanceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AttendanceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AttendanceRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AttendanceRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AudioAnimatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMRaidExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMRaidExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMUIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CameraExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CameraExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogSubtitleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVoiceSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceSubtitleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CheatCodeListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CheatCodeListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanAssistSlotExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanAssistSlotExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanChattingEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanChattingEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CombatEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CombatEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentEnterCostReduceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentEnterCostReduceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsShortcutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsShortcutExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CurrencyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CurrencyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DuplicateBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EmblemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmblemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentNotifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentNotifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureCellRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureCellRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureRoundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FarmingDungeonLocationManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FarmingDungeonLocationManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FavorLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FavorLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FavorLevelRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FavorLevelRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedEchelonSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedEchelonSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FormationLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FormationLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaElementRecursiveExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaElementRecursiveExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GoodsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GoodsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundModuleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundModuleRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionOpenStageConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionOpenStageConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_IdCardBackgroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_IdCardBackgroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LoadingImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LoadingImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCodeInBuildExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCodeInBuildExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeErrorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeErrorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeEtcExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeEtcExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeSkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MemoryLobbyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MemoryLobbyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MessagePopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MessagePopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseCharacterBanExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseCharacterBanExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseFixedStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseFixedStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamCollectionScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamCollectionScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamDailyPointExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamDailyPointExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamEndingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamEndingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamEndingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamEndingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamParameterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamParameterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamReplayScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamReplayScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamScheduleResultExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamScheduleResultExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamTimelineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameDreamVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameDreamVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleAdditionalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleMapTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleMapTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleRailSetRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleRailTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleRailTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleRoadRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleRoadRoundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MissionEmergencyCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionEmergencyCompleteExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidStatChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidStatChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_OpenConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_OpenConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_OperatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_OperatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ParcelAutoSynthExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ParcelAutoSynthExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PickupDuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PickupDuplicateBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PossessionCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PossessionCheckExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetCharacterGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetCharacterGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetCharacterGroupSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetCharacterGroupSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetParcelsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetParcelsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductMonthlyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductMonthlyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGNameExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterEmotionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterEmotionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterNameExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterSituationSetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterSituationSetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioContentCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioModeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioModeRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioModeRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioResourceInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioTransitionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioTransitionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SchoolDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SchoolDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SchoolDungeonStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SchoolDungeonStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ServiceActionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ServiceActionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopCashExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopCashExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopCashScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopCashScenarioResourceInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFilterClassifiedExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFilterClassifiedExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFreeRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFreeRecruitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFreeRecruitPeriodExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFreeRecruitPeriodExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRecruitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRefreshExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShortcutTypeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShortcutTypeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillAdditionalTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillAdditionalTooltipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SoundUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SoundUIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpineLipsyncExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpineLipsyncExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StatLevelInterpolationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StatLevelInterpolationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StickerGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StickerGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StickerPageContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StickerPageContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StoryStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StoryStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonGeasExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ToastExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ToastExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialCharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialCharacterDialogExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialFailureImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialFailureImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_UnderCoverStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_UnderCoverStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VideoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VideoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceLogicEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceLogicEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceRoomExceptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceRoomExceptionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceSpineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceSpineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceTimelineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidBossGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidFavorBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidFavorBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }
