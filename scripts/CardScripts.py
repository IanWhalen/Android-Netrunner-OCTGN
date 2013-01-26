ScriptsLocal = {
  "cards":[
    {
      "title"       : "Virus Scan",
      "guid"        : "23473bd3-f7a5-40be-8c66-7d35796b6031",
      "autoActions" : "A3B0G0T0:CustomScript"
    },
    {
      "title"       : "Accelerated Beta Test",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01055",
      "autoScripts" : "onScore:CustomScript"
    },
    {
      "title"       : "Access to Globalsec",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01052",
      "autoScripts" : "whileRezzed:Gain1Base Link"
    },
    {
      "title"       : "Account Siphon",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01018",
      "autoScripts" : "onPlay:RunHQ||atSuccessfulRun:Lose5Credits-ofOpponent-isOptional-isAlternativeRunResult$$Gain2Credits-perX$$Gain2Tags$$TrashMyself-ifSuccessfulRunHQ-isSilent"
    },
    {
      "title"       : "Adonis Campaign",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01056",
      "autoScripts" : "onRez:Put12Credits||atTurnStart:Transfer3Credits-byMe$$TrashMyself-ifEmpty"
    },
    {
      "title"       : "Aesop's Pawnshop",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01047",
      "autoActions" : "A0B0G0T2:TrashTarget-Targeted-targetMine$$Gain3Credits"
    },
    {
      "title"       : "Aggressive Negotiation",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01097"
    },
    {
      "title"       : "Aggressive Secretary",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01057",
      "autoScripts" : "onAccess:Reveal-ifInstalled",
      "autoActions" : "A0B2G0T0:Remove1Advancement-perTargetAny-isCost-onAccess$$TrashMulti-Targeted-atProgram"
    },
    {
      "title"       : "Akamatsu Mem Chip",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01038",
      "autoScripts" : "whileRezzed:Gain1MU"
    },
    {
      "title"       : "Akitaro Watanabe",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01079"
    },
    {
      "title"       : "Anonymous Tip",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01083",
      "autoScripts" : "onPlay:Draw3Cards"
    },
    {
      "title"       : "Archer",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01101",
      "autoScripts" : "onRez:ExileTarget-Targeted-atAgenda",
      "autoActions" : "A0B0G0T0:Gain2Credits-isSubroutine||A0B0G0T0:TrashTarget-Targeted-atProgram-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Archived Memories",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01058"
    },
    {
      "title"       : "Armitage Codebusting",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01053",
      "autoScripts" : "onInstall:Put12Credits",
      "autoActions" : "A1B0G0T0:Transfer2Credits$$TrashMyself-ifEmpty"
    },
    {
      "title"       : "AstroScript Pilot Program",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01081",
      "autoScripts" : "onScore:Put1Agenda",
      "autoActions" : "A0B0G0T0:Remove1Agenda-isCost$$Put1Advancement-Targeted"
    },
    {
      "title"       : "Aurora",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01025",
      "autoActions" : "A0B2G0T0:SimplyAnnounce{break barrier subroutine}||A0B2G0T0:Put3PlusOne"
    },
    {
      "title"       : "Bank Job",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01029",
      "autoScripts" : "onInstall:Put8Credits||atSuccessfulRun:RequestInt-isOptional-isAlternativeRunResult$$Transfer1Credits-perX-ifSuccessfulRunRemote$$TrashMyself-ifEmpty"
    },
    {
      "title"       : "Battering Ram",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01042",
      "autoActions" : "A0B2G0T0:SimplyAnnounce{break up to 2 barrier subroutines}||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Beanstalk Royalties",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01098",
      "autoScripts" : "onPlay:Gain3Credits"
    },
    {
      "title"       : "Biotic Labor",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01059",
      "autoScripts" : "onPlay:Gain2Clicks"
    },
    {
      "title"       : "Breaking News",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01082",
      "autoScripts" : "onScore:Gain2Tags-onOpponent$$Put1BreakingNews||atTurnEnd:Remove1BreakingNews-isCost-byMe$$Lose2Tags-onOpponent"
    },
    {
      "title"       : "Cell Portal",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01074",
      "autoActions" : "A0B0G0T0:SimplyAnnounce{deflects the runner to the outermost piece of ice}-isSubroutine$$DerezMyself"
    },
    {
      "title"       : "Chum",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01075",
      "autoActions" : "A0B0G0T0:Put2PlusOne-Targeted-atICE-isSubroutine||A0B0G0T0:Inflict3NetDamage-onOpponent-isSubroutine"
    },
    {
      "title"       : "Closed Accounts",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01084",
      "autoScripts" : "onPlay:Lose999Credits-onOpponent-ifTagged1"
    },
    {
      "title"       : "Corporate Troubleshooter",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01065",
      "autoActions" : "A0B0G0T1:RequestInt$$Lose1Credits-perX-isCost$$Put1PlusOne-perX-Targeted-atICE-isRezzed"
    },
    {
      "title"       : "Corroder",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01007",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break barrier subroutine}||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Crash Space",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01030",
      "autoScripts" : "onInstall:Put2Credits||whileRezzed:Reduce#CostDeltag-forAll-excludeDummy-forMe||atTurnStart:Refill2Credits-excludeDummy-byMe||onDamage:Put3protectionMeatDMG-trashCost-excludeDummy",
      "autoActions" : "A0B0G0T1:CreateDummy-with3protectionMeatDMG-trashCost"
    },
    {
      "title"       : "Crypsis",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01051",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break ice subroutine}||A0B1G0T0:Put1PlusOne||A0B0G0T0:Remove1Virus||A1B0G0T0:Put1Virus"
    },
    {
      "title"       : "Cyberfeeder",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01005",
      "autoScripts" : "onInstall:Put1Credits||whileRezzed:Reduce#CostUse-forIcebreaker-forMe||whileRezzed:Reduce#CostInstall-forVirus-forMe||atTurnStart:Refill1Credits-byMe"
    },
    {
      "title"       : "Data Dealer",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01031",
      "autoActions" : "A1B0G0T0:ExileTarget-Targeted-atAgenda-targetMine$$Gain9Credits"
    },
    {
      "title"       : "Data Mine",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01076",
      "autoActions" : "A0B0G0T1:Inflict1NetDamage-onOpponent-isSubroutine"
    },
    {
      "title"       : "Data Raven",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01088",
      "autoActions" : "A0B0G0T0:Trace3-isSubroutine-traceEffects<Put1Power,None>||A0B0G0T0:Remove1Power-isCost$$Gain1Tags-onOpponent"
    },
    {
      "title"       : "Datasucker",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01008",
      "autoScripts" : "atSuccessfulRun:Put1Virus-ifSuccessfulRunHQ||atSuccessfulRun:Put1Virus-ifSuccessfulRunR&D||atSuccessfulRun:Put1Virus-ifSuccessfulRunArchives",
      "autoActions" : "A0B0G0T0:Remove1Virus-isCost$$Put1MinusOne-Targeted-atICE"
    },
    {
      "title"       : "Decoy",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01032",
      "autoActions" : "A0B0G0T1:Lose1Tags-isPenalty"
    },
    {
      "title"       : "Deja Vu",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01002"
    },
    {
      "title"       : "Demolition Run",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01003",
      "autoScripts" : "onPlay:RunGeneric"
    },
    {
      "title"       : "Desperado",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01024",
      "autoScripts" : "whileRezzed:Gain1MU||atSuccessfulRun:Gain1Credits"
    },
    {
      "title"       : "Diesel",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01034",
      "autoScripts" : "onPlay:Draw3Cards"
    },
    {
      "title"       : "Djinn",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01009",
      "autoScripts" : "onInstall:Put3DaemonMU-isSilent",
      "autoActions" : "A0B0G0T0:PossessTarget-Targeted-atProgram_and_nonIcebreaker-targetMine||A1B1G0T0:SimplyAnnounce{look through his deck for a virus program}"
    },
    {
      "title"       : "Easy Mark",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01019",
      "autoScripts" : "onPlay:Gain3Credits"
    },
    {
      "title"       : "Enigma",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01111",
      "autoActions" : "A0B0G0T0:Lose1Clicks-onOpponent-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Experiential Data",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01066"
    },
    {
      "title"       : "Femme Fatale",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01026",
      "autoScripts" : "onInstall:Put1Femme Fatale-Targeted-atICE-isOptional",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break sentry subroutine}||A0B2G0T0:Put1PlusOne||A0B0G0T0:RequestInt-Msg{How many subroutines does the target ice have?}$$Lose1Credits-perX$$SimplyAnnounce{bypass target ice}"
    },
    {
      "title"       : "Forged Activation Orders",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01020"
    },
    {
      "title"       : "Gabriel Santiago",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01017",
      "autoScripts" : "atSuccessfulRun:Gain2Credits-ifSuccessfulRunHQ-onlyOnce"
    },
    {
      "title"       : "Ghost Branch",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01087",
      "autoScripts" : "onAccess:Reveal-ifInstalled",
      "autoActions" : "A0B0G0T0:Gain1Tags-onOpponent-perMarker{Advancement}-onAccess"
    },
    {
      "title"       : "Gordian Blade",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01043",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break code gate subroutine}||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Grimoire",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01006",
      "autoScripts" : "whileRezzed:Gain2MU||whileRezzed:Put1Virus-afterCardInstall-onTriggerCard-typeVirus",
      "autoActions" : "A0B0G0T0:Put1Virus-Targeted-atProgram_and_Virus"
    },
    {
      "title"       : "Haas-Bioroid",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01054",
      "autoScripts" : "whileRezzed:Gain1Credits-perCardInstall-byMe-onlyOnce"
    },
    {
      "title"       : "Hadrian's Wall",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01102",
      "autoActions" : "A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Hedge Fund",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01110",
      "autoScripts" : "onPlay:Gain9Credits"
    },
    {
      "title"       : "Heimdall 1.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01061",
      "autoActions" : "A0B0G0T0:Inflict1BrainDamage-onOpponent-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Hostile Takeover",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01094",
      "autoScripts" : "onScore:Gain7Credits$$Gain1Bad Publicity"
    },
    {
      "title"       : "Hunter",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01112",
      "autoActions" : "A0B0G0T0:Trace3-isSubroutine-traceEffects<Gain1Tags-onOpponent,None>"
    },
    {
      "title"       : "Ice Carver",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01015"
    },
    {
      "title"       : "Ice Wall",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01103",
      "autoActions" : "A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Ichi, 1.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01062",
      "autoActions" : "A0B0G0T0:TrashTarget-Targeted-atProgram-isSubroutine||A0B0G0T0:Trace1-isSubroutine-traceEffects<Gain1Tags-onOpponent++Inflict1BrainDamage-onOpponent,None>"
    },
    {
      "title"       : "Infiltration",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01049",
      "autoScripts" : "onPlay:CustomScript"
    },
    {
      "title"       : "Inside Job",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01021",
      "autoScripts" : "onPlay:RunGeneric"
    },
    {
      "title"       : "Jinteki",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01067",
      "autoScripts" : "whileRezzed:Inflict1NetDamage-onOpponent-perAgendaScored||whileRezzed:Inflict1NetDamage-onOpponent-perAgendaLiberated"
    },
    {
      "title"       : "Kate \"Mac\" McCaffrey",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01033",
      "autoScripts" : "whileRezzed:Reduce1CostInstall-forHardware-onlyOnce-forMe||whileRezzed:Reduce1CostInstall-forProgram-onlyOnce-forMe"
    },
    {
      "title"       : "Lemuria Codecracker",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01023",
      "autoActions" : "A1B1G0T0:ExposeTarget-Targeted"
    },
    {
      "title"       : "Magnum Opus",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01044",
      "autoActions" : "A1B0G0T0:Gain2Credits"
    },
    {
      "title"       : "Matrix Analyzer",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01089",
      "autoActions" : "A0B1G0T0:Put1Advancement-Targeted||A0B0G0T0:Trace2-isSubroutine-traceEffects<Gain1Tags-onOpponent,None>"
    },
    {
      "title"       : "Medium",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01010",
      "autoScripts" : "atSuccessfulRun:Put1Virus-ifSuccessfulRunR&D"
    },
    {
      "title"       : "Melange Mining Corp",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01108",
      "autoActions" : "A3B0G0T0:Gain7Credits"
    },
    {
      "title"       : "Mimic",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01011",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break sentry subroutine}"
    },
    {
      "title"       : "Modded",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01035",
      "autoScripts" : "onPlay:Put3Credits$$Put1Click-isPriority||whileRezzed:Reduce#CostInstall-forHardware-onlyOnce-forMe||whileRezzed:Reduce#CostInstall-forProgram-onlyOnce-forMe||whileRezzed:Transfer1Click-perCardInstall"
    },
    {
      "title"       : "NBN",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01080",
      "autoScripts" : "atTurnStart:Refill2Credits-byMe||whileRezzed:Reduce#CostTrace-forAll-forMe"
    },
    {
      "title"       : "Net Shield",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01045",
      "autoScripts" : "onDamage:Lose1Credits-isCost$$Put1protectionNetDMG-onlyOnce-isPriority",
      "autoActions" : "A0B1G0T2:Put1protectionNetDMG-onlyOnce"
    },
    {
      "title"       : "Neural EMP",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01072",
      "autoScripts" : "onPlay:Inflict1NetDamage-onOpponent"
    },
    {
      "title"       : "Neural Katana",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01077",
      "autoActions" : "A0B0G0T0:Inflict3NetDamage-onOpponent-isSubroutine"
    },
    {
      "title"       : "Ninja",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01027",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break sentry subroutine}||A0B3G0T0:Put5PlusOne"
    },
    {
      "title"       : "Nisei MK II",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01068",
      "autoScripts" : "onScore:Put1Agenda",
      "autoActions" : "A0B0G0T0:Remove1Agenda-isCost$$RunEnd"
    },
    {
      "title"       : "Noise",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01001",
      "autoScripts" : "whileRezzed:Draw1Card-toTrash-ofOpponent-perCardInstall-typeVirus-byMe"
    },
    {
      "title"       : "PAD Campaign",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01109",
      "autoScripts" : "atTurnStart:Gain1Credits-byMe"
    },
    {
      "title"       : "Parasite",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01012",
      "autoScripts" : "atTurnStart:Put1Virus-byMe||Placement:ICE-isRezzed"
    },
    {
      "title"       : "Pipeline",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01046",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break sentry subroutine}||A0B2G0T0:Put1PlusOne"
    },
    {
      "title"       : "Posted Bounty",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01095",
      "autoScripts" : "onScore:Gain1Bad Publicity-isOptional$$Gain1Tags-onOpponent$$ExileMyself"
    },
    {
      "title"       : "Precognition",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01073"
    },
    {
      "title"       : "Priority Requisition",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01106",
      "autoScripts" : "onScore:RezTarget-Targeted-atICE"
    },
    {
      "title"       : "Private Security Force",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01107",
      "autoActions" : "A1B0G0T0:Inflict1MeatDamage-onOpponent-ifTagged1"
    },
    {
      "title"       : "Project Junebug",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01069",
      "autoScripts" : "onAccess:Reveal-ifInstalled",
      "autoActions" : "A0B1G0T0:Inflict2NetDamage-onOpponent-perMarker{Advancement}-onAccess"
    },
    {
      "title"       : "Psychographics",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01085",
      "autoScripts" : "onPlay:RequestInt$$Lose1Credits-perX-isCost$$Put1Advancement-perX-Targeted"
    },
    {
      "title"       : "Rabbit Hole",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01039",
      "autoScripts" : "whileRezzed:Gain1Base Link||onInstall:CustomScript"
    },
    {
      "title"       : "Red Herrings",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01091"
    },
    {
      "title"       : "Research Station",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01105",
      "autoScripts" : "whileRezzed:Gain2Hand Size"
    },
    {
      "title"       : "Rototurret",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01064",
      "autoActions" : "A0B0G0T0:TrashTarget-Targeted-atProgram-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Sacrificial Construct",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01048",
      "autoActions" : "A0B0G0T1:SimplyAnnounce{prevent an installed program or hardware from being trashed}"
    },
    {
      "title"       : "SanSan City Grid",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01092"
    },
    {
      "title"       : "Scorched Earth",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01099",
      "autoScripts" : "onPlay:Inflict4MeatDamage-onOpponent-ifTagged1"
    },
    {
      "title"       : "SEA Source",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01086",
      "autoScripts" : "onPlay:Trace3-traceEffects<Gain1Tags-onOpponent,None>"
    },
    {
      "title"       : "Security Subcontract",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01096",
      "autoActions" : "A1B0G0T0:TrashTarget-Targeted-atICE-targetMine-isRezzed$$Gain4Credits"
    },
    {
      "title"       : "Shadow",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01104",
      "autoActions" : "A0B0G0T0:Gain2Credits-isSubroutine||A0B0G0T0:Trace3-isSubroutine-traceEffects<Gain1Tags-onOpponent,None>"
    },
    {
      "title"       : "Shipment from Kaguya",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01100",
      "autoScripts" : "onPlay:Put1Advancement-Targeted"
    },
    {
      "title"       : "Shipment from Mirrormorph",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01060",
      "autoScripts" : "onPlay:Put3Click||whileRezzed:Transfer1Click-perCardInstall"
    },
    {
      "title"       : "Snare!",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01070",
      "autoScripts" : "onAccess:Reveal",
      "autoActions" : "A0B4G0T0:Inflict3NetDamage-onOpponent-onAccess$$Gain1Tags-onOpponent"
    },
    {
      "title"       : "Sneakdoor Beta",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01028",
      "autoActions" : "A1B0G0T0:RunArchives-feintToHQ"
    },
    {
      "title"       : "Special Order",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01022"
    },
    {
      "title"       : "Stimhack",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01004",
      "autoScripts" : "onPlay:RunGeneric$$Put9Credits||whileRunning:Reduce#CostAll-forAll-forMe||atJackOut:Inflict1BrainDamage-nonPreventable$$TrashMyself"
    },
    {
      "title"       : "Sure Gamble",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01050",
      "autoScripts" : "onPlay:Gain9Credits"
    },
    {
      "title"       : "The Maker's Eye",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01036",
      "autoScripts" : "onPlay:RunR&D"
    },
    {
      "title"       : "The Personal Touch",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01040",
      "autoScripts" : "onInstall:Put1PlusOnePerm-Targeted-atIcebreaker||Placement:Icebreaker"
    },
    {
      "title"       : "The Toolbox",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01041",
      "autoScripts" : "whileRezzed:Gain2MU$$Gain2Base Link||onInstall:Put2Credits||atTurnStart:Refill2Credits-byMe||whileRezzed:Reduce#CostUse-forIcebreaker-forMe"
    },
    {
      "title"       : "Tinkering",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01037",
      "autoScripts" : "onPlay:Put1Keyword:Sentry-Targeted-atICE-isSilent$$Put1Keyword:Code Gate-Targeted-atICE-isSilent$$Put1Keyword:Barrier-Targeted-atICE-isSilent$$Put1Tinkering-Targeted-atICE"
    },
    {
      "title"       : "Tollbooth",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01090",
      "autoActions" : "A0B0G0T0:UseCustomAbility||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Viktor 1.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01063",
      "autoActions" : "A0B0G0T0:Inflict1BrainDamage-onOpponent-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Wall of Static",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01113",
      "autoActions" : "A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Wall of Thorns",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01078",
      "autoActions" : "A0B0G0T0:Inflict2NetDamage-onOpponent-isSubroutine||A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Weyland Consortium",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01093",
      "autoScripts" : "whileRezzed:Gain1Credits-perCardPlay-typeTransaction-byMe"
    },
    {
      "title"       : "Wyldside",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01016",
      "autoScripts" : "atTurnStart:Draw2Cards-byMe$$Lose1Clicks"
    },
    {
      "title"       : "Wyrm",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01013",
      "autoActions" : "A0B3G0T0:SimplyAnnounce{break ice subroutine}||A0B1G0T0:Put1MinusOne-Targeted-atICE||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Yog.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01014",
      "autoActions" : "A0B0G0T0:SimplyAnnounce{break code gate subroutine}"
    },
    {
      "title"       : "Zaibatsu Loyalty",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda01071",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{prevent card from being exposed}||A0B0G0T1:SimplyAnnounce{prevent card from being exposed}"
    },
    {
      "title"       : "Ash 2X3ZB9CY",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02013",
      "autoActions" : "A0B0G0T0:Trace4-traceEffects<SimplyAnnounce{stop the runner from accessing anymore cards},None>"
    },
    {
      "title"       : "Braintrust",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02014",
      "autoScripts" : "onScore:Put1Agenda-perMarker{Advancement}-ignore3-div2||whileScored:ReduceXCostRez-forICE-perMarker{Agenda}-forMe"
    },
    {
      "title"       : "Caduceus",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02019",
      "autoActions" : "A0B0G0T0:Trace3-isSubroutine-traceEffects<Gain3Credits,None>||A0B0G0T0:Trace2-isSubroutine-traceEffects<RunEnd,None>"
    },
    {
      "title"       : "Cortez Chip",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02005",
      "autoActions" : "A0B0G0T1:Put1Cortez Chip-Targeted-onICE"
    },
    {
      "title"       : "Draco",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02020",
      "autoScripts" : "onRez:RequestInt-Msg{How many Power counters do you want to add on Draco?}$$Lose1Credits-perX-isCost$$Put1PlusOnePerm-perX",
      "autoActions" : "A0B0G0T0:Trace2-isSubroutine-traceEffects<Gain1Tags-onOpponent++RunEnd,None>"
    },
    {
      "title"       : "Imp",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02003",
      "autoScripts" : "onInstall:Put2Virus",
      "autoActions" : "A0B0G0T2:Remove1Virus-isCost$$SimplyAnnounce{trash an accessed card}"
    },
    {
      "title"       : "Janus 1.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02012",
      "autoActions" : "A0B0G0T0:Inflict1BrainDamage-onOpponent-isSubroutine"
    },
    {
      "title"       : "Mandatory Upgrades",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02011",
      "autoScripts" : "whileScored:Gain1Max Click||onScore:Gain1Clicks"
    },
    {
      "title"       : "Morning Star",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02004",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break any number of barrier subroutines}"
    },
    {
      "title"       : "Peacock",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02006",
      "autoActions" : "A0B2G0T0:SimplyAnnounce{break code gate subroutine}||A0B2G0T0:Put3PlusOne"
    },
    {
      "title"       : "Plascrete Carapace",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02009",
      "autoScripts" : "onInstall:Put4protectionMeatDMG"
    },
    {
      "title"       : "Project Atlas",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02018",
      "autoScripts" : "onScore:Put1Agenda-perMarker{Advancement}-ignore3",
      "autoActions" : "A0B0G0T0:Remove1Agenda-isCost$$SimplyAnnounce{Retrieve one card from R&D}"
    },
    {
      "title"       : "Restructured Datapool",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02016",
      "autoActions" : "A1B0G0T0:Trace2e-traceEffects<Gain1Tags-onOpponent,None>"
    },
    {
      "title"       : "Snowflake",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02015",
      "autoActions" : "A0B0G0T0:CustomScript"
    },
    {
      "title"       : "Spinal Modem",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02002",
      "autoScripts" : "onInstall:Put2Credits-isSilent||whileInstalled:Gain1MU||atTurnStart:Refill2Credits-byMe||whileRezzed:Reduce#CostUse-forIcebreaker-forMe||whileRunning:Inflict1BrainDamage-afterUnavoidedTrace-byMe"
    },
    {
      "title"       : "The Helpful AI",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02008",
      "autoScripts" : "whileRezzed:Gain1Base Link",
      "autoActions" : "A0B0G0T1:Put2PlusOne-Targeted-atIcebreaker"
    },
    {
      "title"       : "TMI",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02017",
      "autoScripts" : "onRez:Trace2-traceEffects<None,DerezMyself>",
      "autoActions" : "A0B0G0T0:RunEnd"
    },
    {
      "title"       : "Whizzard",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02001",
      "autoScripts" : "atTurnStart:Refill3Credits-byMe||Reduce#CostTrash-forAll-forMe"
    },
    {
      "title"       : "ZU.13 Key Master",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02007",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break code gate subroutine}||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Amazon Industrial Zone",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02038"
    },
    {
      "title"       : "Big Brother",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02035",
      "autoScripts" : "onPlay:Gain2Tags-onOpponent-ifTagged1"
    },
    {
      "title"       : "ChiLo City Grid",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02036",
      "autoActions" : "A0B0G0T0:Gain1Tags-onOpponent"
    },
    {
      "title"       : "Compromised Employee",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02025",
      "autoScripts" : "onInstall:Put1Credits-isSilent||atTurnStart:Refill1Credits||whileRezzed:Reduce#CostTrace-forAll-forMe||whileRezzed:Gain1Credits-perCardRezzed-typeICE"
    },
    {
      "title"       : "Dyson Mem Chip",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02028",
      "autoScripts" : "whileRezzed:Gain1Base Link$$Gain1MU"
    },
    {
      "title"       : "E3 Feedback Implants",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02024",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break 1 additional subroutine on the current ICE}"
    },
    {
      "title"       : "Encryption Protocol",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02029",
      "autoScripts" : "whileRezzed:Increase1CostTrash-forAll-forOpponent-ifInstalled"
    },
    {
      "title"       : "Executive Retreat",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02039",
      "autoScripts" : "onScore:Put1Agenda-isSilent$$ReshuffleHQ",
      "autoActions" : "A1B0G0T0:Remove1Agenda-isCost$$Draw5Cards"
    },
    {
      "title"       : "Fetal AI",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02032",
      "autoScripts" : "onAccess:Inflict2NetDamage-onOpponent||onLiberate:Lose2Credits-isCost-onOpponent"
    },
    {
      "title"       : "Freelancer",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02040",
      "autoScripts" : "onPlay:TrashMulti-Targeted-atResource"
    },
    {
      "title"       : "Jinteki",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02031"
    },
    {
      "title"       : "Liberated Account",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02022",
      "autoScripts" : "onInstall:Put16Credits",
      "autoActions" : "A1B0G0T0:Transfer4Credits$$TrashMyself-ifEmpty"
    },
    {
      "title"       : "Notoriety",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02026",
      "autoScripts" : "onPlay:Gain1Agenda Points$$Put1Scored-isSilent"
    },
    {
      "title"       : "Power Grid Overload",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02037",
      "autoScripts" : "onPlay:Trace2",
      "autoActions" : "A0B0G0T0:TrashTarget-Targeted-atHardware"
    },
    {
      "title"       : "Satellite Uplink",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02023",
      "autoScripts" : "onPlay:ExposeMulti-Targeted-isUnrezzed"
    },
    {
      "title"       : "Sensei",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02034",
      "autoActions" : "A0B0G0T0:RunEnd-isSubroutine"
    },
    {
      "title"       : "Sherlock 1.0",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02030",
      "autoActions" : "A0B0G0T0:Trace4||A0B0G0T0:UninstallTarget-toStack-Targeted-atProgram"
    },
    {
      "title"       : "Snowball",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02027",
      "autoScripts" : "atJackOut:Remove999Snowball",
      "autoActions" : "A0B1G0T0:SimplyAnnounce{break barrier subroutine}$$Put1Snowball||A0B1G0T0:Put1PlusOne"
    },
    {
      "title"       : "Trick of Light",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02033"
    },
    {
      "title"       : "Vamp",
      "guid"        : "bc0f047c-01b1-427f-a439-d451eda02021",
      "autoScripts" : "onPlay:RunHQ||atSuccessfulRun:RequestInt-Msg{How many credits do you want to burn?}$$Lose1Credits-perX-isCost-isOptional-isAlternativeRunResult$$Lose1Credits-perX-ofOpponent$$Gain1Tags$$TrashMyself-ifSuccessfulRunHQ"
    }
  ]
}