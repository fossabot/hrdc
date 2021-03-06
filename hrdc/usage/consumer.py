from .usage import *

ConsumerControl = Usage("consumer.ConsumerControl", 0xc0001, CA)
NumericKeyPad = Usage("consumer.NumericKeyPad", 0xc0002, NAry)
ProgrammableButtons = Usage("consumer.ProgrammableButtons", 0xc0003, NAry)
Microphone = Usage("consumer.Microphone", 0xc0004, CA)
Headphone = Usage("consumer.Headphone", 0xc0005, CA)
GraphicEqualizer = Usage("consumer.GraphicEqualizer", 0xc0006, CA)
Plus10 = Usage("consumer.Plus10", 0xc0020, OSC)
Plus100 = Usage("consumer.Plus100", 0xc0021, OSC)
AmPm = Usage("consumer.AmPm", 0xc0022, OSC)
Power = Usage("consumer.Power", 0xc0030, OOC)
Reset = Usage("consumer.Reset", 0xc0031, OSC)
Sleep = Usage("consumer.Sleep", 0xc0032, OSC)
SleepAfter = Usage("consumer.SleepAfter", 0xc0033, OSC)
SleepMode = Usage("consumer.SleepMode", 0xc0034, RTC)
Illumination = Usage("consumer.Illumination", 0xc0035, OOC)
FunctionButtons = Usage("consumer.FunctionButtons", 0xc0036, NAry)
Menu = Usage("consumer.Menu", 0xc0040, OOC)
MenuPick = Usage("consumer.MenuPick", 0xc0041, OSC)
MenuUp = Usage("consumer.MenuUp", 0xc0042, OSC)
MenuDown = Usage("consumer.MenuDown", 0xc0043, OSC)
MenuLeft = Usage("consumer.MenuLeft", 0xc0044, OSC)
MenuRight = Usage("consumer.MenuRight", 0xc0045, OSC)
MenuEscape = Usage("consumer.MenuEscape", 0xc0046, OSC)
MenuValueIncrease = Usage("consumer.MenuValueIncrease", 0xc0047, OSC)
MenuValueDecrease = Usage("consumer.MenuValueDecrease", 0xc0048, OSC)
DataOnScreen = Usage("consumer.DataOnScreen", 0xc0060, OOC)
ClosedCaption = Usage("consumer.ClosedCaption", 0xc0061, OOC)
ClosedCaptionSelect = Usage("consumer.ClosedCaptionSelect", 0xc0062, OSC)
VcrTv = Usage("consumer.VcrTv", 0xc0063, OOC)
BroadcastMode = Usage("consumer.BroadcastMode", 0xc0064, OSC)
Snapshot = Usage("consumer.Snapshot", 0xc0065, OSC)
Still = Usage("consumer.Still", 0xc0066, OSC)

# HUTRR 35
PipToggle = Usage("consumer.PipToggle", 0xc0067, OSC)
PipSwap = Usage("consumer.PipSwap", 0xc0068, OSC)

# HUTRR36
Red = Usage("consumer.Red", 0xc0069, MC)
Green = Usage("consumer.Green", 0xc006a, MC)
Blue = Usage("consumer.Blue", 0xc006b, MC)
Yellow = Usage("consumer.Yellow", 0xc006c, MC)

# HUTRR37
Aspect = Usage("consumer.Aspect", 0xc006d, OSC)

# HUTRR38
ThreeDMode = Usage("consumer.ThreeDMode", 0xc006e, OSC)

# HUTRR41
DisplayBrightnessIncrement = Usage("consumer.DisplayBrightnessIncrement", 0xc006F, RTC)
DisplayBrightnessDecrement = Usage("consumer.DisplayBrightnessDecrement", 0xc0070, RTC)
DisplayBrightness = Usage("consumer.DisplayBrightness", 0xc0071, LC)
DisplayBacklightToggle = Usage("consumer.DisplayBacklightToggle", 0xc0072, OOC)
DisplaySetBrightnesstoMinimum = Usage("consumer.DisplaySetBrightnesstoMinimum", 0xc0073, OSC)
DisplaySetBrightnesstoMaximum = Usage("consumer.DisplaySetBrightnesstoMaximum", 0xc0074, OSC)
DisplaySetAutoBrightness = Usage("consumer.DisplaySetAutoBrightness", 0xc0075, OOC)

