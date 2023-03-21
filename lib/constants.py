import re

TMNT_STRESSES = re.compile(r"1[02]1[02]1[02]1[02]")
CHARS_ONLY = re.compile("[^a-zA-Z]")

BANNED_WORDS = ("rape", "nazi", "victim", "shootings", "bombing", "bombings")
BANNED_PHRASES = ("shooting", "railway station", "rugby union",
                  "historic district", "murder of", "killing of",
                  "rugby player", ", baron ")  # parens are back, baby  r"("
PRONUNCIATION_OVERRIDES = (("HD", "10"), ("U.S.", "10"), ("Laos", "1"), ("vs.",
                                                                         "10"))
