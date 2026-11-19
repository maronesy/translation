# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 224 (printed ٢٢٣)."""

PAGE_NUMBER = 224
PRINTED_PAGE = "٢٢٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والمضاف إليه، فإنهما متغايران بالذات.",
     "en": "…and the noun annexed to it, for these two are distinct in essence."},
    {"type": "matn",
     "ar": "وحكى يونس: أن رجلا ضاع له قدحان فقال: «وا جمجمتي الشاميتيناه». والجمجمة: القدح[[١]].",
     "en": "Yūnus related that a man lost two cups and said: “wā jumjumatayya al-shāmiyyataynāh” (O my two Syrian cups!). The jumjuma is a cup (qadaḥ)."},

    {"type": "section", "ar": "[حذف حرف النداء]",
     "en": "Omission of the Vocative Particle"},

    {"type": "matn",
     "ar": "(ويجوز) لقيام قرينة (حذف حرف النداء إلا) إذا كان مقارنا (مع اسم الجنس[[٢]])",
     "en": "(And) when there is a contextual indication, (omitting the vocative particle is permitted, except) when it is accompanied (by a generic noun—ism al-jins);"},
    {"type": "matn",
     "ar": "ونعني به: ما كان نكرة[[٣]] قبل النداء[[٤]] سواء تعرف بالنداء كـ«يا رجل» أو لم يتعرف مثل: «يا رجلا»؛",
     "en": "by which we mean what was indefinite before the vocative, whether it became definite through the vocative, as in “yā rajulu,” or did not, as in “yā rajulan”;"},
    {"type": "matn",
     "ar": "لأن نداءه لم يكثر كثرة نداء العلم[[٥]]، فلو حذف منه حرف النداء لم يسبق الذهن إلى أنه منادى.",
     "en": "because addressing it is not as frequent as addressing a proper name, so if the vocative particle were omitted from it the mind would not readily take it to be a vocative."},
    {"type": "matn",
     "ar": "(والإشارة) أي: وإلا مع اسم الإشارة؛ لأنه كاسم الجنس[[٦]] في الإبهام",
     "en": "(And the demonstrative), that is, and except with a demonstrative noun, because it is like the generic noun in vagueness;"},
    {"type": "matn",
     "ar": "(والمستغاث والمندوب)؛ لأن المطلوب فيهما مد الصوت، وتطويل الكلام، والحذف ينافيه،",
     "en": "(and the one called for help—al-mustaghāth—and the lamented noun), because what is sought in them is prolonging the voice and lengthening the utterance, and omission runs counter to that."},
    {"type": "matn",
     "ar": "فبقي على هذا من المعارف التي يجوز فيها حذف حرف النداء العلم سواء كان مع بدل عن حرف النداء كلفظة «الله»،",
     "en": "On this basis, among the definite nouns in which omitting the vocative particle is permitted there remains the proper name, whether with a substitute for the vocative particle, as with the word “Allāh,”"},
    {"type": "matn",
     "ar": "فإنه لا يحذف منه إلا مع إبدال الميم المشددة منه نحو: «اللهم»",
     "en": "from which it is omitted only when the doubled mīm is substituted for it, as in “Allāhumma”;"},
    {"type": "matn",
     "ar": "أو بغير بدل (نحو: ﴿يوسف أعرض عن هذا﴾[[٧]])، أي: «يا يوسف»",
     "en": "or without a substitute, (as in: “Joseph, turn away from this”) (Qurʾān, Sūrat Yūsuf 12:29), that is, “O Joseph”;"},
    {"type": "matn",
     "ar": "ولفظة «أي» إذا وصف بذي اللام (نحو: «أيها الرجل») أي: «يا أيها الرجل»",
     "en": "and the word “ayy” when qualified by a noun with the definite article, (as in “ayyuhā al-rajulu”), that is, “yā ayyuhā al-rajulu” (O you man);"},
    {"type": "matn",
     "ar": "أو بالموصوف بذي اللام (نحو: «أيهذا الرجل») أي: «يا أيها الرجل»،",
     "en": "or by what is qualified by a noun with the definite article, (as in “ayyuhādhā al-rajulu”), that is, “yā ayyuhā al-rajulu”;"},
    {"type": "matn",
     "ar": "فلا يجوز الحذف من «أيهذا» من غير أن يوصف هذا بذي اللام،",
     "en": "so omission from “ayyuhādhā” is not permitted unless “hādhā” is qualified by a noun with the definite article;"},
    {"type": "matn",
     "ar": "والمضاف إلى أي معرفة[[٨]] كانت نحو: «غلام زيد",
     "en": "and the noun annexed to any definite noun whatever, as in “ghulāma Zaydin…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال بعض المحققين: ومن الغرائب أنه قال المصنف في شرح المفصل: الجمجمة الرأس،",
     "en": "One of the verifying scholars said: among the oddities is that the author said in his commentary on al-Mufaṣṣal: “the jumjuma is the head.”"},
    {"type": "pair",
     "ar": "ولعله الكأس، والخطأ من الناسخ.",
     "en": "Perhaps it was “the goblet” (al-kaʾs), and the error is the copyist’s."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى إلا مقارنا مع اسم الجنس؛ لأنه لا وجه بتقدير إذا كان.",
     "en": "Better would be “except accompanied by a generic noun,” since there is no reason to supply “when it is.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سواء كان مضافا أو غيره، وفيه رد على من قال: المراد باسم الجنس ما يصح دخول اللام عليه.",
     "en": "Whether it is annexed or not. This refutes whoever said that what is meant by the generic noun is that on which the definite article may properly enter."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وفيه رد على من قال: المراد باسم الجنس ما دخل اللام عليه.",
     "en": "This refutes whoever said that what is meant by the generic noun is that on which the definite article has entered."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وأما غير العلم من المعارف وإن لم يكثر كثرة العلم، فألحق بالعلم لمزيد المناسبة بالعلم،",
     "en": "As for the definite nouns other than the proper name, although they are not as frequent as the proper name, they were assimilated to it because of their closer affinity with it;"},
    {"type": "pair",
     "ar": "فلا يرد فاء التعليل يقتضي اختصاص الحذف بالعلم.",
     "en": "so the objection does not arise that the fāʾ of causation requires omission to be restricted to the proper name."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولأنه موضوع في الأصل لما يشار إليه للمخاطب وبين كون الاسم مشارا إليه وكونه منادى أي: مخاطبا تنافر ظاهر،",
     "en": "Also because it is originally coined for what is pointed out to the addressee, and between a noun’s being pointed to and its being a vocative, that is, addressed, there is a clear incompatibility;"},
    # REVIEW: print reads «تغييرهن» (probably for «تغييره عنه»); transcribed as printed.
    {"type": "pair",
     "ar": "فلما أخرج في النداء عن ذلك الأصل احتيج إلى علامة ظاهرة تدل على تغييرهن وجعله مخاطبا، وهي حرف النداء.",
     "en": "so when in the vocative it was taken out of that original, a visible sign was needed to indicate its change and its being made addressed, and that is the vocative particle."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة يوسف: ٢٩.",
     "en": "Qurʾān, Sūrat Yūsuf 12:29."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "عطف على قوله: لفظة أي.",
     "en": "Coordinated with his words “the word ‘ayy.’”"},
]
