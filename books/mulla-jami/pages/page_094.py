# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 94 (printed ٩٣)."""

PAGE_NUMBER = 94
PRINTED_PAGE = "٩٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "منه، فحينئذ لا حاجة في تصحيح هذا التعريف إلى ارتكاب تلك التكلفات[[١]].",
     "en": "than it; in that case there is no need, in order to validate this definition, to resort to those forced constructions (al-takalluffāt)."},
    {"type": "matn",
     "ar": "واعلم أنا نعلم قطعا[[٢]] أنهم لما وجدوا «ثلاث، ومثلث، وأخر وجمع وعمر» غير منصرف، ولم يجدوا فيها سببا ظاهرا غير الوصفية أو العلمية احتاجوا[[٣]] إلى اعتبار سبب آخر،",
     "en": "Know that we know for certain that, when they found “thulātha,” “mathlatha,” “ukhara,” “jumaʿa,” and “ʿumara” to be diptote, yet found in them no apparent cause besides adjectival status (al-waṣfiyya) or proper-name status (al-ʿalamiyya), they needed to posit another cause;"},
    {"type": "matn",
     "ar": "ولما لم يصلح للاعتبار إلا العدل، اعتبروه فيها، لا أنهم تنبهوا للعدل[[٤]] فيما عدا «عمر» من هذه الأمثلة، فجعلوه غير منصرف للعدل وسبب آخر.",
     "en": "and since nothing was fit to be posited except deviation (al-ʿadl), they posited it in them — not that they [independently] noticed deviation in these examples apart from “ʿumar” and then made it diptote on account of deviation and another cause."},
    {"type": "matn",
     "ar": "ولكن لا بد في اعتبار العدل من أمرين:",
     "en": "But in positing deviation two things are indispensable:"},
    {"type": "matn",
     "ar": "أحدهما: وجود الأصل للاسم المعدول.",
     "en": "the first: the existence of the base form (al-aṣl) for the deviated noun;"},
    {"type": "matn",
     "ar": "وثانيهما: اعتبار إخراجه عن ذلك الأصل؛ إذ لا يتحقق الفرعية بدون اعتبار ذلك الإخراج.",
     "en": "and the second: the reckoning of its being brought out from that base form, since secondariness (al-farʿiyya) is not realized without reckoning that bringing-out."},
    {"type": "matn",
     "ar": "ففي بعض تلك الأمثلة[[٥]] يوجد دليل غير منع الصرف على وجود الأصل المعدول عنه، فوجوده محقق بلا شك،",
     "en": "Now in some of those examples there exists an indicant, other than diptosy (manʿ al-ṣarf), of the existence of the base form from which the deviation was made, so its existence is established beyond doubt;"},
    {"type": "matn",
     "ar": "وفي بعضها لا يوجد غير دليل منع الصرف، فيفرض له أصل، ليتحقق العدل بإخراجه عن ذلك الأصل، فانقسام العدل إلى التحقيقي",
     "en": "while in others there exists nothing but the indicant of diptosy, so a base form is posited for it in order that deviation may be realized by bringing it out from that base — hence the division of deviation into the actual (al-taḥqīqī)"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لما كانت العبارة غير صريحة في إفادة بعض القيود سماه تكلفات، وإلا فهو قدر العبارة على وجه يفهم المقصود بطريق التبادر منها من غير تكلف.",
     "en": "Since the wording was not explicit in conveying some of the restrictions, he called them “forced constructions”; otherwise it is [only] the measure of the wording, in a way that the intended meaning is grasped from it by immediate apprehension (tabādur), without forcing."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "كأن وجهه أن نظر النحاة في تتبعهم أولا إلى إعراب الكلمة وبنائها، فإذا نظروا إلى إعراب ثلاثة وأخواته وجدوا إعرابها إعراب منع الصرف.",
     "en": "It is as though its rationale is that the grammarians’ attention, in their inductive survey, was first directed to the inflection (iʿrāb) and indeclinability (bināʾ) of the word; and when they looked at the inflection of “thulātha” and its sisters, they found their inflection to be that of the diptote."},
    {"type": "pair",
     "ar": "ولما علموا بالتتبع أن منع الصرف لا يكون إلا بفرعيتين حقيقة أو حكما فتشوا عن حال تلك الأمثلة، فوجدوا فرعية ظاهرة، وهي العلمية والوصفية، ولم يجدوا أخرى،",
     "en": "And when they knew by induction that diptosy occurs only through two [modes of] secondariness — either in reality or in ruling — they investigated the state of those examples and found one apparent secondariness, namely proper-name status and adjectival status, but found no other;"},
    {"type": "pair",
     "ar": "فاضطروا إلى اعتبار فرعية أخرى، ولم يصلح للاعتبار إلا العدل، فاعتبروه، ثم فتشوا عن حال الأصل، ففي بعض الأمثلة لم يجدوا ما يدل على ثبوت الأصل إلا اقتضاء العدل المعدول عنه،",
     "en": "so they were compelled to posit another secondariness, and nothing was fit to be posited except deviation, so they posited it. Then they investigated the state of the base form: in some examples they found nothing indicating the existence of the base except deviation’s requiring that from which it deviated,"},
    {"type": "pair",
     "ar": "وفي بعضها وجدوا دليلا آخر، فالثاني هو العدل التحقيقي أي: العدل المنسوب إلى ما هو محقق، أي: في الخارج.",
     "en": "while in others they found another indicant. The latter is actual deviation (al-ʿadl al-taḥqīqī) — that is, deviation attributed to what is actually realized, namely in extramental reality (fī al-khārij)."},
    {"type": "pair",
     "ar": "والأول هو العدل التقديري أي: العدل المنسوب إلى ما هو مقدر ليس ثابتا في الخارج.",
     "en": "The former is estimative deviation (al-ʿadl al-taqdīrī) — that is, deviation attributed to what is [merely] posited and not established in extramental reality."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جواب «لما» أي: اضطروا لحفظ قاعدتهم إلى سبب آخر.",
     "en": "[This is] the answer to “when” (lammā) — that is: they were compelled, in order to preserve their rule, to [posit] another cause."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "اعلم أن التنبه على ذات السبب في غير العدل والجمع التقديري مقدم على منع الصرف، ولا يتوقف على معرفة منع الصرف أصلا.",
     "en": "Know that noticing the substance of the cause, in causes other than deviation and estimative plurality (al-jamʿ al-taqdīrī), precedes diptosy and does not depend on knowledge of diptosy at all."},
    {"type": "pair",
     "ar": "وأما علمية الأسباب فلا يعرف في شيء منها إلا بعد معرفة منع الصرف.",
     "en": "As for the causal status of the causes, it is not known in any of them except after knowledge of diptosy."},
    {"type": "pair",
     "ar": "وأما في العدل التحقيقي فإن كان هو الخروج عما هو القياس، فيمكن أن يعرف بدون معرفة منع الصرف كسائر الأسباب،",
     "en": "As for actual deviation: if it is departure from what is analogical, then it can be known without knowledge of diptosy, like the remaining causes;"},
    {"type": "pair",
     "ar": "وإن كان هو الخروج عما كان للمادة، كما قرر في الشرح، فلا يعرف إلا بمنع الصرف.",
     "en": "but if it is departure from what belonged to the [original] material substance, as was established in the commentary (al-sharḥ), then it is known only through diptosy."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو ما عدا عمر، وهذا إشارة إلى التفتيش عن حال أصولها.",
     "en": "That is, [the examples] apart from “ʿumar”; and this is an allusion to the investigation of the state of their base forms."},
]
