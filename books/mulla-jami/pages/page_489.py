# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 489 (printed ٤٨٨)."""

PAGE_NUMBER = 489
PRINTED_PAGE = "٤٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وفي خبر كاد نحو: «كاد زيد» at the foot of PDF p. 488 (mid-sentence).
    {"type": "matn",
     "ar": "يقوم»، وفي نحو: «يقوم الزيدان».",
     "en": "…yaqūmu” (Zayd was about to stand), and in a case like “yaqūmu al-Zaydāni” (the two Zayds stand)."},
    # REVIEW: printed «علي أن» (with dotted yāʾ) for «على أن»; transcribed as printed.
    {"type": "matn",
     "ar": "وأجيب عن: نحو: «الذي يضرب، ويقوم الزيدان»: بأنه واقع موقعه؛ لأنك تقول: «الذي ضارب هو» علي أن «ضارب» خبر مبتدأ مقدم عليه، وكذا «قائمان الزيدان»،",
     "en": "It has been answered regarding cases like “alladhī yaḍribu” and “yaqūmu al-Zaydāni” that it does occur in its position, for you say “alladhī ḍāribun huwa”, “ḍārib” being the predicate of a subject (mubtadaʾ), placed before it; and likewise “qāʾimāni al-Zaydāni”;"},
    {"type": "matn",
     "ar": "ويكفينا[[١]] وقوعه موقع الاسم وإن كان الإعراب[[٢]] مع تقديره اسما غير الإعراب مع تقديره فعلا.",
     "en": "and its occurring in the position of the noun suffices us, even if the inflection when it is supposed to be a noun differs from the inflection when it is supposed to be a verb."},
    {"type": "matn",
     "ar": "وعن نحو: «سيقوم»: أن «سيقوم» مع «السين» واقع موقع الاسم لا يقوم وحده، و«السين»[[٣]] صار كأحد أجزاء الكلمة، و«سوف» في حكم السين.",
     "en": "And regarding a case like “sa-yaqūmu”: that “sa-yaqūmu” together with the “sīn” occurs in the position of the noun, not “yaqūmu” alone, the “sīn” having become like one of the parts of the word; and “sawfa” has the status of the sīn."},
    {"type": "matn",
     "ar": "وعن نحو: «كاد زيد يقوم»: أن الأصل فيه الاسم، وإنما عدل عن الأصل لما يجيء في باب أفعال المقاربة إن شاء الله تعالى.",
     "en": "And regarding a case like “kāda Zaydun yaqūmu”: that the base form in it is the noun, and it departed from the base only for what will come in the chapter on the verbs of approximation (afʿāl al-muqāraba), if Allah the Exalted wills."},

    {"type": "section", "ar": "[نواصب الفعل المضارع]",
     "en": "The Particles Governing the Accusative of the Imperfect Verb"},

    # REVIEW: the matn opens with «(بـ«أن») ملفوظة» directly under the heading; the governing verb of the Kāfiya clause («وينتصب») is not printed here. Transcribed as printed.
    {"type": "matn",
     "ar": "(بـ«أن») ملفوظة.",
     "en": "[It is put in the accusative] (by “an”), when pronounced,"},
    {"type": "matn",
     "ar": "(و«لن») قال الفراء: أصله «لا» أبدل الألف نونا[[٤]].",
     "en": "(and “lan”). Al-Farrāʾ said: its origin is “lā”, the alif being replaced by a nūn."},
    {"type": "matn",
     "ar": "وقال الخليل: أصله «لا أن»، فقصر كـ«أيش» في «أي شيء».",
     "en": "Al-Khalīl said: its origin is “lā an”, which was shortened, like “aysh” for “ayyu shayʾin”."},
    {"type": "matn",
     "ar": "وقال سيبويه: إنه حرف برأسه.",
     "en": "Sībawayh said: it is a particle in its own right."},
    {"type": "matn",
     "ar": "(و«إذن») قيل: أصله «إذ أن» فخفف.",
     "en": "(And “idhan”). It has been said: its origin is “idh an”, which was lightened."},
    {"type": "matn",
     "ar": "وقيل: أصله «إذ» الظرفية[[٥]]، فنون عوضا عن المضاف إليه[[٦]].",
     "en": "And it has been said: its origin is the adverbial “idh”, which was given a nūn in compensation for the term annexed to it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: في ارتفاعه.",
     "en": "That is, for its being in the nominative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: وإن كان إعراب ما بعده مع تقديره أي: الواقع اسما غير إعرابه مع تقديره فعلا؛ إذ هو مع تقدير الاسم مبتدأ، ومع تقدير الفعل فاعل،",
     "en": "He means: even if the inflection of what follows it, when it, that is, what occurs [there], is supposed to be a noun, differs from its inflection when it is supposed to be a verb; for with the supposition of the noun it is a subject (mubtadaʾ), and with the supposition of the verb an agent (fāʿil)."},
    {"type": "pair",
     "ar": "وليس المراد أن إعراب المضارع مع التقدير الأول غير إعرابه مع التقدير الثاني؛",
     "en": "What is meant is not that the inflection of the muḍāriʿ under the first supposition differs from its inflection under the second;"},
    {"type": "pair",
     "ar": "لأن ذلك التغاير متحقق في جميع المواد؛ إذ العامل على تقدير الاسم لفظي، وعلى تقدير الفعل معنوي، فلا معنى لـ«إن» الوصلية.",
     "en": "for that difference holds in all instances, since the governor on the supposition of the noun is verbal (lafẓī) and on the supposition of the verb abstract (maʿnawī); so the connective “in” (even if) would have no point."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "دفع لما يقال: فحينئذ لم يقع المضارع موقع الاسم، بل مع حرف التنفيس.",
     "en": "A rebuttal of what may be said: “In that case the muḍāriʿ has not occurred in the position of the noun, but [only] together with the particle of futurity (ḥarf al-tanfīs).”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أنه لا مناسبة بين الألف والنون إلا أن يقال: النون الخفيفة تقلب في الوقف ألفا، وكذا التنوين.",
     "en": "Against this: there is no affinity between the alif and the nūn, unless it be said that the light nūn is converted into an alif in pause, and likewise the tanwīn."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "في الرضي: وإنما حملني على ذلك ظهور معنى الزمان فيها في جميع الاستعمالات كما في «إذ».",
     "en": "In al-Raḍī: “What led me to that is only that the sense of time appears in it in all its uses, as in ‘idh’.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "في الرضي: وذلك أنهم أرادوا الإشارة إلى زمان فعل مذكور، فقصدوا إلى لفظ «إذ» الذي هو بمعنى مطلق الوقت لخفة لفظه، وجردوه عن معنى الماضي، وجعلوه صالحا للأزمنة بالثلاثة،",
     "en": "In al-Raḍī: “That is because they wanted to point to the time of a mentioned action, so they resorted to the word ‘idh’, which means time without qualification, for the lightness of its form; they stripped it of the sense of the past and made it suitable for the three times;"},
    {"type": "pair",
     "ar": "وحذفوا منه الجملة المضاف هو إليها لدلالة الفعل السابق عليها كما يقول لك شخص: أنا أزورك، فتقول: إذن",
     "en": "and they omitted from it the sentence to which it is annexed, because the preceding verb indicates it; as when someone says to you, ‘I will visit you’, and you say: ‘idhan…"},
]
