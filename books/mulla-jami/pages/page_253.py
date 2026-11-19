# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 253 (printed ٢٥٢)."""

PAGE_NUMBER = 253
PRINTED_PAGE = "٢٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(أو شبهه) وهو ما يعمل عمل الفعل، وهو من تركيبه:» from the foot of PDF p. 252.
    {"type": "matn",
     "ar": "١-كاسم الفاعل نحو: «زيد ذاهب راكبا» و«زيد في الدار قاعدا» إن كان الظرف مقدرا باسم الفاعل.",
     "en": "…1. such as the active participle (ism al-fāʿil), as in “Zayd is going, riding,” and “Zayd is in the house, sitting,” if the adverbial phrase is construed with an implied active participle;"},
    {"type": "matn",
     "ar": "٢-وكاسم المفعول نحو: «زيد مضروب قائما».",
     "en": "2. and such as the passive participle (ism al-mafʿūl), as in “Zayd is struck, standing”;"},
    {"type": "matn",
     "ar": "٣-والصفة المشبهة نحو: «زيد حسن ضاحكا».",
     "en": "3. and the qualificative adjective (al-ṣifa al-mushabbaha), as in “Zayd is handsome, laughing.”"},
    {"type": "matn",
     "ar": "(أو معناه) المستنبط[[١]] من فحوى الكلام من غير التصريح به أو تقديره،",
     "en": "(Or its meaning), derived from the purport of the speech without its being stated explicitly or implied,"},
    {"type": "matn",
     "ar": "كالإشارة[[٢]] والتنبيه في نحو: «هذا زيد قائما» كما مر،",
     "en": "such as pointing and drawing attention in, for example, “This is Zayd, standing,” as has passed;"},
    {"type": "matn",
     "ar": "وكالنداء والتمني والترجي[[٣]] والتشبيه في نحو: «يا زيد قائما»، و«ليتك عندنا مقيما»، و«لعله في الدار قائما»، و«كأنه الأسد صائلا»[[٤]].",
     "en": "and such as vocation, wishing, hoping and likening in, for example, “O Zayd, standing!”, “Would that you were with us, staying!”, “Perhaps he is in the house, standing,” and “As though he were the lion, attacking.”"},
    {"type": "matn",
     "ar": "(وشرطها) أي: شرط الحال (أن تكون نكرة)؛ لأن النكرة[[٥]] أصل،",
     "en": "(Its condition), that is, the condition of the ḥāl, (is that it be indefinite—nakira); because the indefinite is the base,"},
    {"type": "matn",
     "ar": "والغرض وهو تقييد الحدث المنسوب إلى صاحبها يحصل لها، والتعريف زائد على الغرض.",
     "en": "and the purpose—restricting the event attributed to its owner—is attained by it, while definiteness is in excess of the purpose."},
    {"type": "matn",
     "ar": "(و) أن يكون (صاحبها معرفة)؛ لأنه محكوم عليه في المعنى، فكان الأصل فيه التعريف",
     "en": "(And) that (its owner be definite—maʿrifa); because it is the subject of a judgement in meaning, so definiteness is the base for it,"},
    {"type": "matn",
     "ar": "(غالبا) أي: ليس اشتراطها بكون صاحبها معرفة في جميع موادها، بل في غالب موادها أي: في أكثرها،",
     "en": "(for the most part), that is, its being conditioned on its owner’s being definite does not hold in all its instances, but in the majority of its instances, that is, in most of them."},
    {"type": "matn",
     "ar": "وبيان ذلك أن مواد وقوع الحال حالا على قسمين:",
     "en": "The explanation of this is that the instances in which the ḥāl occurs as a ḥāl are of two kinds:"},
    {"type": "matn",
     "ar": "أحدهما: ما يكون ذو الحال فيه نكرة موصوفة[[٦]] نحو: «جاءني رجل من بني تميم فارسا»",
     "en": "the first: that in which the owner of the ḥāl is a qualified indefinite, as in “A man of the Banū Tamīm came to me, on horseback,”"},
    {"type": "matn",
     "ar": "أو مغنية غناء المعرفة لاستغراقها[[٧]] نحو قوله تعالى: ﴿فيها يفرق كل",
     "en": "or one that suffices as a definite does because of its all-inclusiveness (istighrāq), as in His words, the Exalted: “Therein is made distinct every…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولا عمل لكل ما يستنبط، فإن إن وأن والاستفهام والنفي لا يعمل ما استنبط منها بل العمل سماعي،",
     "en": "Not everything that is derived governs; for what is derived from inna, anna, interrogation and negation does not govern—rather, government is a matter of attested usage (samāʿī)."},
    {"type": "pair",
     "ar": "وجعل حروف النداء منه مبني على ألا يكون المنادى بتقدير أدعو، بل العامل في المنادى حرف النداء، فهي ليست من العامل المعنوي عند المصنف.",
     "en": "Counting the vocative particles among it rests on the vocative (munādā) not being construed with an implied “I call”; rather, the governor of the munādā is the vocative particle—so for the author they are not among the semantic governors."},
    {"type": "pair",
     "ar": "ومما سمع عند النحاة التمني والترجي.",
     "en": "Among what the grammarians have heard [attested] are wishing and hoping."},
    {"type": "pair",
     "ar": "وخالفهم الشيخ الرضي في أن المعنى على تقييد خبر التمني بالحال لا على تقييد التمني.",
     "en": "Shaykh al-Raḍī disagreed with them, [holding] that the meaning is the restriction of the predicate of the wish by the ḥāl, not the restriction of the wishing."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "دون الاستفهام والنفي، وإن وأن من الحروف المشبهة لعدم ورود الاستعمال على عملها.",
     "en": "Not interrogation and negation, nor inna and anna among the particles resembling verbs, because usage is not attested for their governing [a ḥāl]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الظاهر أنهما ليسا بعاملين؛ لأنهما ليسا مقيدين، بل المقيد هو الخبر فهو العامل.",
     "en": "Shaykh al-Raḍī said: What appears is that these two do not govern, because they are not what is restricted; rather, what is restricted is the predicate, so it is the governor."},
    {"type": "pair",
     "ar": "فيه بحث لأنك إذا قلت: ليت ابني فقيرا راجع وجعلت فقيرا قيدا للخبر لكان المعنى ليت ابني راجع وهو فقير،",
     "en": "This is open to discussion: if you say “Would that my son, poor, were returning,” and take “poor” as a restriction of the predicate, the meaning would be “Would that my son were returning while he is poor”;"},
    {"type": "pair",
     "ar": "وليس المعنى على ذلك، بل معناه تمنيت ابني كان فقيرا راجعا.",
     "en": "yet that is not the meaning; rather its meaning is “I wished that my son, being poor, were returning.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وزيد كعمرو كاتبا، وزيد أسد صائلا بحذف أداة التشبيه.",
     "en": "And “Zayd is like ʿAmr, writing,” and “Zayd is a lion, attacking,” with the particle of likening elided."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: ولأن الحال جواب لكيف، والسؤال ينافي المعلومية.",
     "en": "It has been said: and because the ḥāl is the answer to “how?”, and a question is incompatible with [the thing’s] being known."},
    {"type": "pair",
     "ar": "وفيه أن المفعولية له جواب لـ«لم» مع أنه يصح أن يكون معلوما،",
     "en": "Against this: the object of purpose (mafʿūl lahu) is an answer to “why?”, although it may validly be known;"},
    {"type": "pair",
     "ar": "والحال أن المعلوم باعتبار يجوز أن يكون مجهولا باعتبار آخر.",
     "en": "and the fact is that what is known in one respect may be unknown in another."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لو قيل: «مخصوصة» بدل «موصوفة» ليشمل المخصوصة بالإضافة لكان أحسن.",
     "en": "Had “specified” (makhṣūṣa) been said instead of “qualified” (mawṣūfa), so as to include what is specified by annexation, it would have been better."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وعمومها بنفسها، أو بوقوعها في حيز نهي أو نفي أو ما بمعناه.",
     "en": "Its generality being either in itself or through its falling within the scope of a prohibition, a negation or what has their sense."},
]
