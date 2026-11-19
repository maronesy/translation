# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 190 (printed ١٨٩)."""

PAGE_NUMBER = 190
PRINTED_PAGE = "١٨٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "لما وقع مثبتا بعد نفي،",
     "en": "…of what occurs affirmed after a negation."},
    {"type": "matn",
     "ar": "وإنما أورد مثالين تنبيها على أن الاسم الواقع موقع الخبر[[١]] ينقسم إلى النكرة والمعرفة، أو إلى ما هو فعل للمبتدأ، وإلى ما يشبه به فعله، أو إلى مفرد ومضاف.",
     "en": "He adduced two examples only to draw attention to the fact that the noun occurring in the position of the predicate divides into indefinite and definite; or into what is the act of the mubtadaʾ and what its act is likened to; or into single (mufrad) and annexed (muḍāf)."},
    {"type": "matn",
     "ar": "(وإنما أنت سيرا) أي: «تسير سيرا» مثال لما وقع بعد معنى النفي.",
     "en": "(And “You are only going”—wa-innamā anta sayran), that is: “you go a going”—an example of what occurs after the sense of negation."},
    {"type": "matn",
     "ar": "(وزيد سيرا سيرا) أي: «يسير سيرا سيرا» مثال لما وقع مكررا.",
     "en": "(And “Zayd [is] going, going”—wa-Zaydun sayran sayran), that is: “he goes a going, a going”—an example of what occurs repeated."},
    {"type": "matn",
     "ar": "(ومنها) أي: من المواضع التي يجب حذف الفعل الناصب للمفعول المطلق فيها (ما وقع) أي: موضع مفعول مطلق وقع (تفصيلا[[٢]] لأثر مضمون جملة[[٣]] متقدمة[[٤]]).",
     "en": "(And among them)—that is, among the places in which the elision of the verb that puts the absolute object in the accusative is obligatory—is (what occurs), that is, the place of an absolute object that occurs (as a detailing of the effect of the content of a preceding sentence—tafṣīlan li-athari maḍmūni jumlatin mutaqaddimatin)."},
    {"type": "matn",
     "ar": "والمراد بمضمون الجملة: مصدرها[[٥]] المضاف إلى الفاعل أو المفعول،",
     "en": "What is meant by “the content of the sentence” is its maṣdar annexed to the agent or the object;"},
    {"type": "matn",
     "ar": "وبأثره: غرضه[[٦]] المطلوب منه، وبتفصيل الأثر: بيان أنواعه المختلفة المحتملة[[٧]]",
     "en": "by “its effect,” its purpose sought from it; and by “detailing of the effect,” the setting out of its various possible kinds,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: (﴿فشدوا الوثاق فإما منا بعد﴾[[٨]]) أي: بعد شد الوثاق (﴿وإما فداء﴾).",
     "en": "as in His saying, the Exalted: (“Then secure the bond; then either favour afterwards”), that is: after securing the bond, (“or ransom”)."},
    {"type": "matn",
     "ar": "فقوله: ﴿فشدوا الوثاق﴾ جملة مضمونها شد الوثاق، والغرض المطلوب من ﴿فشدوا الوثاق﴾ إما المن أو الفداء،",
     "en": "So His saying “Then secure the bond” is a sentence whose content is the securing of the bond; and the purpose sought from “Then secure the bond” is either favour (mann) or ransom (fidāʾ);"},
    {"type": "matn",
     "ar": "ففصل الله سبحانه هذا الغرض المطلوب بقوله: ﴿فإما منا بعد وإما",
     "en": "so Allah, Glorified is He, detailed this purpose sought by His saying: “then either favour afterwards or…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو على أنه يكون للتأكيد والنوع. ولم يلتفت الشارح إلى هذا الوجه؛ لأنه يوهم الحصر فيهما،",
     "en": "Or [to draw attention] to its being for emphasis and for kind. The commentator did not attend to this aspect, because it suggests restriction to these two;"},
    {"type": "pair",
     "ar": "أو على أنه قد يكون بحيث يجب تقدير عامله بعد «إلا» كالمثال الأول؛ إذ لا يصح استثناء السير المطلق عن السير المطلق،",
     "en": "or to its being sometimes such that its governor must be supposed after “illā,” as in the first example, since excepting unqualified going from unqualified going is not valid;"},
    {"type": "pair",
     "ar": "وقد يكون بحيث لا يجب كما في المثال الثاني، فإنه يصح فيه تقدير العامل قبل إلا، أي: ما أنت تسير إلا سير البريد.",
     "en": "and sometimes such that it is not required, as in the second example, for there it is valid to suppose the governor before illā, that is: “You do not go except the going of the courier.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما وجب حذف الفعل ههنا لدلالة الجملة المتقدمة على المصدر الذي ينتقل الذهن منه إلى غاياته التي هي المصادر وقيامها مقام عواملها.",
     "en": "The elision of the verb is obligatory here only because the preceding sentence indicates the maṣdar from which the mind passes to its ends, which are the [detailing] maṣdars, and because they stand in place of their governors."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: print reads «فأما قراءة بعد»; context (paired with «فإما بيعا وإما أكلا») suggests «فإما»; transcribed as printed.
    {"type": "pair",
     "ar": "إنشائية أو خبرية نحو: «زيد يكتب». فأما قراءة بعد أو «بيعا»، ويشتري طعاما فإما بيعا وإما أكلا.",
     "en": "[A sentence,] whether performative (inshāʾiyya) or informative (khabariyya), as in: “Zayd writes; then either reading afterwards or ‘selling’”; and “He buys food; then either selling or eating.”"},
    {"type": "pair",
     "ar": "وإنما قال: مضمون جملة ليخرج نحو: له سفر يصح صحة، أو يغتنم اغتناما",
     "en": "He said “the content of a sentence” only to exclude such as: “He has a journey; he becomes healthy [with] a health, or he gains [with] a gain,”"},
    {"type": "pair",
     "ar": "لا ليخرج نحو: له سفر سفرا قريبا أو سفرا بعيدا؛ لأن السفر القريب والبعيد ليس من آثار السفر، بل من أنواعه.",
     "en": "not to exclude such as “He has a journey, a near journey or a far journey,” because the near and the far journey are not among the effects of the journey but among its kinds."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بيان للواقع، أو احتراز إذا جوز تقديم التفصيل، نحو: إما تمنون منا أو تفدون فداء شدوا.",
     "en": "[“Preceding” is] a statement of fact, or a precaution if placing the detailing first is allowed, as in: “Either you grant favour or you take ransom—secure [the bond].”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: المصدر المفهوم منها.",
     "en": "That is: the maṣdar understood from it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: غايته، وإنما سمي غاية الشيء أثرا؛ لأنها تحصل بعده كالأثر الذي يكون بعد المؤثر.",
     "en": "That is: its end (ghāya). The end of a thing is called an “effect” (athar) only because it comes about after it, like the effect that comes after the efficient cause."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هكذا فسره الشيخ الرضي، وتبعه الشارح.",
     "en": "Thus Shaykh al-Raḍī explained it, and the commentator followed him."},
    {"type": "pair",
     "ar": "والظاهر أن المراد من الاحتمال: أن يكون الآثار على سبيل البدل.",
     "en": "What is apparent is that what is meant by “possible” is that the effects be by way of alternation (ʿalā sabīl al-badal)."},
    {"type": "pair",
     "ar": "فعلى هذا يلزم ألا يكون الحذف واجبا في «فشدوا الوثاق» منا بعد وإما فداء أو ففداء أو ثم فداء، ولم يذكر المحتملة لتناوله.",
     "en": "On this [reading], it follows that the elision is not obligatory in “Then secure the bond,” favour afterwards and either ransom, or then ransom, or thereafter ransom; and he did not mention “possible” so that it would include it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة محمد: ٤.",
     "en": "Qurʾān, Sūrat Muḥammad 47:4."},
]
