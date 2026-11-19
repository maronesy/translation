# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 469 (printed ٤٦٨)."""

PAGE_NUMBER = 469
PRINTED_PAGE = "٤٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وهي: استعماله» at the foot of PDF p. 468 (mid-sentence).
    {"type": "matn",
     "ar": "بالإضافة، أو «من»، أو اللام على سبيل الانفصال الحقيقي.",
     "en": "…with annexation, or with “min”, or with the article, by way of real disjunction (munfaṣila ḥaqīqiyya)."},
    {"type": "matn",
     "ar": "فلا بد من واحد منها؛ لأن وضعه لتفضيل الشيء على غيره، فلا بد فيه من ذكر الغير الذي هو المفضل عليه،",
     "en": "So one of them is indispensable, because it is coined for preferring a thing over another, so the other, the one surpassed (al-mufaḍḍal ʿalayhi), must be mentioned in it."},
    {"type": "matn",
     "ar": "وذكره مع «من» والإضافة ظاهر. وأما مع «اللام»، فهو في حكم المذكور ظاهرا؛",
     "en": "Its mention with “min” and with annexation is evident. With the article, it is as though explicitly mentioned,"},
    {"type": "matn",
     "ar": "لأنه يشار باللام إلى معين بتعيين المفضل عليه مذكور قبله لفظا أو حكما",
     "en": "because the article points to something specified through the specification of the one surpassed, mentioned before it explicitly or by implication;"},
    {"type": "matn",
     "ar": "كما إذا طلب شخصا أفضل من زيد قلت: «عمرو الأفضل» أي: الشخص الذي قلنا: إنه أفضل من زيد،",
     "en": "as when someone seeks a person more excellent than Zayd and you say “ʿAmrun al-afḍal” (ʿAmr is the more excellent), that is, the person of whom we said that he is more excellent than Zayd."},
    {"type": "matn",
     "ar": "فعلى هذا لا يكون اللام في أفعل التفضيل إلا للعهد، فيجب أن يستعمل:",
     "en": "On this basis the article in the elative afʿal is only for prior reference (ʿahd). So it must be used:"},
    {"type": "matn",
     "ar": "١-(إما مضافا[[١]]) نحو: «زيد أفضل الناس».",
     "en": "1. (either annexed), as in “Zaydun afḍalu l-nās” (Zayd is the most excellent of people);"},
    {"type": "matn",
     "ar": "٢-(أو بـ«من») نحو: «زيد أفضل من عمرو».",
     "en": "2. (or with “min”), as in “Zaydun afḍalu min ʿAmrin” (Zayd is more excellent than ʿAmr);"},
    {"type": "matn",
     "ar": "٣-(أو معرفا باللام) نحو: «زيد الأفضل».",
     "en": "3. (or made definite by the article), as in “Zaydun al-afḍal” (Zayd is the more excellent)."},
    {"type": "matn",
     "ar": "(فلا يجوز) الجمع بين الاثنين منها («زيد الأفضل من عمرو»)، وإلا يكون ذكر[[٢]] «اللام» أو «من» لغوا[[٣]]،",
     "en": "(So it is not permitted) to combine two of them: (“Zaydun al-afḍalu min ʿAmrin”); otherwise mentioning the article or “min” would be redundant."},
    {"type": "matn",
     "ar": "وأما قوله:",
     "en": "As for the poet’s words:"},
    {"type": "verse",
     "ar": "ولست بالأكثر[[٤]] منهم حصى          وإنما العزة للكاثر",
     "en": "You are not the greater of them in number (lit. pebbles); might belongs only to the more numerous."},
    # REVIEW: the verse prints «ولست» (second person, as fn ٤ confirms: «على صيغة الخطاب»), but the gloss prints «ليست من بينهم». Transcribed as printed.
    {"type": "matn",
     "ar": "فقيل: «من» فيه ليست تفضيلية، بل للتبعيض، أي: ليست من بينهم بالأكثر حصى.",
     "en": "it has been said that “min” in it is not comparative but partitive, that is, “you are not, from among them, the greater in number.”"},
    {"type": "matn",
     "ar": "(ولا يجوز) خلوه عن الكل أيضا، لفوات الغرض، نحو: («زيد أفضل» إلا أن يعلم[[٥]]) المفضل عليه[[٦]]، مثل: «الله أكبر»،",
     "en": "(Nor is it permitted) that it be free of all of them, since the purpose would be lost, as in (“Zaydun afḍal”, unless) the one surpassed (is known), as in “Allāhu akbar” (Allah is greater)."},
    {"type": "matn",
     "ar": "ويجوز أن يقال في مثله: أن المحذوف[[٧]]",
     "en": "It may be said of the like of it that what is omitted…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بدل عنه. وأشار إليه بإعادة «يستعمل» في قوله: فيجب أن يستعمل، فإن البدل في حكم تكرار العامل.",
     "en": "A substitute (badal) for it. He indicated this by repeating “is used” in his words “so it must be used”, for the substitute is as though the governing word were repeated."},
    {"type": "pair",
     "ar": "وأورد الفاء الدالة على كونه قريبا على ما تقدم لكونه تفصيلا له إشارة إلى فائدة البدل، وهو إفادة العلم التفصيلي بعد العلم الإجمالي،",
     "en": "He brought the fāʾ, which indicates that it follows on what preceded as its detailing, to point to the benefit of the substitute, namely conveying detailed knowledge after summary knowledge;"},
    {"type": "pair",
     "ar": "وزاد الوجوب ليترتب عليه قوله: فلا يجوز.",
     "en": "and he added necessity so that his words “so it is not permitted” follow from it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: كونه مذكورا.",
     "en": "That is, its being mentioned."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لحصول الغرض، وهو تعيين المفضل عليه بأحدهما، وليس المقام مقام التأكيد.",
     "en": "Because the purpose, namely specifying the one surpassed, is achieved by one of them, and the context is not one of emphasis."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "على صيغة الخطاب والكاثر للمبالغة أي: العزة للغالب في الأكثرية.",
     "en": "In the second-person form; and “al-kāthir” is for intensiveness, that is, might belongs to the one who prevails in number."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "استثناء منقطع؛ لأنه حينئذ يكون المفضل عليه محذوفا، فلا يكون اسم التفضيل خاليا عنه.",
     "en": "A disjoined exception (istithnāʾ munqaṭiʿ), because in that case the one surpassed is omitted, so the elative is not free of it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: printed «مع الأفعال الذي» (plural «الأفعال» with singular «الذي»); «أفعل» may be intended. Transcribed as printed.
    {"type": "pair",
     "ar": "ومع العلم بالمفضل عليه الحذف مع الأفعال الذي خبر غالب، ومع غيره قليل.",
     "en": "When the one surpassed is known, omission with the afʿal that is a predicate is frequent, and with other than it rare."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    # REVIEW: printed «فاستبقى» and «نحو جواز»; «جوار» (jawārin, with tanwīn in place of the yāʾ) may be intended. Transcribed as printed.
    {"type": "pair",
     "ar": "ولم يعوض عنه التنوين لكون أفعل غير منصرف، فاستبقى.",
     "en": "Tanwīn is not substituted for it, because afʿal is diptote; so it was kept [without it]."},
    {"type": "pair",
     "ar": "وأما نحو جواز فقد ذكرنا قصدهم تعويض التنوين فيه، كذا في الرضي.",
     "en": "As for the like of “jawāz” [sic], we have mentioned their intent to substitute tanwīn in it; so in al-Raḍī."},
    {"type": "pair",
     "ar": "ويجوز أن يقال: ههنا بالبناء على الضم كما في قبل؛ لأنه مختص بالغايات",
     "en": "It may be said here [that it is] by being made indeclinable on the ḍamma, as in “qablu”; [but] this is specific to the ghāyāt (adverbs cut off from their complement)…"},
]
