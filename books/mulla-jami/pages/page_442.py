# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 442 (printed ٤٤١)."""

PAGE_NUMBER = 442
PRINTED_PAGE = "٤٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أو لأنه محبوس من» at the foot of PDF p. 441 (mid-sentence).
    {"type": "matn",
     "ar": "الحركات، والقصر «الحبس»",
     "en": "…the vowels, qaṣr meaning “withholding”."},
    # REVIEW: the matn prints «ألوان» and «ألي» (hamza above the alif, dotted yāʾ), whereas footnote ١ prints «إلوان» and «إلى» (the particle ilā). Transcribed as printed in each place.
    {"type": "matn",
     "ar": "(إن كان ألفه منقلبة عن واو) حقيقة كـ«عصوان»[[١]]، أو حكما بأن كان مجهول الأصل[[٢]] ولم يمل[[٣]] كـ«ألوان» في المسمى بـ«ألي»[[٤]]",
     "en": "(If its alif is converted from a wāw), really, as in “ʿaṣawān” (two staffs), or by status, in that its origin is unknown and it does not undergo inclination (imāla), as in “ilawān” for something named “ilā”,"},
    {"type": "matn",
     "ar": "(وهو ثلاثي) أي: والحال أن ذلك المقصور ثلاثي، أي: غير ما فيه[[٥]] أربعة أحرف فصاعدا من الرباعي والثلاثي المزيد فيه",
     "en": "(and it is triliteral), that is, while that maqṣūr is triliteral, that is, other than what has four letters or more, whether quadriliteral or augmented triliteral,"},
    {"type": "matn",
     "ar": "(قلبت) ألفه (واوا) اعتبارا للأصل حقيقة أو حكما، وخفة الثلاثي، بخلاف ما فوقه حيث لا يرد فيه لمكان الثقل.",
     "en": "(it is converted), its alif, (into a wāw), in regard of the origin, real or by status, and the lightness of the triliteral; unlike what is above it, where it is not restored, because of the heaviness."},
    {"type": "matn",
     "ar": "(وإلا) وإن لم يكن كذلك بأن كان ألفه عن ياء حقيقة كـ«رحيان» في رحى",
     "en": "(Otherwise), if it is not so, in that its alif is from a yāʾ, really, as in “raḥayān” for “raḥā” (millstone),"},
    {"type": "matn",
     "ar": "أو حكما بأن كان مجهول الأصل أو عديمه، وقد أميل[[٦]] كـ«متيان» في متى حيث جاء متى ممالا،",
     "en": "or by status, in that its origin is unknown or non-existent and it has undergone inclination, as in “matayān” for “matā”, since “matā” occurs with inclination;"},
    {"type": "matn",
     "ar": "أو كان على أربعة أحرف فصاعدا أصلية كانت الألف كـ«الأعلى والمصطفى» أو زائدة كـ«حبلى»",
     "en": "or it has four letters or more, the alif being radical, as in “al-aʿlā” and “al-muṣṭafā”, or augmentative, as in “ḥublā”,"},
    {"type": "matn",
     "ar": "(فبالياء) أي: فألفه مقلوبة بالياء اعتبارا للأصل فيما أصله الياء حقيقة أو حكما، وتخفيفا فيما زاد على ثلاثة أحرف.",
     "en": "(then with the yāʾ), that is, its alif is converted into the yāʾ, in regard of the origin in what has the yāʾ as its origin, really or by status, and for lightness in what exceeds three letters."},
    {"type": "matn",
     "ar": "(و) الاسم (الممدود إن كانت همزته أصلية) أي: غير زائدة[[٧]] ولا منقلبة عن",
     "en": "(And) the (lengthened) noun, (if its hamza is radical), that is, neither augmentative nor converted from…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الظاهر كعصا وكإلى بدل قوله: كعصوان وإلوان في المسمى بـ«إلى»",
     "en": "The evident thing would be “like ʿaṣā and like ilā” in place of his words “like ʿaṣawān and ilawān for something named ‘ilā’”;"},
    {"type": "pair",
     "ar": "فإن عصوان وإلوان مثالان للتثنية لا للمقصور الذي ألفه منقلبة عن واو حقيقة أو حكما،",
     "en": "for “ʿaṣawān” and “ilawān” are examples of the dual, not of the maqṣūr whose alif is converted from a wāw, really or by status;"},
    {"type": "pair",
     "ar": "وأن يورد كعصوان وإلوان بعد قوله: قلبت ألفه واوا. وكذا الكلام في رحيان ومتيان.",
     "en": "and he should give “ʿaṣawān” and “ilawān” after his words “its alif is converted into a wāw”. The same applies to “raḥayān” and “matayān”."},
    {"type": "pair",
     "ar": "وإنما كان أصل ألف عصا واوا حقيقة لقولهم: عصوته أي: ضربته بالعصا.",
     "en": "The origin of the alif of “ʿaṣā” is really a wāw because of their saying “ʿaṣawtuhu”, that is, “I struck him with the staff”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: غير معلومة سواء كان له أصل في الواقع أو لا.",
     "en": "That is, not known, whether or not it has an origin in fact."},
    {"type": "pair",
     "ar": "وللإشارة إلى إرادة معنى العام أورد المثال من عديم الأصل،",
     "en": "To indicate that the general sense is meant, he gave the example from what has no origin;"},
    {"type": "pair",
     "ar": "فإن الألف في الأسماء العريقة في البناء كـ«متى وإذا وإلى» لا أصل لها،",
     "en": "for the alif in nouns deeply rooted in indeclinability, like “matā”, “idhā” and “ilā”, has no origin,"},
    {"type": "pair",
     "ar": "وفي الأسماء المتمكنة لها أصل، وهو محل الإعراب، وهو قد يكون معلوما، وقد لا يكون معلوما.",
     "en": "while in declinable nouns it has an origin, since it is the seat of inflection; and that origin is sometimes known and sometimes not."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هكذا وقع في التسهيل، وقيده في الرضي بألا يكون هناك سبب للإمالة غير انقلاب الألف عن الياء،",
     "en": "So it occurs in al-Tashīl; in al-Raḍī it is restricted by the condition that there be no cause of inclination other than the alif’s conversion from the yāʾ;"},
    {"type": "pair",
     "ar": "وفيه أنه حينئذ يكون معلوم الأصل.",
     "en": "against which: in that case its origin would be known."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «الغريقة» (with ghayn), whereas footnote ٢ has «العريقة في البناء»; transcribed as printed, translated as «العريقة».
    {"type": "pair",
     "ar": "الألف في الأسماء الغريقة البناء كـ«متى وعلى وإلى وإذا» أعلاما عديم الأصل",
     "en": "The alif in nouns deeply rooted in indeclinability, like “matā”, “ʿalā”, “ilā” and “idhā”, [used] as proper names, has no origin;"},
    {"type": "pair",
     "ar": "ومجهول الأصل ما هو في اسم متمكن لم يعرف أصلها كذا حققه الرضي، فجعل إلى علما مجهول الأصل محل نظر.",
     "en": "and “of unknown origin” is what is in a declinable noun whose origin is not known; so al-Raḍī established. So making “ilā” as a proper name of unknown origin is questionable."},
    {"type": "pair",
     "ar": "وينبغي أن يقول: ولم يمل وأميل، وكان لإمالته سبب غير انقلاب الألف عن الياء،",
     "en": "He ought to say: “and it does not undergo inclination, or it does undergo inclination but there is a cause of its inclination other than the alif’s conversion from the yāʾ”;"},
    {"type": "pair",
     "ar": "فإن الرضي شرط في قلب عديم الأصل ومجهوله ياء أن يكون مما سمع فيه الإمالة، ولم يكن هناك سبب الإمالة غير انقلاب الألف عن الياء.",
     "en": "for al-Raḍī made it a condition for converting [an alif] of no origin or of unknown origin into a yāʾ that it be among what inclination is attested for, and that there be no cause of inclination other than the alif’s conversion from the yāʾ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: المراد بالثلاثي المعنى اللغوي أي: ذو ثلاثة أحرف لا الاصطلاحي، وهو ما تكون حروفه الأصلية ثلاثة.",
     "en": "That is, by “triliteral” the lexical sense is meant, that is, having three letters, not the technical sense, which is that whose radical letters are three."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا بد من قيد آخر، وهو ألا يكون لإمالته سبب سوى كون الألف منقلبة عن الياء.",
     "en": "A further restriction is necessary: that there be no cause of its inclination other than the alif’s being converted from the yāʾ."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فالأصلية بمعنى الثابتة في محل ليخرج عنها الأقسام الثلاثة",
     "en": "So “radical” means “fixed in its place”, so that the three [other] kinds are excluded from it;"},
    {"type": "pair",
     "ar": "لا بالمعنى المتعارف، وهو ما تكون في مقابلة الفاء والعين واللام، فإنه لا يخرج حينئذ ما تكون منقلبة عن أصلية.",
     "en": "not in the customary sense, namely what stands opposite the fāʾ, ʿayn and lām [of the pattern], for then what is converted from a radical letter would not be excluded."},
]
