# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 576 (printed ٥٧٥)."""

PAGE_NUMBER = 576
PRINTED_PAGE = "٥٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 575 ends «… على عكس «لا».»; this page continues the discussion of «بل».
    {"type": "matn",
     "ar": "والمعطوف عليه في حكم المسكوت عنه، فكأنه لم يحكم عليه بشيء، لا بالمجيء ولا بعدمه،",
     "en": "The term coordinated upon is treated as something about which nothing is said: it is as though nothing were predicated of it, neither coming nor its absence;"},
    {"type": "matn",
     "ar": "والإخبار الذي وقع منه لم يكن بطريق القصد[[١]]، ولهذا صرف عنه بكلمة «بل».",
     "en": "and the statement made about it was not made by way of intent; for this reason [the judgment] was diverted from it by the word “bal”."},
    {"type": "matn",
     "ar": "وأما كلمة «بل» بعد النفي نحو: «ما جاءني زيد بل عمرو»، ففيه خلاف:",
     "en": "As for the word “bal” after a negation, as in “Zayd did not come to me, but ʿAmr”, there is disagreement about it."},
    {"type": "matn",
     "ar": "فذهب بعضهم: إلى أن كلمة «بل» لصرف حكم المنفي من المعطوف عليه إلى المعطوف أي: بل ما جاءني عمرو، والمعطوف عليه في حكم المسكوت عنه[[٢]].",
     "en": "Some held that the word “bal” is for diverting the negated judgment from the term coordinated upon to the coordinated term, that is, “rather, ʿAmr did not come to me”, the term coordinated upon being treated as something about which nothing is said."},
    {"type": "matn",
     "ar": "وبعضهم: إلى أنها تثبت الحكم المنفي[[٣]] عن المعطوف عليه للمعطوف، والمعطوف عليه في حكم المسكوت عنه أو الحكم منفي عنه.",
     "en": "Others held that it affirms for the coordinated term the judgment negated of the term coordinated upon, the term coordinated upon being either treated as something about which nothing is said, or the judgment being negated of it."},
    {"type": "matn",
     "ar": "فمعنى: «ما جاءني زيد بل عمرو»: بل جاءني عمرو وزيد إما في حكم المسكوت عنه أو المجيء منفي عنه.",
     "en": "So the meaning of “Zayd did not come to me, but ʿAmr” is: rather ʿAmr came to me, while Zayd is either treated as something about which nothing is said, or coming is negated of him."},
    {"type": "matn",
     "ar": "(ولكن لازمة للنفي) أي: غير مستعملة بدونه،",
     "en": "(And “lākin” is bound to negation), that is, it is not used without it."},
    {"type": "matn",
     "ar": "فإن كانت لعطف المفرد على المفرد، فهي نقيضة «لا»، فتكون لإيجاب ما انتفى عن الأول، فتكون لازمة لنفي الحكم عن الأول، نحو: «ما قام زيد لكن عمرو» أي: قام عمرو،",
     "en": "If it coordinates a single term with a single term, it is the contrary of “lā”: it serves to affirm what was negated of the first, and so is bound to the negation of the judgment of the first, as in “Zayd did not stand, but ʿAmr”, that is, ʿAmr stood."},
    {"type": "matn",
     "ar": "وإن كانت في عطف الجملة على الجملة فهي نظيرة «بل» في مجيئها بعد النفي والإثبات،",
     "en": "If it is used to coordinate a sentence with a sentence, it is the counterpart of “bal” in coming after both negation and affirmation:"},
    {"type": "matn",
     "ar": "فبعد النفي لإثبات ما بعدها، وبعد الإثبات لنفي ما بعدها نحو: «جاءني زيد لكن عمرو لم يجيء، وما جاءني زيد لكن عمرو قد جاء»،",
     "en": "after negation it affirms what follows it, and after affirmation it negates what follows it, as in “Zayd came to me, but ʿAmr did not come” and “Zayd did not come to me, but ʿAmr has come”;"},
    {"type": "matn",
     "ar": "فعلى كل تقدير غير مستعملة بدون النفي.",
     "en": "so on every reckoning it is not used without negation."},

    {"type": "section", "ar": "[حروف التنبيه]",
     "en": "The Particles of Alerting (Ḥurūf al-Tanbīh)"},

    {"type": "matn",
     "ar": "(حروف التنبيه[[٤]]: «ألا»، و«أما»، و«ها») يصدر بها الجمل كلها حتى لا يغفل المخاطب عن شيء مما يلقى المتكلم إليه،",
     "en": "(The particles of alerting (tanbīh) are “alā”, “amā” and “hā”): whole sentences are headed by them so that the addressee does not overlook anything of what the speaker conveys to him;"},
    {"type": "matn",
     "ar": "ولهذا سميت حروف التنبيه، نحو: «ألا زيد قائم»، و«أما زيد قائم»، و«ها زيد قائم».",
     "en": "for this reason they are called the particles of alerting, as in “alā Zaydun qāʾimun” (lo, Zayd is standing), “amā Zaydun qāʾimun” and “hā Zaydun qāʾimun”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: ذكره لم يكن مهما أو كان خطأ أو عمدا أو سهوا، وليس المراد أنه وقع لا بطريق القصد.",
     "en": "That is, mentioning it was not of concern, or it was an error, whether deliberate or inadvertent; what is meant is not that it occurred without intent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فهي في النفي والإثبات على طريق واحد.",
     "en": "So in negation and affirmation it follows a single course."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كلمة «عن» متعلقة بالمنفي واللام بـ«تثبت»،",
     "en": "The word “ʿan” is attached to “al-manfī” (negated), and the lām to “tuthbitu” (affirms)."},
    {"type": "pair",
     "ar": "قالوا: ولذا لا يجوز النصب في ما زيد قائم بل قاعد أو يتعين الرفع.",
     "en": "They said: for this reason the accusative is not permissible in “mā Zaydun qāʾiman bal qāʿidun” (Zayd is not standing, but sitting), or rather the nominative is required."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر أن هذه الحروف ليس حروف المعنى، بل أصوات وضعت لغرض التنبيه،",
     "en": "The evident view is that these particles are not particles of meaning, but sounds coined for the purpose of alerting;"},
    {"type": "pair",
     "ar": "فالأليق أن تجعل من قبيل حروف الزيادة.",
     "en": "so it is more fitting that they be classed with the redundant particles (ḥurūf al-ziyāda)."},
]
