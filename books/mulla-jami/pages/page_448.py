# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 448 (printed ٤٤٧)."""

PAGE_NUMBER = 448
PRINTED_PAGE = "٤٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… والمذكر العلم» at the foot of PDF p. 447 (mid-sentence).
    {"type": "matn",
     "ar": "العاقل أشرف من غيره، فأعطي الأشرف للأشرف،",
     "en": "…the rational is nobler than others; so the noblest was given to the noblest."},
    {"type": "matn",
     "ar": "فإن فقد فيه الكل كـ«العين» أو الاثنان كـ«المرأة»، أو واحد نحو: «أعوج» للفرس، لم يجمع هذا الجمع.",
     "en": "If all are lacking in it, as in “al-ʿayn” (the eye), or two, as in “al-marʾa” (the woman), or one, as in “Aʿwaj” as the name of a horse, it is not pluralized with this plural."},
    {"type": "matn",
     "ar": "وأراد بالمذكر: ما يكون مجردا عن التاء ملفوظة أو مقدرة؛ ليخرج عنه نحو: «طلحة»، فإنه لا يجمع بالواو والنون",
     "en": "By “masculine” he meant what is free of the tāʾ, pronounced or implied, so as to exclude from it the like of “Ṭalḥa”, for it is not pluralized with the wāw and nūn,"},
    {"type": "matn",
     "ar": "خلافا للكوفيين وابن كيسان، فإنهم أجازوا «طلحون» بسكون اللام، وابن كيسان بفتحها،",
     "en": "contrary to the Kūfans and Ibn Kaysān: they allowed “Ṭalḥūn”, with a quiescent lām, and Ibn Kaysān with a fatḥa on it."},
    {"type": "matn",
     "ar": "ويدخل فيه نحو: «ورقاء وسلمى» اسمي رجلين، فانهما يجمعان بالواو والنون اتفاقا؛ لأن علم التأنيث هو التاء لا الألف،",
     "en": "Included in it is the like of “Warqāʾ” and “Salmā” as names of two men, for they are pluralized with the wāw and nūn by agreement, because the mark of the feminine is the tāʾ, not the alif;"},
    {"type": "matn",
     "ar": "فلا يمنع من الجمعية بالواو والنون؛ لأن الممدودة تقلب واوا، فتنمحى صورة علامة التأنيث، والمقصورة تحذف، ويبقى الفتحة قبلها دالة عليها.",
     "en": "so it does not prevent pluralization with the wāw and nūn, because the lengthened [alif] is converted into a wāw, so that the form of the feminine marker is effaced, and the shortened one is dropped, the fatḥa before it remaining to point to it."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط الاسم الذي أريد جمعه جمع المذكر الصحيح (إن كان صفة) من الصفات غير علم[[١]] كاسمي الفاعل والمفعول (فمذكر يعقل) أي: له شروط:",
     "en": "(And its condition), that is, the condition of the noun intended to be pluralized with the sound masculine plural, (if it is an adjective), one of the adjectives, not a proper name, like the active and passive participles, (is: a masculine of a rational being), that is, it has conditions:"},
    {"type": "matn",
     "ar": "١-فالشرط الأول: كونه مذكرا يعقل، كما مر.",
     "en": "1. The first condition: its being a masculine of a rational being, as has passed."},
    # REVIEW: printed «مستوفى» (here and in the third condition); context requires «مستو» (“sharing equally”, cf. the matn’s «مستويا فيه» below); transcribed as printed, translated in that sense.
    {"type": "matn",
     "ar": "٢-(و) الشرط الثاني: (ألا يكون) ذلك الاسم[[٢]] الكائن صفة («أفعل فعلاء») أي: مذكرا غير مستوفى صيغة الصفة الكائن ذلك الاسم إياها مع المؤنث،",
     "en": "2. (And) the second condition: (that) that noun, being an adjective, (not be “afʿal–faʿlāʾ”), that is, a masculine that does not share with the feminine the form of the adjective which that noun is,"},
    {"type": "matn",
     "ar": "بل يكون المذكر على صيغة «أفعل»، والمؤنث على صيغة «فعلاء» (مثل: «أحمر، حمراء») للفرق بينه وبين أفعل التفضيل كـ«أفضلون»،",
     "en": "but rather the masculine is on the pattern “afʿal” and the feminine on the pattern “faʿlāʾ”, (as in “aḥmar–ḥamrāʾ”) (red), to distinguish it from the elative “afʿal”, as in “afḍalūn”;"},
    {"type": "matn",
     "ar": "ولم يعكس؛ لأن معنى الصفة في أفعل التفضيل كامل، لدلالته على الزيادة.",
     "en": "and it was not done the other way round, because the adjectival sense in the elative “afʿal” is complete, since it indicates excess."},
    {"type": "matn",
     "ar": "(و) الشرط الثالث: أن (لا) يكون ذلك الاسم («فعلان، فعلى») أي: مذكرا غير مستوفى في تلك الصيغة مع المؤنث،",
     "en": "(And) the third condition: that that noun (not) be (“faʿlān–faʿlā”), that is, a masculine that does not share that form with the feminine,"},
    {"type": "matn",
     "ar": "بل يكون المذكر على صيغة «فعلان» والمؤنث على صيغة «فعلى» (مثل: «سكران سكرى») فإنه لا يقال فيه: «سكرانون»",
     "en": "but rather the masculine is on the pattern “faʿlān” and the feminine on the pattern “faʿlā”, (as in “sakrān–sakrā”) (drunk); for one does not say of it “sakrānūn”,"},
    {"type": "matn",
     "ar": "للفرق بينه وبين «فعلان وفعلانة» كـ«ندمانون»، ولم يعكس؛ لأن «فعلان، فعلانة» أصل في الفرق بين المذكر والمؤنث؛ لأنه فيه بالتاء وعدمها.",
     "en": "to distinguish it from “faʿlān–faʿlāna”, as in “nadmānūn” (boon companions); and it was not done the other way round, because “faʿlān–faʿlāna” is the basic case in distinguishing masculine from feminine, since the distinction in it is by the tāʾ and its absence."},
    # REVIEW: printed «مذكور» (after «الاسم المذكور»), where context suggests «مذكرا»; transcribed as printed.
    {"type": "matn",
     "ar": "(و) الشرط الرابع: أن (لا) يكون الاسم المذكور مذكور (مستويا فيه) أي: في",
     "en": "(And) the fourth condition: that the noun mentioned, [being] masculine, (not be shared equally in it), that is, in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن كان معناه غير منقول من الوصفية، فائدته إخراج نحو: أحمر إذا سمي به ذكر، فإنه يجمع بالواو والنون لصيرورته اسما وعدم اعتبار الوصفية الأصلية،",
     "en": "If its meaning is “not transferred from adjectival status”, its benefit is to exclude the like of “Aḥmar” when a male is named by it, for it is pluralized with the wāw and nūn because it has become a noun and its original adjectival status is disregarded;"},
    # REVIEW: printed «العملية»; context (contrast of ʿalamiyya and waṣfiyya) suggests «العلمية»; transcribed as printed, translated as «العلمية».
    {"type": "pair",
     "ar": "وإن كان معناه غير علم حال الوصفية، ففائدته التنبيه على أن العلمية لا تجامع الوصفية لكونهما متضادين، فلذا لم تشترط العملية في الصفة عند جمعها أشرف الجموع.",
     "en": "and if its meaning is “not a proper name while adjectival”, its benefit is to point out that being a proper name (ʿalamiyya) does not combine with adjectival status, since the two are contraries; this is why being a proper name is not made a condition in the adjective when it is given the noblest of plurals."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يرجع الضمير إلى الصفة بتأويل الوصف لعدم صحته في قوله: ولا مستويا فيه مع المؤنث.",
     "en": "He did not refer the pronoun to the adjective, construed as “the qualifier”, because that would not be sound in his words “nor shared equally in it with the feminine”."},
]
