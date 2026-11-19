# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 281 (printed ٢٨٠)."""

PAGE_NUMBER = 281
PRINTED_PAGE = "٢٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ووقت مجاوزتهم أو مجاوزة» from the foot of PDF p. 280.
    {"type": "matn",
     "ar": "مجيئهم عمرا»، أو على الحالية بجعل المصدر بمعنى اسم الفاعل أي: «جاءوا خاليا بعضهم أو مجيئهم من زيد، ومجاوزا بعضهم أو مجيئهم عمرا».",
     "en": "…of their coming beyond ʿAmr”; or [it is in the accusative] as a circumstantial qualifier, by taking the maṣdar in the sense of the active participle, that is: “They came, some of them—or their coming—being free of Zayd, and some of them—or their coming—passing beyond ʿAmr.”"},
    {"type": "matn",
     "ar": "وعن الأخفش: أنه أجاز الجر بهما على أن «ما» فيهما زائدة،",
     "en": "It is reported from al-Akhfash that he allowed the genitive after them, on the view that “mā” in them is redundant (zāʾida)."},
    {"type": "matn",
     "ar": "ولعل هذا لم يثبت عند المصنف أو لم يعتد به، ولهذا لم يقل في الأكثر.",
     "en": "Perhaps this was not established for the author, or he did not take it into account; for this reason he did not say “in most [usage]” [here]."},
    {"type": "matn",
     "ar": "(و) كذا المستثنى منصوب بعد («ليس») نحو: «جاءني القوم ليس زيدا» (و) بعد («لا يكون»[[١]]) نحو: «سيجيء أهلك لا يكون بشرا»،",
     "en": "(And) likewise the excepted term is in the accusative after (“laysa”), as in “The people came to me, laysa Zayd,” (and) after (“lā yakūnu”), as in “Your family will come, lā yakūnu Bishr.”"},
    {"type": "matn",
     "ar": "وإنما يكون النصب بعدهما واجبا؛ لأنهما من الأفعال الناقصة الناصبة للخبر،",
     "en": "The accusative after them is necessary only because they are among the defective verbs (al-afʿāl al-nāqiṣa) that put the predicate in the accusative;"},
    {"type": "matn",
     "ar": "ويلزم إضمار اسمهما في باب الاستثناء، وهو ضمير راجع إلى اسم الفاعل من الفعل المذكور[[٢]]، أو إلى بعض من المستثنى منه مطلقا، وهما في التركيب في محل النصب على الحالية.",
     "en": "and their subject (ism) must be suppressed in the chapter on exception; it is a pronoun referring to the active participle of the verb mentioned, or to some part of the mustathnā minhu unspecified; and in the construction the two are in the position of the accusative as circumstantial qualifiers."},
    {"type": "matn",
     "ar": "واعلم أنه لا يستعمل هذه الأفعال إلا في المستثنى المتصل الغير المفرغ، ولا يتصرف فيها[[٣]]؛ لأنها قائمة مقام «إلا»، وهي لا يتصرف فيها.",
     "en": "Know that these verbs are used only with the conjoined excepted term (muttaṣil) that is not emptied (mufarragh), and they are not inflected; because they stand in place of “illā,” and it is not inflected."},
    {"type": "matn",
     "ar": "(ويجوز فيه) أي: في المستثنى (النصب) على الاستثناء (ويختار البدل) عن المستثنى منه (فيما بعد «إلا»[[٤]]) حال من الضمير المجرور،",
     "en": "(And in it is permitted), that is, in the excepted term, (the accusative) as an exception, (while the substitute [badal] is preferred) for the mustathnā minhu, (in what follows “illā”)—a circumstantial qualifier of the pronoun in the genitive—"},
    {"type": "matn",
     "ar": "أي: حال كون المستثنى واقعا محل يكون متأخرا عن «إلا»، احتراز عما إذا كان بعد سائر أدوات الاستثناء مثل «عدا وخلا» وغيرهما",
     "en": "that is, the excepted term being in a position where it comes after “illā”; this excludes the case where it comes after the other particles of exception, such as “ʿadā” and “khalā” and the like,"},
    {"type": "matn",
     "ar": "(في كلام غير موجب) احتراز عما إذا وقع في كلام موجب، فإنه منصوب وجوبا كما مر",
     "en": "(in non-affirmative speech): this excludes the case where it occurs in affirmative speech, for then it is necessarily in the accusative, as has preceded,"},
    {"type": "matn",
     "ar": "(و) الحال أنه (قد ذكر المستثنى منه) احتراز عما إذا لم يذكر المستثنى منه، فإنه حينئذ يعرب على حسب العوامل،",
     "en": "(and) the situation being that (the mustathnā minhu has been mentioned): this excludes the case where the mustathnā minhu is not mentioned, for then it is inflected according to the governors."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: ذكر المستثنى منه بغير «واو» على أنه صفة لكلام غير موجب، أي: كلام غير موجب ذكر فيه المستثنى منه،",
     "en": "In some copies [it reads]: “dhukira al-mustathnā minhu” without the “wāw,” as an adjective of “non-affirmative speech,” that is, non-affirmative speech in which the mustathnā minhu has been mentioned;"},
    {"type": "matn",
     "ar": "ولم يشترط ألا يكون منقطعا ولا مقدما على المستثنى منه؛ لأن",
     "en": "and he did not stipulate that it be neither disjoined nor placed before the mustathnā minhu, because…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يستعمل في موضعه غيره مثل: ما كان ولم يكن.",
     "en": "Nothing else is used in its place, such as “mā kāna” and “lam yakun.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يذكر هنا احتمال الرجوع إلى المصدر لعدم صحة أن يكون زيد خبرا عنه.",
     "en": "He did not mention here the possibility of [the pronoun] referring to the maṣdar, because “Zayd” cannot validly be a predicate of it."},
    {"type": "pair",
     "ar": "وفيه نظر لأن عدم صحة وقوع العين خبرا عن المصدر في الإثبات لا في النفي.",
     "en": "This is open to question, because a concrete entity (ʿayn) cannot validly be a predicate of a maṣdar in affirmation, not in negation."},
    {"type": "pair",
     "ar": "والأولى أن نفي زيد عن المجيء لا يوجب إخراج زيد عن المستثنى منه. فلذا لم يجوز رجوع الضمير إلى المصدر.",
     "en": "The better [explanation] is that denying Zayd of the coming does not entail extracting Zayd from the mustathnā minhu; that is why he did not allow the pronoun to refer to the maṣdar."},
    {"type": "pair",
     "ar": "نعم لو جعل زيدا مضافا إليه للمجيء، فيكون التقدير: ليس المجيء زيد يفيد المقصود، لكنه تكلف لفظا ومعنى، فافهم.",
     "en": "Yes, if “Zayd” were made the second term of a genitive construction with “the coming,” so that the implied form is “the coming [of] Zayd is not,” it would convey what is intended; but that is strained in wording and meaning. So understand."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولا يغير لا يكون إلى غيره مما يكون، وما كان، ولم يكن.",
     "en": "“Lā yakūnu” is not changed into other forms, such as “yakūnu,” “mā kāna” and “lam yakun.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حال من الضمير المجرور. وقيل: بدل منه.",
     "en": "A circumstantial qualifier of the pronoun in the genitive. It has also been said: a substitute for it."},
]