Selection = Usage("consumer.Selection", 0xc0080, NAry)
AssignSelection = Usage("consumer.AssignSelection", 0xc0081, OSC)
ModeStep = Usage("consumer.ModeStep", 0xc0082, OSC)
RecallLast = Usage("consumer.RecallLast", 0xc0083, OSC)
EnterChannel = Usage("consumer.EnterChannel", 0xc0084, OSC)
OrderMovie = Usage("consumer.OrderMovie", 0xc0085, OSC)
Channel = Usage("consumer.Channel", 0xc0086, LC)
MediaSelection = Usage("consumer.MediaSelection", 0xc0087, NAry)
MediaSelectComputer = Usage("consumer.MediaSelectComputer", 0xc0088, Sel)
MediaSelectTv = Usage("consumer.MediaSelectTv", 0xc0089, Sel)
MediaSelectWww = Usage("consumer.MediaSelectWww", 0xc008A, Sel)
MediaSelectDvd = Usage("consumer.MediaSelectDvd", 0xc008B, Sel)
MediaSelectTelephone = Usage("consumer.MediaSelectTelephone", 0xc008C, Sel)
MediaSelectProgramGuide = Usage("consumer.MediaSelectProgramGuide", 0xc008D, Sel)
MediaSelectVideoPhone = Usage("consumer.MediaSelectVideoPhone", 0xc008E, Sel)
MediaSelectGames = Usage("consumer.MediaSelectGames", 0xc008F, Sel)
MediaSelectMessages = Usage("consumer.MediaSelectMessages", 0xc0090, Sel)
MediaSelectCd = Usage("consumer.MediaSelectCd", 0xc0091, Sel)
MediaSelectVcr = Usage("consumer.MediaSelectVcr", 0xc0092, Sel)
MediaSelectTuner = Usage("consumer.MediaSelectTuner", 0xc0093, Sel)
Quit = Usage("consumer.Quit", 0xc0094, OSC)
Help = Usage("consumer.Help", 0xc0095, OOC)
MediaSelectTape = Usage("consumer.MediaSelectTape", 0xc0096, Sel)
MediaSelectCable = Usage("consumer.MediaSelectCable", 0xc0097, Sel)
MediaSelectSatellite = Usage("consumer.MediaSelectSatellite", 0xc0098, Sel)
MediaSelectSecurity = Usage("consumer.MediaSelectSecurity", 0xc0099, Sel)
MediaSelectHome = Usage("consumer.MediaSelectHome", 0xc009A, Sel)
MediaSelectCall = Usage("consumer.MediaSelectCall", 0xc009B, Sel)
ChannelIncrement = Usage("consumer.ChannelIncrement", 0xc009C, OSC)
ChannelDecrement = Usage("consumer.ChannelDecrement", 0xc009D, OSC)
MediaSelectSap = Usage("consumer.MediaSelectSap", 0xc009E, Sel)
VcrPlus = Usage("consumer.VcrPlus", 0xc00A0, OSC)
Once = Usage("consumer.Once", 0xc00A1, OSC)
Daily = Usage("consumer.Daily", 0xc00A2, OSC)
Weekly = Usage("consumer.Weekly", 0xc00A3, OSC)
Monthly = Usage("consumer.Monthly", 0xc00A4, OSC)
Play = Usage("consumer.Play", 0xc00B0, OOC)
Pause = Usage("consumer.Pause", 0xc00B1, OOC)
Record = Usage("consumer.Record", 0xc00B2, OOC)
FastForward = Usage("consumer.FastForward", 0xc00B3, OOC)
Rewind = Usage("consumer.Rewind", 0xc00B4, OOC)
ScanNextTrack = Usage("consumer.ScanNextTrack", 0xc00B5, OSC)
ScanPreviousTrack = Usage("consumer.ScanPreviousTrack", 0xc00B6, OSC)
Stop = Usage("consumer.Stop", 0xc00B7, OSC)
Eject = Usage("consumer.Eject", 0xc00B8, OSC)
RandomPlay = Usage("consumer.RandomPlay", 0xc00B9, OOC)
SelectDisc = Usage("consumer.SelectDisc", 0xc00BA, NAry)
EnterDisc = Usage("consumer.EnterDisc", 0xc00BB, MC)
Repeat = Usage("consumer.Repeat", 0xc00BC, OSC)
Tracking = Usage("consumer.Tracking", 0xc00BD, LC)
TrackNormal = Usage("consumer.TrackNormal", 0xc00BE, OSC)
SlowTracking = Usage("consumer.SlowTracking", 0xc00BF, LC)
FrameForward = Usage("consumer.FrameForward", 0xc00C0, RTC)
FrameBack = Usage("consumer.FrameBack", 0xc00C1, RTC)
Mark = Usage("consumer.Mark", 0xc00C2, OSC)
ClearMark = Usage("consumer.ClearMark", 0xc00C3, OSC)
RepeatFromMark = Usage("consumer.RepeatFromMark", 0xc00C4, OOC)
ReturnToMark = Usage("consumer.ReturnToMark", 0xc00C5, OSC)
SearchMarkForward = Usage("consumer.SearchMarkForward", 0xc00C6, OSC)
SearchMarkBackwards = Usage("consumer.SearchMarkBackwards", 0xc00C7, OSC)
CounterReset = Usage("consumer.CounterReset", 0xc00C8, OSC)
ShowCounter = Usage("consumer.ShowCounter", 0xc00C9, OSC)
TrackingIncrement = Usage("consumer.TrackingIncrement", 0xc00CA, RTC)
TrackingDecrement = Usage("consumer.TrackingDecrement", 0xc00CB, RTC)
StopEject = Usage("consumer.StopEject", 0xc00CC, OSC)
PlayPause = Usage("consumer.PlayPause", 0xc00CD, OSC)
PlaySkip = Usage("consumer.PlaySkip", 0xc00CE, OSC)

