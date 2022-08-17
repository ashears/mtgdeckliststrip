
# format mtg decklist from moxfield.com to format of printproxy.com 

def no_paren(stri):
    list = stri.split("\n")
    new_l = []
    for line in list:
        newl = line.split(" (",)
        print(newl[0])
        

li = """1 Ad Nauseam (2xm) 76
1 Altar of Dementia (mh1) 218
1 Angel's Grace (tsr) 4
1 Animate Dead (ema) 78
1 Arcane Signet (cmr) 689
1 Arid Mesa (mm3) 229
1 Badlands (3ed) 282
1 Bastion of Remembrance (iko) 73
1 Blood Artist (c17) 99
1 Blood Crypt (rna) 245
1 Bloodstained Mire (ktk) 230
1 Buried Alive (uma) 88
1 Burnt Offering (ice) 116
1 Cabal Ritual (v16) 2
1 Cavern of Souls (mm3) 232
1 Changeling Outcast (mh1) 82
1 Chrome Mox (2xm) 358
1 City of Brass (md1) 15
1 Cloudstone Curio (rav) 257
1 Command Tower (eld) 333
1 Cruel Celebrant (war) 188
1 Culling the Weak (exo) 55
1 Dance of the Dead (ice) 118
1 Dark Confidant (2xm) 81
1 Dark Ritual (sta) 26
1 Dauthi Voidwalker (mh2) 81
1 Demonic Tutor (sta) 27
1 Diabolic Intent (bbd) 141
1 Dockside Extortionist (c19) 24
1 Edgar Markov (c17) 36
1 Enlightened Tutor (j20) 2
1 Entomb (ema) 87
1 Esper Sentinel (mh2) 12
1 Faithless Looting (c19) 140
1 Fellwar Stone (c17) 210
1 Flooded Strand (ktk) 233
1 Gamble (j20) 6
1 Gemstone Caverns (tsr) 280
1 Godless Shrine (rna) 248
1 Grand Abolisher (e01) 12
1 Grim Monolith (ulg) 126
1 Imperial Seal (j16) 6
1 Indulgent Aristocrat (soi) 118
1 Insolent Neonate (soi) 168
1 Leonin Relic-Warder (c17) 65
1 Liliana's Standard Bearer (m21) 110
1 Lion's Eye Diamond (mir) 307
1 Lotus Petal (v09) 7
1 Luxury Suite (bbd) 82
1 Mana Confluence (jou) 163
1 Mana Crypt (ema) 225
1 Mana Vault (uma) 229
1 Marsh Flats (mm3) 239
1 Mox Diamond (v10) 10
1 Mox Opal (j19) 3
1 Necromancy (vis) 64
1 Oathsworn Vampire (rix) 80
1 Peer into the Abyss (m21) 360
1 Phyrexian Altar (uma) 232
1 Plateau (3ed) 284
1 Plumb the Forbidden (stx) 81
1 Polluted Delta (ktk) 239
1 Prismatic Vista (mh1) 244
1 Pyre of Heroes (khm) 370
1 Pyroblast (ss3) 5
1 Rain of Filth (usg) 151
1 Ranger-Captain of Eos (mh1) 21
1 Razaketh, the Foulblooded (hou) 73
1 Reanimate (uma) 110
1 Red Elemental Blast (a25) 147
1 Scalding Tarn (mm3) 244
1 Scrubland (3ed) 286
1 Sevinne's Reclamation (c19) 5
1 Silence (m14) 35
1 Silent Clearing (mh1) 246
1 Skullclamp (c20) 251
1 Sol Ring (c20) 252
1 Songs of the Damned (uma) 115
5 Swamp (c19) 294
1 Swords to Plowshares (sld) 110
1 Talisman of Indulgence (e01) 91
1 Underworld Breach (thb) 161
1 Universal Automaton (mh1) 235
1 Unmarked Grave (mh2) 453
1 Urborg, Tomb of Yawgmoth (m15) 248
1 Vampire Cutthroat (emn) 110
1 Vampire of the Dire Moon (m20) 120
1 Vampiric Tutor (ema) 112
1 Vault of Champions (cmr) 360
1 Verdant Catacombs (mm3) 249
1 Village Rites (sta) 35
1 Viscera Seer (c13) 99
1 Wheel of Fortune (3ed) 185
1 Windswept Heath (ktk) 248
1 Wishclaw Talisman (eld) 110
1 Wooded Foothills (ktk) 249
"""
no_paren(li)
