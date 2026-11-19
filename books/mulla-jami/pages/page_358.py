# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 358 (printed ٣٥٧)."""

PAGE_NUMBER = 358
PRINTED_PAGE = "٣٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ويخرج بهذا القيد لفظ المتكلم والمخاطب،» from the foot of PDF p. 357.
    {"type": "matn",
     "ar": "فإن الأسماء الظاهرة كلها موضوعة للغائب مطلقا[[١]]",
     "en": "…for all the overt nouns (al-asmāʾ al-ẓāhira) are coined for the absent [third person] without qualification."},
    {"type": "matn",
     "ar": "(أو غائب: تقدم ذكره) ويخرج بهذا القيد الأسماء الظاهرة[[٢]] وإن كانت موضوعة للغائب؛ إذ ليس تقدم ذكر الغائب شرطا فيها",
     "en": "(Or an absent person whose mention has preceded): by this qualification the overt nouns are excluded, even though they are coined for the absent, since prior mention of the absent person is not a condition for them."},
    {"type": "matn",
     "ar": "(لفظا، أو معنى، أو حكما) أراد بالتقدم اللفظي[[٣]] ما يكون المتقدم ملفوظا:",
     "en": "(In wording, in meaning, or by legal status): by precedence in wording he meant that the antecedent is uttered,"},
    {"type": "matn",
     "ar": "إما متقدما تحقيقا مثل: «ضرب زيد غلامه»، أو تقديرا مثل: «ضرب غلامه زيد»[[٤]]،",
     "en": "whether it actually precedes, as in “ḍaraba Zaydun ghulāmahu” (Zayd struck his servant), or precedes by supposition, as in “ḍaraba ghulāmahu Zaydun” (his servant, Zayd struck);"},
    {"type": "matn",
     "ar": "وبالتقدم المعنوي أن يكون المتقدم مذكورا من حيث المعنى لا من حيث اللفظ[[٥]]،",
     "en": "and by precedence in meaning, that the antecedent is mentioned in respect of meaning, not in respect of wording."},
    {"type": "matn",
     "ar": "وذلك المعنى إما مفهوم من لفظ بعينه كقوله تعالى: ﴿اعدلوا هو أقرب للتقوى﴾[[٦]]،",
     "en": "That meaning is either understood from a specific word, as in His words, the Exalted: “Be just; that is nearer to piety”,"},
    {"type": "matn",
     "ar": "فإن مرجع الضمير هو «العدل» المفهوم من قوله تعالى: ﴿اعدلوا﴾، فكأنه متقدم من",
     "en": "for the referent of the pronoun is “justice” (al-ʿadl), understood from His words, the Exalted, “Be just”; so it is as though it preceded in…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 357 (footnote ٥ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "ذاتهما، ولفظا المتكلم والمخاطب موضوعان للمفهوم.",
     "en": "…their very selves, whereas the two words “speaker” and “addressee” are coined for the concept."},
    {"type": "pair",
     "ar": "وبقيد الحيثية هناك يخرج زيد إذا عبر المسمى بزيد عن نفسه بزيد، وقس عليه حال المخاطب.",
     "en": "By the qualification “insofar as” there, “Zayd” is excluded when the one named Zayd refers to himself as “Zayd”; judge the case of the addressee by analogy with it."},
    {"type": "pair",
     "ar": "ومنهم من فسر قوله: ما وضع لمتكلم بقوله أي: مادة، أو بطريق الكناية.",
     "en": "Some of them explained his words “what has been coined for a speaker” by saying: that is, as [its] material [meaning], or by way of allusion (kināya)."},
    {"type": "pair",
     "ar": "وقال: بهذا خرج لفظا المتكلم والمخاطب؛ لأنهما موضوعان صيغة وصريحا.",
     "en": "He said: by this the two words “speaker” and “addressee” are excluded, because they are coined [for that] by their form and explicitly."},
    {"type": "pair",
     "ar": "ولعله أراد بالصيغة الهيئة الاشتقاقية، فلا يرد أن لفظ «أنا» موضوع لصيغة المتكلم",
     "en": "Perhaps by “form” he meant the derivational pattern; so the objection does not arise that the word “anā” is coined for the speaker by its form,"},
    # REVIEW: the closing clause about «الهمزة مع النون» reads as printed; its link to the argument is not evident.
    {"type": "pair",
     "ar": "بناء على أن الهمزة مع النون قد يكون للشرط، وقد يكون للتحقيق.",
     "en": "on the basis that the hamza together with the nūn is sometimes for the condition and sometimes for affirmation."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: لما كان ليس متكلما من حيث إنه متكلم ولا مخاطبا من حيث إنه مخاطب.",
     "en": "He means: since it is neither a speaker insofar as he is a speaker nor an addressee insofar as he is an addressee."},
    {"type": "pair",
     "ar": "ولهذا تقول: يا تميم كلهم نظرا إلى أصل المنادى قبل النداء.",
     "en": "Hence you say “yā Tamīmu kulluhum” (O Tamīm, all of them), with regard to the original state of the vocative before the call."},
    {"type": "pair",
     "ar": "ويقول المسمى بزيد: زيد ضرب، ولا يقول: زيد ضربت.",
     "en": "And the one named Zayd says “Zaydun ḍaraba” (Zayd struck), not “Zaydun ḍarabtu” (Zayd, I struck)."},
    {"type": "pair",
     "ar": "وإنما جاز يا تميم كلهم؛ لأن «يا» دليل الخطاب، وليس في زيد ضرب دليل التكلم.",
     "en": "“Yā Tamīmu kulluhum” is permitted only because “yā” indicates address, whereas in “Zaydun ḍaraba” there is no indication of the first person."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إن قيل: إذا أريد الوضع بطريق الكناية خرج الأسماء الظاهرة به، فلم يكن قوله: تقدم داخلا في الحد بناء على ذلك التفسير؟",
     "en": "If it is said: when coining by way of allusion is meant, the overt nouns are excluded by it; so why is his phrase “whose mention has preceded” included in the definition on that interpretation?"},
    {"type": "pair",
     "ar": "قلنا: لم يخرج به بعض أسماء الظاهرة مثل: كم وكذا، فلا بد منه لإخراجه.",
     "en": "We say: some overt nouns, such as “kam” and “kadhā”, are not excluded by it, so it is needed to exclude them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اعلم أن تفسير التقدم اللفظي بما ذكره يدل على أنه جعل قوله: لفظا أو معنى أو حكما من أقسام الذكر حقيقة لا من أقسام التقدم حقيقة،",
     "en": "Know that his explaining verbal precedence as he did shows that he made his words “in wording, in meaning, or by legal status” in reality divisions of mention, not in reality divisions of precedence;"},
    {"type": "pair",
     "ar": "لكن لما كان المقصود الأصلي هنا بيان التقدم جعله من أقسامه.",
     "en": "but since the primary aim here is to set out precedence, he made them divisions of it."},
    {"type": "pair",
     "ar": "وبهذا اندفع اعتراض الشيخ الرضي بأن تقسيم التقدم اللفظي إلى الحقيقي والتقديري خلاف دأبه،",
     "en": "By this, Shaykh al-Raḍī’s objection is averted, namely that dividing verbal precedence into the actual and the supposed is contrary to his practice,"},
    {"type": "pair",
     "ar": "فإن عادته جعل اللفظ قسيم التقدير كما مر في بيان حكم المعرب وبيان الإعراب،",
     "en": "for his custom is to make “wording” the co-division of “supposition”, as has passed in setting out the rule of the declinable and setting out inflection."},
    {"type": "pair",
     "ar": "بل نقول: لقائل أن يقول: لا معنى لأن يجعل الحكمي من أقسام التقدم حقيقة بناء على تفسير المصنف؛",
     "en": "Rather, we say: someone may say that there is no sense in making the “by legal status” kind in reality a division of precedence on the author’s explanation,"},
    {"type": "pair",
     "ar": "لأنه جعل الحضور الذهني وعهديته قبل ذكر الضمير بمنزلة الذكر، ولا خفاء في أن التمحل حينئذ ليس إلا في جعل العهد في حكم الذكر.",
     "en": "because he made mental presence and its being familiar before the pronoun is mentioned equivalent to mention; and it is plain that the contrivance is then only in treating familiarity as having the status of mention."},
    {"type": "pair",
     "ar": "وأما التقدم الحقيقي لا حاجة فيه إلى تمحل.",
     "en": "As for actual precedence, there is no need for contrivance in it."},
    {"type": "pair",
     "ar": "نعم لو جعل الضمير راجعا إلى المفسر الذي بعده احتيج إلى تمحل في التقدم بأن يقال مثلا: إنه متقدم بحكم وضع الضمير واقتضائه،",
     "en": "Yes, if the pronoun were made to refer to the explicator that follows it, a contrivance would be needed concerning precedence, by saying, for example, that it precedes by virtue of the pronoun’s coinage and what it requires,"},
    {"type": "pair",
     "ar": "فإنه يقتضي لذاته تقدم المرجع، لكن قد يخالف وضعه ومقتضاه لغرض.",
     "en": "for in itself it requires the referent to precede, though it may depart from its coinage and what it requires for a purpose."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جعل التقدم رتبة داخلا في التقدم لفظا، لكن تقديرا لأنه أنسب به منه لسائر الأقسام،",
     "en": "He made precedence in rank part of precedence in wording, but [precedence] by supposition, since it is more fitting to it than to the other divisions."},
    {"type": "pair",
     "ar": "نعم يتجه عليه أنه شاع مقابلته لفظا بقوله: تقديرا فجعل تقديرا تحته ملتبس مخل بالبيان.",
     "en": "Yes, it may be objected against him that it is common to set it against “in wording” by saying “by supposition”; so making “by supposition” fall under it is confusing and impairs clarity."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أراد بالذكر من حيث اللفظ أن يكون المعنى مقصودا باللفظ باستعمال فيه، وإلا فمعنى اللفظ باعتبار أنه مدلول اللفظ مذكور لفظا.",
     "en": "By mention in respect of wording he meant that the meaning is intended by the word through its being used for it; otherwise, the meaning of a word, considered as what the word signifies, is mentioned in wording."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة المائدة: ٨.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:8."},
]