# HUTRR45
VoiceCommand = Usage("consumer.VoiceCommand", 0xc00cf, OSC)

Volume = Usage("consumer.Volume", 0xc00E0, LC)
Balance = Usage("consumer.Balance", 0xc00E1, LC)
Mute = Usage("consumer.Mute", 0xc00E2, OOC)
Bass = Usage("consumer.Bass", 0xc00E3, LC)
Treble = Usage("consumer.Treble", 0xc00E4, LC)
BassBoost = Usage("consumer.BassBoost", 0xc00E5, OOC)
SurroundMode = Usage("consumer.SurroundMode", 0xc00E6, OSC)
Loudness = Usage("consumer.Loudness", 0xc00E7, OOC)
Mpx = Usage("consumer.Mpx", 0xc00E8, OOC)
VolumeIncrement = Usage("consumer.VolumeIncrement", 0xc00E9, RTC)
VolumeDecrement = Usage("consumer.VolumeDecrement", 0xc00EA, RTC)
SpeedSelect = Usage("consumer.SpeedSelect", 0xc00F0, OSC)
PlaybackSpeed = Usage("consumer.PlaybackSpeed", 0xc00F1, NAry)
StandardPlay = Usage("consumer.StandardPlay", 0xc00F2, Sel)
LongPlay = Usage("consumer.LongPlay", 0xc00F3, Sel)
ExtendedPlay = Usage("consumer.ExtendedPlay", 0xc00F4, Sel)
Slow = Usage("consumer.Slow", 0xc00F5, OSC)
FanEnable = Usage("consumer.FanEnable", 0xc0100, OOC)
FanSpeed = Usage("consumer.FanSpeed", 0xc0101, LC)
LightEnable = Usage("consumer.LightEnable", 0xc0102, OOC)
LightIlluminationLevel = Usage("consumer.LightIlluminationLevel", 0xc0103, LC)
ClimateControlEnable = Usage("consumer.ClimateControlEnable", 0xc0104, OOC)
RoomTemperature = Usage("consumer.RoomTemperature", 0xc0105, LC)
SecurityEnable = Usage("consumer.SecurityEnable", 0xc0106, OOC)
FireAlarm = Usage("consumer.FireAlarm", 0xc0107, OSC)
PoliceAlarm = Usage("consumer.PoliceAlarm", 0xc0108, OSC)
Proximity = Usage("consumer.Proximity", 0xc0109, LC)
Motion = Usage("consumer.Motion", 0xc010A, OSC)
DuressAlarm = Usage("consumer.DuressAlarm", 0xc010B, OSC)
HoldupAlarm = Usage("consumer.HoldupAlarm", 0xc010C, OSC)
MedicalAlarm = Usage("consumer.MedicalAlarm", 0xc010D, OSC)
BalanceRight = Usage("consumer.BalanceRight", 0xc0150, RTC)
BalanceLeft = Usage("consumer.BalanceLeft", 0xc0151, RTC)
BassIncrement = Usage("consumer.BassIncrement", 0xc0152, RTC)
BassDecrement = Usage("consumer.BassDecrement", 0xc0153, RTC)
TrebleIncrement = Usage("consumer.TrebleIncrement", 0xc0154, RTC)
TrebleDecrement = Usage("consumer.TrebleDecrement", 0xc0155, RTC)
SpeakerSystem = Usage("consumer.SpeakerSystem", 0xc0160, CL)
ChannelLeft = Usage("consumer.ChannelLeft", 0xc0161, CL)
ChannelRight = Usage("consumer.ChannelRight", 0xc0162, CL)
ChannelCenter = Usage("consumer.ChannelCenter", 0xc0163, CL)
ChannelFront = Usage("consumer.ChannelFront", 0xc0164, CL)
ChannelCenterFront = Usage("consumer.ChannelCenterFront", 0xc0165, CL)
ChannelSide = Usage("consumer.ChannelSide", 0xc0166, CL)
ChannelSurround = Usage("consumer.ChannelSurround", 0xc0167, CL)
ChannelLowFrequencyEnhancement = Usage("consumer.ChannelLowFrequencyEnhancement", 0xc0168, CL)
ChannelTop = Usage("consumer.ChannelTop", 0xc0169, CL)
ChannelUnknown = Usage("consumer.ChannelUnknown", 0xc016A, CL)
SubChannel = Usage("consumer.SubChannel", 0xc0170, LC)
SubChannelIncrement = Usage("consumer.SubChannelIncrement", 0xc0171, OSC)
SubChannelDecrement = Usage("consumer.SubChannelDecrement", 0xc0172, OSC)
AlternateAudioIncrement = Usage("consumer.AlternateAudioIncrement", 0xc0173, OSC)
AlternateAudioDecrement = Usage("consumer.AlternateAudioDecrement", 0xc0174, OSC)
ApplicationLaunchButtons = Usage("consumer.ApplicationLaunchButtons", 0xc0180, NAry)
AlLaunchButtonConfigurationTool = Usage("consumer.AlLaunchButtonConfigurationTool", 0xc0181, Sel)
AlProgrammableButtonConfiguration = Usage("consumer.AlProgrammableButtonConfiguration", 0xc0182, Sel)
AlConsumerControlConfiguration = Usage("consumer.AlConsumerControlConfiguration", 0xc0183, Sel)
AlWordProcessor = Usage("consumer.AlWordProcessor", 0xc0184, Sel)
AlTextEditor = Usage("consumer.AlTextEditor", 0xc0185, Sel)
AlSpreadsheet = Usage("consumer.AlSpreadsheet", 0xc0186, Sel)
AlGraphicsEditor = Usage("consumer.AlGraphicsEditor", 0xc0187, Sel)
AlPresentationApp = Usage("consumer.AlPresentationApp", 0xc0188, Sel)
AlDatabaseApp = Usage("consumer.AlDatabaseApp", 0xc0189, Sel)
AlEmailReader = Usage("consumer.AlEmailReader", 0xc018A, Sel)
AlNewsreader = Usage("consumer.AlNewsreader", 0xc018B, Sel)
AlVoicemail = Usage("consumer.AlVoicemail", 0xc018C, Sel)
AlContactsAddressBook = Usage("consumer.AlContactsAddressBook", 0xc018D, Sel)
AlCalendarSchedule = Usage("consumer.AlCalendarSchedule", 0xc018E, Sel)
AlTaskProjectManager = Usage("consumer.AlTaskProjectManager", 0xc018F, Sel)
AlLogJournalTimecard = Usage("consumer.AlLogJournalTimecard", 0xc0190, Sel)
AlCheckbookFinance = Usage("consumer.AlCheckbookFinance", 0xc0191, Sel)
AlCalculator = Usage("consumer.AlCalculator", 0xc0192, Sel)
AlAVCapturePlayback = Usage("consumer.AlAVCapturePlayback", 0xc0193, Sel)
AlLocalMachineBrowser = Usage("consumer.AlLocalMachineBrowser", 0xc0194, Sel)
AlLanWanBrowser = Usage("consumer.AlLanWanBrowser", 0xc0195, Sel)
AlInternetBrowser = Usage("consumer.AlInternetBrowser", 0xc0196, Sel)
AlRemoteNetworkingIspConnect = Usage("consumer.AlRemoteNetworkingIspConnect", 0xc0197, Sel)
AlNetworkConference = Usage("consumer.AlNetworkConference", 0xc0198, Sel)
AlNetworkChat = Usage("consumer.AlNetworkChat", 0xc0199, Sel)
AlTelephonyDialer = Usage("consumer.AlTelephonyDialer", 0xc019A, Sel)
AlLogon = Usage("consumer.AlLogon", 0xc019B, Sel)
AlLogoff = Usage("consumer.AlLogoff", 0xc019C, Sel)
AlLogonLogoff = Usage("consumer.AlLogonLogoff", 0xc019D, Sel)
AlTerminalLockScreensaver = Usage("consumer.AlTerminalLockScreensaver", 0xc019E, Sel)
AlControlPanel = Usage("consumer.AlControlPanel", 0xc019F, Sel)
AlCommandLineProcessorRun = Usage("consumer.AlCommandLineProcessorRun", 0xc01A0, Sel)
AlProcessTaskManager = Usage("consumer.AlProcessTaskManager", 0xc01A1, Sel)
AlSelectTaskApplication = Usage("consumer.AlSelectTaskApplication", 0xc01A2, Sel)
AlNextTaskApplication = Usage("consumer.AlNextTaskApplication", 0xc01A3, Sel)
AlPreviousTaskApplication = Usage("consumer.AlPreviousTaskApplication", 0xc01A4, Sel)
AlPreemptiveHaltTaskApplication = Usage("consumer.AlPreemptiveHaltTaskApplication", 0xc01A5, Sel)
AlIntegratedHelpCenter = Usage("consumer.AlIntegratedHelpCenter", 0xc01A6, Sel)
AlDocuments = Usage("consumer.AlDocuments", 0xc01A7, Sel)
AlThesaurus = Usage("consumer.AlThesaurus", 0xc01A8, Sel)
AlDictionary = Usage("consumer.AlDictionary", 0xc01A9, Sel)
AlDesktop = Usage("consumer.AlDesktop", 0xc01AA, Sel)
AlSpellCheck = Usage("consumer.AlSpellCheck", 0xc01AB, Sel)
AlGrammarCheck = Usage("consumer.AlGrammarCheck", 0xc01AC, Sel)
AlWirelessStatus = Usage("consumer.AlWirelessStatus", 0xc01AD, Sel)
AlKeyboardLayout = Usage("consumer.AlKeyboardLayout", 0xc01AE, Sel)
AlVirusProtection = Usage("consumer.AlVirusProtection", 0xc01AF, Sel)
AlEncryption = Usage("consumer.AlEncryption", 0xc01B0, Sel)
AlScreenSaver = Usage("consumer.AlScreenSaver", 0xc01B1, Sel)
AlAlarms = Usage("consumer.AlAlarms", 0xc01B2, Sel)
AlClock = Usage("consumer.AlClock", 0xc01B3, Sel)
AlFileBrowser = Usage("consumer.AlFileBrowser", 0xc01B4, Sel)
AlPowerStatus = Usage("consumer.AlPowerStatus", 0xc01B5, Sel)
AlImageBrowser = Usage("consumer.AlImageBrowser", 0xc01B6, Sel)
AlAudioBrowser = Usage("consumer.AlAudioBrowser", 0xc01B7, Sel)
AlMovieBrowser = Usage("consumer.AlMovieBrowser", 0xc01B8, Sel)
AlDigitalRightsManager = Usage("consumer.AlDigitalRightsManager", 0xc01B9, Sel)
AlDigitalWallet = Usage("consumer.AlDigitalWallet", 0xc01BA, Sel)
AlInstantMessaging = Usage("consumer.AlInstantMessaging", 0xc01BC, Sel)
AlOemFeaturesTipsTutorialBrowser = Usage("consumer.AlOemFeaturesTipsTutorialBrowser", 0xc01BD, Sel)
AlOemHelp = Usage("consumer.AlOemHelp", 0xc01BE, Sel)
AlOnlineCommunity = Usage("consumer.AlOnlineCommunity", 0xc01BF, Sel)
AlEntertainmentContentBrowser = Usage("consumer.AlEntertainmentContentBrowser", 0xc01C0, Sel)
AlOnlineShoppingBrowser = Usage("consumer.AlOnlineShoppingBrowser", 0xc01C1, Sel)
AlSmartcardInformationHelp = Usage("consumer.AlSmartcardInformationHelp", 0xc01C2, Sel)
AlMarketMonitorFinanceBrowser = Usage("consumer.AlMarketMonitorFinanceBrowser", 0xc01C3, Sel)
AlCustomizedCorporateNewsBrowser = Usage("consumer.AlCustomizedCorporateNewsBrowser", 0xc01C4, Sel)
AlOnlineActivityBrowser = Usage("consumer.AlOnlineActivityBrowser", 0xc01C5, Sel)
AlResearchSearchBrowser = Usage("consumer.AlResearchSearchBrowser", 0xc01C6, Sel)
AlAudioPlayer = Usage("consumer.AlAudioPlayer", 0xc01C7, Sel)
GenericGuiApplicationControls = Usage("consumer.GenericGuiApplicationControls", 0xc0200, NAry)
AcNew = Usage("consumer.AcNew", 0xc0201, Sel)
AcOpen = Usage("consumer.AcOpen", 0xc0202, Sel)
AcClose = Usage("consumer.AcClose", 0xc0203, Sel)
AcExit = Usage("consumer.AcExit", 0xc0204, Sel)
AcMaximize = Usage("consumer.AcMaximize", 0xc0205, Sel)
AcMinimize = Usage("consumer.AcMinimize", 0xc0206, Sel)
AcSave = Usage("consumer.AcSave", 0xc0207, Sel)
AcPrint = Usage("consumer.AcPrint", 0xc0208, Sel)
AcProperties = Usage("consumer.AcProperties", 0xc0209, Sel)
AcUndo = Usage("consumer.AcUndo", 0xc021A, Sel)
AcCopy = Usage("consumer.AcCopy", 0xc021B, Sel)
AcCut = Usage("consumer.AcCut", 0xc021C, Sel)
AcPaste = Usage("consumer.AcPaste", 0xc021D, Sel)
AcSelectAll = Usage("consumer.AcSelectAll", 0xc021E, Sel)
AcFind = Usage("consumer.AcFind", 0xc021F, Sel)
AcFindAndReplace = Usage("consumer.AcFindAndReplace", 0xc0220, Sel)
AcSearch = Usage("consumer.AcSearch", 0xc0221, Sel)
AcGoTo = Usage("consumer.AcGoTo", 0xc0222, Sel)
AcHome = Usage("consumer.AcHome", 0xc0223, Sel)
AcBack = Usage("consumer.AcBack", 0xc0224, Sel)
AcForward = Usage("consumer.AcForward", 0xc0225, Sel)
AcStop = Usage("consumer.AcStop", 0xc0226, Sel)
AcRefresh = Usage("consumer.AcRefresh", 0xc0227, Sel)
AcPreviousLink = Usage("consumer.AcPreviousLink", 0xc0228, Sel)
AcNextLink = Usage("consumer.AcNextLink", 0xc0229, Sel)
AcBookmarks = Usage("consumer.AcBookmarks", 0xc022A, Sel)
AcHistory = Usage("consumer.AcHistory", 0xc022B, Sel)
AcSubscriptions = Usage("consumer.AcSubscriptions", 0xc022C, Sel)
AcZoomIn = Usage("consumer.AcZoomIn", 0xc022D, Sel)
AcZoomOut = Usage("consumer.AcZoomOut", 0xc022E, Sel)
AcZoom = Usage("consumer.AcZoom", 0xc022F, LC)
AcFullScreenView = Usage("consumer.AcFullScreenView", 0xc0230, Sel)
AcNormalView = Usage("consumer.AcNormalView", 0xc0231, Sel)
AcViewToggle = Usage("consumer.AcViewToggle", 0xc0232, Sel)
AcScrollUp = Usage("consumer.AcScrollUp", 0xc0233, Sel)
AcScrollDown = Usage("consumer.AcScrollDown", 0xc0234, Sel)
AcScroll = Usage("consumer.AcScroll", 0xc0235, LC)
AcPanLeft = Usage("consumer.AcPanLeft", 0xc0236, Sel)
AcPanRight = Usage("consumer.AcPanRight", 0xc0237, Sel)
AcPan = Usage("consumer.AcPan", 0xc0238, LC)
AcNewWindow = Usage("consumer.AcNewWindow", 0xc0239, Sel)
AcTileHorizontally = Usage("consumer.AcTileHorizontally", 0xc023A, Sel)
AcTileVertically = Usage("consumer.AcTileVertically", 0xc023B, Sel)
AcFormat = Usage("consumer.AcFormat", 0xc023C, Sel)
AcEdit = Usage("consumer.AcEdit", 0xc023D, Sel)
AcBold = Usage("consumer.AcBold", 0xc023E, Sel)
AcItalics = Usage("consumer.AcItalics", 0xc023F, Sel)
AcUnderline = Usage("consumer.AcUnderline", 0xc0240, Sel)
AcStrikethrough = Usage("consumer.AcStrikethrough", 0xc0241, Sel)
AcSubscript = Usage("consumer.AcSubscript", 0xc0242, Sel)
AcSuperscript = Usage("consumer.AcSuperscript", 0xc0243, Sel)
AcAllCaps = Usage("consumer.AcAllCaps", 0xc0244, Sel)
AcRotate = Usage("consumer.AcRotate", 0xc0245, Sel)
AcResize = Usage("consumer.AcResize", 0xc0246, Sel)
AcFlipHorizontal = Usage("consumer.AcFlipHorizontal", 0xc0247, Sel)
AcFlipVertical = Usage("consumer.AcFlipVertical", 0xc0248, Sel)
AcMirrorHorizontal = Usage("consumer.AcMirrorHorizontal", 0xc0249, Sel)
AcMirrorVertical = Usage("consumer.AcMirrorVertical", 0xc024A, Sel)
AcFontSelect = Usage("consumer.AcFontSelect", 0xc024B, Sel)
AcFontColor = Usage("consumer.AcFontColor", 0xc024C, Sel)
AcFontSize = Usage("consumer.AcFontSize", 0xc024D, Sel)
AcJustifyLeft = Usage("consumer.AcJustifyLeft", 0xc024E, Sel)
AcJustifyCenterH = Usage("consumer.AcJustifyCenterH", 0xc024F, Sel)
AcJustifyRight = Usage("consumer.AcJustifyRight", 0xc0250, Sel)
AcJustifyBlockH = Usage("consumer.AcJustifyBlockH", 0xc0251, Sel)
AcJustifyTop = Usage("consumer.AcJustifyTop", 0xc0252, Sel)
AcJustifyCenterV = Usage("consumer.AcJustifyCenterV", 0xc0253, Sel)
AcJustifyBottom = Usage("consumer.AcJustifyBottom", 0xc0254, Sel)
AcJustifyBlockV = Usage("consumer.AcJustifyBlockV", 0xc0255, Sel)
AcIndentDecrease = Usage("consumer.AcIndentDecrease", 0xc0256, Sel)
AcIndentIncrease = Usage("consumer.AcIndentIncrease", 0xc0257, Sel)
AcNumberedList = Usage("consumer.AcNumberedList", 0xc0258, Sel)
AcRestartNumbering = Usage("consumer.AcRestartNumbering", 0xc0259, Sel)
AcBulletedList = Usage("consumer.AcBulletedList", 0xc025A, Sel)
AcPromote = Usage("consumer.AcPromote", 0xc025B, Sel)
AcDemote = Usage("consumer.AcDemote", 0xc025C, Sel)
AcYes = Usage("consumer.AcYes", 0xc025D, Sel)
AcNo = Usage("consumer.AcNo", 0xc025E, Sel)
AcCancel = Usage("consumer.AcCancel", 0xc025F, Sel)
AcCatalog = Usage("consumer.AcCatalog", 0xc0260, Sel)
AcBuyCheckout = Usage("consumer.AcBuyCheckout", 0xc0261, Sel)
AcAddToCart = Usage("consumer.AcAddToCart", 0xc0262, Sel)
AcExpand = Usage("consumer.AcExpand", 0xc0263, Sel)
AcExpandAll = Usage("consumer.AcExpandAll", 0xc0264, Sel)
AcCollapse = Usage("consumer.AcCollapse", 0xc0265, Sel)
AcCollapseAll = Usage("consumer.AcCollapseAll", 0xc0266, Sel)
AcPrintPreview = Usage("consumer.AcPrintPreview", 0xc0267, Sel)
AcPasteSpecial = Usage("consumer.AcPasteSpecial", 0xc0268, Sel)
AcInsertMode = Usage("consumer.AcInsertMode", 0xc0269, Sel)
AcDelete = Usage("consumer.AcDelete", 0xc026A, Sel)
AcLock = Usage("consumer.AcLock", 0xc026B, Sel)
AcUnlock = Usage("consumer.AcUnlock", 0xc026C, Sel)
AcProtect = Usage("consumer.AcProtect", 0xc026D, Sel)
AcUnprotect = Usage("consumer.AcUnprotect", 0xc026E, Sel)
AcAttachComment = Usage("consumer.AcAttachComment", 0xc026F, Sel)
AcDeleteComment = Usage("consumer.AcDeleteComment", 0xc0270, Sel)
AcViewComment = Usage("consumer.AcViewComment", 0xc0271, Sel)
AcSelectWord = Usage("consumer.AcSelectWord", 0xc0272, Sel)
AcSelectSentence = Usage("consumer.AcSelectSentence", 0xc0273, Sel)
AcSelectParagraph = Usage("consumer.AcSelectParagraph", 0xc0274, Sel)
AcSelectColumn = Usage("consumer.AcSelectColumn", 0xc0275, Sel)
AcSelectRow = Usage("consumer.AcSelectRow", 0xc0276, Sel)
AcSelectTable = Usage("consumer.AcSelectTable", 0xc0277, Sel)
AcSelectObject = Usage("consumer.AcSelectObject", 0xc0278, Sel)
AcRedoRepeat = Usage("consumer.AcRedoRepeat", 0xc0279, Sel)
AcSort = Usage("consumer.AcSort", 0xc027A, Sel)
AcSortAscending = Usage("consumer.AcSortAscending", 0xc027B, Sel)
AcSortDescending = Usage("consumer.AcSortDescending", 0xc027C, Sel)
AcFilter = Usage("consumer.AcFilter", 0xc027D, Sel)
AcSetClock = Usage("consumer.AcSetClock", 0xc027E, Sel)
AcViewClock = Usage("consumer.AcViewClock", 0xc027F, Sel)
AcSelectTimeZone = Usage("consumer.AcSelectTimeZone", 0xc0280, Sel)
AcEditTimeZones = Usage("consumer.AcEditTimeZones", 0xc0281, Sel)
AcSetAlarm = Usage("consumer.AcSetAlarm", 0xc0282, Sel)
AcClearAlarm = Usage("consumer.AcClearAlarm", 0xc0283, Sel)
AcSnoozeAlarm = Usage("consumer.AcSnoozeAlarm", 0xc0284, Sel)
AcResetAlarm = Usage("consumer.AcResetAlarm", 0xc0285, Sel)
AcSynchronize = Usage("consumer.AcSynchronize", 0xc0286, Sel)
AcSendReceive = Usage("consumer.AcSendReceive", 0xc0287, Sel)
AcSendTo = Usage("consumer.AcSendTo", 0xc0288, Sel)
AcReply = Usage("consumer.AcReply", 0xc0289, Sel)
AcReplyAll = Usage("consumer.AcReplyAll", 0xc028A, Sel)
AcForwardMsg = Usage("consumer.AcForwardMsg", 0xc028B, Sel)
AcSend = Usage("consumer.AcSend", 0xc028C, Sel)
AcAttachFile = Usage("consumer.AcAttachFile", 0xc028D, Sel)
AcUpload = Usage("consumer.AcUpload", 0xc028E, Sel)
AcDownload = Usage("consumer.AcDownload", 0xc028F, Sel)
AcSetBorders = Usage("consumer.AcSetBorders", 0xc0290, Sel)
AcInsertRow = Usage("consumer.AcInsertRow", 0xc0291, Sel)
AcInsertColumn = Usage("consumer.AcInsertColumn", 0xc0292, Sel)
AcInsertFile = Usage("consumer.AcInsertFile", 0xc0293, Sel)
AcInsertPicture = Usage("consumer.AcInsertPicture", 0xc0294, Sel)
AcInsertObject = Usage("consumer.AcInsertObject", 0xc0295, Sel)
AcInsertSymbol = Usage("consumer.AcInsertSymbol", 0xc0296, Sel)
AcSaveAndClose = Usage("consumer.AcSaveAndClose", 0xc0297, Sel)
AcRename = Usage("consumer.AcRename", 0xc0298, Sel)
AcMerge = Usage("consumer.AcMerge", 0xc0299, Sel)
AcSplit = Usage("consumer.AcSplit", 0xc029A, Sel)
AcDisributeHorizontally = Usage("consumer.AcDisributeHorizontally", 0xc029B, Sel)
AcDistributeVertically = Usage("consumer.AcDistributeVertically", 0xc029C, Sel)

