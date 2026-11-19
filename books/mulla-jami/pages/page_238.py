# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 238 (printed ٢٣٧)."""

PAGE_NUMBER = 238
PRINTED_PAGE = "٢٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the discussion of «إياك والأسد» and «إياك أن تحذف» from PDF p. 237.
    {"type": "matn",
     "ar": "ومعناهما: «بعد نفسك من الأسد والأسد من نفسك»، و«بعد نفسك عن حذف الأرنب» وهو ضربه بالعصا، و«بعد حذف الأرنب عن نفسك»،",
     "en": "…and their meaning is: “Keep yourself far from the lion, and the lion far from yourself,” and “Keep yourself far from striking (ḥadhf) the hare”—that is, hitting it with a stick—“and keep striking the hare far from yourself.”"},
    {"type": "matn",
     "ar": "وعلى التقديرين المحذر منه هو الأسد والحذف، فإن المراد من تبعيد الأسد أو الحذف من نفسك تحذيرها منهما، لا تحذيرهما منها.",
     "en": "On both construals the thing warned against is the lion and the striking; for what is meant by keeping the lion or the striking far from yourself is warning yourself against them, not warning them against you."},
    {"type": "matn",
     "ar": "(و«الطريق الطريق») مثال لثاني نوعيه أي: «اتق الطريق الطريق».",
     "en": "(And “The road, the road!”—al-ṭarīqa al-ṭarīqa) is an example of its second kind, that is: “Beware of the road, the road.”"},
    # REVIEW: print has a closing guillemet after «الأسد» with no opening one; transcribed as printed.
    {"type": "matn",
     "ar": "ولا يخفى[[١]] عليك أن تقدير «اتق» في أول النوعين غير صحيح؛ لأنه لا يقال: اتقيت زيدا من الأسد»،",
     "en": "It is not hidden from you that supplying “ittaqi” in the first of the two kinds is incorrect, because one does not say “I guarded (ittaqaytu) Zayd from the lion”;"},
    {"type": "matn",
     "ar": "فينبغي أن يقدر فيه مثل: «بعد ونح» وتقدير «بعد» في مثال النوع الثاني غير مناسب؛ لأن المعنى على الاتقاء عن الطريق لا على تبعيده،",
     "en": "so in it something like “baʿʿid” (keep far) or “naḥḥi” (remove) should be supplied. And supplying “baʿʿid” in the example of the second kind is unsuitable, because the meaning is guarding against the road, not keeping it far."},
    {"type": "matn",
     "ar": "فالصواب أن يقال[[٢]]: بتقدير «بعد أو اتق» أو نحوهما،",
     "en": "So the correct [formulation] is to say: “by supplying ‘baʿʿid’ or ‘ittaqi’ or the like of them”;"},
    {"type": "matn",
     "ar": "فيقدر مثل: «بعد» في جميع أفراد النوع الأول، وفي بعض أفراد النوع الثاني مثل: «نفسك نفسك»،",
     "en": "so something like “baʿʿid” is supplied in all instances of the first kind, and in some instances of the second kind, such as “nafsaka nafsaka” (yourself, yourself!);"},
    {"type": "matn",
     "ar": "فإن المعنى على هذا: «بعد نفسك مما يؤذيك[[٣]] كالأسد ونحوه»، ويقدر مثل: «اتق» في بعضها كالمثال المذكور.",
     "en": "for the meaning on this is: “Keep yourself far from what harms you, such as the lion and the like”; and something like “ittaqi” is supplied in some of them, as in the example mentioned."},
    {"type": "matn",
     "ar": "قيل: لفظ الأسد في «إياك والأسد» خارج عن النوعين، فينبغي ألا يكون تحذيرا. وليس كذلك، فإنه أيضا تحذير؟",
     "en": "It has been said: the word “al-asad” in “iyyāka wa-l-asada” falls outside the two kinds, so it ought not to be a warning; yet that is not so, for it too is a warning."},
    {"type": "matn",
     "ar": "وأجيب: بأنه تابع للتحذير، والتوابع خارجة عن المحدود، بدليل ذكرها فيما بعد.",
     "en": "It was answered that it is a dependent (tābiʿ) of the warning, and dependents lie outside what is defined, as shown by their being treated later."},
    # REVIEW: print reads «إيك والأسد» (for «إياك») and «وان تحذف» (bare alif); transcribed as printed.
    {"type": "matn",
     "ar": "(وتقول) في قسمي النوع الأول: (إياك من الأسد[[٤]]) كما كنت تقول: «إيك والأسد» (من أن تحذف) كما كنت تقول: «إياك وان تحذف»",
     "en": "(And you say), in the two subdivisions of the first kind: (“iyyāka mina al-asadi”—beware of the lion), just as you would say “iyyāka wa-l-asada”; (“[iyyāka] min an taḥdhifa”—beware of striking), just as you would say “iyyāka wa-an tuḥdhafa.”"},
    {"type": "matn",
     "ar": "(و) تقول في المثال الأخير: («إياك أن تحذف بتقدير «من»») أي: «إياك من أن تحذف»؛",
     "en": "(And) you say in the last example: (“iyyāka an taḥdhifa,” with “min” supplied), that is: “iyyāka min an tuḥdhafa”;"},
    {"type": "matn",
     "ar": "لأن حذف حرف الجر[[٥]] عن «أن وأن» قياس.",
     "en": "because eliding the preposition (ḥarf al-jarr) before “anna” and “an” is regular (qiyās)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إلى قوله غير صحيح. يمكن أن يضمن في اتق معنى التبعيد. ويكون التقدير: اتق مبعدا نفسك.",
     "en": "[“It is not hidden…”] up to his words “incorrect”: “ittaqi” may be made to include the sense of keeping far, the implied form being: “Beware, keeping yourself far.”"},
    {"type": "pair",
     "ar": "ولا يخفى أن في تقدير اتق مع تضمينه معنى التبعيد تأكيدا ليس في تقدير بعد.",
     "en": "It is not hidden that supplying “ittaqi” while making it include the sense of keeping far carries an emphasis not found in supplying “baʿʿid.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يمكن أن يقال: أراد تقدير اتق ونحوه.",
     "en": "It may be said: he meant supplying “ittaqi” and the like of it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه تأمل؛ لأن نفسك محذر منه لا محذر. فكيف يصح القول بأن المعنى بعد نفسك مما يؤذيك؟",
     "en": "This needs consideration, because “nafsaka” is what is warned against, not the one warned; so how can it be correct to say that the meaning is “keep yourself far from what harms you”?"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: إن اتقاء الشخص من نفسه. والتحذير منها ليس إلا لإيقاعها الشخص في ضر،",
     "en": "Unless it is said: a person’s guarding is against his own self, and warning against it is only because it casts the person into harm;"},
    {"type": "pair",
     "ar": "فالمحذر منه في الحقيقة هو الضر، وهي محذرة بالمآل، فإذا نظر إلى المآل صح هذا المعنى.",
     "en": "so what is warned against in reality is the harm, while [the self] is the one warned in the outcome; when the outcome is considered, this meaning is correct."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فتذكر المحذوف، وتحذف المعطوف؛ لأن المقام لا يسع المحذوف والمعطوف معا.",
     "en": "So you mention the elided [preposition] and elide the conjoined [wāw], because the context does not admit the elided and the conjoined together."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن «أن» حرف موصولة طويلة بصلتها، لكونها مع الجملة التي بعدها في تأويل اسم،",
     "en": "Because “an” is a relative particle lengthened by its relative clause, since together with the sentence after it it is interpreted as a noun;"},
    {"type": "pair",
     "ar": "فلما طال لفظ «ما» هو في الحقيقة اسم واحد، أجازوا فيه التخفيف قياسا بحذف حرف الجر.",
     "en": "so when the wording of what is in reality a single noun became long, they allowed lightening it, as a regular rule, by eliding the preposition."},
]
