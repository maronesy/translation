# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 326 (printed ٣٢٥)."""

PAGE_NUMBER = 326
PRINTED_PAGE = "٣٢٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 325 ends with a complete sentence; this page opens a new paragraph.
    {"type": "matn",
     "ar": "واعلم أن الإعراب المعتبر في هذا التعريف[[١]] بالنسبة إلى اللاحق والسابق أعم من أن يكون لفظيا أو تقديريا أو محليا، حقيقة أو حكما،",
     "en": "Know that the inflection taken into account in this definition, with respect to both the follower and what precedes it, is more general than being overt, supposed or positional, whether really or by legal fiction (ḥukman);"},
    {"type": "matn",
     "ar": "فلا يرد نحو: «جاءني هؤلاء الرجال»، و«يا زيد العاقل»، و«لا رجل ظريفا».",
     "en": "so no objection arises from such as “These men came to me,” “O Zayd the intelligent,” and “There is no man, a witty one.”"},
    {"type": "matn",
     "ar": "ثم إن لفظة «كل»[[٢]] ههنا ليست في موقعها؛ لأن التعريف إنما يكون للجنس، وبالجنس لا للإفراد وبالإفراد[[٣]]،",
     "en": "Further, the word “kull” (every) here is out of place, because definition is only of the genus and by the genus, not of individuals and by individuals."},
    {"type": "matn",
     "ar": "فالمحدود بالحقيقة التابع[[٤]]، والحد مدخول «كل»، وهو ثان بإعراب سابقه من جهة واحدة،",
     "en": "What is defined is in reality “the appositive,” and the definition is what “kull” governs, namely “a second [element] bearing the inflection of what precedes it from one aspect.”"},
    {"type": "matn",
     "ar": "لكنه لما أدخل «كل»[[٥]] عليه أفاد صدق المحدود على كل أفراد الحد، فيكون مانعا،",
     "en": "But since he placed “kull” upon it, it conveyed that what is defined is true of every instance of the definition; so it is exclusive (māniʿ);"},
    {"type": "matn",
     "ar": "والظاهر انحصار المحدود فيها[[٦]]، لعدم ذكر غيرها، فيكون جامعا،",
     "en": "and what is apparent is that what is defined is confined to them, since nothing else is mentioned; so it is comprehensive (jāmiʿ)."},
    {"type": "matn",
     "ar": "فيحصل حد جامع ومانع يكون جمعه ومنعه كالمنصوص عليه.",
     "en": "Thus a comprehensive and exclusive definition results, whose comprehensiveness and exclusiveness are as though explicitly stated."},

    {"type": "section", "ar": "[النعت]",
     "en": "The Attribute (al-Naʿt)"},

    {"type": "matn",
     "ar": "(النعت[[٧]]: تابع) جنس شامل للتوابع كلها.",
     "en": "(The attribute, al-naʿt, is an appositive): a genus covering all the appositives."},
    {"type": "matn",
     "ar": "وقوله: (يدل على معنى[[٨]] في متبوعه) أي: يدل بهيئة تركيبية مع متبوعه على",
     "en": "His words (that indicates a meaning in what it follows), that is, it indicates, through a compositional form together with what it follows,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأحسن أن التعريف هنا للتابع في الإعراب.",
     "en": "It is better [to hold] that the definition here is of the appositive in inflection."},
    {"type": "pair",
     "ar": "ولما لم يكن شاملا لتابع حركة المنادى، وتابع حركة اسم \"لا\" تعرض لهما في محلهما، ولم يرض بإحالتهما إلى هذا الباب.",
     "en": "Since it did not cover the follower of the vowel of the vocative or the follower of the vowel of the noun of “lā,” he dealt with them in their own place and was not content to refer them to this chapter."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وكذا لفظة التوابع؛ لأن التعريف للجنس.",
     "en": "Likewise the word “al-tawābiʿ,” because definition is of the genus."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: إن صيغة الجمع، ولفظة «كل» مقحمتان زيدتا لبيان الجمع والمنع.",
     "en": "It may be said that the plural form and the word “kull” are intrusive, added to show comprehensiveness and exclusiveness."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وأيضا لا يصدق على تابع أنه كل ثان، فذكر \"كل\" يمنع صحة الحمل،",
     "en": "Further, it is not true of an appositive that it is “every second [element]”; so mentioning “kull” prevents the predication from being sound."},
    {"type": "pair",
     "ar": "فاحفظه فإنه من سوانح الزمان.",
     "en": "Retain this, for it is among the rare finds of the age."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا فرده. ولم يقل: إن لفظ التوابع ليس في موضعه؛ لأنه ليس معرفا،",
     "en": "Not its individual instance. He did not say that the word “al-tawābiʿ” is out of place, because it is not what is defined;"},
    {"type": "pair",
     "ar": "بل على وزان المرفوعات ونظائره بتقدير هذا الباب التوابع والمعرف هو المحذوف أي: كل ثان،",
     "en": "rather, on the model of “al-marfūʿāt” and its like, it is to be understood as “this is the chapter of the appositives,” and what is defined is the elided [term], that is, [what is] “every second [element].”"},
    {"type": "pair",
     "ar": "فمن استدرك على الشارح بأن ذكر التوابع أيضا ليس في محله، فقد أتى بالمستدرك.",
     "en": "Whoever objected to the commentator that mentioning “al-tawābiʿ” is also out of place has himself brought a correctable point."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: لفظة «كل» مقحم زائد أشير بزيادته إلى كون التعريف مانعا.",
     "en": "He means: the word “kull” is intrusive and redundant; by adding it he indicated that the definition is exclusive."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا تكلف مستغنى عنه كما لا يخفى على من له حظ أوفى بأساليب دقائق التراكيب،",
     "en": "This is a needless strain, as is not hidden from anyone with an ample share in the modes of the subtleties of constructions;"},
    {"type": "pair",
     "ar": "بل مما يلقيه البحر عن وجه الماء الصافي إلى الساحل من الأعاجيب.",
     "en": "rather, it is among the wonders that the sea casts from the face of clear water onto the shore."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قدمه لكونه أشد متابعة، وأكثر استعمالا وأوفر فائدة.",
     "en": "He put it first because it is the most closely following, the most frequently used and the most abundant in benefit."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: على حالة ثابتة في متبوعه سواء كان باعتبار نفسه أو باعتبار متعلقه، فدخل فيه نحو: «جاء رجل حسن غلامه».",
     "en": "That is, a state established in what it follows, whether with respect to itself or with respect to something connected to it; so such as “A man whose slave is handsome came” falls under it."},
]
