# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 447 (printed ٤٤٦)."""

PAGE_NUMBER = 447
PRINTED_PAGE = "٤٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "فإن قيل: اسم التفضيل يوجب ثبوت أصل الفعل في المفضل عليه، ولا كثرة في الواحد؟",
     "en": "If it is said: the elative noun (ism al-tafḍīl) requires that the root of the action be established in what is surpassed, yet there is no plurality in the single one?"},
    {"type": "matn",
     "ar": "قيل: ثبوت أصل الفعل إما أن يكون محققا، أو على سبيل الفرض، كما يقال: «فلان أفقه من الحمار وأعلم من الجدار».",
     "en": "It is answered: the establishment of the root of the action is either real or by way of supposition, as one says: “So-and-so has more understanding than a donkey and more knowledge than a wall.”"},
    {"type": "matn",
     "ar": "(فإن كان آخره[[١]]) أي: آخر مفرده[[٢]] (ياء) ملفوظة كـ«القاضي»، أو مقدرة كـ«قاض» (قبلها كسرة حذفت) الياء",
     "en": "(If its end), that is, the end of its singular, (is a yāʾ), pronounced, as in “al-qāḍī”, or implied, as in “qāḍin”, (preceded by a kasra, it is dropped), the yāʾ,"},
    {"type": "matn",
     "ar": "(مثل: «قاضون») جمع «قاض»، فإن أصله: «قاضيون» نقلت ضمة الياء إلى ما قبلها بعد سلب حركة ما قبلها طلبا للخفة، وحذفت الياء لالتقاء الساكنين،",
     "en": "(as in “qāḍūn”), the plural of “qāḍin”; for its origin is “qāḍiyūn”: the ḍamma of the yāʾ was moved to what precedes it, after removing the vowel of what precedes it, for lightness, and the yāʾ was dropped because of the meeting of two quiescent letters."},
    {"type": "matn",
     "ar": "وعلى هذا القياس حالتا النصب والجر مثل: «قاضين»، فإن أصله: «قاضيين» حذفت كسرة الياء لثقل اجتماع الكسرتين واليائين، فسقطت لالتقاء الساكنين.",
     "en": "On this pattern are the accusative and genitive states, as in “qāḍīn”, for its origin is “qāḍiyīn”: the kasra of the yāʾ was dropped because of the heaviness of the coming together of two kasras and two yāʾs, and [the yāʾ] fell away because of the meeting of two quiescent letters."},
    {"type": "matn",
     "ar": "(وإن كان آخره) أي: آخر الاسم الذي[[٣]] أريد جمعه (مقصورا) أي: ألفا مقصورة[[٤]] (حذفت الألف) لالتقاء الساكنين",
     "en": "(And if its end), that is, the end of the noun whose plural is intended, (is shortened), that is, a shortened alif, (the alif is dropped), because of the meeting of two quiescent letters,"},
    {"type": "matn",
     "ar": "(وبقي) بعد الحذف (ما قبلها) أي: حرف كان قبل الألف على ما كان عليه (مفتوحا) ولم يغير ليدل الفتحة على الألف",
     "en": "(and there remains), after the dropping, (what precedes it), that is, the letter that was before the alif, as it was, (with a fatḥa); it is not changed, so that the fatḥa may point to the alif,"},
    {"type": "matn",
     "ar": "(مثل: «مصطفون») في حالة الرفع (و«مصطفين») في حالتي النصب والجر،",
     "en": "(as in “muṣṭafawn”) in the nominative state (and “muṣṭafayn”) in the accusative and genitive states;"},
    {"type": "matn",
     "ar": "فأصلهما: «مصطفيون ومصطفيين» قلبت الياء ألفا، لتحركها وانفتاح ما قبلها، وحذفت الألف لالتقاء الساكنين.",
     "en": "their origins are “muṣṭafayūn” and “muṣṭafayīn”: the yāʾ was converted into an alif because it is vowelled and what precedes it has a fatḥa, and the alif was dropped because of the meeting of two quiescent letters."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط اسم أريد جمعيته جمع الصحيح المذكر، يعني: شرط صحة جمعيته",
     "en": "(Its condition), that is, the condition of a noun intended to be pluralized with the sound masculine plural, meaning: the condition for the validity of its pluralization,"},
    {"type": "matn",
     "ar": "(إن كان) ذلك الاسم (اسما) أي: اسما محضا[[٥]] من غير معنى وصفية فيه (فمذكر علم) أي: فكونه مذكرا علما (يعقل) من حيث مسماه لا من حيث لفظه،",
     "en": "(if) that noun (is a noun), that is, a pure noun, with no adjectival sense in it, (is: a masculine proper name), that is, its being a masculine proper name, (of a rational being), in respect of what it names, not in respect of its wording."},
    {"type": "matn",
     "ar": "وإنما اشترط ذلك، لكون هذا الجمع أشرف الجموع، لصحة بناء الواحد فيه، والمذكر العلم",
     "en": "He made this a condition only because this plural is the noblest of plurals, since the structure of the singular remains sound in it; and the masculine, the proper name…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "جعل الضمير المستتر في «كان» راجعا إلى لفظ آخره ليوافق المعطوف عليه بخلاف ما إذا رجع إلى الاسم.",
     "en": "He made the concealed pronoun in “kāna” refer to the word “its end” so as to agree with what it is coordinated with, unlike if it referred to the noun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "على حذف المضاف؛ لأن الياء والألف ليسا آخر الجمع بل وسطه.",
     "en": "By ellipsis of the annexed term, because the yāʾ and the alif are not the end of the plural but its middle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جعل ضمير كان لآخر الاسم ولك أن تجعله للاسم.",
     "en": "He made the pronoun of “kāna” refer to the end of the noun; you may make it refer to the noun."},
    {"type": "pair",
     "ar": "وقوله: حذفت دون حذف الضمير الراجع إلى الآخر يدل عليه.",
     "en": "His saying “ḥudhifat” (it was dropped), without dropping the pronoun referring to “the end”, indicates this."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ملفوظة أو مقدرة.",
     "en": "Pronounced or implied."},
    {"type": "pair",
     "ar": "وقد نبه المصنف على أن الياء والألف أعم من المذكورة والمقدرة حيث مثل بقاضين دون القاضين وبمصطفون دون المصطفون، فتأمل.",
     "en": "The author has pointed out that the yāʾ and the alif are more general than the expressed and the implied, since he gave as examples “qāḍīn” rather than “al-qāḍīn” and “muṣṭafawn” rather than “al-muṣṭafawn”; so reflect."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأخصر غير صفة يعني: أن المراد بالاسم ما يقابل الصفة لا ما يقابل الفعل والحرف، فلا يلزم اتحاد اسم «كان» وخبرها.",
     "en": "More concise would be “not an adjective”. He means that what is meant by “noun” is what stands opposite the adjective, not what stands opposite the verb and the particle; so it does not follow that the subject of “kāna” and its predicate are identical."},
]
