# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 294 (printed ٢٩٣)."""

PAGE_NUMBER = 294
PRINTED_PAGE = "٢٩٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والياء المفتوح ما قبلها في المثنى، والمكسور» from the foot of PDF p. 293.
    {"type": "matn",
     "ar": "ما قبلها في جمع المذكر السالم نحو: «لا مسلمين ولا مسلمين لك».",
     "en": "…by a kasra in the sound masculine plural, as in “lā muslimayni wa-lā muslimīna laka” (you have no two Muslims and no Muslims)."},
    {"type": "matn",
     "ar": "ونعني بالمفرد: ما ليس بمضاف ولا مضارع له، فيدخل فيه المثنى والمجموع.",
     "en": "By “single” (mufrad) we mean what is neither annexed nor resembling the annexed; so the dual and the plural are included in it."},
    {"type": "matn",
     "ar": "وإنما بني لتضمنه معنى «من»؛ إذ معنى «لا رجل في الدار»: لا من رجل فيها؛",
     "en": "It was made indeclinable only because it implies the meaning of “min,” since the meaning of “lā rajula fī l-dār” is “there is not any man in it” (lā min rajulin fīhā),"},
    {"type": "matn",
     "ar": "لأنه جواب لمن يقول: «هل من رجل في الدار؟» حقيقة أو تقديرا، فحذف تخفيفا.",
     "en": "because it is an answer to one who says, actually or by supposition, “Is there any man in the house?” (hal min rajulin fī l-dār); and [min] was elided for lightness."},
    {"type": "matn",
     "ar": "وإنما بني على ما ينصب به، لكون البناء على حركة أو حرف استحقها النكرة في الأصل قبل البناء،",
     "en": "It was made indeclinable on that by which it is put in the accusative only so that the indeclinability would be on a vowel or a letter which the indefinite noun originally merited before indeclinability."},
    {"type": "matn",
     "ar": "ولم يبين المضاف ولا المضارع له؛ لأن الإضافة[[١]] ترجح جانب الاسمية[[٢]]، فيصير الاسم بها مائلا إلى ما يستحقه في الأصل، أعني: الإعراب.",
     "en": "The annexed noun and what resembles it were not made indeclinable, because annexation (iḍāfa) strengthens the side of nounhood, so that through it the noun inclines toward what it originally merits, namely inflection (iʿrāb)."},
    {"type": "matn",
     "ar": "(وإن كان) أي: المسند إليه بعد دخولها (معرفة) بانتفاء شرط النكارة",
     "en": "(If it is), that is, that to which [something] is predicated after its entry, (definite), through the absence of the condition of indefiniteness,"},
    {"type": "matn",
     "ar": "(أو مفصولا بينه) أي: بين ذلك المسند إليه (وبين «لا») بانتفاء شرط الاتصال على سبيل منع الخلو",
     "en": "(or separated from), that is, if there is a separation between that to which [something] is predicated (and “lā”), through the absence of the condition of adjacency—by way of disjunction that excludes the absence of both (manʿ al-khuluww)—"},
    {"type": "matn",
     "ar": "سواء كانا مع انتفاء شرط كونه مضافا أو مشبها به أو لا،",
     "en": "whether the two [absences] are accompanied by the absence of the condition of its being annexed or resembling the annexed, or not;"},
    {"type": "matn",
     "ar": "وهي ست صور نحو: «لا زيد في الدار ولا عمرو»، و«لا غلام زيد في الدار ولا عمرو»، و«لا في الدار رجل ولا امرأة»، و«لا في الدار غلام رجل ولا امرأة»، و«لا في الدار زيد ولا عمرو»، و«لا في الدار غلام زيد ولا عمرو»",
     "en": "these are six cases, as in “Zayd is not in the house, nor ʿAmr,” “Zayd’s slave is not in the house, nor ʿAmr,” “There is in the house no man nor woman,” “There is in the house no slave of a man nor a woman,” “There is in the house neither Zayd nor ʿAmr,” and “There is in the house neither Zayd’s slave nor ʿAmr,”"},
    # REVIEW: print reads «الصورة الست» (singular); the sense requires «الصور»; transcribed as printed.
    {"type": "matn",
     "ar": "(وجب) في جميع هذه الصورة الست (الرفع) على الابتداء.",
     "en": "(it is obligatory) in all these six cases [that it take] (the nominative), as a subject of a nominal sentence (ʿalā l-ibtidāʾ)."},
    {"type": "matn",
     "ar": "أما في المعرفة فلامتناع أثر «لا» النافية للجنس فيها.",
     "en": "As for the definite noun, it is because the effect of the “lā” that negates the genus cannot occur in it."},
    {"type": "matn",
     "ar": "وأما في المفصول فلضعف «لا» عن التأثير مع الفصل.",
     "en": "As for the separated noun, it is because “lā” is too weak to have an effect when there is a separation."},
    {"type": "matn",
     "ar": "(والتكرير[[٣]]) أي: وجب تكرير اسمه لكن مطلقا لا بعينه[[٤]].",
     "en": "(And repetition), that is, the repetition of its noun is obligatory—but [repetition] in general, not of the same [noun]."},
    {"type": "matn",
     "ar": "أما في المعرفة: فليكون كالعوض عما في التنكير من معنى نفي الآحاد.",
     "en": "As for the definite noun: so that it may be a kind of compensation for the meaning of negating individuals contained in indefiniteness."},
    {"type": "matn",
     "ar": "وأما في النكرة: فليكون مطابقا[[٥]] لما هو جواب له من مثل قول السائل: «أفي الدار رجل أم امرأة؟»،",
     "en": "As for the indefinite noun: so that it corresponds to that of which it is the answer, such as the questioner’s saying, “Is there in the house a man or a woman?”"},
    {"type": "matn",
     "ar": "وهذا التعليل جار في المعرفة أيضا.",
     "en": "This explanation applies to the definite noun as well."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الإضافة إلى الاسم الصريح ترجح جانب الاسمية،",
     "en": "That is, annexation to an explicit noun strengthens the side of nounhood;"},
    {"type": "pair",
     "ar": "فإن المضاف إلى الاسم الصريح لا يكون مبنيا إلا نادرا نحو خمسة عشرك ونحوه.",
     "en": "for what is annexed to an explicit noun is not indeclinable except rarely, as in “khamsata ʿashraka” (your fifteen) and the like."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: الإضافة إلى المفرد.",
     "en": "That is, annexation to a single noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكذا وجب التكرير في النكرة المتصلة بلا إذا ألغيت عملها؛",
     "en": "Likewise repetition is obligatory with an indefinite noun adjacent to lā when its government is cancelled;"},
    {"type": "pair",
     "ar": "لأن القرينة على إرادة نفي الجنس نصب الاسم أو بناؤه وقد انتفيا، فلا بد من التكرير للتنبيه عليها.",
     "en": "because the indication that negation of the genus is intended is the noun’s being accusative or indeclinable, and both are absent; so repetition is necessary to signal it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أراد تكرير النوع لا تكرير الشخص.",
     "en": "He means: he intended repetition of the kind, not repetition of the individual [word]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما قدر السؤال مكررا؛ إذ لو لم يكن مكررا لكفى نعم أو لا.",
     "en": "He supposed the question to be repeated only because, were it not repeated, “yes” or “no” would suffice."},
]
