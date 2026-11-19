# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 493 (printed ٤٩٢)."""

PAGE_NUMBER = 493
PRINTED_PAGE = "٤٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(بمعنى: «كي») أي: حال كون «حتى» بمعنى «كي» للسببية» at the foot of PDF p. 492 (mid-sentence).
    {"type": "matn",
     "ar": "(أو «إلى») لانتهاء الغاية (مثل: «أسلمت حتى أدخل الجنة») مثال لـ«حتى» بمعنى: «كي»، ولاستقبال المضارع بالنظر إلى ما قبله، وبالنظر إلى زمان التكلم أيضا",
     "en": "…(or of “ilā”), for the termination of the extent; (as in “aslamtu ḥattā adkhula al-jannata” (I embraced Islam so that I may enter Paradise)): an example of “ḥattā” in the sense of “kay”, and of the muḍāriʿ being future both in relation to what precedes it and in relation to the time of speaking;"},
    {"type": "matn",
     "ar": "(و«كنت سرت حتى أدخل البلد») مثال لـ«حتى» بمعنى: «كي»، أو «إلى»، ولاستقبال المضارع بالنظر إلى ما قبله.",
     "en": "(and “kuntu sirtu ḥattā adkhula al-balada” (I had travelled so that / until I might enter the town)): an example of “ḥattā” in the sense of “kay” or “ilā”, and of the muḍāriʿ being future in relation to what precedes it."},
    {"type": "matn",
     "ar": "وأما بالنظر إلى زمان التكلم، فيحتمل أن يكون ماضيا، أو حالا، أو مستقبلا[[١]].",
     "en": "As for its relation to the time of speaking, it may be past, present or future."},
    {"type": "matn",
     "ar": "(و«أسير حتى تغيب الشمس») مثال لـ«حتى» بمعنى «إلى»، ولاستقبال ما بعدها تحقيقا.",
     "en": "(And “asīru ḥattā taghība al-shamsu” (I shall travel until the sun sets)): an example of “ḥattā” in the sense of “ilā”, and of what follows it being future in actual fact."},
    {"type": "matn",
     "ar": "(فإن أردت) بالفعل الذي دخله «حتى» (الحال) يعني: زمان الحال (تحقيقا) أي: بطريق التحقيق، بأن يكون هي زمان التكلم بعينه، وسيجيء مثاله",
     "en": "(If you intend) by the verb that “ḥattā” enters (the present), meaning the present time, (in actual fact), that is, by way of actuality, such that it is the time of speaking itself (its example will come),"},
    {"type": "matn",
     "ar": "(أو حكاية) أي: بطريق الحكاية، كما تقول: «كنت سرت أمس حتى أدخل البلد»،",
     "en": "(or by narration), that is, by way of narrating [a past state], as when you say, “kuntu sirtu amsi ḥattā adkhulu al-balada” (I had travelled yesterday until I was entering the town),"},
    {"type": "matn",
     "ar": "فـ«أدخل» في هذا الموضع حكاية الحال الماضية، كأنك كنت في زمان الدخول هيئة هذه العبارة[[٢]]، وتحكيها في زمان التكلم على ما كنت هيئته،",
     "en": "then “adkhulu” in this place is the narration of a past state: it is as though, at the time of entering, you had framed this expression, and you narrate it at the time of speaking just as you had framed it;"},
    {"type": "matn",
     "ar": "وكان ما بعد «حتى» في هذه العبارة مرفوعا، فأبقيته على ما كان عليه وحكيته،",
     "en": "and what follows “ḥattā” in this expression was in the nominative, so you kept it as it was and narrated it;"},
    {"type": "matn",
     "ar": "ففي زمان الحكاية أيضا يكون مرفوعا؛ إذ لا يمكن[[٣]] حينئذ تقدير «أن»؛ لأنها علم الاستقبال[[٤]].",
     "en": "so at the time of narration too it is in the nominative, since supposing “an” is then impossible, because it is the mark of the future."},
    {"type": "matn",
     "ar": "(كانت) أي: «حتى» عند هذه الإرادة (حرف ابتداء) لا جارة[[٥]] ولا عاطفة.",
     "en": "(it is), that is, “ḥattā”, given this intention, (a particle of inception (ḥarf ibtidāʾ)), neither governing the genitive nor coordinating."},
    {"type": "matn",
     "ar": "ومعنى كونها حرف ابتداء: أن يبتدأ بها كلام مستأنف لا أن يقدر بعدها مبتدأ يكون الفعل خبره، لتكون «حتى» داخلة على اسم كما توهمه بعضهم[[٦]]",
     "en": "The meaning of its being a particle of inception is that a fresh sentence begins with it; not that a subject (mubtadaʾ) is supposed after it with the verb as its predicate, so that “ḥattā” would be entering upon a noun, as some have imagined."},
    {"type": "matn",
     "ar": "(فيرفع) أي: ما بعد «حتى» لعدم الناصب والجازم",
     "en": "(So it is put in the nominative), that is, what follows “ḥattā”, for want of anything governing the accusative or the jussive;"},
    {"type": "matn",
     "ar": "(ويجب السببية) أي: كون ما قبلها سببا لما بعدها، ليحصل الاتصال المعنوي، وإن فات الاتصال اللفظي",
     "en": "(and causation is required), that is, that what precedes it be a cause of what follows it, so that a connection in meaning is obtained, even if the connection in wording is lost;"},
    {"type": "matn",
     "ar": "(مثل: «مرض فلان حتى لا يرجونه»)",
     "en": "(as in “mariḍa fulānun ḥattā lā yarjūnahu” (So-and-so fell ill, so that they no longer hold out hope for him))…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يحتمل الاستقبال كما لا يخفى.",
     "en": "It does not admit the future, as is evident."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل حكاية الحال بمعنى حكاية اللفظ الدال على الحال، وهو خلاف عبارة المصنف،",
     "en": "He took “narration of the present” in the sense of narrating the wording that signifies the present, which goes against the author’s expression;"},
    {"type": "pair",
     "ar": "والأظهر أن المراد زمان الحال المحكي به من حيث إنه حال بأن تبرزه في نظر السامع في معرض الحال.",
     "en": "the more evident view is that what is meant is the present time narrated, insofar as it is present, in that you set it before the hearer’s view in the guise of the present."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "دليل لقوله: فأبقيته يعني: إن إبقاءه على الرفع الذي كان عليه لامتناع نصبه؛ إذ لا يمكن تقدير «أن».",
     "en": "A justification of his words “so you kept it”; he means that keeping it in the nominative it had is due to the impossibility of its accusative, since supposing “an” is impossible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أنها علم الاستقبال حقيقة أو بالنظر إلى ما قبله، وهو لا ينافي الحال",
     "en": "There is [an objection] here: it is the mark of the future either in actual fact or in relation to what precedes it, and this is not incompatible with the present;"},
    {"type": "pair",
     "ar": "إلا أن يقال: ينافي إفادة الحال، فلا يصح ذكره في مقام إفادته.",
     "en": "unless it is said that it is incompatible with conveying the present, so it cannot properly be mentioned where the present is to be conveyed."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأنها لاختصاصها بالاسم لا تدخل على الفعل إلا بتقدير «أن»، وقد امتنع ههنا؛ لأنه علم الاستقبال،",
     "en": "Because, being specific to nouns, it does not enter upon a verb except by supposing “an”, and that is ruled out here, because [“an”] is the mark of the future;"},
    {"type": "pair",
     "ar": "وتقديرها: لم يثبت في كلامهم.",
     "en": "and supposing it [i.e. a subject after it] is not attested in their speech."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وجه التوهم أنهم يقولون: إنها حرف ابتداء، ويريدون لزوم المبتدأ بعدها.",
     "en": "The ground of the illusion is that they say it is a particle of inception, and take this to mean that a subject must follow it."},
]
