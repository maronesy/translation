# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 45 (printed ٤٤)."""

PAGE_NUMBER = 45
PRINTED_PAGE = "٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "(و) القسم (الأول) وهو ما يدل على معنى في نفسها مقترن بأحد الأزمنة الثلاثة (الفعل) سمي به، لتضمنه الفعل[[١]] اللغوي[[٢]]، وهو المصدر.",
     "en": "(And) the (first) category — which is that which signifies a meaning in itself, conjoined with one of the three times — is (the verb, al-fiʿl). It was named thus because it comprises the linguistic “fiʿl” (act), which is the verbal noun (maṣdar)."},
    {"type": "matn",
     "ar": "(وقد علم[[٣]] بذلك)[[٤]] أي: بوجه[[٥]] حصر الكلمة في الأقسام الثلاثة (حد كل واحد منها)[[٦]] أي: من تلك الأقسام.",
     "en": "(And by that there has come to be known) — that is, by the manner of restricting the word to the three categories — (the definition of each one of them), that is: of those categories."},
    {"type": "matn",
     "ar": "وذلك لأنه قد علم به، أي: بوجه الحصر[[٧]]:",
     "en": "That is because there has come to be known by it — that is, by the manner of restriction — [the following]:"},
    {"type": "matn",
     "ar": "١- أن الحرف: كلمة لا تدل على معنى في نفسها، بل تحتاج إلى انضمام كلمة إليها.",
     "en": "1 — that the particle (ḥarf) is a word that does not signify a meaning in itself, but rather requires another word to be adjoined to it."},
    {"type": "matn",
     "ar": "٢- والفعل: كلمة تدل على معنى في نفسها، لكنه[[٨]] مقترن بأحد الأزمنة الثلاثة.",
     "en": "2 — the verb (fiʿl) is a word that signifies a meaning in itself, but it is conjoined with one of the three times."},
    {"type": "matn",
     "ar": "٣- والاسم: كلمة تدل على معنى في نفسها غير مقترن بأحد الأزمنة الثلاثة.",
     "en": "3 — the noun (ism) is a word that signifies a meaning in itself, not conjoined with one of the three times."},
    {"type": "matn",
     "ar": "فالكلمة مشتركة[[٩]] بين الأقسام الثلاثة. والحرف ممتاز عن أخويه بعدم الاستقلال في الدلالة.",
     "en": "So the word (kalima) is shared in common among the three categories. The particle is distinguished from its two brothers by the lack of independence in signification."},
    {"type": "matn",
     "ar": "والفعل ممتاز عن الحرف بالاستقلال، وعن الاسم بالاقتران. والاسم ممتاز عن الحرف بالاستقلال، وعن الفعل بعدم الاقتران.",
     "en": "The verb is distinguished from the particle by independence, and from the noun by conjunction [with time]. The noun is distinguished from the particle by independence, and from the verb by the absence of conjunction."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولك أن تقول: لمشابهته الفعل في أن له مصدرا كما للفعل.",
     "en": "You may [instead] say: [it was named a verb] on account of its resembling the [inflected] verb, in that it has a verbal noun (maṣdar) just as the verb does."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو المعنى المعتد به في الفعل حتى يراد عند الإطلاق هذا المعنى، وهو المعنى الذي في نفسه، فيكون من قبيل تسمية الدال باسم المدلول.",
     "en": "It [the maṣdar] is the meaning that is reckoned with in the verb, such that upon absolute usage this meaning is intended; and it is the meaning that is “in itself”; so it is of the type of naming the signifier (dāll) by the name of the signified (madlūl)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الواو للاعتراض لتنبيه من لا يجديه الإشارة، أو للعطف على «انحصرت»؛ لأنها، أو للعطف على العلم بالانحصار الذي أفاده الدليل، أي: علم انحصار الكلمة،",
     "en": "The wāw is for parenthetical interjection (iʿtirāḍ), to alert one whom the pointing (ishāra) does not avail; or for conjunction upon “inḥaṣarat” (it was restricted) — because of it; or for conjunction upon the knowledge of the restriction (inḥiṣār) which the proof (dalīl) conveyed — that is, the restriction of the word came to be known,"},
    {"type": "pair",
     "ar": "وقد علم بذلك أي: بوجهه. وعلى هذا التقدير يحتمل أن يكون الواو للحال.",
     "en": "“And by that it has been known,” that is: by its manner (wajh). On this estimation it is possible that the wāw be for the circumstantial (ḥāl)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الباء للاستعانة أو للسببية، اختار اسم الإشارة موضع الضمير للإشارة إلى زيادة تمكنه في الذهن وكمال انكشافه،",
     "en": "The bāʾ is for seeking aid (istiʿāna) or for causation; he chose the demonstrative noun in place of the pronoun to point to the added firmness of its establishment in the mind and the completeness of its manifestation;"},
    {"type": "pair",
     "ar": "وإيراد «ذلك» دون «هذا» لبعده من الحس بسبب كونه أمرا معنويا، أو استحقاقه التعظيم لكمال جودته.",
     "en": "and his bringing “that” (dhālika) rather than “this” (hādhā) is because of its remoteness from sense-perception — on account of its being an abstract matter — or [because of] its deserving magnification due to the perfection of its excellence."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الوجه بمعنى الدليل، والباء بمعنى «مع».",
     "en": "“Manner” (wajh) here means “indicant/proof” (dalīl), and the bāʾ means “with” (maʿa)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إضافة الحد إلى «كل» بمعنى اللام، ويجوز التصريح بها. وإضافة «كل» إلى «واحد» بمعنى اللام أيضا، لكنه يمتنع التصريح بها،",
     "en": "The annexation of “definition” (ḥadd) to “each” (kull) is in the sense of the lām [of possession], and explicitly stating it is permissible. And the annexation of “each” to “one” (wāḥid) is likewise in the sense of the lām, though explicitly stating it is precluded,"},
    {"type": "pair",
     "ar": "كما حققه قدس سره في بحث الإضافة من أنه لا يلزم فيما هو بمعنى اللام أن يصح التصريح بها، بل يكفي إفادة الاختصاص الذي هو مدلول اللام كيوم الأحد، وكل رجل وكل واحد.",
     "en": "as he — may his secret be sanctified — verified in the discussion of annexation (iḍāfa): that in what is [construed] in the sense of the lām it is not required that the explicit statement [with a lām] be valid; rather it suffices that it convey the [relation of] specification (ikhtiṣāṣ) which is the import of the lām — as in “the day of Sunday” (yawm al-aḥad), “every man” (kull rajul), and “every one” (kull wāḥid)."},
    {"type": "pair",
     "ar": "و«من» في قوله: «منها» للتبعيض، والجار والمجرور صفة لقوله: «واحد».",
     "en": "And “min” in his statement “of them” (minhā) is for partition (tabʿīḍ), and the prepositional phrase is an attribute of his word “one.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا وجه لإرجاع الضمير، ثم تفسيره بقوله: «أي: بوجه الحصر»، بل الأولى أن يقال: لأنه قد علم بوجه الحصر،",
     "en": "There is no ground for referring the pronoun back, then explaining it by his words “that is, by the manner of restriction”; rather it would be better to say: “because it has been known by the manner of restriction,”"},
    {"type": "pair",
     "ar": "إلا أن يقال: أشار بذكر الضمير ههنا إلى أن الإشارة في قوله: «وقد علم بذلك» وقع موقع الضمير، وفيه بعد.",
     "en": "unless it be said: he indicated, by mentioning the pronoun here, that the demonstrative in his statement “and by that it has been known” stands in the position of the pronoun; but in this there is [some] far-fetchedness."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأولى ترك «لكنه».",
     "en": "It would be better to omit “lākinnahu” (“but it”)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: اسم مفعول بمعنى مشترك فيها. والأقسام مشتركات بالكسر، يعني: أن الكلمة جنس تحته هذه الأنواع الثلاثة.",
     "en": "That is: [mushtaraka is] a passive participle meaning “shared in” (mushtarak fīhā). And “the categories” are “sharers” (mushtarikāt, with a kasra) — meaning that the word (kalima) is a genus falling under these three species."},
]
