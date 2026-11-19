# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 66 (printed ٦٥)."""

PAGE_NUMBER = 66
PRINTED_PAGE = "٦٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "العوامل[[١]]) أي: بسبب اختلاف العوامل الداخلة عليه[[٢]] في العمل، بأن يعمل بعضها[[٣]] خلافا ما يعمل البعض الآخر، وإنما خصصنا اختلافها[[٤]] بكونه[[٥]] في العمل، لئلا ينتقض[[٦]] بمثل قولنا: «إن زيدا مضروب»، و«إني ضربت زيدا»، و«إني ضارب زيد»، فإن العامل في «زيد» في هذه الصور مختلف بالاسمية، والفعلية، والحرفية، مع أن آخر المعرب لم يختلف باختلافها.",
     "en": "“…the governing agents (al-ʿawāmil)” — that is, by reason of the variation of the governing agents entering upon it with respect to governance (ʿamal), such that some of them govern differently from how the others govern. We restricted their variation to being “with respect to governance” only so that [the definition] not be invalidated by the likes of our saying: “inna Zaydan maḍrūbun” (verily Zayd is one struck), “innī ḍarabtu Zaydan” (verily I struck Zayd), and “innī ḍāribu Zaydin” (verily I am one striking Zayd); for the governing agent of “Zayd” in these constructions differs — being nominal, verbal, and particle-based [respectively] — even though the ending of the muʿrab did not vary with their variation."},

    {"type": "matn",
     "ar": "(لفظا أو تقديرا) نصب على التمييز، أي: يختلف لفظ آخره[[٧]]، أو تقديره[[٨]]، أو على المصدرية، أي: يختلف اختلاف لفظ أو تقدير[[٩]].",
     "en": "“Verbally or by estimation (lafẓan aw taqdīran)”: [these are] in the accusative as a specifier (tamyīz) — that is, the wording of its ending varies, or its estimated [ending] varies; or [they are accusative] as a verbal noun (maṣdariyya) — that is, it varies by a variation of wording or of estimation."},

    {"type": "matn",
     "ar": "والاختلاف لفظا: كما في قولك: «جاءني زيد»، و«رأيت زيدا»، و«مررت بزيد».",
     "en": "Variation verbally is as in your saying: “jāʾanī Zaydun” (Zayd came to me), “raʾaytu Zaydan” (I saw Zayd), and “marartu bi-Zaydin” (I passed by Zayd)."},

    {"type": "matn",
     "ar": "وتقديرا: كما في قولك: «جاءني فتى»، و«رأيت فتى»، و«مررت بفتى»، فإن أصله:",
     "en": "And by estimation is as in your saying: “jāʾanī fatan” (a youth came to me), “raʾaytu fatan” (I saw a youth), and “marartu bi-fatan” (I passed by a youth); for its origin is:"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: الفاعل لا يجمع على فواعل إلا اسما؟ قلت: فليكن جمع عاملة؛ لأن العامل قلما يكون غير كلمة. وقيل: العامل صار اسما في عرف النحاة.",
     "en": "If you say: [a word of the pattern] fāʿil is not pluralized as fawāʿil unless it is a noun [whereas “ʿāmil” is a participle]? I say: then let it be the plural of “ʿāmila”; for the governing agent is seldom other than a word (kalima). It has also been said: “ʿāmil” has become a noun in the usage of the grammarians."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما قيد بالعوامل الداخلة عليه؛ لأن معربا لا يخلو عن اختلاف العوامل في وقت ما، ولا يختلف آخره به، وإنما يختلف بسبب اختلاف العوامل الداخلة عليه.",
     "en": "He restricted [it] to the governing agents “entering upon it” only because a muʿrab is never free of a variation of governing agents at some moment, yet its ending does not vary merely by that; rather it varies by reason of the variation of the governing agents entering upon it."},
    {"type": "pair",
     "ar": "وهذا أولى مما قيل: خرج بهذا التقييد اختلاف آخر المستفهم عنه بكلمة «من» باعتبار العوامل الداخلة على المستفهم عنه نحو: من زيد؟ ومن زيدا؟ أو من زيد؟ إذا قيل: جاءني زيد، ورأيت زيدا، أو مررت بزيد.",
     "en": "This is preferable to what has been said, [namely] that by this restriction there is excluded the variation of the ending of the thing asked about by the word “man” (who?) in view of the governing agents entering upon the thing asked about — as in “man Zaydun?”, “man Zaydan?”, or “man Zaydin?” when it is said “jāʾanī Zaydun,” “raʾaytu Zaydan,” or “marartu bi-Zaydin.”"},
    {"type": "pair",
     "ar": "ثم تقييد العوامل بالداخلة عليه يخرج عامل المبدأ والخبر؛ لأن الدخول إما اللحوق بالآخر أو الأول، وذا لا يتصور في الأمور المعنوية.",
     "en": "Then restricting the governing agents by “those entering upon it” excludes the governing agent of the mubtadaʾ (subject) and the khabar (predicate) [i.e., the notional agent of ibtidāʾ]; for entering (dukhūl) is either attaching to the end or to the beginning, and that is not conceivable among purely notional matters (al-umūr al-maʿnawiyya)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: من العوامل.",
     "en": "That is: of the governing agents."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: اختلاف العوامل.",
     "en": "That is: the variation of the governing agents."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بكون الاختلاف واقعا.",
     "en": "That is: by the variation’s being one that actually occurs [in governance]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وليكون اللفظ محمولا على ما يقصد به في عرفهم إلا هو.",
     "en": "And so that the expression be construed according to what is intended by it in their [technical] usage — and nothing but that."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: صورة آخره.",
     "en": "That is: the [outward] form of its ending."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: يختلف آخره سواء كان بحسب التقدير نفس الآخر كما في مسلمي، أو تقديره وتقدير صفته كما في عصا وقاض، أو بحسب تقدير بالصفة فقط كما في حبلى وغلامي، فإن آخرهما لا يمتنع عن قبول الإعراب بحسب الفرض والحكم، وإن كان يمتنع عن قبوله بحسب الخارج.",
     "en": "That is: its ending varies — whether, by way of estimation, [what is estimated] is the ending itself, as in “muslimiyya” [i.e. muslimī]; or [both] it and the estimation of its attribute, as in “ʿaṣā” (a staff) and “qāḍin” (a judge); or by way of estimation of the attribute alone, as in “ḥublā” (pregnant) and “ghulāmī” (my servant) — for the ending of these two [latter] is not barred from receiving inflection by supposition and in effect (bi-ḥasab al-farḍ wa-l-ḥukm), even if it is barred from receiving it in external reality (bi-ḥasab al-khārij)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: اختلافا منسوبا إلى الصورة، أو إلى التقدير. وإنما لم يقل: اختلافا ملفوظا أو مقدرا باعتبار سببه بأن يجعل قوله: لفظا أو تقديرا تفصيلا للعوامل؛ لأن العامل قد يكون ملفوظا ومقدرا.",
     "en": "That is: a variation ascribed to the [outward] form or to estimation. He did not say “a spoken or an estimated variation” with respect to its cause — so as to make his words “verbally or by estimation” a detailing of the governing agents — because the governing agent may be spoken or estimated."},
    {"type": "pair",
     "ar": "أي: سواء كانت العوامل ملفوظة ومقدرة، لأن العامل لا ينحصر في الملفوظ والمقدر؛ لأنه قد يكون معنويا، ولا يلائم قوله الآتي: التقديري واللفظي في بيان إعراب الأسماء. وذلك لأن الظاهر أنه يشير إلى ما يشير إليه قوله: لفظا أو تقديرا.",
     "en": "That is: whether the governing agents are spoken or estimated — since the governing agent is not confined to the spoken and the estimated, for it may be notional (maʿnawī); and [because] that would not accord with his forthcoming statement, “the estimated and the verbal,” in expounding the inflection of nouns. That is because what is apparent is that he is pointing to the same thing to which his words “verbally or by estimation” point."},
]
