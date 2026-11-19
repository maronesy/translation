# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 210 (printed ٢٠٩)."""

PAGE_NUMBER = 210
PRINTED_PAGE = "٢٠٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "فإن جواز الضمة لا يكون إلا في المبني على الضم",
     "en": "…for the permissibility of the ḍamma exists only in what is built on the ḍamma;"},
    {"type": "matn",
     "ar": "(الموصوف[[١]] بـ«ابن») مجرد عن التاء أو ملحق بها[[٢]] أعني: «ابنة» بلا تخلل واسطة بين الابن وموصوفه، كما هو المتبادر[[٣]] إلى الفهم،",
     "en": "(qualified by “ibn”), whether bare of the tāʾ or with it attached—I mean “ibna”—with no intermediary intervening between “ibn” and what it qualifies, as is what first comes to mind;"},
    {"type": "matn",
     "ar": "فيخرج عنه مثل: «يا زيد الظريف ابن عمرو»",
     "en": "so such as “O Zayd the witty, son of ʿAmr” is excluded from it;"},
    {"type": "matn",
     "ar": "(مضافا) أي: حال كون ذلك الابن مضافا (إلى علم آخر)،",
     "en": "(annexed), that is, that “ibn” being annexed (to another proper name)."},
    {"type": "matn",
     "ar": "فكل علم يكون كذلك يجوز فيه الضم؛ لما عرفت من قاعدة بناء المنادى المفرد المعرفة على ما يرفع به،",
     "en": "Every proper name that is so may take the ḍamma, by the rule you have learned that a definite singular vocative is built on what marks its nominative;"},
    # REVIEW: print reads «والكسرة مناسبة للتخفيف»; the sense suggests «والكثرة» (frequency); transcribed as printed.
    {"type": "matn",
     "ar": "لكن (يختار فتحه) لكثرة وقوع المنادى الجامع لهذه الصفات، والكسرة مناسبة للتخفيف،",
     "en": "but (its fatḥa is preferred), because of the frequency with which a vocative combining these attributes occurs, and the kasra [sic; perhaps “frequency”] suits lightening;"},
    {"type": "matn",
     "ar": "فخففوه بالفتحة[[٤]] التي هي حركته الأصلية[[٥]]؛ لكونه مفعولا.",
     "en": "so they lightened it with the fatḥa, which is its original vowel, because it is an object."},
    {"type": "matn",
     "ar": "(وإذا نودي المعرف باللام[[٦]]) أي: إذا أريد نداؤه[[٧]] (قيل:) مثلا[[٨]] («يا أيها الرجل») بتوسيط «أي»[[٩]] مع هاء التنبيه[[١٠]] بين حرف النداء والمنادى المعرف باللام؛ تحرزا عن اجتماع",
     "en": "(And when a noun made definite by the lām is called), that is, when its vocation is intended, (one says), for example, (“yā ayyuhā al-rajulu”—O you man), by interposing “ayy” together with the hāʾ of alerting (hāʾ al-tanbīh) between the vocative particle and the vocative made definite by the lām, to guard against the combination…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: هذا من مسائل المنادى فكيف ذكر مع مسائل التابع؟",
     "en": "If you say: this is among the questions of the vocative, so how is it mentioned with the questions of the appositive?"},
    # REVIEW: print reads «التوابع المضاف»; probably «التابع المضاف»; transcribed as printed.
    {"type": "pair",
     "ar": "قلت: هو من مسائل التابع باعتبار أن التوابع المضاف أوجب اختيار بناء المنادى على الفتح.",
     "en": "I say: it is among the questions of the appositive, inasmuch as the annexed appositive necessitated the preference for building the vocative on the fatḥa."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: من غير تغير؛ إذ لا يجوز الفتح في يا هند بنت عمرو.",
     "en": "He means: without alteration; for the fatḥa is not allowed in “yā Hindu binta ʿAmrin.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "المتبادر ما هو الأعم.",
     "en": "What first comes to mind is the more general."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وتحذف الألف خطا في «ابن وابنة»، وخففوا العلم الجامع لتلك الصفات في غير النداء بحذف تنوينه والألف خطا في «ابن».",
     "en": "The alif is dropped in writing in “ibn” and “ibna”; and outside vocation they lightened the proper name combining these attributes by dropping its tanwīn, and the alif in writing in “ibn.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: سهل ذلك كون الفتحة حركته المستحقة في الأصل.",
     "en": "That is: this was made easy by the fatḥa being the vowel originally due to it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن نداء مثنى العلم وجمعه المعرفين باللام بحذف اللام لا بالتوسيط، فيقال في الزيدان والزيدون: يا زيدان ويا زيدون.",
     "en": "Against this: the vocation of the dual and plural of a proper name made definite by the lām is by dropping the lām, not by interposition; so one says for “al-Zaydān” and “al-Zaydūn”: “yā Zaydāni” and “yā Zaydūna.”"},
    {"type": "pair",
     "ar": "وقد يجاب: بأن اللام فيهما لجبر نقص التعريف الزائل بالتنكير لا للتعريف، فيخرجان بقوله: المعرف باللام.",
     "en": "It may be answered that the lām in these two serves to repair the loss of definiteness removed by indefiniteness, not for definiteness; so the two are excluded by his words “made definite by the lām.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "كثيرا ما يطلق الأفعال الاختيارية ويراد مبدأها، أعني: الإرادة.",
     "en": "Voluntary acts are often named while their source, namely the will, is meant."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إنما قال: مثلا؛ لأن قصد نداء المعرف باللام على إطلاقه لا يستلزم قول يا أيها الرجل وأخويه بخصوصها.",
     "en": "He said “for example” only because intending to call a noun made definite by the lām, taken generally, does not entail saying “yā ayyuhā al-rajulu” and its two sister forms specifically."},
    {"type": "pair",
     "ar": "ولك أيضا في تصحيح الاستلزام أن تريد بقوله: يا أيها الرجل وأخويه الكلام الذي وسط فيه أي: أو هذا أو أيهذا",
     "en": "You may also, to make the entailment hold, take his “yā ayyuhā al-rajulu” and its two sisters to mean speech in which “ayy,” or “hādhā,” or “ayyuhādhā” is interposed,"},
    {"type": "pair",
     "ar": "كما قيل في: لكل فرعون موسى: أن المراد لكل ظالم عادل.",
     "en": "just as is said of “for every Pharaoh a Moses”: what is meant is “for every oppressor a just man.”"},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "هي موصوفة. قال الأخفش: هي موصولة حذف صدر صلتها وجوبا لمناسبة التخفيف للمنادي.",
     "en": "It (ayy) is a qualified noun. Al-Akhfash said: it is a relative noun, the head of whose relative clause is obligatorily elided, because lightening suits the vocative."},
    {"type": "pair",
     "ar": "ويؤيده كثرة وقوعها موصولة وندرة وقوعها موصوفة.",
     "en": "This is supported by its frequent occurrence as a relative and its rare occurrence as a qualified noun."},
    {"type": "pair",
     "ar": "وإنما لم ينتصب مع أنها مشبهة بالمضاف؛ لأنها إذا حذف صدر صلتها تبنى على الضم.",
     "en": "It does not take the accusative, though it resembles the annexed, only because when the head of its relative clause is elided it is built on the ḍamma."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "المشاركة لحرف النداء في التنبيه؛ لأن النداء أيضا تنبيه، فانجبر بقرب هاء التنبيه ما فات ببعد حرف النداء.",
     "en": "[Its hāʾ] shares alerting with the vocative particle, since vocation too is alerting; so the nearness of the hāʾ of alerting repairs what was lost by the distance of the vocative particle."},
]
