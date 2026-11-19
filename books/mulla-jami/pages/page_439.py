# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 439 (printed ٤٣٨)."""

PAGE_NUMBER = 439
PRINTED_PAGE = "٤٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… (فعلت وفعلن) أي: ضمير «فعلت»» at the foot of PDF p. 438 (mid-sentence).
    {"type": "matn",
     "ar": "مقرونا بتاء التأنيث بتأويل الجماعة، وضمير «فعلن» أي: بالنون.",
     "en": "…joined to the feminine tāʾ, by construing [them] as a group, and the pronoun of “faʿalna”, that is, with the nūn."},
    {"type": "matn",
     "ar": "أما في جمع المؤنث فظاهر؛ لأن هذه النون موضوعة له.",
     "en": "In the feminine plural this is evident, because this nūn is coined for it."},
    {"type": "matn",
     "ar": "وأما في جمع المذكر الغير العاقل كـ«الأيام»؛ فلأنه لا أصل له في التذكير كـ«الرجال»، فيراعى حقه، فأجري مجرى المؤنث.",
     "en": "In the plural of a non-rational masculine, like “al-ayyām”, it is because it has no standing in masculinity, as “al-rijāl” has, such that its due would be observed; so it was treated like the feminine."},
    {"type": "matn",
     "ar": "وفي الحواشي الهندية موافقا لشرح الرضي: أن النون موضوعة لجمع غير العقلاء كـ«الواو» وضعت لجمع العاقلين،",
     "en": "In the Indian glosses (al-Ḥawāshī al-Hindiyya), in agreement with al-Raḍī’s commentary: the nūn is coined for the plural of non-rational beings, as the wāw was coined for the plural of rational beings;"},
    {"type": "matn",
     "ar": "فاستعمالها في النساء للحمل على جمع غير العقلاء؛ إذ الإناث لنقصان عقولهن تجرين مجرى غير العقلاء.",
     "en": "its use for women is by assimilation to the plural of non-rational beings, since females, owing to the deficiency of their intellects, are treated like non-rational beings."},

    {"type": "section", "ar": "[المثنى]",
     "en": "The Dual"},

    {"type": "matn",
     "ar": "(المثنى: ما لحق آخره) أي: آخر مفرده، بتقدير المضاف[[١]]، أو قدر بعد قوله: «ونون مكسورة» قولنا: «مع لواحقه»[[٢]]،",
     "en": "(The dual (muthannā) is that to whose end is attached), that is, to the end of its singular, by supposing an elided first term of annexation; or else our words “with its attachments” are supposed after his words “and a nūn with kasra”;"},
    {"type": "matn",
     "ar": "وإلا[[٣]] لا يصدق[[٤]] التعريف إلا على مثل: «مسلم»[[٥]] من «مسلمان ومسلمين» كما لا يخفى.",
     "en": "otherwise the definition is true only of the like of “muslim” in “muslimān” and “muslimayn”, as is evident."},
    {"type": "matn",
     "ar": "ولو اكتفى بظهور المراد لاستغنى عن هذه التكلفات[[٦]]",
     "en": "Had he relied on the meaning being clear, he would have had no need of these contrivances."},
    {"type": "matn",
     "ar": "(ألف) حالة الرفع (أو ياء مفتوح ما قبلها) أي: مفتوح حرف كان قبل الياء، حالتي النصب والجر ليمتاز عن صيغة الجمع،",
     "en": "(An alif), in the nominative state, (or a yāʾ with fatḥa on what precedes it), that is, with fatḥa on the letter before the yāʾ, in the accusative and genitive states, so as to be distinguished from the plural form;"},
    {"type": "matn",
     "ar": "ولم يعكس لكثرة التثنية وخفة الفتحة",
     "en": "it was not reversed, because the dual is more frequent and the fatḥa is lighter,"},
    {"type": "matn",
     "ar": "(ونون) عوضا عن الحركة أو التنوين (مكسورة) لئلا يتوالى الفتحات في صورة الرفع، وهي فتحة ما قبل الألف التي في حكم الفتحتين وفتحة النون",
     "en": "(and a nūn), in compensation for the vowel or the nunation (tanwīn), (with kasra), so that fatḥas do not follow one another in the nominative form, namely the fatḥa before the alif, which counts as two fatḥas, and the fatḥa of the nūn,"},
    {"type": "matn",
     "ar": "(ليدل) ذلك اللحوق أو اللاحق وحده أو مع الملحوق،",
     "en": "(so as to indicate), that is, that attachment, or the attached element alone or together with what it is attached to."},
    {"type": "matn",
     "ar": "ولا بأس باشتماله على لحوق النون وعدم دلالة لحوقها على ذلك؛",
     "en": "There is no harm in its including the attachment of the nūn, though the nūn’s attachment does not indicate that;"},
    {"type": "matn",
     "ar": "لأنه على تقدير تسليمه[[٧]] إذا دل أمران من أمور ثلاثة",
     "en": "for, granting it, if two of three things indicate…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يخفى أنه يصدق على مسلمون ومسلمات، فقد تبدل بهذا التقدير إشكال بإشكال.",
     "en": "It is evident that it is true of “muslimūn” and “muslimāt”; so by this supposition one difficulty has been exchanged for another."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فحينئذ يكون التثنية مجموع المفرد، والألف والياء والنون،",
     "en": "Then the dual would be the sum of the singular and the alif, yāʾ and nūn;"},
    {"type": "pair",
     "ar": "فلم يكن مسلما البلد تثنية؛ إذ لم يوجد المسلم مع تلك اللواحق،",
     "en": "so “muslimā al-baladi” (the two Muslims of the town) would not be a dual, since “muslim” is not found with those attachments."},
    {"type": "pair",
     "ar": "لا يقال: النون مقدرة؛ لأن النون في حال الإضافة كالتنوين كما لا تقدير للتنوين معها لا تقدر للنون.",
     "en": "It cannot be said that the nūn is supposed, because the nūn in annexation is like the nunation: just as the nunation is not supposed with it, the nūn is not supposed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: وإن لم يكن أحد الأمرين، بل ترك على ظاهره.",
     "en": "That is: if neither of the two is the case, but it is left as it appears."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فلا يكون صادقا على المحدود، فلا يكون تعريفا؛ لأنه لا يكون جامعا ولا مانعا.",
     "en": "So it is not true of the thing defined, and so it is not a definition, because it is neither inclusive nor exclusive."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فلم يكن جامعا لعدم صدقه على شيء من أفراده، ولا مانعا لصدقه على المفرد.",
     "en": "So it is not inclusive, since it is not true of any of its instances, nor exclusive, since it is true of the singular."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لعله أراد أن المراد الظاهر من هذه العبارة ما في آخره ألف أو ياء ونون ملحقات، فاعرفه.",
     "en": "Perhaps he meant that the evident meaning of this expression is that at whose end there are an alif or a yāʾ, and a nūn, attached; so take note of it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذا منع ما أجمعوا عليه من كون علامة التثنية الألف والياء وكون النون عوضا عن الحركة أو التنوين في المفرد،",
     "en": "This is a denial of what they agreed upon: that the sign of the dual is the alif and the yāʾ, and that the nūn is in compensation for the vowel or the nunation in the singular;"},
    {"type": "pair",
     "ar": "وما ذكره على تقدير التسليم في غاية السخافة،",
     "en": "and what he says on the supposition of granting it is extremely weak."},
    {"type": "pair",
     "ar": "وكيف لا وليس الغرض عن إلحاق الألف أو الياء والنون الدلالة، بل عن مجرد إلحاق الألف أو الياء.",
     "en": "How could it be otherwise, when the purpose of attaching the alif or the yāʾ and the nūn is not the indication; rather, [the indication comes] from the mere attachment of the alif or the yāʾ."},
]
