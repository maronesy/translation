# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 532 (printed ٥٣١)."""

PAGE_NUMBER = 532
PRINTED_PAGE = "٥٣١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… و«جعل يقول»، وقال» at the foot of PDF p. 531 (mid-sentence).
    {"type": "matn",
     "ar": "الله تعالى: ﴿وطفقا يخصفان﴾[[١]]،",
     "en": "…Allah, the Exalted: “and they began to sew together” (wa-ṭafiqā yakhṣifāni)."},
    {"type": "matn",
     "ar": "(و«أوشك») بمعنى: «أسرع»، عطف على «طفق»",
     "en": "(And “awshaka”), in the sense of “asraʿa” (he hastened), coordinated with “ṭafiqa”;"},
    {"type": "matn",
     "ar": "(وهي) أي: «أوشك» (مثل: «عسى» و«كاد» في الاستعمال[[٢]]) فتارة يستعمل استعمال «عسى» على وجهيه، نحو: «أوشك زيد أن يجيء» و«أوشك أن يجيء زيد»،",
     "en": "(and it), that is, “awshaka”, (is like “ʿasā” and “kāda” in usage): at times it is used as “ʿasā” is used, in both its ways, as in “awshaka Zaydun an yajīʾa” and “awshaka an yajīʾa Zaydun” (Zayd is about to come);"},
    {"type": "matn",
     "ar": "وتارة يستعمل استعمال «كاد» بدون «أن» نحو: «أوشك زيد يجيء».",
     "en": "and at times it is used as “kāda” is used, without “an”, as in “awshaka Zaydun yajīʾu”."},

    {"type": "section", "ar": "[فعل التعجب]",
     "en": "The Verb of Wonder (Fiʿl al-Taʿajjub)"},

    {"type": "matn",
     "ar": "(فعل التعجب: ما وضع لإنشاء التعجب) وفي بعض النسخ: «أفعال التعجب».",
     "en": "(The verb of wonder (fiʿl al-taʿajjub) is what was coined for the performative expression (inshāʾ) of wonder.) In some copies: “the verbs of wonder”."},
    {"type": "matn",
     "ar": "وفي أكثر النسخ: «فعلا التعجب» بصيغة التثنية،",
     "en": "In most copies: “the two verbs of wonder”, in the dual form."},
    {"type": "matn",
     "ar": "فإفراد الفعل بالنظر إلى أن التعريف للجنس، وجمعه بالنظر إلى كثرة أفراده، وتثنيته بالنظر إلى نوعي صيغته[[٣]]،",
     "en": "So the singular “verb” is in view of the definition being of the genus; its plural, in view of the multitude of its individual instances; and its dual, in view of the two kinds of its form."},
    {"type": "matn",
     "ar": "وعلى كل تقدير فالتعريف للجنس المفهوم في ضمن التثنية والجمع أيضا[[٤]]،",
     "en": "On every supposition, the definition is of the genus understood within the dual and the plural as well."},
    {"type": "matn",
     "ar": "فهو «ما وضع» أي: «فعل وضع»؛ لأن الكلام في قسم الأفعال، فلا ينتقض الحد بمثل: «لله دره فارسا» و«واها له»،",
     "en": "So it is “what was coined”, that is, “a verb that was coined”, since the discussion is in the section on verbs; hence the definition is not breached by such [expressions] as “li-llāhi darruhu fārisan” (how excellent a horseman he is!) and “wāhan lahu” (how wonderful he is!)."},
    {"type": "matn",
     "ar": "لكن ينتقض بنحو: «قاتله الله من شاعر» و«لا شل عشره»، فإنه فعل وضع لإنشاء التعجب وليس بمحض الدعاء[[٥]]،",
     "en": "But it is breached by such [expressions] as “qātalahu Allāhu min shāʿirin” (God fight him, what a poet!) and “lā shalla ʿashruhu” (may his ten [fingers] not wither!); for this is a verb coined for the performative expression of wonder, and is not pure supplication;"},
    {"type": "matn",
     "ar": "إلا أن يقال: هذه الأفعال ليست موضوعة للتعجب، بل استعملت لذلك بعد الوضع،",
     "en": "unless it is said that these verbs are not coined for wonder, but were used for it after the coinage;"},
    {"type": "matn",
     "ar": "أو المراد: ما وضع لإنشاء التعجب فحسب بحيث لا يستعمل في غيره، وما ذكر من مواد النقض فكثيرا ما يستعمل في الدعاء.",
     "en": "or that what is meant is what was coined for the performative expression of wonder alone, such that it is not used for anything else, while the instances cited as breaches are often used for supplication."},
    {"type": "matn",
     "ar": "(وله) أي: لفعل التعجب[[٦]] أو لما وضع لإنشاء التعجب (صيغتان):",
     "en": "(And it), that is, the verb of wonder, or what was coined for the performative expression of wonder, (has two forms):"},
    {"type": "matn",
     "ar": "إحداهما: صيغة الفعل الذي تضمنه تركيب (ما أفعله).",
     "en": "the first of them is the form of the verb contained in the construction (mā afʿalahu) (how … he is!);"},
    {"type": "matn",
     "ar": "(و) أخراهما: صيغة الفعل الذي تضمنه تركيب (وأفعل به) بشرط أن يكونا في هذين التركيبين.",
     "en": "(and) the other is the form of the verb contained in the construction (afʿil bihi) (how … he is!), on condition that the two be within these two constructions."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الأعراف:٢٢، سورة طه: ١٢١.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:22; Sūrat Ṭāhā 20:121."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا في المعنى. وفيه إشارة إلى أن الاستعمالين شائعان بخلاف «طفق، وكرب، وجعل، وأخذ»، فإن الشائع فيها التجريد، وإن جاءت مع «أن» على قلة.",
     "en": "Not in meaning. In it there is an indication that both usages are common, unlike “ṭafiqa, karaba, jaʿala and akhadha”, for what is common with them is the bare form [without “an”], although they occur with “an” rarely."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وللتنبيه على أن الموجود من هذا المفهوم الأعم ليس إلا النوعين.",
     "en": "And to draw attention to the fact that what exists of this more general concept is only the two kinds."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "متعلق بقوله: للجنس، أي: كما كان في تقدير الإفراد.",
     "en": "Connected with his words “of the genus”, that is, just as it was on the supposition of the singular."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «والأشل عشرة»; the matn has «لا شل عشره» (apparently «ولا شل عشره» run together). Transcribed as printed.
    {"type": "pair",
     "ar": "يمكن أن يجاب: بأن المراد ما وضع لإنشاء التعجب في نفس مصدر هذا الفعل، وقاتله الله من شاعر والأشل عشرة ليس كذلك.",
     "en": "It can be answered that what is meant is what was coined for the performative expression of wonder at the very verbal noun of this verb, and “qātalahu Allāhu min shāʿirin” and “lā shalla ʿashruhu” are not so."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كون المقصود من التعريف إجراء الأحكام يرجح الأول، وقرب المرجح مع اتحاد المعرف، والمعرف يرجح الثاني، فلذا سوى بينهما.",
     "en": "That the purpose of the definition is the application of the rules favours the first; while the nearness of the antecedent, together with the identity of the defined and the definition, favours the second; that is why he treated them as equal."},
]
