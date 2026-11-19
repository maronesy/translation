# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 307 (printed ٣٠٦)."""

PAGE_NUMBER = 307
PRINTED_PAGE = "٣٠٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… مثل: «كل رجل وكل واحد».» at the foot of PDF p. 306 (new sentence).
    {"type": "matn",
     "ar": "(وهو) أي: كون الإضافة بمعنى «في» (قليل) في استعمالاتهم، وردها أكثر النحاة إلى الإضافة بمعنى «اللام»،",
     "en": "(And it), that is, the genitive construction’s being in the sense of “fī” (in), (is rare) in their usage, and most grammarians reduced it to the construction in the sense of “lām”;"},
    {"type": "matn",
     "ar": "فإن معنى «ضرب اليوم»[[١]]: ضرب له اختصاص باليوم بملابسة الوقوع فيه.",
     "en": "for the meaning of “ḍarb al-yawm” (the day’s beating) is: a beating that has a particular connection (ikhtiṣāṣ) with the day through the association of occurring in it."},
    {"type": "matn",
     "ar": "فإن قلت: فعلى هذا يمكن رد الإضافة بمعنى «من» أيضا إلى الإضافة بمعنى «اللام» للاختصاص الواقع بين المبين والمبين؟",
     "en": "If you say: on this basis, the construction in the sense of “min” could also be reduced to the construction in the sense of “lām,” because of the particular connection that obtains between the explicating term and the term explicated?"},
    {"type": "matn",
     "ar": "قلنا: نعم، لكن لما كانت الإضافة بمعنى «في» قليلا، ردوه إلى الإضافة بمعنى «اللام» تقليلا للأقسام.",
     "en": "We say: yes; but since the construction in the sense of “fī” was rare, they reduced it to the construction in the sense of “lām” so as to reduce the number of divisions."},
    {"type": "matn",
     "ar": "وأما الإضافة بمعنى «من»، فهي كثيرة[[٢]] في كلامهم، فالأولى بها أن تجعل قسما على حدة.",
     "en": "As for the construction in the sense of “min,” it is frequent in their speech, so it is more fitting that it be made a division of its own."},
    {"type": "matn",
     "ar": "(نحو: «غلام زيد») مثال للإضافة بمعنى «اللام» أي: «غلام لزيد».",
     "en": "(As in “ghulām Zayd” [Zayd’s slave]) is an example of the construction in the sense of “lām,” that is, “a slave belonging to Zayd.”"},
    {"type": "matn",
     "ar": "(و«خاتم فضة») مثال للإضافة بمعنى «من» أي: «خاتم من فضة».",
     "en": "(And “khātam fiḍḍa” [a silver ring]) is an example of the construction in the sense of “min,” that is, “a ring of silver.”"},
    {"type": "matn",
     "ar": "(و«ضرب اليوم») مثال للإضافة بمعنى «في» أي: «ضرب واقع في اليوم»[[٣]].",
     "en": "(And “ḍarb al-yawm” [the day’s beating]) is an example of the construction in the sense of “fī,” that is, “a beating occurring in the day.”"},
    {"type": "matn",
     "ar": "(وتفيد) أي: الإضافة المعنوية (تعريفا) أي: تعريف المضاف (مع المعرفة[[٤]])؛",
     "en": "(And it conveys), that is, the semantic genitive construction (al-iḍāfa al-maʿnawiyya) [conveys], (definiteness), that is, the definiteness of the annexed term (muḍāf), (with a definite [annexing term]);"},
    {"type": "matn",
     "ar": "لأن الهيئة التركيبية في الإضافة المعنوية موضوعة للدلالة على معلومية المضاف،",
     "en": "because the compositional form of the semantic genitive construction is coined to signify that the annexed term is known,"},
    {"type": "matn",
     "ar": "لا أن نسبة أمر إلى معين تستلزم معلومية المنسوب ومعهوديته، فإن ذلك غير لازم، كما لا يخفى[[٥]].",
     "en": "not that relating a thing to a specific [referent] entails that what is related is known and familiar; for that does not follow, as is evident."},
    {"type": "matn",
     "ar": "فإن قلت: قد يقال: «جاءني غلام زيد» من غير إشارة إلى واحد معين، فلا يكون",
     "en": "If you say: one sometimes says “Zayd’s slave came to me” without pointing to a specific individual, so it would not be…"},

    {"type": "rule"},

    # ---------------- Footnote ٧ of PDF p. 306, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "فك «كل» عن الإضافة، وذا لا يجوز.",
     "en": "…the detachment of “kull” from the genitive construction, and that is not permitted."},
    {"type": "pair",
     "ar": "وفيه بحث لأن «كلا» للإحاطة، والجزئي والفرد ملحوظ من جانب المضاف إليه كما تقرر في الميزان.",
     "en": "This is open to discussion, because “kull” is for comprehensiveness, and the particular and the individual are considered from the side of the annexing term (muḍāf ilayhi), as was established in logic (al-mīzān)."},
    {"type": "pair",
     "ar": "وتصحيح إضافة الجزئي إلى الكلي مما لا يجدي نفعا في تصحيح إضافة كل إلى الجزئي أو الفرد.",
     "en": "And validating the annexation of a particular to a universal is of no use in validating the annexation of “kull” to a particular or an individual."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن هذه الإضافة بأدنى ملابسة، ويكفي في الإضافة بمعنى اللام أدنى ملابسة،",
     "en": "He means that this construction rests on the slightest association, and the slightest association suffices for the construction in the sense of lām,"},
    {"type": "pair",
     "ar": "نحو: كوكب الخرقاء لسهيل، أي: كوكب له اختصاص بالمرأة الخرقاء بملابسة أنها تشرع في التهيء لأسباب الشتاء عند طلوعها لا قبله،",
     "en": "as in “kawkab al-kharqāʾ” (the clumsy woman’s star) for Canopus (Suhayl), that is, a star that has a particular connection with the clumsy woman through the association that she begins preparing the provisions for winter when it rises, not before,"},
    {"type": "pair",
     "ar": "كما هو شأن النساء المدبرة المهيئة للأمور في أحيانها.",
     "en": "as is the way of provident women who prepare matters in their due times."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وأيضا لما كثرت لزم ارتكاب مجاز كثير، وذلك لأن الإضافة بأدنى ملابسة مجاز.",
     "en": "Also, since it is frequent, [reducing it] would entail resorting to much figurative usage (majāz); that is because a construction resting on the slightest association is figurative."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الظاهر أن في اليوم فيما هو أصل ضرب اليوم، أعني: ضرب في اليوم متعلق بالضرب، وليس صفة لضرب بتقدير واقع في اليوم.",
     "en": "The apparent [view] is that “fī al-yawm” in what underlies “ḍarb al-yawm,” I mean “ḍarb fī al-yawm,” is attached to “al-ḍarb” and is not an adjective of “ḍarb” on the supposition [of an implied] “wāqiʿ fī al-yawm” (occurring in the day)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قول المصنف: وتفيد تعريفا مع المعرفة ظاهره تعريف أحد طرفي الإضافة مع معرفة هي أحد طرفيها،",
     "en": "The author’s words “and it conveys definiteness with a definite [term]”: their apparent sense is the definiteness of one of the two terms of the construction together with a definite noun that is one of its two terms;"},
    {"type": "pair",
     "ar": "إلا أنه خص المستفيد بالمضاف والمعرفة بالمضاف إليه. قوله: وشرطها تجريد المضاف من التعريف.",
     "en": "except that he restricted the one that acquires [definiteness] to the annexed term and the definite noun to the annexing term. [This is shown by] his words: “and its condition is that the annexed term be stripped of the definite article.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ألا يرى أن نسبة الفعل إلى فاعله المعين لا تستلزم معهودية الفعل وتعريفه.",
     "en": "Does one not see that relating a verb to its specific agent does not entail the verb’s being familiar and definite?"},
]
