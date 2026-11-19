# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 380 (printed ٣٧٩)."""

PAGE_NUMBER = 380
PRINTED_PAGE = "٣٧٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإنه لو أريد بها معناها الاصطلاحي لكان هذا القول مستدركا؛» at the foot of PDF p. 379.
    {"type": "matn",
     "ar": "لأنه لإخراج مثل: «إذ وحيث»، وليس لهما صلة اصطلاحية.",
     "en": "… for it serves to exclude the like of “idh” and “ḥaythu”, and these have no relative clause in the technical sense."},
    {"type": "matn",
     "ar": "ولقائل أن يقول: يمكن أن يعرف الصلة[[١]] بما لا يتوقف معرفته على معرفة الموصول،",
     "en": "Someone might say: the relative clause can be defined by something whose knowledge does not depend on knowing the relative noun,"},
    {"type": "matn",
     "ar": "بأن يقال: الصلة جملة متصلة باسم لا يتم جزء إلا مع هذه الجملة المشتملة على عائد إليه،",
     "en": "by saying: the relative clause is a sentence attached to a noun that is not complete as a part except together with this sentence, which contains a pronoun returning to it."},
    {"type": "matn",
     "ar": "فعلى هذا يجوز أن يكون المراد بالصلة معناها الاصطلاحي، ولا يلزم الدور،",
     "en": "On this basis it is possible that the technical meaning of ṣila is intended, and no circularity follows;"},
    {"type": "matn",
     "ar": "وذكر العائد مع أنه مأخوذ في مفهوم الصلة[[٢]] الاصطلاحية تصريح بما علم ضمنا مبالغة في الاحتراز عن مثل: «إذ وحيث».",
     "en": "and the mention of the returning pronoun, though it is included in the concept of the technical ṣila, is an explicit statement of what was known implicitly, for emphasis in guarding against the like of “idh” and “ḥaythu”."},
    {"type": "matn",
     "ar": "ولما كانت الصلة[[٣]] بمعنييها أعم بحسب المفهوم من أن تكون خبرية أو غير خبرية، ولا تكون بحسب الواقع إلا خبرية،",
     "en": "Since the relative clause, in both its meanings, is more general in concept than being declarative (khabariyya) or non-declarative, while in fact it is only ever declarative;"},
    {"type": "matn",
     "ar": "والعائد أعم من أن يكون ضميرا أو غيره، وإذا كان ضميرا أعم من أن يكون للموصول أو لغيره، والواجب أن يكون ضميرا للموصول،",
     "en": "and the returning element is more general than being a pronoun or something else, and when it is a pronoun it is more general than being [a pronoun] of the relative noun or of something else, whereas what is required is that it be a pronoun of the relative noun,"},
    {"type": "matn",
     "ar": "عينهما بقوله: (وصلته) أي: صلة ما لا يتم جزء[[٤]] إلا بصلة وعائد",
     "en": "he specified both by saying: (and its relative clause), that is, the relative clause of that which is not complete as a part except with a relative clause and a returning pronoun,"},
    {"type": "matn",
     "ar": "(جملة خبرية[[٥]]) أو في معناها[[٦]] كاسمي الفاعل والمفعول[[٧]] (والعائد ضمير) لا غير ضمير[[٨]] (له) أي: للموصول لا لغيره.",
     "en": "(is a declarative sentence), or what has its meaning, such as the active and passive participles; (and the returning element is a pronoun), not something other than a pronoun, (of it), that is, of the relative noun, not of anything else."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يقال: إن تعريف الصلة يصدق على الشروط للأسماء الشرطية، نحو: «من تضربه أضربه»، و«ما تفعله أفعله» إلى غير ذلك",
     "en": "It should not be said: the definition of the relative clause applies to the conditions of conditional nouns, as in “man taḍribhu aḍribhu” (whomever you strike, I shall strike) and “mā tafʿalhu afʿalhu” (whatever you do, I shall do), and so on;"},
    {"type": "pair",
     "ar": "لأنا نقول \"من\" في قولنا: «من تضرب» مفعول تضرب، فهو جزء بدون جملة.",
     "en": "for we say: “man” in our saying “man taḍrib” is the object of taḍrib, so it is a part without a sentence."},
    # REVIEW: printed «الشرطة» (one expects «الشرطية»); transcribed as printed.
    {"type": "pair",
     "ar": "وبهذا عرفت أن من قال: بل يجب أن يحمل الصلة على الاصطلاحي، وإلا لزم نقض الحد بـ«من» الشرطة فقد سها سهوا بينا.",
     "en": "From this you know that whoever said “rather, ṣila must be taken in the technical sense, otherwise the definition would be broken by conditional ‘man’” has made an evident slip."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يخفى أنه تكلف، ومع ذلك يلزم أن يكون ما لا يتم جزءا لغوا لدخوله في مفهوم الصلة.",
     "en": "It is not hidden that this is forced; moreover, it would follow that “that which is not complete as a part” is superfluous, since it is included in the concept of the relative clause."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: ليس المقصود تعريف الصلة كما هو ظاهر السوق، حتى يرد أن التعريف غير مانع.",
     "en": "He means: the aim is not to define the relative clause, as the apparent course of the text suggests, so that the objection would arise that the definition is not exclusive (ghayr māniʿ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جعل الضمير راجعا إلى ما اعتبر الصلة بالقياس إليه لا إلى الموصول.",
     "en": "He made the pronoun refer to that in relation to which the relative clause is considered, not to the relative noun."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «بعرفه» (with bāʾ), evidently for «يعرفه»; transcribed as printed.
    {"type": "pair",
     "ar": "إنما كان كذلك لأن وضع الموصول على أن يطلقه المتكلم على ما يعتقد أن المخاطب بعرفه بكونه محكوما عليه بحكم معلوم الحصول له.",
     "en": "It is so only because the relative noun is assigned so that the speaker applies it to what he believes the addressee knows as being the subject of a judgement known to hold of it."},
    {"type": "pair",
     "ar": "وذلك لا يتصور إلا في الجملة الخبرية.",
     "en": "That is conceivable only in a declarative sentence."},
    {"type": "pair",
     "ar": "وأما وقوع الجملة القسمية صلة كقوله تعالى: ﴿وإن منكم لمن ليبطئن﴾ (النساء: ٧٢)؛ فلأن الصلة هي جواب القسم، وهو جملة خبرية.",
     "en": "As for an oath sentence occurring as a relative clause, as in His words, the Exalted, “And among you is he who lags behind” (Qurʾān, Sūrat al-Nisāʾ 4:72), it is because the relative clause is the answer to the oath, and that is a declarative sentence."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا حاجة إلى هذا التأويل؛ لأن اسم الفاعل والمفعول مع مرفوعهما مركبان تامان خبريان.",
     "en": "There is no need for this interpretation, because the active and passive participles together with their nominatives are complete, declarative compounds."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فلا حاجة حينئذ إلى القول بأن قوله: وصلة الألف واللام اسم فاعل أو مفعول بمنزلة الاستثناء.",
     "en": "So there is then no need to say that his words “the relative clause of alif-lām is an active or passive participle” are in the position of an exception."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لم يفرق المالكي في التسهيل بين العائد إلى المبتدأ والموصول، فالحق أن المراد بالضمير أعم منه وما ينوب منابه.",
     "en": "Al-Mālikī [Ibn Mālik] in al-Tashīl did not distinguish between the element returning to the subject and that returning to the relative noun; so the truth is that what is meant by “pronoun” is more general: it and what stands in its place."},
    {"type": "pair",
     "ar": "قال عبد الغفور: إلا نادرا، فإنه قد يجيء الظاهر موضع الضمير.",
     "en": "ʿAbd al-Ghafūr said: “except rarely, for the overt noun sometimes comes in place of the pronoun.”"},
]
