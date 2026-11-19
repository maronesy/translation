# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 466 (printed ٤٦٥)."""

PAGE_NUMBER = 466
PRINTED_PAGE = "٤٦٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أعني: ما» at the foot of PDF p. 465 (mid-sentence).
    {"type": "matn",
     "ar": "جاء للفاعل، وما جاء للمفعول (بزيادة على غيره) في أصل ذلك الفعل،",
     "en": "…comes for the agent and what comes for the object, (by way of excess over another) in the root of that action."},
    {"type": "matn",
     "ar": "والباء في قوله: «بزيادة» إما ظرف لغو[[١]] للموصوف أي: لذات متصفة بتلك الزيادة، أو ظرف مستقر[[٢]] أي: لموصوف متلبس بتلك الزيادة.",
     "en": "The bāʾ in his words “bi-ziyāda” (by way of excess) is either a dependent adverbial (ẓarf laghw) attached to “qualified thing”, that is, for an entity qualified by that excess, or an independent adverbial (ẓarf mustaqarr), that is, for a qualified thing invested with that excess."},
    {"type": "matn",
     "ar": "فقوله: «ما اشتق من فعل» شامل لجميع المشتقات.",
     "en": "His words “what is derived from a verb” cover all derived forms."},
    {"type": "matn",
     "ar": "وقوله: «لموصوف» يخرج أسماء الزمان والمكان والآلة؛ لأن المراد بالموصوف ذات مبهمة، ولا إبهام في تلك الأسماء[[٣]].",
     "en": "His words “for a qualified thing” exclude the nouns of time, place and instrument, because what is meant by “qualified thing” is an unspecified entity, and there is no unspecificity in those nouns."},
    {"type": "matn",
     "ar": "وقوله: «بزيادة على غيره» يخرج اسمي الفاعل والمفعول والصفة المشبهة[[٤]].",
     "en": "His words “by way of excess over another” exclude the active and passive participles and the resembling adjective."},
    {"type": "matn",
     "ar": "(وهو) أي: اسم التفضيل، من حيث صيغته[[٥]] (أفعل) للمذكر (وفعلى) للمؤنث[[٦]]، وإن كان بحسب أصل الوضع،",
     "en": "(It), that is, the elative, with respect to its form, (is afʿal) for the masculine (and fuʿlā) for the feminine, even if [only] according to its original coinage;"},
    {"type": "matn",
     "ar": "فيدخل فيه «خير وشر»[[٧]] لكونهما في الأصل «أخير وأشر»، فخففتا بالحذف، لكثرة الاستعمال، وقد يستعملان على الأصل.",
     "en": "so “khayr” (better) and “sharr” (worse) are included in it, since they were originally “akhyar” and “asharr”, and were lightened by omission because of frequent use; they are sometimes used in the original form."},
    {"type": "matn",
     "ar": "(وشرطه: أن يبنى) أي: اسم التفضيل (من) حدث[[٨]] (ثلاثي) لا رباعي (مجرد)",
     "en": "(Its condition is that it be formed), that is, the elative, (from) an event (that is triliteral), not quadriliteral, (bare)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: صلة مفعول له بالواسطة.",
     "en": "That is, a complement governed by it through an intermediary."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وموصوف مقطوع عن المفعول بالواسطة لعدم تعلق الغرض به كما يدل عليه قوله: أي: الموصوف متلبس بتلك الزيادة،",
     "en": "And “qualified thing” is cut off from the object through an intermediary because the purpose is not concerned with it, as his words indicate: “that is, the qualified thing invested with that excess”;"},
    {"type": "pair",
     "ar": "ويقدر مفعوله أي: الموصوف به أي: بالفعل كما في الحواشي الهندية.",
     "en": "and its object is supplied, that is, “qualified by it”, that is, by the action, as in the Indian glosses (al-Ḥawāshī al-Hindiyya)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنها تدل على المكان والزمان دلالة ما، ففيها نوع تعيين.",
     "en": "Because they signify place and time in some way, so there is a kind of specification in them."},
    {"type": "pair",
     "ar": "وما قيل: إنه لا حاجة في الإخراج إلى حمل الموصوف على ذلك؛ لأن تلك الأسماء لم توضع لمكان أو زمان أول موصوف،",
     "en": "As for what has been said, that for the exclusion there is no need to take “qualified thing” in this way, because those nouns were not coined for a place or time [as] a first qualified thing,"},
    {"type": "pair",
     "ar": "ففيه أن اسم التفضيل الذي جاء للمفعول موضوع لموصوف بمعنى ما وقع عليه الفعل كذلك تلك الأسماء موضوعة لموصوف بمعنى ما وقع عليه الفعل، أو وقع به الفعل.",
     "en": "against it [is the point] that the elative which comes for the object is coined for a qualified thing in the sense of that on which the action falls; likewise those nouns are coined for a qualified thing in the sense of that on which the action falls, or by which the action takes place."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لعدم دلالتها على الزيادة على الغير كصيغ المبالغة، أو لعدم دلالتها على الزيادة في ذلك الفعل كفاضل وطائل،",
     "en": "Because they do not signify excess over another, like the intensive forms; or because they do not signify excess in that action, like “fāḍil” (excellent) and “ṭāʾil” (substantial);"},
    # REVIEW: printed «الصفة الشبهة»; expected «الصفة المشبهة». Transcribed as printed.
    {"type": "pair",
     "ar": "أو لعدم دلالتها على الزيادة في أصل الفعل، بل في خلقتها كصيغ الصفة الشبهة الدالة على الدوام والاستمرار.",
     "en": "or because they do not signify excess in the root of the action but in its natural constitution, like the forms of the resembling adjective that signify permanence and continuity."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: هيئته لا من حيث مادته، فإنه غير منحصر بهذا الاعتبار في «أفعل».",
     "en": "That is, its shape, not with respect to its material, for in that respect it is not confined to “afʿal”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إنما تعرض لبيان صيغة المؤنث دفعا لتوهم استواء المذكر والمؤنث في «أفعل» مطلقا.",
     "en": "He undertook to state the feminine form only to ward off the supposition that masculine and feminine are equal in “afʿal” unconditionally."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: أخير وأشر المستعملين بـ«من» المستوى فيهما المذكر والمؤنث،",
     "en": "That is, “akhyar” and “asharr” used with “min”, in which masculine and feminine are equal;"},
    {"type": "pair",
     "ar": "فحذف الهمزة، ونقل فتحة الياء والراء إلى الخاء والشين، وأدغم الراء في الراء.",
     "en": "the hamza was omitted, the fatḥa of the yāʾ and of the rāʾ was transferred to the khāʾ and the shīn, and the rāʾ was assimilated into the rāʾ."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قدر بقرينة التعريض، فلا يبنى من اسم جامد، وأقل الناس شاذ؛ لأنه من غير متصرف،",
     "en": "He supplied [“event”] by the indication of the implicit allusion; so it is not formed from a non-derived noun, and “aqallu l-nās” (the fewest of people) is anomalous, because it is from a non-inflecting [verb];"},
    {"type": "pair",
     "ar": "ولا من فعل لازم النفي نحو: ما نبس بكلمة أي: تكلم لعدم المصدر له من حيث لزوم النفي.",
     "en": "nor from a verb bound to negation, as in “mā nabasa bi-kalima” (he did not utter a word), that is, speak, since it has no maṣdar by reason of being bound to negation."},
    {"type": "pair",
     "ar": "وأما الأفعال الناقصة، فإن قلنا: إنها لا تدل على الحدث بل على الزمان فقط كما قيل فظاهر.",
     "en": "As for the defective verbs (al-afʿāl al-nāqiṣa): if we say that they do not signify an event but only time, as has been said, then [the matter] is evident."},
    {"type": "pair",
     "ar": "وإن قلنا: إنها دالة على الحدث وهو الحق، فالظاهر جواز البناء منها قياسا؛ إذ لا مانع من أن يقال: زيد أصير من عمرو غنيا؛ إذ لم يستعمل.",
     "en": "If we say that they signify an event, which is the truth, then the evident [view] is that forming [the elative] from them is permitted by analogy, since nothing prevents saying “Zaydun aṣyaru min ʿAmrin ghaniyyan” (Zayd becomes rich more than ʿAmr), though it is not in use."},
    {"type": "pair",
     "ar": "فقوله: من حدث مشتمل على الشروط الثلاثة.",
     "en": "So his words “from an event” comprise the three conditions."},
    {"type": "pair",
     "ar": "وأما اشتراط كون الحدث مما لا يقبل الزيادة",
     "en": "As for the condition that the event be among what does not admit excess…"},
]
