# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 80 (printed ٧٩)."""

PAGE_NUMBER = 80
PRINTED_PAGE = "٧٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "أي: نظائرها السبع، وهي «ثلاثون إلى تسعين»، وليس «عشرون» جمع «عشرة»، ولا «ثلاثون» جمع «ثلاثة»؛",
     "en": "That is: its seven counterparts, which are “thirty” through “ninety.” “Twenty” is not the plural of “ten,” nor is “thirty” the plural of “three”;"},
    {"type": "matn",
     "ar": "وإلا لصح إطلاق «عشرين» على[[١]] ثلاثة مقادير العشرة، وإطلاق ثلاثين على التسعة؛ لأنه[[٢]] ثلاثة مقادير الثلاثة، وعلى هذا القياس البواقي.",
     "en": "for otherwise it would be valid to apply “twenty” to three measures of ten [= thirty], and to apply “thirty” to the nine — because it [the nine] is three measures of three — and the remaining [numbers follow] by this analogy."},
    {"type": "matn",
     "ar": "وأيضا هذه الألفاظ تدل على معان معينة، ولا تعيين في الجموع. فإعرابها (بالواو) رفعا (والياء) نصبا وجرا.",
     "en": "Moreover, these words denote specific meanings, whereas there is no specification (taʿyīn) in plurals. So their inflection is (by the wāw) in the nominative (and the yāʾ) in the accusative and genitive."},
    {"type": "matn",
     "ar": "وإنما جعل إعراب المثنى مع ملحقاته، والجمع مع ملحقاته بالحروف؛ لأنها فروع للواحد، وفي آخرها حرف يصلح للإعراب، وهو[[٣]] علامة التثنية والجمع[[٤]]، فناسب أن يجعل ذلك الحرف إعرابهما، ليكون إعرابهما فرعا لإعرابه[[٥]]، كما أنهما فرعان له؛ لأن الإعراب بالحروف فرع الإعراب بالحركة.",
     "en": "The dual — together with its appendages — and the plural — together with its appendages — were made to be inflected with letters only because they are derivatives (furūʿ) of the singular, and at their end is a letter suited to inflection, which is [also] the sign of duality and plurality; so it was fitting that this letter be made their inflection, in order that their inflection be a derivative of its [the singular’s] inflection, just as they are derivatives of it — for inflection by letters is a derivative of inflection by vowel."},
    {"type": "matn",
     "ar": "ولما جعل إعرابهما بالحروف، وكانت حروف الإعراب ثلاثة، وإعرابهما[[٦]] ستة: ثلاثة للمثنى، وثلاثة للمجموع، فلو جعل إعراب كل واحد منهما بتلك الحروف الثلاثة لوقع الالتباس بينهما.",
     "en": "And since their inflection was made by letters, while the letters of inflection are three [alif, wāw, yāʾ] and their inflection [comes to] six — three for the dual and three for the plural — then had the inflection of each of the two been [assigned] by those three letters, confusion (iltibās) would have occurred between them."},
    {"type": "matn",
     "ar": "ولو خص المثنى بها بقي المجموع بلا إعراب، ولو خص المجموع بها بقي المثنى بلا إعراب، فوزعت عليهما[[٧]] بأن جعلوا الألف علامة الرفع في المثنى؛ لأنه[[٨]] الضمير المرفوع للتثنية في الفعل نحو: «يضربان» و«ضربا»،",
     "en": "Had it [alif] been assigned exclusively to the dual, the plural would remain without inflection; and had it been assigned exclusively to the plural, the dual would remain without inflection; so they were distributed between the two, in that they made the alif the sign of the nominative in the dual — because it is the nominative pronoun of the dual in the verb, as in “yaḍribāni” and “ḍarabā” —"},
    {"type": "matn",
     "ar": "والواو علامة الرفع في المجموع؛ لأنه[[٩]] الضمير المرفوع للجمع في الفعل نحو: «يضربون» و«ضربوا»، وجعلوا إعرابهما[[١٠]] بالياء حالة الجر على الأصل، وفرقوا بينهما بأن فتحوا ما قبل...",
     "en": "and [they made] the wāw the sign of the nominative in the plural — because it is the nominative pronoun of the plural in the verb, as in “yaḍribūna” and “ḍarabū.” They made the inflection of the two by the yāʾ in the state of the genitive, in accordance with the default, and they distinguished between them by putting a fatḥa on what precedes ..."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: ثلاثين.",
     "en": "That is: thirty."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: التسعة.",
     "en": "That is: the nine."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: ذلك الحرف.",
     "en": "That is: that letter."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: جعلت الألف علامة للتثنية، والواو علامة للجمع لمناسبة الألف بخفته لقلة عدد المثنى، والواو بثقله لكثرة عدد الجمع،",
     "en": "Shaykh al-Raḍī said: The alif was made the sign of the dual and the wāw the sign of the plural because of the suitability of the alif — by its lightness — to the smallness of the dual’s number, and of the wāw — by its heaviness — to the largeness of the plural’s number;"},
    {"type": "pair",
     "ar": "وهذا الحكم مطرد في جميع المثنى والمجموع نحو: ضربا، وضربوا، وأنتما، وأنتموا، وهما، وهموا، وكما، وكموا.",
     "en": "and this ruling is consistent throughout all duals and plurals, as in: ḍarabā and ḍarabū, antumā and antumū, humā and humū, kumā and kumū."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: إعراب الواحد.",
     "en": "That is: the inflection of the singular."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: إعراب المثنى والجمع.",
     "en": "That is: the inflection of the dual and the plural."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: على المثنى والجمع.",
     "en": "That is: over the dual and the plural."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الألف.",
     "en": "That is: the alif."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: الواو.",
     "en": "That is: the wāw."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: المثنى والجمع.",
     "en": "That is: the dual and the plural."},
]
