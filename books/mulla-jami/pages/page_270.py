# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 270 (printed ٢٦٩)."""

PAGE_NUMBER = 270
PRINTED_PAGE = "٢٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وإلا) أي: وإن لم يكن بتنوين أو بنون التثنية» from the foot of PDF p. 269.
    {"type": "matn",
     "ar": "بأن يكون بنون الجمع[[١]] أو الإضافة (فلا) يجوز الإضافة إلا بقلة في نون الجمع نحو: «عشرو درهم».",
     "en": "…by being [complete] by the nūn of the plural or by a genitive construction, (then) the genitive construction is (not) permitted, except rarely with the nūn of the plural, as in “ʿishrū dirhamin” (twenty of dirhams)."},
    {"type": "matn",
     "ar": "وأما في الإضافة: فلئلا يلزم إضافة المضاف.",
     "en": "As for the genitive construction, [it is not permitted] lest a muḍāf be made muḍāf [again]."},
    {"type": "matn",
     "ar": "وأما في نون الجمع: فلأنه جاز أن يضاف إلى غير المميز نحو: «عشريك وعشري رمضان» بالاتفاق لكثرة الحاجة إليه،",
     "en": "As for the nūn of the plural, it is because it may be annexed to what is not the specified term, as in “your twenty” and “the twenty of Ramaḍān,” by agreement, owing to the frequent need for it;"},
    {"type": "matn",
     "ar": "فلو أضيف إلى المميز لزم الالتباس في بعض الصور؛",
     "en": "so if it were annexed to the specified term, ambiguity would follow in some forms;"},
    {"type": "matn",
     "ar": "لأنه لا يعلم مثلا عند إضافة «عشرين»[[٢]] إلى «رمضان» أنه أراد «عشرين رمضان»[[٣]] أو أراد «اليوم العشرين من رمضان»،",
     "en": "for when “twenty” is annexed to “Ramaḍān,” for example, it is not known whether he meant “twenty Ramaḍāns” or “the twentieth day of Ramaḍān.”"},
    {"type": "matn",
     "ar": "فلا يضاف في غير صورة الالتباس أيضا، إلا على قلة، ليكون الباب أقرب إلى الاطراد.",
     "en": "So it is not annexed even where there is no ambiguity, except rarely, so that the chapter may come nearer to consistency."},
    {"type": "matn",
     "ar": "(وعن غير مقدار[[٤]]) عطف على «عن مفرد مقدار»",
     "en": "(And from what is not a measure): conjoined to “from a single term that is a measure”;"},
    {"type": "matn",
     "ar": "أي: الأول كما يرفع الإبهام عن مفرد مقدار كذلك يرفعه عن مفرد غير مقدار،",
     "en": "that is, just as the first removes vagueness from a single term that is a measure, so it removes it from a single term that is not a measure,"},
    {"type": "matn",
     "ar": "أي: ما ليس بعدد، ولا وزن، ولا ذراع، ولا كيل، ولا مقياس (نحو: «خاتم حديدا»)،",
     "en": "that is, what is not a number, weight, cubit, dry measure or standard of comparison, (as in “a ring of iron”);"},
    {"type": "matn",
     "ar": "فإن «الخاتم» مبهم باعتبار الجنس، تام بالتنوين، فاقتضى تمييزا.",
     "en": "for “ring” is vague with respect to genus and complete by the tanwīn, so it called for a tamyīz."},
    {"type": "matn",
     "ar": "(والخفض) أي: خفض التمييز بإضافة غير المقدار إليه (أكثر) استعمالا، لحصول الغرض مع الخفة،",
     "en": "(The genitive), that is, putting the tamyīz in the genitive by annexing the non-measure to it, (is more frequent) in use, because the purpose is achieved together with lightness,"},
    {"type": "matn",
     "ar": "ولقصور غير المقدار عن طلب التمييز[[٥]]؛ لأن الأصل في المبهمات المقادير، وغيرها ليس بهذه المثابة.",
     "en": "and because the non-measure falls short in calling for a tamyīz; for the primary vague nouns are measures, and other [nouns] are not of this standing."},
    {"type": "matn",
     "ar": "(والثاني) أي: القسم الثاني من التمييز، وهو ما يرفع الإبهام عن ذات مقدرة يرفعه",
     "en": "(And the second), that is, the second division of the tamyīz, which removes vagueness from an implied entity, removes it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أراد شبه نون الجمع.",
     "en": "He meant what resembles the nūn of the plural."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يخفى أن رمضان لو كان تمييزا لكان نكرة، ولو لم يكن تمييزا لاحتمل أن يكون علما،",
     "en": "It is evident that “Ramaḍān,” were it a tamyīz, would be indefinite; and were it not a tamyīz, it could be a proper name;"},
    {"type": "pair",
     "ar": "بل الظاهر أنه علم، فالالتباس ليس إلا على تقدير ألا يكون علما.",
     "en": "indeed it is apparently a proper name; so the ambiguity arises only on the supposition that it is not a proper name."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يجب أن يقال: عشرين رمضانا؛ لأن رمضان وإن كان غير منصرف للعلمية والألف والنون المزيدتين، لكنه إذا وقع تمييزا يكون منكرا لوجوب تنكير التمييز.",
     "en": "One ought to say “ʿishrīna Ramaḍānan”; for although “Ramaḍān” is diptote (ghayr munṣarif) because of being a proper name and having the added alif and nūn, when it occurs as a tamyīz it is indefinite, since the tamyīz must be indefinite."},
    {"type": "pair",
     "ar": "وحينئذ في الالتباس في هذا المثال أيضا نظرا؛",
     "en": "So the ambiguity in this example too is open to question;"},
    # REVIEW: «نظرا» printed in the accusative where «نظر» is expected; transcribed as printed.
    {"type": "pair",
     "ar": "لأنه في صورة الإضافة إلى التمييز نكرة مصروفة، وفي صورة الإضافة إلى غيره معرفة غير مصروفة،",
     "en": "for when annexed as tamyīz it is an indefinite, fully declined noun, and when annexed as something else it is a definite diptote,"},
    {"type": "pair",
     "ar": "إلا أن يراد اليوم العشرين من رمضان ما، لكن سوق كلامه لا يساعده.",
     "en": "unless what is meant is the twentieth day of some Ramaḍān; but the drift of his discourse does not support this."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: هو كل فرع حصل له بالتفريع اسم خاص يليه أصله، ويكون بحيث يصح إطلاق اسم ذلك الأصل عليه،",
     "en": "Shaykh al-Raḍī said: it is every derivative that has acquired, through derivation, a name of its own, followed by [the name of] its source, and is such that the name of that source may correctly be applied to it,"},
    {"type": "pair",
     "ar": "نحو: خاتم حديدا، وهو ينتصب عنه التمييز.",
     "en": "as in “a ring of iron”; from such a noun the tamyīz takes the accusative."},
    {"type": "pair",
     "ar": "وأما الفرع الذي لم يحصل له اسم خاص، فلا يجوز انتصاب ما يليه على التمييز نحو: قطعة ذهب.",
     "en": "As for the derivative that has not acquired a name of its own, what follows it may not take the accusative as a tamyīz, as in “a piece of gold.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وإذا قصر عن طلبه لم يحتج إلى نصب التمييز الذي يكون للتنصيص على التمييز، فإن التنصيص عليه إنما يناسب ما هو طالب للتمييز.",
     "en": "When it falls short in calling for it, there is no need for the accusative of the tamyīz, which serves to mark it explicitly as tamyīz; for such explicit marking suits only what calls for a tamyīz."},
]
