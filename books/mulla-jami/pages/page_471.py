# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 471 (printed ٤٧٠)."""

PAGE_NUMBER = 471
PRINTED_PAGE = "٤٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فلا يشترط كونه بعض المضاف إليه» at the foot of PDF p. 470.
    {"type": "matn",
     "ar": "(فيجوز) بهذا المعنى أن تضيفه إلى جماعة هو داخل فيهم، نحو قولك: «نبينا عليه السلام أفضل قريش» أي: أفضل الناس من بين قريش،",
     "en": "…(so it is permissible), in this sense, for you to annex it to a group in which it is included, as in your saying “our Prophet, upon him be peace, is the most excellent of Quraysh”, that is, the most excellent of people from among Quraysh;"},
    {"type": "matn",
     "ar": "وأن تضيفه إلى جماعة من جنسه ليس داخلا فيهم، كقولك: (يوسف أحسن إخوته) فإن «يوسف» لا يدخل في جملة إخوة يوسف،",
     "en": "and for you to annex it to a group of its own kind in which it is not included, as in your saying (“Yūsuf is the most handsome of his brothers”), for “Yūsuf” is not included among the brothers of Yūsuf;"},
    {"type": "matn",
     "ar": "وأن تضيفه إلى غير جماعة نحو: «فلان أعلم بغداد» أي: أعلم مما سواه، وهو مختص ببغداد؛ لأنها منشؤه أو مسكنه.",
     "en": "and for you to annex it to what is not a group, as in “so-and-so is the most learned of Baghdad”, that is, more learned than anyone besides him, while he is particular to Baghdad because it is where he grew up or where he lives."},
    {"type": "matn",
     "ar": "(ويجوز في) النوع (الأول) من نوعي اسم التفضيل المضاف، وهو الذي يقصد به الزيادة على من أضيف إليه",
     "en": "(And in the first) kind of the two kinds of the annexed elative noun (ism al-tafḍīl), namely that by which excess over what it is annexed to is intended, (there is permitted)"},
    {"type": "matn",
     "ar": "(الإفراد) أي: إفراد اسم التفضيل وإن كان موصوفه مثنى أو مجموعا، وكذا التذكير وإن كان موصوفه مؤنثا",
     "en": "(the singular), that is, putting the elative in the singular even if what it qualifies is dual or plural, and likewise the masculine even if what it qualifies is feminine,"},
    {"type": "matn",
     "ar": "نحو: «زيد أو الزيدان أو الزيدون، أو هند أو الهندان أو الهندات أفضل الناس»،",
     "en": "as in “Zayd, or the two Zayds, or the Zayds, or Hind, or the two Hinds, or the Hinds, is/are the most excellent of people”;"},
    {"type": "matn",
     "ar": "وهذا لأنه يشابه أفعل من الذي ليس فيه إلا الإفراد والتذكير في كون المفضل عليه مذكورا معه",
     "en": "this is because it resembles afʿal min, which admits only the singular and the masculine, in that the one surpassed (al-mufaḍḍal ʿalayhi) is mentioned with it;"},
    {"type": "matn",
     "ar": "(والمطابقة) أي: مطابقة اسم التفضيل إفرادا وتثنية وجمعا، وتذكيرا وتأنيثا (لمن هو) أي: اسم التفضيل صفة (له)",
     "en": "(and agreement), that is, agreement of the elative in singular, dual and plural, and in masculine and feminine, (with that of which it), the elative, is an attribute,"},
    {"type": "matn",
     "ar": "نحو: «الزيدان أفضلا الناس، والزيدون أفضلوهم، وهند فضلى النساء، والهندان فضلياهن، والهندات فضلياتهن»",
     "en": "as in “the two Zayds are the two most excellent of people, the Zayds are the most excellent of them, Hind is the most excellent of women, the two Hinds are the two most excellent of them, and the Hinds are the most excellent of them”,"},
    {"type": "matn",
     "ar": "لمشابهته ما فيه الألف واللام في كونه معرفة.",
     "en": "because of its resemblance to what has the alif and lām, in being definite."},
    {"type": "matn",
     "ar": "(وأما) النوع (الثاني) من نوعي اسم التفضيل (المضاف) وهو الذي يقصد به زيادة مطلقة (و) القسم (المعرف باللام) منه",
     "en": "(As for) the (second) kind of the two kinds of the (annexed) elative, namely that by which absolute excess is intended, (and) the division of it (defined by the lām),"},
    {"type": "matn",
     "ar": "(فلا بد) فيهما (من المطابقة) أي: مطابقة اسم التفضيل لموصوفه إفرادا وتثنية وجمعا، وتذكيرا وتأنيثا",
     "en": "(agreement is indispensable) in both, that is, agreement of the elative with what it qualifies in singular, dual and plural, and in masculine and feminine,"},
    {"type": "matn",
     "ar": "للزوم مطابقة الصفة لموصوفها مع عدم قيام المانع، وهو امتزاجه بـ«من» التفضيلية لفظا أو معنى، لعدم ذكر المفضل عليه بعدهما.",
     "en": "since an attribute must agree with what it qualifies when no impediment is present; the impediment is its fusion with the comparative “min”, in wording or in meaning, and [there is none here] because the one surpassed is not mentioned after these two."},
    {"type": "matn",
     "ar": "(و) اسم التفضيل (الذي استعمل بـ«من» مفرد مذكر لا غير) أي: لا غير المفرد المذكر",
     "en": "(And) the elative (that is used with “min” is singular masculine, nothing else), that is, nothing other than singular masculine,"},
    {"type": "matn",
     "ar": "لكراهتهم لحوق أداة التثنية والجمع والتأنيث المختصة بالآخر بما هو في حكم الوسط باعتبار امتزاجه بـ«من» التفضيلية",
     "en": "because of their dislike of attaching the markers of dual, plural and feminine, which belong to the end [of a word], to what is in the position of a middle by virtue of its fusion with the comparative “min”,"},
    {"type": "matn",
     "ar": "لكونها الفارقة بينه وبين باب «أحمر»، فكأنها من تمام الكلمة[[١]].",
     "en": "since it is what distinguishes it from the class of “aḥmar” (red), so it is as though it were part of the completion of the word."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «إلا لعموم أفعل»; the sense would lead one to expect «إلا بمعمول أفعل» (“except by what afʿal governs”). Transcribed as printed; translated literally.
    {"type": "pair",
     "ar": "أي: متمها. ولذا لا يفصل بينهما إلا لعموم أفعل. وذلك أيضا قليل.",
     "en": "That is, what completes it. For this reason the two are not separated except for the generality of afʿal, and that too is rare."},
    {"type": "pair",
     "ar": "وقد يفصل بينهما بـ«لو» وفعلها نحو: هي أحسن لو أنصفت من الشمس.",
     "en": "They are sometimes separated by “law” and its verb, as in: “she is more beautiful, were she fair, than the sun.”"},
]
