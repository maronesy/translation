# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 305 (printed ٣٠٤)."""

PAGE_NUMBER = 305
PRINTED_PAGE = "٣٠٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أن التقسيم إلى الإضافة» from the foot of PDF p. 304.
    {"type": "matn",
     "ar": "المعنوية واللفظية، إنما هو للإضافة بتقدير حرف الجر،",
     "en": "…semantic and verbal annexation applies only to annexation by supposition of a preposition;"},
    {"type": "matn",
     "ar": "لكنه لم يبين تقدير حرف الجر فيها لا في المتن ولا في شرحه، ولم ينقل عنه شيء في سائر مصنفاته.",
     "en": "but he did not explain the supposition of the preposition in it, either in the base text or in his commentary, and nothing on it is transmitted from him in the rest of his works."},
    {"type": "matn",
     "ar": "وقد تكلف بعضهم في إضافة الصفة إلى معمولها مثل: «ضارب زيد» بتقدير «اللام» تقوية للعمل أي: «ضارب لزيد»،",
     "en": "Some have strained, in the annexation of an adjective to what it governs, as in “ḍāribu Zaydin,” [to explain it] by supposing a lām that strengthens the governing, that is, “ḍāribun li-Zaydin” (a striker of Zayd);"},
    {"type": "matn",
     "ar": "وفي إضافتها إلى فاعلها مثل: «الحسن الوجه» بتقدير «من» البيانية،",
     "en": "and in its annexation to its agent, as in “al-ḥasanu l-wajhi,” by supposing the explicative “min” (min al-bayāniyya);"},
    {"type": "matn",
     "ar": "فإن ذكر «الوجه» في قوة قولنا: «جاءني زيد الحسن الوجه» بمنزلة التمييز،",
     "en": "for the mention of “the face” in our saying “Zayd, the one handsome of face, came to me” is equivalent to a specifying accusative (tamyīz),"},
    {"type": "matn",
     "ar": "فإن في إسناد «الحسن» إلى «زيد» إبهاما، فإنه لا يعلم أنه أي شيء منه حسن، فإذا ذكر الوجه فكأنه قال من حيث الوجه.",
     "en": "since in predicating “handsome” of “Zayd” there is vagueness: it is not known which part of him is handsome; so when “the face” is mentioned, it is as though he said “with respect to the face.”"},
    {"type": "matn",
     "ar": "فإن قلت: هذا في الحقيقة تخصيص، فلا يصح أن الإضافة اللفظية لا تفيد إلا تخفيفا في اللفظ؟",
     "en": "If you say: this is in reality specification; so is it not unsound [to say] that verbal annexation yields nothing but lightening in the wording?"},
    {"type": "matn",
     "ar": "قلت: كان هذا التخصيص واقعا قبل الإضافة، فلا يكون مما يفيده الإضافة، فليست فائدة الإضافة اللفظية إلا التخفيف في اللفظ.",
     "en": "I say: this specification was present before the annexation, so it is not something the annexation yields; hence the benefit of verbal annexation is nothing but lightening in the wording."},
    {"type": "matn",
     "ar": "(وهي) أي: الإضافة بتقدير حرف الجر: (معنوية) أي: منسوبة إلى المعنى؛ لأنها تفيد معنى[[١]] في المضاف تعريفا أو تخصيصا.",
     "en": "(And it), that is, annexation by supposition of a preposition, is (semantic) (maʿnawiyya), that is, related to meaning, because it yields a meaning in the muḍāf, definiteness or specification;"},
    {"type": "matn",
     "ar": "(ولفظية) أي: منسوبة إلى اللفظ فقط دون المعنى، لعدم سرايتها إليه.",
     "en": "(and verbal) (lafẓiyya), that is, related to the wording only and not to the meaning, since it does not extend to [the meaning]."},
    {"type": "matn",
     "ar": "(فالمعنوية) علامتها: (أن يكون[[٢]] المضاف) فيها (غير صفة) كاسم الفاعل، والمفعول، والصفة المشبهة[[٣]].",
     "en": "(Semantic [annexation]): its sign is (that the muḍāf) in it (is not an adjective), such as the active participle, the passive participle and the assimilated adjective (al-ṣifa al-mushabbaha),"},
    {"type": "matn",
     "ar": "(مضافة إلى معمولها) أي: فاعلها أو مفعولها قبل الإضافة،",
     "en": "(annexed to what it governs), that is, to what was its agent or its object before the annexation;"},
    {"type": "matn",
     "ar": "سواء لم تكن صفة كـ«غلام زيد»، أو كانت صفة ولكن غير مضافة إلى معمولها، بل إلى غيره كـ«مصارع مصر، وكريم البلد»،",
     "en": "whether it is not an adjective, as in “ghulāmu Zaydin,” or is an adjective but not annexed to what it governs, rather to something else, as in “muṣāriʿu Miṣra” (the wrestler of Egypt) and “karīmu l-baladi” (the noble one of the town)."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «ضارب زيد، وحسن الوجه».",
     "en": "By this he excluded such as “ḍāribu Zaydin” and “ḥasanu l-wajhi.”"},
    {"type": "matn",
     "ar": "(وهي) أي: الإضافة المعنوية بحكم الاستقراء:",
     "en": "(And it), that is, semantic annexation, by the verdict of induction (istiqrāʾ), is:"},
    {"type": "matn",
     "ar": "(إما بمعنى «اللام» فيما) أي: في المضاف إليه الذي (عدا جنس المضاف وظرفه)",
     "en": "(either in the sense of “li” [the lām] in what), that is, in the muḍāf ilayhi that (is other than the genus of the muḍāf and its adverbial container [ẓarf]),"},
    {"type": "matn",
     "ar": "أي: لا يكون صادقا على المضاف وغيره ولا ظرفا له نحو: «غلام زيد»، فإن زيدا ليس",
     "en": "that is, that is neither predicable of the muḍāf and of other things nor an adverbial container for it, as in “ghulāmu Zaydin”; for Zayd is not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أراد به ما قام بالغير، وهو معنى التعريف والتخصيص.",
     "en": "By it he meant what subsists in another, namely the meaning of definiteness and specification."},
    {"type": "pair",
     "ar": "وأراد بالمعنى المذكور في المدعى ما يقابل اللفظ.",
     "en": "And by “meaning” (maʿnā) mentioned in the claim he meant what is opposed to wording."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قدر علامتها ليصح الحمل.",
     "en": "He supplied “its sign” so that the predication would be sound."},
    {"type": "pair",
     "ar": "والمشهور العام في مثله تقدير «ذو»، لكن تقدير العلامة أجدر معنى، كما لا يخفى.",
     "en": "The common, well-known practice in such cases is to supply “dhū” (possessor of); but supplying “sign” is more apt in meaning, as is evident."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والمنسوب.",
     "en": "And the relative adjective (al-mansūb)."},
]
