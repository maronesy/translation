# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 225 (printed ٢٢٤)."""

PAGE_NUMBER = 225
PRINTED_PAGE = "٢٢٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "افعل كذا»، والموصولات نحو: «من لا يزال محسنا أحسن إلي».",
     "en": "…do such-and-such” (Zayd’s servant, do such-and-such); and the relative nouns, as in “man lā yazālu muḥsinan aḥsin ilayya” (you who never cease to do good, do good to me)."},
    {"type": "matn",
     "ar": "وأما المضمرات، فشذ نداؤها نحو: «يا أنت ويا إياك».",
     "en": "As for the pronouns, addressing them is anomalous, as in “yā anta” and “yā iyyāka.”"},
    {"type": "matn",
     "ar": "(وشذ) حذف حرف النداء من اسم الجنس (في «أصبح ليل») أي: «صر صبحا[[١]] يا ليل»",
     "en": "(And) omitting the vocative particle from a generic noun (is anomalous in “aṣbiḥ laylu”), that is, “become morning, O night”:"},
    {"type": "matn",
     "ar": "حذف حرف النداء من الليل مع أنه اسم جنس شذوذا، قالته امرأة امرئ القيس[[٢]] حين كرهته",
     "en": "the vocative particle was omitted from “layl” (night), anomalously, although it is a generic noun. The wife of Imruʾ al-Qays said it when she had come to loathe him;"},
    {"type": "matn",
     "ar": "(وفي «افتد مخنوق»[[٣]]) أي: «يا مخنوق» قاله شخص[[٤]] وقع في الليل على نائم مستلق فخنقه، وقال: «إفتد مخنوق»،",
     "en": "(and in “iftadi makhnūqu”), that is, “ransom yourself, O strangled one”: it was said by a man who at night fell upon someone sleeping on his back and strangled him, saying “iftadi makhnūqu”;"},
    {"type": "matn",
     "ar": "حذف حرف النداء عن المخنوق مع أنه اسم جنس شذوذا",
     "en": "the vocative particle was omitted from “makhnūq,” anomalously, although it is a generic noun;"},
    {"type": "matn",
     "ar": "(و) في («أطرق كرا») أي: «يا كروان» وفيه شذوذان حذف حرف النداء من اسم الجنس، وترخيم غير العلم.",
     "en": "(and) in (“aṭriq karā”), that is, “[lower your head,] O curlew (karawān)”; this has two anomalies: omitting the vocative particle from a generic noun, and truncating what is not a proper name."},
    {"type": "matn",
     "ar": "قيل: هي رقية[[٥]] يصيدون بها الكروان، يقولون: «أطرق كرا أطرق كرا إن النعامة في القرى»، فيسكن ويطرق حتى يصاد[[٦]]،",
     "en": "It has been said that it is a charm (ruqya) with which they hunt the curlew; they say: “Lower your head, curlew, lower your head, curlew; the ostrich is in the villages,” and it keeps still and lowers its head until it is caught."},
    # REVIEW: print reads «فلا تخلي» (sense: so do not feel secure); transcribed as printed.
    {"type": "matn",
     "ar": "والمعنى: أن النعام الذي هو أكبر منك قد أصطيد وحمل إلى القرى فلا تخلي أيضا.",
     "en": "The meaning is: the ostrich, which is bigger than you, has been caught and carried to the villages, so do not you be at ease either."},
    {"type": "matn",
     "ar": "(وقد يحذف المنادى؛ لقيام قرينة جوازا نحو: «ألا يا اسجدوا») بتخفيف «ألا» على أنه حرف تنبيه، و«يا» حرف نداء، أي: «يا قوم اسجدوا»،",
     "en": "(The vocative itself is sometimes omitted, permissibly, when there is a contextual indication, as in “a-lā yā sjudū”), with “alā” unstressed as a particle of alerting and “yā” as the vocative particle, that is, “O people, prostrate!”;"},
    {"type": "matn",
     "ar": "والقرينة امتناع دخول «يا» على الفعل،",
     "en": "the contextual indication is that “yā” cannot enter upon a verb."},
    {"type": "matn",
     "ar": "بخلاف قراءة ﴿ألا يسجدوا﴾[[٧]] بتشديد اللام؛ لأنه ليس من هذا الباب،",
     "en": "This is unlike the reading “allā yasjudū” (Qurʾān, Sūrat al-Naml 27:25) with a doubled lām, which does not belong to this topic;"},
    {"type": "matn",
     "ar": "فإن «أن» ناصبة[[٨]] للمضارع، أدغمت نونها في لام «لا»، و«يسجدوا» فعل مضارع سقط نونه بالنصب.",
     "en": "for “an” governs the imperfect in the subjunctive, its nūn assimilated into the lām of “lā,” and “yasjudū” is an imperfect verb whose nūn has fallen through the subjunctive."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو ادخل في الصباح.",
     "en": "Or: enter into the morning."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فلما أصبحت أخذت منه الطلاق، وهو مثل في شدة طلب الشيء.",
     "en": "When morning came she obtained a divorce from him. It is a proverb for intense longing for something."},
    {"type": "pair",
     "ar": "وقيل مثل يستعمله المغموم.",
     "en": "It has also been said to be a proverb used by one in distress."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: هو مثل للتحريض على تخليص النفس من الورطة الشديدة.",
     "en": "It has been said: it is a proverb urging one to free oneself from a severe predicament."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "صار مثلا للحث على تخليص النفس من الورطة الشديدة.",
     "en": "It became a proverb for urging one to free oneself from a severe predicament."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إذا سمعها تلبد بالأرض، فيلقى عليه ثوب، فيصاد،",
     "en": "When it hears it, it presses itself to the ground; a cloth is thrown over it and it is caught."},
    {"type": "pair",
     "ar": "صار مثلا لمن تكبر، وقد تواضع من هو أشرف منه.",
     "en": "It became a proverb for one who acts proudly when one nobler than he has humbled himself."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بأن يلقى عليه ثوب، فيصاد صار مثلا لمن تكبر وقد تواضع من هو أشرف منه.",
     "en": "By a cloth being thrown over it, and so it is caught. It became a proverb for one who acts proudly when one nobler than he has humbled himself."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة النمل: ٢٥.",
     "en": "Qurʾān, Sūrat al-Naml 27:25."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وألا يسجدوا مفعول لا يهتدون قبله، ولا زائدة أو بدل من أعمالهم، أو متعلق بصدهم، أو يزين بتقدير لام التعليل.",
     "en": "“Allā yasjudū” is the object of “lā yahtadūn” before it, with “lā” redundant; or it is a substitute for “aʿmālahum”; or it is attached to “ṣaddahum,” or to “zayyana,” with the lām of cause understood."},
]
