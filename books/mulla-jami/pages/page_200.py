# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 200 (printed ١٩٩)."""

PAGE_NUMBER = 200
PRINTED_PAGE = "١٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues from p.199: «… أو للنيابة أي: نيابة لفظية بأن يكون النائب»
    {"type": "matn",
     "ar": "ملفوظا أو تقديريا بأن يكون النائب مقدرا كما في المثالين المذكورين أو للمنادى[[١]]،",
     "en": "…uttered, or an implied [representation], in that the representative is implied, as in the two examples mentioned; or [the qualification “verbally or by implication” applies] to the vocative noun (munādā),"},
    {"type": "matn",
     "ar": "والمنادى الملفوظ مثل: «يا زيد»، والمقدر مثل: ﴿ألا يا اسجدوا﴾[[٢]] أي: «ألا يا قوم اسجدوا».",
     "en": "the uttered munādā being as in “O Zayd” (yā Zaydu), and the implied one as in “Will they not—O, prostrate yourselves” (alā yā-sjudū), that is: “Will you not, O people, prostrate yourselves.”"},
    {"type": "matn",
     "ar": "وانتصاب المنادى عند سيبويه على أنه مفعول به، وناصبه الفعل المقدر[[٣]]،",
     "en": "According to Sībawayh, the munādā is in the accusative as a direct object (mafʿūl bihi), and what puts it in the accusative is the implied verb."},
    {"type": "matn",
     "ar": "وأصل «يا زيد»: أدعو زيدا، فحذف الفعل حذفا لازما، لكثرة استعماله، ولدلالة حرف النداء عليه وإفادته فائدته.",
     "en": "The underlying form of “yā Zaydu” is “I call Zayd” (adʿū Zaydan); the verb was elided by obligatory elision, because of its frequent use, and because the vocative particle (ḥarf al-nidāʾ) indicates it and conveys what it conveys."},
    {"type": "matn",
     "ar": "وعند المبرد بحرف النداء؛ لسده مسد الفعل[[٤]].",
     "en": "According to al-Mubarrad, [it is in the accusative] by the vocative particle, because it stands in place of the verb."},
    {"type": "matn",
     "ar": "وقال أبو علي[[٥]] في بعض كلامه: إن «يا وأخواته» أسماء أفعال،",
     "en": "Abū ʿAlī said in one of his statements that “yā and its sisters” are verbal nouns (asmāʾ afʿāl)."},
    {"type": "matn",
     "ar": "فعلى هذين المذهبين لا يكون من هذا الباب أي: مما انتصب المفعول به بعامل واجب الحذف.",
     "en": "On these two doctrines, then, it does not belong to this section, that is: to [the cases] in which the direct object is put in the accusative by a governor whose elision is obligatory."},
    {"type": "matn",
     "ar": "وعلى المذاهب كلها مثل: «يا زيد» جملة، وليس المنادى أحد جزئي الجملة،",
     "en": "On all the doctrines, something like “yā Zaydu” is a sentence (jumla), and the munādā is not one of the two parts of the sentence."},
    {"type": "matn",
     "ar": "فعند سيبويه كلا جزئي الجملة أي: الفعل والفاعل مقدران.",
     "en": "For according to Sībawayh both parts of the sentence, that is, the verb and the agent (fāʿil), are implied."},
    {"type": "matn",
     "ar": "وعند المبرد: حرف النداء قائم مقام أحد جزئي الجملة أي: الفعل والفاعل مقدر[[٦]].",
     "en": "According to al-Mubarrad, the vocative particle stands in place of one of the two parts of the sentence, that is, the verb, and the agent is implied."},
    {"type": "matn",
     "ar": "وعند أبي علي: أحد جزأيها اسم الفعل، والآخر ضمير مستتر فيه.",
     "en": "According to Abū ʿAlī, one of its two parts is the verbal noun, and the other is a pronoun latent in it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بأن يكون حالا من ضمير «إقباله».",
     "en": "In that it is a circumstantial qualifier (ḥāl) of the pronoun in “iqbāluhu” (his coming forward)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النمل: ٢٥.",
     "en": "Qurʾān, Sūrat al-Naml 27:25."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو ينصب المصدر اتفاقا، نحو: «يا زيد» دعاء حقا،",
     "en": "It puts the maṣdar in the accusative by agreement, as in “yā Zaydu,” a true call (duʿāʾan ḥaqqan);"},
    {"type": "pair",
     "ar": "والحال أيضا عند المبرد نحو: «يا زيد قائما» إذا ناديته في حال القيام.",
     "en": "and also the ḥāl according to al-Mubarrad, as in “yā Zaydu qāʾiman” when you call him while he is standing."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن القول بأنه ساد مسد الفعل يستدعي بحسب الظاهر أن يكون نسبة العمل إليه مجازا.",
     "en": "Against this: the claim that it stands in place of the verb requires, on the face of it, that ascribing government (ʿamal) to it be figurative (majāz)."},
    {"type": "pair",
     "ar": "والظاهر أن سيبويه يجوز هذا المجاز.",
     "en": "It appears that Sībawayh allows this figurative usage."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "رد بأن الهمزة من أدوات النداء، واسم الفاعل لا يكون أقل من حرفين،",
     "en": "This was rejected [on three grounds]: that the hamza is among the vocative particles, while a verbal noun is not shorter than two letters;"},
    # REVIEW: «واسم الفاعل» as printed; the argument concerns اسم الفعل (verbal noun).
    {"type": "pair",
     "ar": "وبأن ضمير المتكلم لا يستتر في اسم الفعل، وبأنه لو كان اسم فعل لتم بدون المنادى لكونه جملة.",
     "en": "that the first-person pronoun is not latent in a verbal noun; and that, were it a verbal noun, it would be complete without the munādā, since it would be a sentence."},
    {"type": "pair",
     "ar": "وأجيب عن الأول: بأن أدوات النداء لكثرة استعمالاتها جاز فيها ما لا يجوز في غيرها، ألا ترى إلى الترخيم.",
     "en": "To the first it was answered that, because the vocative particles are used so frequently, what is not allowed in other words is allowed in them; consider truncation (tarkhīm)."},
    {"type": "pair",
     "ar": "وعن الثاني: بأنه قد يستتر نحو «أف» بمعنى «أتضجر».",
     "en": "To the second: that it is sometimes latent, as in “uff” in the sense of “I am vexed” (ataḍajjaru)."},
    {"type": "pair",
     "ar": "وعن الثالث: بأنه قد يعرض للجملة ما لا يستقل به كلاما كالجملة القسمية والشرطية.",
     "en": "To the third: that something may befall a sentence by which it is not independent as speech (kalām), like the oath sentence and the conditional sentence."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن الحرف لا يقوم مقام الفعل في إفادة معناه، والفاعل ضمير مستتر لا يكون أيضا مقدرا إلا بتبعية الفعل،",
     "en": "Against this: the particle does not stand in place of the verb in conveying its meaning, and the agent, being a latent pronoun, is likewise implied only as a dependent of the verb."},
    {"type": "pair",
     "ar": "فلا بد أن يحمل كلام المبرد على أن الحرف قائم مقام الفعل في العمل، وكلا جزئي الجملة مقدران.",
     "en": "So al-Mubarrad’s statement must be taken to mean that the particle stands in place of the verb in government, and that both parts of the sentence are implied."},
]
