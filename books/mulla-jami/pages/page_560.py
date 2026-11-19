# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 560 (printed ٥٥٩)."""

PAGE_NUMBER = 560
PRINTED_PAGE = "٥٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإن جعلت «ما» موصولة» at the foot of PDF p. 559.
    {"type": "matn",
     "ar": "أو موصوفة كان حاصل المعنى: أو مقولاتي، تعين الكسر؛ لأن أول المقولات أني أحمد الله[[١]] لا المعنى المصدري.",
     "en": "…or qualified (mawṣūfa), the resulting sense is “the first of the things I say”, and kasra is fixed, because the first of the things said is “innī aḥmadu llāha”, not the verbal-noun meaning."},
    {"type": "matn",
     "ar": "فإن المعنى المصدري أعني: الحمد، قول خاص، وليس من جنس المقولات.",
     "en": "For the verbal-noun meaning, namely praising, is a particular act of saying, and is not of the genus of the things said."},
    {"type": "matn",
     "ar": "وإن جعلت «ما» مصدرية كان حاصل المعنى: «أول أقوالي» تعين الفتح؛",
     "en": "If you take “mā” as maṣdariyya, the resulting sense is “the first of my sayings”, and fatḥa is fixed,"},
    {"type": "matn",
     "ar": "لأن أول الأقوال[[٢]] هو المعنى المصدري الذي هو معنى «أن» المفتوحة مع جملتها، لا ما هو من جنس المقول.",
     "en": "because the first of the sayings is the verbal-noun meaning, which is the meaning of “anna” with fatḥa together with its clause, not what is of the genus of the thing said."},
    {"type": "matn",
     "ar": "(ولذلك[[٣]]) أي: لأجل أن «إن» المكسورة لا تغير معنى الجملة كأن اسمها المنصوب في محل الرفع؛ لأنها في حكم العدم[[٤]]، إذ فائدتها التأكيد فقط.",
     "en": "(And for that reason), that is, because “inna” with kasra does not alter the meaning of the sentence, it is as though its accusative noun were in the position of the nominative, since it counts as non-existent, its only function being emphasis (taʾkīd);"},
    {"type": "matn",
     "ar": "(جاز العطف على) محل (اسم «إن»[[٥]] المكسورة) من جهة أنه في محل الرفع،",
     "en": "(coordination is permitted with) the position of (the noun of “inna” with kasra), in that it is in the position of the nominative,"},
    {"type": "matn",
     "ar": "سواء كان المكسورة مكسورة (لفظا أو حكما بالرفع) بأن تكون المفتوحة في حكم المكسورة، كما إذا وقعت بعد «العلم»",
     "en": "whether the kasra form is such (in wording or by rule, with the nominative), the latter when the fatḥa form counts as the kasra form, as when it occurs after [a verb of] “knowledge”,"},
    {"type": "matn",
     "ar": "مثل: «إن زيدا قائم وعمرو» و«علمت أن زيدا قائم وعمرو»",
     "en": "as in “inna Zaydan qāʾimun wa-ʿAmrun (Zayd is standing, and ʿAmr)” and “ʿalimtu anna Zaydan qāʾimun wa-ʿAmrun (I knew that Zayd is standing, and ʿAmr)”."},
    {"type": "matn",
     "ar": "فـ«أن» في هذا المثال وإن كانت مفتوحة لفظا، فهي مكسورة حكما، حيث يكون مع ما عملت فيه بتأويل الجملة[[٦]]، فصح أن يرفع المعطوف على اسمه،",
     "en": "“Anna” in this example, though it has fatḥa in wording, has kasra by rule, since together with what it governs it is construed as a sentence; so it is sound for what is coordinated with its noun to take the nominative,"},

    {"type": "rule"},

    # ---------------- Footnote 2 of PDF p. 559 (continued) ----------------
    # Continuation of footnote [٢] from the previous page (PDF 559), on «لا جرم».
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الرشد فمعنى: ﴿لا جرم أن لهم النار﴾ (النحل:٦٢) لا قطع من أن لهم النار،",
     "en": "…of rushd. So the meaning of “lā jarama anna lahumu l-nāra” (Qurʾān, Sūrat al-Naḥl 16:62) is “there is no cutting off from their having the Fire”;"},
    {"type": "pair",
     "ar": "فهو كلا بد بمعنى لا قطع إلا أنه صار بمعنى القسم للتأكيد الذي فيه حتى يجاب بما يجاب به القسم،",
     "en": "it is like “lā budda”, meaning “no cutting off”, except that it has come to have the sense of an oath because of the emphasis in it, so that it is answered with what answers an oath."},
    {"type": "pair",
     "ar": "فيقال: لا جرم لآتينك، ولا جرم أنك قائم بالكسر، والفتح بعده نظرا إلى الأصل، والكسر نظرا إلى عارض القسمية.",
     "en": "So one says “lā jarama la-ātiyannaka (I shall surely come to you)” and “lā jarama innaka qāʾimun” with kasra; fatḥa after it looks to the origin, and kasra to its acquired character as an oath."},
    {"type": "pair",
     "ar": "وحكى الكوفيون فيه تغييرات: إسقاط الميم وزيادة ذا بعد «لا» في الحالين، وزيادة «أن» و«إذا».",
     "en": "The Kūfans reported variations in it: dropping the mīm, adding “dhā” after “lā” in both cases, and adding “an” and “idhā”."},
    {"type": "pair",
     "ar": "قيل: جرم، وتبديل همزة أن بالعين فمما يمتحن به لا عن ذا جرم أن زيدا قائم، فاحفظه.",
     "en": "It has been said: “jarama”, and replacing the hamza of “an” with ʿayn; so among the things used to test [students] is “lā ʿan dhā jarama anna Zaydan qāʾimun”; memorize it."},
    {"type": "pair",
     "ar": "ومن جملة ما يتوهم أنه من أشباهه قمت، كما أنك قائم، وليس من أشباهه لتعين الفتح؛",
     "en": "Among what is imagined to be of its like is “qumtu kamā annaka qāʾimun (I stood, just as you are standing)”, but it is not of its like, because fatḥa is fixed there;"},
    {"type": "pair",
     "ar": "لأن «ما» زائدة غير كافة التزموا زيادة «ما» مع الكاف الجارة لئلا يشتبه بـ«كأن».",
     "en": "for “mā” is redundant and not restraining (kāffa); they made the addition of “mā” to the prepositional kāf obligatory so that it would not be confused with “kaʾanna”."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: هذا الكلام، فيكون قد قال كلاما أوله: إني أحمد الله، ثم أخبر عن ذلك،",
     "en": "That is, this speech; so he will have uttered speech whose beginning is “innī aḥmadu llāha”, and then reported about that."},
    {"type": "pair",
     "ar": "ولا يكون أني أحمد الله معمولا في اللفظ لـ«أقول»؛ لأنه وقع خبرا عن أول، وإن كان مقولا من حيث المعنى.",
     "en": "“Innī aḥmadu llāha” is then not governed in wording by “aqūlu”, because it stands as the predicate of “awwal”, even though it is what is said in respect of meaning."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيكون فقط خبرا عن المصدر بالمصدر، ولا يكون الحمد بهذا اللفظ.",
     "en": "So it is merely a report about a verbal noun by a verbal noun, and the praising is not with this wording."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قدم العلة ليحصل الحكم معللا، فإنه أوقع في النفوس.",
     "en": "He put the cause first so that the ruling comes already justified, for this makes a stronger impression on minds."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فهو بمنزلة الباء في «كفى بالله».",
     "en": "So it is like the bāʾ in “kafā bi-llāhi (Allah suffices)”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الظاهر فجاز ليرتبط بما قبله، وكأنه حفظ كتابة المتن، وأعرض عن الربط.",
     "en": "The expected wording is “fa-jāza”, so that it is linked to what precedes; it seems he kept to the wording of the matn and set aside the linkage."},
    {"type": "pair",
     "ar": "واختلف عبارة النحاة جعل بعضهم المعطوف عليه اسم إن، وبعضهم مجموع الاسم وكلمة إن،",
     "en": "The grammarians’ formulations differ: some made the thing coordinated with the noun of inna, and some the noun and the word inna taken together."},
    {"type": "pair",
     "ar": "ورجح المصنف الأول، وتبعه الرضي وأوضحه.",
     "en": "The author preferred the first, and al-Raḍī followed him and clarified it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأنه نائب مناب مفعولين.",
     "en": "Because it stands in place of two objects."},
    {"type": "pair",
     "ar": "ورد بأن مفعولي «علمت» في تأويل المفرد، فكيف يوجب كون المفتوحة مع ما يتعلق بها نائبا عن مفعولية كونه في تأويل الجملة،",
     "en": "This was rejected on the ground that the two objects of “ʿalimtu” are construed as single terms; so how could the fatḥa form, with what relates to it, standing in for their objecthood, entail its being construed as a sentence?"},
    {"type": "pair",
     "ar": "ولم يجوز السيرافي العطف على محل اسم أن المفتوحة أصلا.",
     "en": "Al-Sīrāfī did not permit coordination with the position of the noun of anna with fatḥa at all."},
]
