# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 452 (printed ٤٥١)."""

PAGE_NUMBER = 452
PRINTED_PAGE = "٤٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 451 ends with a complete sentence («… مفعولا مطلقا.»); this page opens a new one.
    # REVIEW: printed «كتب الصريف»; the expected word is «التصريف» (cf. «علم التصريف» below). Transcribed as printed, translated as «التصريف».
    {"type": "matn",
     "ar": "(وهو) أي: المصدر (من الثلاثي) المجرد (سماع) أي: سماعي، ويرتقي عدده إلى اثنين وثلاثين كما بين في كتب الصريف",
     "en": "(And it), that is, the verbal noun, (from the) bare (triliteral is by attestation), that is, known by hearing (samāʿī); its number rises to thirty-two, as has been set out in the books of morphology (taṣrīf),"},
    {"type": "matn",
     "ar": "(وفي غيره) أي: غير الثلاثي المجرد، يعني: الثلاثي المزيد فيه والرباعي المجرد والمزيد فيه (قياس) أي: قياسي،",
     "en": "(and in what is other than it), that is, other than the bare triliteral, meaning the augmented triliteral and the bare and augmented quadriliteral, (it is by analogy), that is, regular (qiyāsī),"},
    {"type": "matn",
     "ar": "كما تقول: كل ما ماضيه على «أفعل» فمصدره على «إفعال»، وكل ما ماضيه على «استفعل» فمصدره على «استفعال»",
     "en": "as you say: everything whose past tense is on the pattern “afʿala” has its verbal noun on the pattern “ifʿāl”, and everything whose past tense is on “istafʿala” has its verbal noun on “istifʿāl”,"},
    {"type": "matn",
     "ar": "(مثل: «أخرج إخراجا» و«استخرج استخراجا») إلى غير ذلك مما علمته في علم التصريف.",
     "en": "(as in “akhraja ikhrājan” (he brought out) and “istakhraja istikhrājan” (he extracted)), and so on, as you have learned in the science of morphology (taṣrīf)."},
    {"type": "matn",
     "ar": "(ويعمل[[١]]) أي: المصدر بالقطع (عمل فعله[[٢]]) المشتق منه حال كونه (ماضيا) نحو: «أعجبني ضرب زيد عمرا أمس»",
     "en": "(And it governs), that is, the verbal noun, definitely, (as its verb governs), the verb derived from it, whether it is (past), as in “Zayd’s striking ʿAmr yesterday pleased me”,"},
    {"type": "matn",
     "ar": "(و) حال كونه (غيره) أي: غير الماضي -مستقبلا كان أو حالا- نحو: «أعجبني إكرام عمرو خالدا غدا أو الآن»،",
     "en": "(or) whether it is (other than it), that is, other than past, whether future or present, as in “ʿAmr’s honouring Khālid tomorrow, or now, pleased me”;"},
    {"type": "matn",
     "ar": "وذلك العمل لمناسبة الاشتقاق بينهما لا باعتبار الشبه[[٣]]، فلهذا لم يشترط فيه الزمان كاسمي الفاعل والمفعول",
     "en": "this governing is due to the affinity of derivation between the two, not by virtue of resemblance; for this reason time is not made a condition in it, as it is in the active and passive participles,"},
    {"type": "matn",
     "ar": "(إذا لم يكن مفعولا مطلقا) يعني: عمل المصدر عمل فعله بالقطع مشروط بألا يكون مفعولا مطلقا أصلا، فإنه إذا كان مفعولا مطلقا، فسيجيء حكمه.",
     "en": "(when it is not an absolute object), meaning: the verbal noun’s governing as its verb governs, definitely, is conditional on its not being an absolute object at all; for when it is an absolute object, its rule will come later."},
    {"type": "matn",
     "ar": "(ولا يتقدم معموله[[٤]]) أي: معمول المصدر (عليه) لكونه بتقدير الفعل مع «أن»، وشيء مما في حيز «أن» لا يتقدم عليه، فلا يقال: «أعجبني عمرا ضرب زيد».",
     "en": "(And what it governs does not precede), that is, what the verbal noun governs, (it), because it is to be construed as the verb with “an”, and nothing within the domain of “an” precedes it; so one does not say “aʿjabanī ʿAmran ḍarbu Zaydin”."},
    {"type": "matn",
     "ar": "(ولا يضمر) أي: معموله (فيه) أو يكون الظرف مفعول ما لم يسم فاعله؛",
     "en": "(And it is not concealed), that is, what it governs, (in it), or else the adverbial [phrase “fīhi”] is the object of [a verb] whose agent is not named;"},
    {"type": "matn",
     "ar": "لأنه لو أضمر فيه لأضمر في المثنى والمجموع قياسا على الواحد، فيلزم اجتماع التثنيتين والجمعين نظرا إلى المصدر والفاعل،",
     "en": "for if [the agent] were concealed in it, it would be concealed in the dual and the plural by analogy with the singular, and two duals and two plurals would then come together, with regard to the verbal noun and the agent;"},
    {"type": "matn",
     "ar": "ولما كان تثنية الفعل وجمعه راجعين في الحقيقة إلى الفاعل، وكذا في اسمي الفاعل والمفعول والصفة المشبهة لا يلزم فيها",
     "en": "and since the dual and plural of the verb in reality go back to the agent, and likewise in the active and passive participles and the resembling adjective (al-ṣifa al-mushabbaha), there does not follow in them…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بشروطه، وهي أن تكون مظهرا مكبرا غير محدود ولا منعوت قبل تمامه، كذا في التسهيل.",
     "en": "[It governs] under its conditions: that it be overt, non-diminutive, not delimited, and not qualified before its completion; so in al-Tashīl."},
    {"type": "pair",
     "ar": "فلا يعمل المضمر والمصغر والمحدود، وهو الدال على المرة والمنعوت قبل استيفاء ما يتعلق به من مفعول ومجرور وغيره.",
     "en": "So the concealed [verbal noun], the diminutive and the delimited, namely that which denotes a single instance, do not govern, nor does the one qualified before it has taken in what attaches to it, whether object, genitive or other."},
    {"type": "pair",
     "ar": "وفي كل منها اختلاف من النحاة مذكور في شرح المصري.",
     "en": "On each of these there is disagreement among the grammarians, mentioned in the commentary of al-Miṣrī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: من اللازم والمتعدي بنفسه أو بحرف.",
     "en": "That is, whether intransitive, or transitive by itself or by means of a particle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إذ لا مشابهة بينه وبين الفعل لا لفظا لعدم موازنته إياه ولا معنى لعدم صحة إقامته مقامه",
     "en": "For there is no resemblance between it and the verb, neither in wording, since it does not match its measure, nor in meaning, since it cannot validly be put in its place;"},
    # REVIEW: printed «بخلافه اسم الفاعل»; the expected form is «بخلاف اسم الفاعل». Transcribed as printed, translated as «بخلاف».
    {"type": "pair",
     "ar": "بخلافه اسم الفاعل والمفعول، فإنهما يعملان لمشابهة الفعل لفظا ومعنى دون الاشتقاق لعدم اشتقاقهما منه عند الجمهور،",
     "en": "unlike the active and passive participles, for they govern because of their resemblance to the verb in wording and meaning, not because of derivation, since according to the majority they are not derived from it;"},
    {"type": "pair",
     "ar": "فاشتراط كونهما بمعنى الحال والاستقبال لتقوية تلك المشابهة.",
     "en": "so the condition that they have the sense of the present or the future is to strengthen that resemblance."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جوز الشارح الرضي تقديم الظرف والجار والمجرور.",
     "en": "The commentator al-Raḍī permitted the adverbial and the preposition with its object to precede."},
]
