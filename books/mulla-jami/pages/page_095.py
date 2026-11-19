# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 95 (printed ٩٤)."""

PAGE_NUMBER = 95
PRINTED_PAGE = "٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "والتقديري[[١]] إنما هو باعتبار كون ذلك الأصل محققا أو مقدرا.",
     "en": "The presumptive [origin] is [determined] only by regarding that origin as being either actualized or merely presumed."},
    {"type": "matn",
     "ar": "وأما اعتبار إخراج المعدول عن ذلك الأصل ليتحقق العدل، فلا دليل عليه إلا منع الصرف.",
     "en": "As for taking into account the removal of the deviated form (al-maʿdūl) from that origin so that the deviation (ʿadl) may be realized — there is no evidence for it except its being denied full inflection (manʿ al-ṣarf)."},
    {"type": "matn",
     "ar": "فعلى هذا قوله: (تحقيقا[[٢]]) معناه: خروجا كائنا عن أصل محقق، يدل عليه دليل غير منع الصرف.",
     "en": "Accordingly, his words “taḥqīqan” (actually) mean: a deviation issuing from an actualized origin, indicated by evidence other than the denial of full inflection."},
    {"type": "matn",
     "ar": "(ك«ثلاث ومثلث»[[٣]])، والدليل على أن أصلهما في معناهما تكرارا دون لفظهما.",
     "en": "(As in “thulātha” and “mathlath”); the evidence that their origin lies in the repetition present in their meaning, not in their wording."},
    {"type": "matn",
     "ar": "والأصل: أنه إذا كان المعنى مكررا يكون اللفظ أيضا مكررا، كما في «جاءني القوم ثلاثة ثلاثة»[[٤]].",
     "en": "The principle is that when the meaning is repeated, the wording too is repeated, as in “the people came to me three by three (thalāthatan thalāthatan).”"},
    {"type": "matn",
     "ar": "فعلم أن أصلهما لفظ مكرر، وهو «ثلاثة ثلاثة».",
     "en": "So it is known that their origin is a repeated expression, namely “thalātha thalātha.”"},
    {"type": "matn",
     "ar": "وكذا الحال في «أحاد» و«موحد» و«ثناء» و«مثنى» إلى «رباع»[[٥]] و«مربع» بلا خلاف، وفيما وراءها إلى «عشار ومعشر» خلاف، والصواب مجيئها.",
     "en": "The same holds for “uḥād” and “muwaḥḥad,” “thunāʾ” and “mathnā,” up to “rubāʿ” and “marbaʿ” without dispute; concerning what lies beyond them up to “ʿushār” and “maʿshar” there is disagreement, but the correct view is that they do occur."},
    {"type": "matn",
     "ar": "والسبب[[٦]] في منع صرف «ثلاث ومثلث»، وأخواتهما العدل والوصف؛ لأن الوصفية العرضية التي كانت في «ثلاثة ثلاثة»[[٧]] صارت أصلية في «ثلاث ومثلث»",
     "en": "The cause of denying full inflection to “thulāth” and “mathlath” and their sisters is [both] deviation (ʿadl) and adjectival quality (waṣf); for the accidental adjectival quality that was present in “thalātha thalātha” became intrinsic in “thulāth” and “mathlath”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "المشهور أن انقسام العدل إليهما ليس باعتبار الأصل، بل باعتبار أن عدل بعض الأمثلة ثابت بغير منع الصرف، وعدل بعضها ثابت بمجرد منع الصرف.",
     "en": "The well-known view is that the division of deviation into these two [the actualized and the presumptive] is not by regard to the origin, but by regard to the fact that the deviation of some examples is established by something other than the denial of inflection, while the deviation of others is established by the denial of inflection alone."},
    {"type": "pair",
     "ar": "ولعل وجهه أن إثبات الأصل قصدا إثبات للفرع ضمنا، فإذا ثبت بدليل غير منع الصرف أن أصل «ثلاث»: ثلاثة ثلاثة، ثبت أن «ثلاث» فرعه، وليس فرعيته لذلك الأصل إلا باعتبار المعدول عنه، فقد ثبت العدل بدليل غير منع الصرف.",
     "en": "Perhaps its rationale is that establishing the origin directly is implicitly establishing the derivative; so when it is established by evidence other than the denial of inflection that the origin of “thulāth” is “thalātha thalātha,” it is established that “thulāth” is its derivative — and its being a derivative of that origin is only by regard to that from which it deviated. Thus the deviation has been established by evidence other than the denial of inflection."},
    {"type": "pair",
     "ar": "إن قلت: فكيف يصح قوله الآتي فلا دليل عليه إلا منع الصرف؟",
     "en": "If you say: How, then, can his forthcoming statement be valid — “there is no evidence for it except the denial of inflection”?"},
    {"type": "pair",
     "ar": "قلنا: أراد به أن الدليل المؤثر المثبت أولا للعدل في نظر النحاة واعتبارهم ليس إلا منع الصرف أو ضرورة مثله. وأما ثبوت العدل فيما لا ضرورة فيه كما سيجيء فبالعرض.",
     "en": "We answer: he meant by it that the effective evidence which first establishes the deviation, in the view and consideration of the grammarians, is nothing but the denial of inflection or a comparable necessity. As for the establishment of deviation in a case where there is no such necessity, as will come, that is only incidental."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وصف بحال المتعلق. وأما على المشهور فمعناه: خروج تحقيق، أي خروجا محققا كرجل سواء بمعنى رجل مسيء، فيكون وصفه بالتحقيق وصفا بحال نفسه، وكذا معنى قوله: تقديرا.",
     "en": "It is a qualification by the state of that which is related to it. On the well-known view, however, its meaning is “a deviation of actualization,” that is, an actualized deviation — like “a bad man (rajul sawāʾ)” meaning “a wrongdoing man” — so that its qualification by “actualization” is a qualification by its own state; and likewise is the meaning of his words “taqdīran” (presumptively)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صفة بعد صفة لـ«خروجا» أو خبر محذوف أي: ذلك الخروج كخروج ثلاث.",
     "en": "[It is] an adjective following [another] adjective of “khurūjan” (a deviation), or the predicate of an omitted [subject], that is: “that deviation is like the deviation of thulāth.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كلاهما منصوبان على الحالية، مؤول بلفظ واحد، أي مفصلا بهذا التفصيل، فلما كان كلا اللفظين عبارة عن الحال، أجري الإعراب عليهما.",
     "en": "Both are in the accusative as circumstantial qualifiers (ḥāl), interpreted as a single expression, that is: “detailed by this detailing”; and since both words express the circumstantial state, the inflection was applied to them [both]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أراد بـ«إلى» تعيين الحد، وإلا فالأظهر الواو بدل «إلى».",
     "en": "By “ilā” (up to) he intended to specify the limit; otherwise the more evident [usage] would be the wāw (and) in place of “ilā.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إلى قوله: العدل، والوصف عند سيبويه. وذهب جماعة إلى أن السبب تكرار العدل؛ لأنه عدل فيه عن صيغة إلى صيغة، وعن مكرر إلى غير مكرر، أو اسمية إلى وصفية.",
     "en": "Up to his words: the deviation and the adjectival quality — [this is] according to Sībawayh. A group held that the cause is the doubling of deviation, since in it there is deviation from one form to another, from a repeated form to a non-repeated one, or from a substantival status to an adjectival one."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "اعلم أن ثلاثة من أسماء العدد، وهي موضوعة للوحدات لا لما له الوحدات، حتى يكون أوصافا بحسب الأصل، نعم يستعمل فيما له الوحدات مجازا.",
     "en": "Know that “thalātha” is one of the number-nouns, and these are coined for the units themselves, not for that which possesses the units — so that they might be adjectives by origin; yes, [such a noun] is used for that which possesses the units figuratively."},
    {"type": "pair",
     "ar": "وذلك المعنى المجازي لثلاثة ثلاثة لما وضع لفظ ثلاث ومثلث له صارت الوصفية أصلية بالقياس إلى وضعهما.",
     "en": "And when the words “thulāth” and “mathlath” were coined for that figurative meaning of “thalātha thalātha,” the adjectival quality became intrinsic with respect to their coinage."},
    {"type": "pair",
     "ar": "ولقائل أن يمنع كون ثلاثة ثلاثة باعتبار الوضع التركيبي مجازا في المعنى الوصفي.",
     "en": "One may object and deny that “thalātha thalātha,” by regard to its compositional coinage, is [used] figuratively in the adjectival meaning."},
]
