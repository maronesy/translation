# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 550 (printed ٥٤٩)."""

PAGE_NUMBER = 550
PRINTED_PAGE = "٥٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: في جميع ما ذكر من» at the foot of PDF p. 549 (mid-sentence).
    {"type": "matn",
     "ar": "حذف الفعل، وكونهما لغير السؤال[[١]]، والدخول على المظهر مطلقا، أو على اسم الله خاصة،",
     "en": "…the omission of the verb, their being for other than a request, and entering upon an explicit noun without restriction, or upon the name of Allah specifically."},
    {"type": "matn",
     "ar": "فهي كما تكون عند حذف الفعل تكون عند ذكره، نحو: «بالله، وأقسم بالله»،",
     "en": "So just as it [the bāʾ] occurs when the verb is omitted, it occurs when the verb is mentioned, as in “bi-llāhi” (by Allah) and “uqsimu bi-llāhi” (I swear by Allah);"},
    {"type": "matn",
     "ar": "وكما تكون لغير السؤال تكون للسؤال أيضا نحو: «بالله لأفعلن» و«بالله أجلس».",
     "en": "and just as it occurs for other than a request, it also occurs for a request, as in “bi-llāhi la-afʿalanna” (by Allah, I shall certainly do [it]) and “bi-llāhi ajlis” (by Allah, sit)."},
    # REVIEW: «بالله أجلس» is printed with hamzat al-qaṭʿ and fatḥa (with fatḥa on the alif); a request
    # would normally read «اجلس». Transcribed as printed.
    {"type": "matn",
     "ar": "وكما تدخل على المظهر تدخل على المضمر، نحو: «بالله لأفعلن» و«بك لأفعلن»،",
     "en": "And just as it enters upon an explicit noun, it enters upon a pronoun, as in “bi-llāhi la-afʿalanna” and “bika la-afʿalanna” (by You, I shall certainly do [it]);"},
    {"type": "matn",
     "ar": "وفي الدخول على المظهر لا تختص باسم الله خاصة، نحو: «بالرحمن لأفعلن»، بخلافهما، فإنهما مختصان ببعض هذه الأمور، كما عرفت.",
     "en": "and in entering upon an explicit noun it is not restricted to the name of Allah specifically, as in “bi-l-raḥmāni la-afʿalanna” (by the All-Merciful, I shall certainly do [it]) — unlike those two [the wāw and the tāʾ], for they are restricted to some of these matters, as you have learned."},
    {"type": "matn",
     "ar": "فالمراد بالجميع: جميع ما ذكر من الأمور المختصة لا الاختصاص،",
     "en": "So what is meant by “all” is all the specific matters mentioned, not the restriction [itself];"},
    {"type": "matn",
     "ar": "فلا يرد أنه لا يصح[[٢]] أن يقال: «الباء توجد مع الاختصاص وبدونه» لمكان التنافي.",
     "en": "hence the objection does not arise that it is not sound to say “the bāʾ is found with the restriction and without it”, on account of the contradiction."},
    {"type": "matn",
     "ar": "(ويتلقى) أي: يجاب[[٣]] (القسم) الذي لغير السؤال (باللام، وإن وحرف النفي) «ما» أو «لا».",
     "en": "(And the oath is met), that is, answered — the oath that is for other than a request — (with the lām, inna, and the particle of negation), “mā” or “lā”."},
    {"type": "matn",
     "ar": "فاللام في الموجبة: اسمية نحو: «والله لزيد قائم»، والفعلية نحو: «والله لأفعلن كذا»",
     "en": "Thus the lām [comes] in the affirmative [answer clause]: the nominal, as in “wa-llāhi la-Zaydun qāʾimun” (by Allah, Zayd is indeed standing), and the verbal, as in “wa-llāhi la-afʿalanna kadhā” (by Allah, I shall certainly do such-and-such);"},
    {"type": "matn",
     "ar": "و«إن» فيها، أي: في الاسمية، نحو: «والله إن زيدا لقائم».",
     "en": "and “inna” in it, that is, in the nominal, as in “wa-llāhi inna Zaydan la-qāʾimun” (by Allah, Zayd is indeed standing)."},
    {"type": "matn",
     "ar": "و«ما» و«لا» في المنفية اسمية كانت أو فعلية نحو: «والله ما زيد بقائم، ولا يقوم زيد».",
     "en": "And “mā” and “lā” [come] in the negative, whether nominal or verbal, as in “wa-llāhi mā Zaydun bi-qāʾimin” (by Allah, Zayd is not standing) and “lā yaqūmu Zaydun” (Zayd will not stand)."},
    {"type": "matn",
     "ar": "وقد يحذف حرف النفي[[٤]] لوجود القرينة، كقوله تعالى: ﴿تالله تفتأ تذكر يوسف﴾[[٥]]، أي: لا تفتؤ تذكر.",
     "en": "The particle of negation is sometimes omitted when there is a contextual indication (qarīna), as in His words, the Exalted: “By Allah, you will not cease remembering Yūsuf”, that is, lā taftaʾu tadhkuru (you will not cease remembering)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إشارة إلى أن اللام في قوله: القسم للعهد أي: القسم المذكور سابقا بقوله: لغير السؤال،",
     "en": "This indicates that the lām in his words “al-qasam” (the oath) is for prior reference (ʿahd), that is, the oath mentioned earlier in his words “for other than a request”;"},
    {"type": "pair",
     "ar": "فإن المعهود كما يكون بلفظه يكون بغير لفظه،",
     "en": "for what is previously referred to may be [mentioned] in its own wording, as it may be in other wording."},
    {"type": "pair",
     "ar": "فما قيل: إنه إشارة إلى أن إطلاق المصنف القسم تقصير منه قصور عن فهم المراد.",
     "en": "So what has been said — that it indicates that the author’s unrestricted use of “the oath” is a shortcoming on his part — is a failure to grasp what is meant."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لكن يراد أنه لو قال: الباء أعم من الواو لكفى.",
     "en": "But it may be objected that had he said “the bāʾ is more general than the wāw”, it would have sufficed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يقال: تلقيت كذا، أي: ألقى إليه،",
     "en": "One says “talaqqaytu kadhā” (I received such-and-such), that is, it was cast to him."},
    {"type": "pair",
     "ar": "فحمل الشارح قوله: يتلقى القسم على أنه يلقى إلى القسم الجواب باللام إلى آخره، فجعل القسم ملقى إليه جوابه تجوزا،",
     "en": "So the commentator took his words “the oath is met” to mean that the answer is cast to the oath with the lām, etc.; thus he made the oath that to which its answer is cast, by way of figurative usage (tajawwuz)."},
    # REVIEW: «فصار مآله، ويجاب القسم» — punctuation as printed; sense is "its upshot became: the oath is answered".
    {"type": "pair",
     "ar": "فصار مآله، ويجاب القسم.",
     "en": "So its upshot became: the oath is answered."},
    # REVIEW: «أو أن» printed with hamza above the alif; the particle in the matn is «إن».
    {"type": "pair",
     "ar": "والأظهر أن المعنى أنه يلقى القسم إلى المخاطب مع اللام في جوابه أو أن أو حرف النفي.",
     "en": "The more apparent [reading] is that the meaning is: the oath is cast to the addressee with the lām in its answer, or inna, or the particle of negation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: مع المضارع والماضي والجملة الاسمية كذا في التسهيل.",
     "en": "That is, with the imperfect, the perfect and the nominal sentence; so it is in al-Tashīl."},
    {"type": "pair",
     "ar": "وأنكر الرضي الحذف مع الماضي والجملة الاسمية،",
     "en": "Al-Raḍī rejected the omission with the perfect and the nominal sentence."},
    {"type": "pair",
     "ar": "وكثر هذا الحذف مع المضارع المجرد عن التأكيد مع ثبوت القسم، كما في المثال المذكور في الشرح،",
     "en": "This omission is frequent with the imperfect free of corroboration (taʾkīd) when the oath is present, as in the example mentioned in the commentary;"},
    {"type": "pair",
     "ar": "ومع الماضي عند تقدم النفي على القسم، نحو: لا والله ضربتني، أي: لا ضربتني،",
     "en": "and with the perfect when the negation precedes the oath, as in “lā wa-llāhi ḍarabtanī” (no, by Allah, you did not strike me), that is, lā ḍarabtanī;"},
    {"type": "pair",
     "ar": "وقل مع حذف القسم، وعند تقدم النفي عليه.",
     "en": "and it is rare when the oath is omitted, and when the negation precedes it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة يوسف: ٨٥.",
     "en": "Qurʾān, Sūrat Yūsuf 12:85."},
]
