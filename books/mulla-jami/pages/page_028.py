# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 28 (printed ٢٧)."""

PAGE_NUMBER = 28          # PDF page
PRINTED_PAGE = "٢٧"       # page number printed in the book

BLOCKS = [
    # ---------------- The main text (matn) ----------------
    {"type": "matn",
     "ar": "وهو حسبي[[١]]، ونعم الوكيل[[٢]].",
     "en": "And He is my sufficiency, and an excellent Guardian is He!"},
    {"type": "matn",
     "ar": "اعلم أن الشيخ –رحمه الله– لم يصدر رسالته هذه[[٣]] بحمد الله سبحانه[[٤]]، بأن جعله[[٥]] جزءا منها[[٦]]، هضما لنفسه[[٧]]، بتخييل[[٨]] أن كتابه هذا من حيث إن كتابه ليس ككتب السلف رحمهم الله تعالى حتى يصدر به على سننها،",
     "en": "Know that the Shaykh — may Allah have mercy on him — did not prefix this treatise of his with the praise of Allah, Glorified is He, by making the praise a part of it, out of self-effacement — imagining that this book of his, inasmuch as it is [merely] his own book, is not like the books of the predecessors (salaf), may Allah the Exalted have mercy on them, such that he should prefix it [with praise] after their manner;"},
    {"type": "matn",
     "ar": "ولا يلزم من ذلك عدم الابتداء به مطلقا، حتى يكون بتركه[[٩]] أقطع، لجواز إتيانه[[١٠]] بالحمد من غير أن يجعله جزءا من كتابه.",
     "en": "yet this does not entail refraining from beginning with it [praise] altogether, so that its omission would be more conclusive; for it is permissible for him to bring the praise without making it a part of his book."},

    {"type": "rule"},

    # ---------------- Footnote (continued from the previous page) ----------------
    {"type": "note", "num": "…"},   # unnumbered ḥāshiya continuing from the previous page (printed ٢٦)
    {"type": "pair",
     "ar": "بل بـ«من»، ويدخل الباء على الآلة. فلا يقال: «الضرب بزيد» إذا كان الضارب زيدا، بل «من زيد».",
     "en": "rather [it should be] with “min”; the bāʾ [of instrumentality] applies to the instrument. Thus one does not say “the striking with (bi-) Zayd” when the striker is Zayd, but rather “from (min) Zayd.”"},
    {"type": "pair",
     "ar": "فالمناسب أن يقال: «وما توفيقي إلا من الله».",
     "en": "So the fitting thing would be to say: “And my success is only from Allah.”"},
    {"type": "pair",
     "ar": "ويمكن أن يقال: لما وقع في كلام الله تعالى بهذا الوجه اختار هذا تبركا بكلامه.",
     "en": "It may be answered: since it occurred in the speech of Allah, the Exalted, in this manner, he chose this [wording], seeking blessing through His speech."},
    {"type": "pair",
     "ar": "فإن قلت: ينقل الكلام إلى كلام الله تعالى؟",
     "en": "If you say: is the [grammatical] usage to be transferred [as a basis] to the speech of Allah, the Exalted?"},
    {"type": "pair",
     "ar": "قلت: لا بد من تطبيق القاعدة بكلام الفصحاء لا العكس، فوقوعه في الكلام الفصيح يدل على عدم صحة ما ذكرته.",
     "en": "I say: the rule must be tested against the speech of the eloquent, not the reverse; so its occurrence in eloquent speech indicates the incorrectness of what you have mentioned."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الحسب في الأصل مصدر يستوي فيه الواحد والمذكر وفروعهما. وههنا بمعنى اسم الفاعل ليصح الحمل، أي: محسبي وكاف.",
     "en": "Ḥasb, in its origin, is a verbal noun (maṣdar) in which the singular and the masculine and their derivatives are alike [invariant]. Here it carries the sense of the active participle (ism al-fāʿil) so that predication may be valid — that is: “that which suffices me” (muḥsibī) and “sufficient” (kāfin)."},
    {"type": "pair",
     "ar": "فلا يتعرف بالإضافة فهو الخبر عن الضمير المتقدم؛ إذ لا يخبر عن نكرة بمعرفة إلا في صور ليس هذا منها.",
     "en": "So it does not become definite through annexation (iḍāfa), and thus it is the predicate (khabar) of the preceding pronoun; for an indefinite is not predicated of by a definite except in [certain] cases, of which this is not one."},
    {"type": "pair",
     "ar": "واعلم أن «حسب»: إن ذكر بعد النكرة فهو صفة لها، وإن بعد المعرفة فحال.",
     "en": "Know that ḥasb: if it is mentioned after an indefinite, it is an adjective (ṣifa) of it; and if after a definite, it is a circumstantial qualifier (ḥāl)."},
    {"type": "pair",
     "ar": "وإنه إن استعمل بحرف جر أصلي كان مفتوح السين نحو قولك: هذا بحسب ذاك، أي: بقدره، وإلا كان ساكنها.",
     "en": "And if it is used with an original genitive particle, its sīn is voweled with fatḥa (ḥasab), as in your saying: “this is according to (bi-ḥasab) that,” i.e., “to its measure”; otherwise its [sīn] is quiescent (ḥasb)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الوكيل: من يفوض إليه الأمور. والجملة عطف على جملة، هي: حسبي. والمخصوص محذوف،",
     "en": "Al-wakīl (the guardian): the one to whom affairs are entrusted. The clause [wa-niʿma al-wakīl] is coordinated upon a clause, namely “He is my sufficiency”; and the specified subject of praise (al-makhṣūṣ) is elided,"},
    {"type": "pair",
     "ar": "أو عطف على «حسبي» لتضمنه معنى الفعل، والمخصوص هو الضمير المتقدم.",
     "en": "or it is coordinated upon “my sufficiency” because it [niʿma] contains the meaning of a verb, in which case the specified subject is the preceding pronoun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صفة الرسالة، مثل: «مررت بزيد هذا».",
     "en": "[“Hādhihi” is] an adjective of “the treatise,” like “I passed by this Zayd (marartu bi-Zaydin hādhā).”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الباء في «بحمد الله» للتعدية، أي: لم يجعل بحمد الله في صدر رسالته. والباء في «بأن جعله» للملابسة، أي: تصديرا ملابسا بأن جعله جزءا.",
     "en": "The bāʾ in “bi-ḥamdi -llāh” is for transitivity (taʿdiya), that is: he did not place the praise of Allah at the opening (ṣadr) of his treatise. And the bāʾ in “bi-an jaʿalahu” is for concomitance (mulābasa), that is: a prefixing accompanied by his making it a part."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "متعلق بالتصدير، وتصوير للمنفي، وهو ظاهر.",
     "en": "[It is] connected to the prefixing (taṣdīr), and a depiction of what is negated; and this is evident."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الجار والمجرور صفة لجزء، والضمير البارز راجع إلى الرسالة.",
     "en": "The prepositional phrase [minhā] is an adjective of “part” (juzʾ), and the visible pronoun refers back to “the treatise.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "مفعول له لما يتضمنه قوله: «لم يصدر»، أي: ترك تصدير الكتاب هضما لنفسه؛",
     "en": "[Haḍman li-nafsihi is] an object of purpose (mafʿūl lahu) for what his words “he did not prefix” imply, that is: he omitted prefixing the book out of self-effacement;"},
    {"type": "pair",
     "ar": "إذ لو لم يؤول أفاد أن التصدير لم يكن للهضم، بل بأمر آخر، بناء على ما اشترط من أن النفي إن دخل على المقيد بقيد توجه إلى ذلك القيد.",
     "en": "for were it not so interpreted, it would imply that the prefixing [would have been] not for self-effacement but for some other reason — based on what has been stipulated: that negation, if it enters upon something qualified by a qualifier, is directed toward that qualifier."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وذلك الكسر بتخييل أن كتابه من حيث إنه صنعه لا من حيث اشتماله على المسائل ليس في مرتبة كتب السلف، حتى يلزم بذلك الترك مخالفتهم،",
     "en": "That humbling (al-kasr) is through the imagining that his book — inasmuch as it is his own making, not inasmuch as it comprises the [scholarly] questions — is not on the level of the books of the predecessors, such that omitting [the praise] would entail differing from them;"},
    {"type": "pair",
     "ar": "فإنهم إنما يستحسنون جعله جزءا فيما يعتنون بشأنه، وما هو في مرتبة كتبهم.",
     "en": "for they only deem it fitting to make it [praise] a part in that whose matter they attend to and which is on the level of their books."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: بترك الحمد كتبا وفعلا.",
     "en": "That is: by omitting the praise both in writing and in deed."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: المصنف.",
     "en": "That is: the author (al-muṣannif)."},
]