# HUTRR42c
ExtendedKeyboardAttributesCollection = Usage("consumer.ExtendedKeyboardAttributesCollection", 0xc02C0, CL)
KeyboardFormFactor = Usage("consumer.KeyboardFormFactor", 0xc02C1, SV)
KeyboardKeyType = Usage("consumer.KeyboardKeyType", 0xc02C2, SV)
KeyboardPhysicalLayout = Usage("consumer.KeyboardPhysicalLayout", 0xc02C3, SV)
VendorSpecificKeyboardPhysicalLayout = Usage("consumer.VendorSpecificKeyboardPhysicalLayout", 0xc02C4, SV)
KeyboardIETFLanguageTagIndex = Usage("consumer.KeyboardIETFLanguageTagIndex", 0xc02C5, SV)
ImplementedKeyboardInputAssistControls = Usage("consumer.ImplementedKeyboardInputAssistControls", 0xc02C6, SV)
KeyboardInputAssistPrevious = Usage("consumer.KeyboardInputAssistPrevious", 0xc02C7, Sel)
KeyboardInputAssistNext = Usage("consumer.KeyboardInputAssistNext", 0xc02C8, Sel)
KeyboardInputAssistPreviousGroup = Usage("consumer.KeyboardInputAssistPreviousGroup", 0xc02C9, Sel)
KeyboardInputAssistNextGroup = Usage("consumer.KeyboardInputAssistNextGroup", 0xc02CA, Sel)
KeyboardInputAssistAccept = Usage("consumer.KeyboardInputAssistAccept", 0xc02CB, Sel)
KeyboardInputAssistCancel = Usage("consumer.KeyboardInputAssistCancel", 0xc02CC, Sel)
