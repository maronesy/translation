# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 390 (printed ٣٨٩)."""

PAGE_NUMBER = 390
PRINTED_PAGE = "٣٨٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فما قيل: «أف» بمعنى» at the foot of PDF p. 389.
    # REVIEW: a small dot is printed between «به» and «تضجرت» («به.«تضجرت»); treated as spacing, not transcribed.
    {"type": "matn",
     "ar": "أتضجر، و«أوه» بمعنى: أتوجع، فالمراد به «تضجرت وتوجعت» عبر عنه بالمضارع؛ لأن المعنى على الإنشاء[[١]]، وهو أنسب بأن يعبر عنه بالمضارع الحالي.",
     "en": "…“ataḍajjaru” (I am vexed), and “awwah” in the sense of “atawajjaʿu” (I am in pain): what is meant by it is “taḍajjartu” and “tawajjaʿtu”, expressed by the imperfect because the meaning is performative (inshāʾ), and that is more fittingly expressed by the imperfect of the present."},
    {"type": "matn",
     "ar": "(مثل: «رويد زيدا»[[٢]] أي: أمهله) مثال لما هو بمعنى الأمر[[٣]].",
     "en": "(As in “ruwayda Zaydan”, that is, give Zayd respite): an example of what has the sense of the imperative."},
    {"type": "matn",
     "ar": "(و«هيهات ذاك») بفتح التاء[[٤]] في الحجاز، وبكسرها في بني تميم، وبالضمة في لغة بعضهم (أي: بعد) مثال لما هو بمعنى الماضي،",
     "en": "(And “hayhāta dhāka”)—with fatḥa on the tāʾ in the Ḥijāz, with kasra among the Banū Tamīm, and with ḍamma in the dialect of some—(that is, it is far): an example of what has the sense of the past."},
    {"type": "matn",
     "ar": "وقدم الأمر لأن أكثر أسماء الأفعال بمعناه،",
     "en": "He put the imperative first because most verbal nouns have its sense."},
    {"type": "matn",
     "ar": "والذي حملهم على أن قالوا: إن هذه الكلمات وأمثالها ليست بأفعال مع تأديتها معاني الأفعال أمر لفظي، وهو أن صيغتها مخالفة لصيغ الأفعال[[٥]]، وأنها لا",
     "en": "What led them to say that these words and their like are not verbs, although they convey the meanings of verbs, is a formal matter: their forms differ from the forms of verbs, and they do not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أن المعنى لو كان على الإنشاء وهو الحق لم يكن صيغة الماضي على الحقيقة؛ إذ ليس المعنى على المضي،",
     "en": "Against this: if the meaning is performative—and that is the truth—then the past form would not be [used] in its proper sense, since the meaning is not one of pastness."},
    {"type": "pair",
     "ar": "فالظاهر في وجه بناء أسماء الأفعال ما قاله الشيخ الرضي. وهو أنها بنيت لكونها أسماء لما أصلها البناء. وهو مطلق الفعل سواء بقي على ذلك الأصل كالماضي والأمر، أو خرج عنه كالمضارع.",
     "en": "So the apparent account of the indeclinability of verbal nouns is what Shaykh al-Raḍī said: they are indeclinable because they are names of what is in origin indeclinable, namely the verb as such, whether it remained on that origin, like the past and the imperative, or departed from it, like the imperfect."},
    {"type": "pair",
     "ar": "فعلى هذا لا حاجة إلى العذر المذكور.",
     "en": "On this view there is no need for the excuse mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "في الأصل تصغير إرواد مصدر أرود أي: رفق صغر تصغير الترخيم أي: ارفق رفقا وإن كان صغيرا قليلا.",
     "en": "In origin it is the diminutive of irwād, the maṣdar of arwada (to be gentle), diminished by the curtailed diminutive (taṣghīr al-tarkhīm); that is, “be gentle, even if it be a small, slight gentleness”."},
    {"type": "pair",
     "ar": "ويجوز أن يكون تصغير رود بضم الراء وسكون الواو بمعنى الرفق تعدى إلى المفعول به مصدرا، أو اسم فعل بتضمينه الإمهال، وجعله بمعناه.",
     "en": "It may also be the diminutive of rūd—with ḍamma on the rāʾ and a quiescent wāw—meaning gentleness, extended to a direct object, as a maṣdar or as a verbal noun, by making it include the sense of granting respite and giving it that meaning."},
    {"type": "pair",
     "ar": "ونحو: رويدك زيدا يحتمل أن يكون اسم فعل، والكاف حرف، وأن يكون مصدرا مضافا إلى الفاعل.",
     "en": "Such as “ruwaydaka Zaydan” may be a verbal noun with the kāf a particle, or a maṣdar annexed to its agent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولما هو بمعنى المتعدي ككون هيهات مثلا لما هو بمعنى الماضي أو اللازم أو لما هو اسم فعل وغير اسم فعل، ولما هو اسم فعل فقط،",
     "en": "And [an example] of what has the sense of the transitive, just as “hayhāta” is an example of what has the sense of the past, or of the intransitive; or of what is a verbal noun and also something else, and of what is a verbal noun only;"},
    # REVIEW: «فيه قط» printed (clear at 700 dpi); «فقط» may be intended; transcribed as printed.
    {"type": "pair",
     "ar": "أو لما استعمل في معناه الأصلي، ولما يستعمل فيه قط",
     "en": "or of what has been used in its original meaning and of what is never [printed “qaṭṭ”] used in it."},
    {"type": "pair",
     "ar": "ورويد إما تصغير مخفف الإرواد بمعنى الرفق، وإما تصغير رود بالضم بمعنى الرفق عدى إلى المفعول لتضمين معنى الإمهال، أو جعله بمعناه.",
     "en": "“Ruwayd” is either the diminutive of the lightened form of irwād, meaning gentleness, or the diminutive of rūd, with ḍamma, meaning gentleness, extended to the object by including the sense of granting respite, or by giving it that meaning."},
    # The following paragraph is printed indented under fn. ٣, without a number.
    {"type": "pair",
     "ar": "قال عبد الغفور: وهو متعد ومستعمل فيما نقل عنه نحو: رويد زيدا أي: إرواده",
     "en": "ʿAbd al-Ghafūr said: it is transitive and used in what it was transferred from, as in “ruwayda Zaydan”, that is, “irwādahu” (granting him respite);"},
    {"type": "pair",
     "ar": "كما أن المثال الثاني مع أنه بمعنى الماضي لازم، وغير مستعمل فيما نقل عنه، ففي هذين المثالين إشارة إلى أقسامها.",
     "en": "just as the second example, besides having the sense of the past, is intransitive and not used in what it was transferred from. So these two examples point to their divisions."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: فتحت التاء نظرا إلى أصله حين كان مفعولا مطلقا جعل بمعنى الفعل، وكسرت للساكنين، وضمت للتنبيه بقوة الحركة على قوة معنى البعد؛ إذ معناه: ما أبعده،",
     "en": "Shaykh al-Raḍī said: the tāʾ was given fatḥa in view of its origin, when it was an absolute object (mafʿūl muṭlaq) made to bear the sense of the verb; kasra because of the two quiescents; and ḍamma to indicate, by the strength of the vowel, the strength of the sense of distance, since its meaning is “how far it is!”."},
    {"type": "pair",
     "ar": "وكان القياس على تقدير أن أصله هيهية كزلزلة ألا يوقف عليها إلا بالهاء.",
     "en": "On the supposition that its origin is hayhaya, like zalzala, analogy would require that one pause on it only with hāʾ."},
    {"type": "pair",
     "ar": "ولكن يوقف عليها في الأكثر بالتاء تنبيها على إلحاقها بالأفعال، فكان تاؤها تاء قامت.",
     "en": "But one mostly pauses on it with tāʾ, to indicate its being attached to the verbs, so its tāʾ is like the tāʾ of qāmat."},
    {"type": "pair",
     "ar": "وقال بعض النحاة: إن مفتوحة التاء مفردة كقوقاة، والوقف على الهاء.",
     "en": "Some grammarians said: the form with fatḥa on the tāʾ is singular, like qawqāt, and the pause is on hāʾ."},
    {"type": "pair",
     "ar": "وأما مكسورة التاء، فجمعت مفتوحة التاء مفردة كمسلمات، والوقف عليها بالتاء، والمضمومة التاء يحتمل الإفراد والجمع، فيجوز الوقف بالهاء والتاء.",
     "en": "As for the form with kasra on the tāʾ, the singular with fatḥa was made plural, like muslimāt, and the pause on it is with tāʾ; the form with ḍamma on the tāʾ admits both singular and plural, so one may pause with hāʾ or with tāʾ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وإن اللام تدخل على بعضها، وأن التنوين يلحق بعضها وهو تنوين التمكن.",
     "en": "And that the definite article enters some of them, and that nunation attaches to some of them, namely the nunation of full declinability (tanwīn al-tamakkun)."},
    {"type": "pair",
     "ar": "وعند بعضهم جرد عن التمكن، وجعل دليلا على كونه موصولا بما بعده كما أن حذفه دليل الوقف عليه.",
     "en": "According to some, it was stripped of [the sense of] full declinability and made an indication that the word is joined to what follows it, just as its omission is an indication of pausing on it."},
    {"type": "pair",
     "ar": "وذلك تنوين التنكير عند الجمهور، وليس لتنكير الفعل؛ لأنه غير صالح لذلك،",
     "en": "According to the majority it is the nunation of indefiniteness (tanwīn al-tankīr); it is not for making the verb indefinite, since the verb is not suited to that;"},
    {"type": "pair",
     "ar": "بل التنكير راجع إلى المصدر الذي ذلك الاسم قبل صيرورته اسم فعل كان بمعناه، وهو دليل على أن ما لحقه كان معرفا، فمعنى «صه» بلا",
     "en": "rather the indefiniteness goes back to the maṣdar whose meaning that noun had before it became a verbal noun; and it is an indication that what it attaches to was definite. So the meaning of “ṣah” without…"},
]
