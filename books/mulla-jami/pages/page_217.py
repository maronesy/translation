# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 217 (printed ٢١٦)."""

PAGE_NUMBER = 217
PRINTED_PAGE = "٢١٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "أي: لمجرد التخفيف[[١]]، لا لعلة أخرى[[٢]] مفضية إلى الحذف المستلزم للتخفيف.",
     "en": "…that is, for lightening alone, not for some other cause leading to an elision that entails lightening."},
    # REVIEW: print reads «ويعلم منه ترخيم المنادى بالمقايسة»; the sense requires «غير المنادى»; transcribed as printed.
    {"type": "matn",
     "ar": "فعلى هذا يكون ذلك التعريف مخصوصا بترخيم المنادى، ويعلم منه ترخيم المنادى بالمقايسة.",
     "en": "On this [reading] that definition is specific to curtailment of the vocative, and curtailment of [what is not] the vocative is known from it by analogy."},
    {"type": "matn",
     "ar": "ويمكن حمله على تعريف الترخيم مطلقا بإرجاع الضمير المرفوع إلى الترخيم مطلقا[[٣]]، والضمير المجرور إلى الاسم[[٤]].",
     "en": "It may also be taken as a definition of curtailment absolutely, by referring the nominative pronoun to curtailment absolutely and the genitive pronoun to the noun."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط ترخيم المنادى على التقدير الأول أو شرط الترخيم إذا كان واقعا في المنادى[[٥]] على التقدير الثاني أمور أربعة، ثلاثة منها عدمية:",
     "en": "(Its condition)—that is, the condition of curtailing the vocative on the first construal, or the condition of curtailment when it occurs in the vocative on the second—consists of four things, three of them negative:"},
    {"type": "matn",
     "ar": "١-وهي (ألا يكون مضافا[[٦]]) حقيقة أو حكما[[٧]]، فدخل فيه المشبه بالمضاف أيضا؛",
     "en": "1. They are: (that it not be annexed), really or by status; so what resembles the annexed is also included in this,"},
    {"type": "matn",
     "ar": "إذ لا يمكن الحذف من الأول؛ لأنه ليس آخر أجزاء المنادى نظرا إلى المعنى[[٨]]، ولا من الثاني[[٩]]؛ لأنه ليس آخر أجزائه[[١٠]] نظرا إلى اللفظ، فامتنع الترخيم فيهما[[١١]] بالكلية.",
     "en": "since elision is not possible from the first [element], because it is not the last of the vocative’s parts with respect to meaning, nor from the second, because it is not the last of its parts with respect to wording; so curtailment is excluded in both entirely."},
    {"type": "matn",
     "ar": "٢-(و) أن (لا) يكون (مستغاثا) ولا مجرورا باللام، لعدم ظهور أثر النداء فيه من",
     "en": "2. (And) that it (not) be (the one called for help—mustaghāthan) and not governed in the genitive by the lām, since the effect of the vocative does not appear in it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فخرج نحو: قاض؛ لأن حذفه للإعلال،",
     "en": "So such as “qāḍin” is excluded, because its elision is due to phonetic weakening (iʿlāl);"},
    {"type": "pair",
     "ar": "وكذا نحو: يد لأن حذف آخره للزوم أحد الأمرين: إما تقدير الإعراب إذا أسكن الآخر، وإما إجراء الإعراب على حرف العلة إذا حرك، وذلك ثقيل.",
     "en": "and likewise such as “yad,” because the elision of its end is due to one of two consequences being unavoidable: either the iʿrāb being implied when the end is made quiescent, or the iʿrāb being placed on the weak letter when it is given a vowel—and that is heavy."},
    {"type": "pair",
     "ar": "وقيل في إخراجه إن الترخيم حذف في التركيب، والحذف في يد حالة الإفراد.",
     "en": "It has been said, regarding its exclusion, that curtailment is an elision within the construction, whereas the elision in “yad” is in the isolated state."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "من قال: إنه حذف في الآخر بلا علة، أو على سبيل الاعتباط أراد هذا المعنى،",
     "en": "Whoever said that it is an elision at the end without cause, or by way of iʿtibāṭ, meant this sense."},
    {"type": "pair",
     "ar": "والاعتباط في اللغة: ذبح الشاة بلا علة.",
     "en": "Iʿtibāṭ in the lexicon is slaughtering a sheep without [its having] an ailment."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن ذكر المقيد مستلزم لذكر المطلق.",
     "en": "Because mentioning the qualified entails mentioning the unqualified."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن الترخيم لا يوجد في غير الاسم.",
     "en": "Because curtailment is not found in other than the noun."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولك أن ترجع الضمير إلى قوله: ترخيم المنادى.",
     "en": "You may also refer the pronoun to his words “curtailment of the vocative.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لو قال: أن يكون مفردا لكان أولى؛ لأنه أظهر في إخراج شبه المضاف إذا سبق منه جعل المفرد في مقابلة المضاف وشبهه.",
     "en": "Had he said “that it be single (mufrad),” it would have been better, because that is clearer in excluding what resembles the annexed, since he earlier set the single against the annexed and what resembles it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيل: اكتفى بذكر المضاف من المشبه به؛ إذ هما يتحدان حكما.",
     "en": "It has been said: he was content to mention the annexed instead of what resembles it, since the two are one in ruling."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هذا ظاهر إذا كان المركب الإضافي علما، فإن الجزء الأول بمنزلة زاي «زيد».",
     "en": "This is evident when the genitive compound is a proper name, for the first element is like the zāy of “Zayd.”"},
    {"type": "pair",
     "ar": "وأما إذا لم يكن علما فبيانه أن المضاف من حيث هو مضاف لا يتم بدون المضاف إليه.",
     "en": "When it is not a proper name, the explanation is that the annexed, as annexed, is not complete without what it is annexed to."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    # REVIEW: the hemistich «خذوا حظكم يا آل عكرم» (a line of poetry, not Qurʾān) is printed inside ornate Qurʾānic brackets; kept as printed.
    {"type": "pair",
     "ar": "خلافا للكوفيين نحو قوله: ﴿خذوا حظكم يا آل عكرم﴾ أي: آل عكرمة.",
     "en": "Contrary to the Kūfans, [who cite] such as his words “Take your share, O family of ʿIkrim,” that is, family of ʿIkrima."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "هذا ظاهر إذا لم يكن المركب الإضافي علما.",
     "en": "This is evident when the genitive compound is not a proper name."},
    {"type": "pair",
     "ar": "أما إذا كان علما، فلأن المركب الإضافي يراعى حال جزأيه قبل العلمية في استقلال كل من الجزئين بإعرابه.",
     "en": "When it is a proper name, [the reason] is that in the genitive compound the state of its two parts before it became a name is observed, each part keeping its own iʿrāb."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "بعد رعاية اللفظ والمعنى.",
     "en": "Once both wording and meaning are taken into account."},
]
