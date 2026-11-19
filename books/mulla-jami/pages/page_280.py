# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 280 (printed ٢٧٩)."""

PAGE_NUMBER = 280
PRINTED_PAGE = "٢٧٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وهو في الأصل لازم يتعدى إلى المفعول» from the foot of PDF p. 279.
    {"type": "matn",
     "ar": "بـ«من» نحو: «خلت الديار من الأنيس»، وقد يضمن معنى «جاوز»، ويحذف «من» ويوصل الفعل فيتعدى بنفسه،",
     "en": "…by means of “min,” as in “The dwellings were empty of any companion”; but it may be made to imply the sense of “jāwaza” (to pass beyond), or “min” may be elided and the verb joined [directly], so that it becomes transitive by itself."},
    {"type": "matn",
     "ar": "والتزموا هذا التضمين أو الحذف والإيصال في باب الاستثناء، ليكون ما بعدها في صورة المستثنى بـ«إلا» التي هي أم الباب[[١]]،",
     "en": "They made this implication, or the elision and joining, obligatory in the chapter on exception, so that what follows these [two] would take the form of what is excepted by “illā,” which is the principal particle of the chapter (umm al-bāb)."},
    {"type": "matn",
     "ar": "وفاعلهما ضمير راجع إما إلى مصدر الفعل المتقدم، أو إلى اسم الفاعل منه[[٢]]، أو إلى بعض مطلق من المستثنى منه[[٣]]،",
     "en": "Their agent (fāʿil) is a pronoun referring either to the maṣdar of the preceding verb, or to its active participle, or to an unspecified part of the mustathnā minhu;"},
    {"type": "matn",
     "ar": "والتقدير: «جاءني القوم عدا أو خلا مجيئهم أو الجائي منهم أو بعض منهم زيدا»، وهما في محل النصب على الحالية[[٤]]،",
     "en": "the implied form is: “The people came to me, their coming—or the one of them who came, or some of them—having passed beyond (ʿadā) or being free of (khalā) Zayd.” The two are in the position of the accusative as circumstantial qualifiers (ḥāl);"},
    {"type": "matn",
     "ar": "ولم يظهر معهما «قد» ليكونا أشبه بـ«إلا» التي هي الأصل في باب الاستثناء",
     "en": "and “qad” does not appear with them, so that they bear more resemblance to “illā,” which is the base in the chapter on exception."},
    {"type": "matn",
     "ar": "(في الأكثر) أي: النصب بهما إنما هو في أكثر الاستعمالات[[٥]]؛ لأنهما فعلان ماضيان كما عرفت، وقد أجيز الجر بهما على أنهما حرفا جر.",
     "en": "(In most [usage]), that is, the accusative after them is only in most usages, because they are two past-tense verbs, as you have learned; and the genitive after them has been allowed, on the view that they are two prepositions (ḥarfā jarr)."},
    {"type": "matn",
     "ar": "قال السيرافي: لم أعلم خلافا في جواز الجر بهما إلا أن النصب بهما أكثر.",
     "en": "Al-Sīrāfī said: I know of no disagreement over the permissibility of the genitive after them, except that the accusative after them is more frequent."},
    {"type": "matn",
     "ar": "(أو «ما خلا، وما عدا») أي: المستثنى منصوب أيضا وجوبا إذا كان بعد «ما خلا، وما عدا»؛ لأن «ما» فيهما مصدرية مختصة بالأفعال",
     "en": "(Or “mā khalā” and “mā ʿadā”), that is, the excepted term is likewise necessarily in the accusative when it comes after “mā khalā” and “mā ʿadā,” because “mā” in them is the maṣdar-forming particle (maṣdariyya), restricted to verbs,"},
    {"type": "matn",
     "ar": "نحو: «جاءني القوم ما خلا زيدا، وما عدا عمرا»، تقديره: «خلو زيد، وعدو عمرو»[[٦]] بالنصب على الظرفية بتقدير مضاف",
     "en": "as in “The people came to me, mā khalā Zayd and mā ʿadā ʿAmr”; its implied form is “khuluwwa Zayd, and ʿadwa ʿAmr,” in the accusative as an adverb of time, with an implied first term of a genitive construction (muḍāf),"},
    {"type": "matn",
     "ar": "أي: «وقت خلوهم[[٧]] أو خلو مجيئهم من زيد ووقت مجاوزتهم أو مجاوزة",
     "en": "that is: “at the time of their being free—or of their coming being free—of Zayd, and at the time of their passing beyond, or the passing beyond…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأنها موضوعة للاستثناء. وما عداها ليست موضوعة له، بل موضوعة لمعان أخر من المغايرة والظرفية والمجاوزة والخلو والنفي وغير ذلك استعملت في الاستثناء بضرب من المناسبة.",
     "en": "Because it was coined for exception. What is besides it was not coined for it, but for other meanings—otherness, adverbial location (ẓarfiyya), passing beyond, being free, negation and so on—and was used for exception by a kind of affinity."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لدلالة الفعل على صاحبه.",
     "en": "Because the verb indicates its doer."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن الضمير راجع إلى بعض منكر للاستغراق في الإيجاب، كما في ﴿علمت نفس﴾ (سورة الانفطار:٥) أي: كل نفس.",
     "en": "He means: the pronoun refers to an indefinite “some” denoting all-inclusiveness (istighrāq) in affirmation, as in “A soul shall know” (Qurʾān, Sūrat al-Infiṭār 82:5), that is, every soul."},
    {"type": "pair",
     "ar": "وإنما قلنا: إلى بعض منكر لدلالة قوله: فيما بعد أو بعض منهم، ولقلة عموم النكرة في الإثبات إذا كان فاعلا.",
     "en": "We said “to an indefinite ‘some’” only because his words further on, “or some of them,” indicate it, and because an indefinite noun is seldom general in affirmation when it is an agent."},
    {"type": "pair",
     "ar": "تكلف من قال: يستعمل البعض بمعنى الكل، وأريد منه ههنا هذا المعنى.",
     "en": "Whoever said that “some” is used in the sense of “all,” and that this sense is meant here, has strained [the text]."},
    {"type": "pair",
     "ar": "والأوجه أن الضمير راجع إلى بعض المضاف، أي: خلا بعضهم، والإضافة للاستغراق.",
     "en": "The better view is that the pronoun refers to “some” in a genitive construction, that is, “some of them was free,” the genitive construction denoting all-inclusiveness."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأحسن أن «خلا» في تقدير زمان مضاف إلى زمان خلا زيدا كما في مذ سافر، فيطابق في المعنى ما خلا.",
     "en": "It is better that “khalā” be taken as implying a time noun in a genitive construction—“the time [when] it was free of Zayd”—as in “mudh sāfara” (since he travelled); it then agrees in meaning with “mā khalā.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأنسب أن يجعل المستثنى المنقطع والمستثنى بخلا مما يختار فيه النصب.",
     "en": "It is more fitting to class the disjoined excepted term and the term excepted by “khalā” among those in which the accusative is preferred [rather than necessary]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهذا لا يستقيم؛ لأن الفعل المسند إلى الفاعل المستتر إذا صار في تقدير المصدر يكون في تقدير المصدر المضاف إلى الفاعل،",
     "en": "This is not sound, because when a verb attributed to a concealed agent comes to be taken as a maṣdar, it is taken as a maṣdar in a genitive construction with its agent;"},
    {"type": "pair",
     "ar": "فيكون تقديره: «خلوه زيدا» على أن الضمير راجع إلى المجيء أو الجائي أو البعض.",
     "en": "so its implied form is “its being free of Zayd” (khuluwwuhu Zaydan), the pronoun referring to the coming, or the one who came, or the “some.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الظاهر خلو بعضهم. وكذا في قوله: وقت مجاوزتهم.",
     "en": "What is apparent is “the being free of some of them”; likewise in his words “at the time of their passing beyond.”"},
    {"type": "pair",
     "ar": "ولا وجه للاقتصار على التوجيهين لاحتمال رجوع ضمير «ما خلا» إلى الجائي أيضا كما سبق في «خلا».",
     "en": "There is no reason to restrict [it] to the two explanations, since the pronoun of “mā khalā” may also refer to “the one who came,” as preceded under “khalā.”"},
]
