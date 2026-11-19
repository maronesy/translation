# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 573 (printed ٥٧٢)."""

PAGE_NUMBER = 573
PRINTED_PAGE = "٥٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(يليها) أي:» at the foot of PDF p. 572.
    {"type": "matn",
     "ar": "يذكر بعدها بلا فاصلة (أحد المستويين[[١]]) والمستوى (الآخر) يلي (الهمزة) أي: همزة الاستفهام",
     "en": "…there is mentioned after it, with no separation, (one of two equivalent things), and the (other) equivalent follows (the hamza), that is, the interrogative hamza,"},
    {"type": "matn",
     "ar": "(بعد ثبوت أحدهما) أي: أحد المستويين عند المتكلم[[٢]] (لطلب التعيين) من المخاطب.",
     "en": "(after one of them is established), that is, one of the two equivalents [is established] in the mind of the speaker, (in order to request specification) from the addressee."},
    {"type": "matn",
     "ar": "(ومن ثم) أي: لأجل أن أم المتصلة يليها أحد المستويين والآخر الهمزة بعد ثبوت أحدهما لطلب التعيين (لم يجز) تركيب (أرأيت زيدا أم عمرا؟)،",
     "en": "(Hence), that is, because one of the two equivalents follows the connected “am” and the other follows the hamza, after one of them is established, in order to request specification, (it is not permissible) to construct (“a-raʾayta Zaydan am ʿAmran?”, did you see Zayd or ʿAmr?),"},
    {"type": "matn",
     "ar": "فإن المستويين فيه «زيد وعمرو» وأحدهما وإن ولي «أم» ولكن الآخر لم يل الهمزة، هذا ما اختاره المصنف.",
     "en": "for the two equivalents in it are “Zayd and ʿAmr”, and although one of them follows “am”, the other does not follow the hamza. This is what the author chose."},
    {"type": "matn",
     "ar": "والمنقول عن سيبويه: إن هذا جائز حسن فصيح، و«أزيدا رأيت أم عمرا؟» أحسن وأفصح،",
     "en": "What is reported from Sībawayh is that this is permissible, good and eloquent, and that “a-Zaydan raʾayta am ʿAmran?” is better and more eloquent;"},
    {"type": "matn",
     "ar": "وحينئذ يكون تركيب «أرأيت زيدا أم عمرا؟» حسنا وفصيحا، وإن لم يكن أحسن وأفصح.",
     "en": "on this view the construction “a-raʾayta Zaydan am ʿAmran?” is good and eloquent, even if it is not the better and more eloquent."},
    {"type": "matn",
     "ar": "وفي الترجمة الشريفية: أنه وجد في بعض نسخ الكافية المقروءة على المصنف، وعليه خطه هكذا:",
     "en": "In al-Tarjama al-Sharīfiyya [it is stated] that in some copies of al-Kāfiya read before the author and bearing his handwriting there was found the following:"},
    {"type": "matn",
     "ar": "«يليها أحد المستويين والآخر الهمزة على الأفصح، ومن ثم ضعف: «أرأيت زيدا أم عمرا»».",
     "en": "“One of the two equivalents follows it and the other the hamza, according to the more eloquent usage; hence ‘a-raʾayta Zaydan am ʿAmran’ is weak.”"},
    {"type": "matn",
     "ar": "ولا يخفى أن الحكم بضعفه لتنزيله عن مرتبة الأفصحية إلى الفصيحية غير مناسب؛ لأن ما كان حسنا فصيحا لا يعد ضعيفا[[٣]].",
     "en": "It is evident that judging it weak because it is lowered from the rank of the more eloquent to that of the eloquent is unfitting, for what is good and eloquent is not counted weak."},
    {"type": "matn",
     "ar": "وبالجملة فكلام المصنف ههنا لا يخلو عن اضطراب، والحق ما نقل عن سيبويه.",
     "en": "In sum, the author’s statement here is not free of inconsistency, and the truth is what is reported from Sībawayh."},
    {"type": "matn",
     "ar": "(و) أيضا (من ثم) أي: من أجل ما ذكر بعينه (كان جوابها) أي: جواب أم المتصلة (بالتعيين) أي: بتعيين أحد الأمرين؛ لأن السؤال عنه",
     "en": "(And) also, (hence), that is, for precisely the reason mentioned, (its answer), that is, the answer to the connected “am”, (is by specification), that is, by specifying one of the two things, since the question is about that,"},
    {"type": "matn",
     "ar": "(دون «نعم، أو لا»)؛ لأنهما لا يفيدان التعيين[[٤]]،",
     "en": "(not by “yes” or “no”), for these two do not convey specification;"},
    {"type": "matn",
     "ar": "بخلاف «أو وإما» مع الهمزة، كما إذا قلت: «أجاءك زيد أو عمرو؟» أو «أجاءك إما زيد وإما عمرو؟»،",
     "en": "unlike “aw” and “immā” with the hamza, as when you say “did Zayd or ʿAmr come to you?” or “did either Zayd or ʿAmr come to you?”;"},
    {"type": "matn",
     "ar": "فإنه لا يصح جوابهما بـ«لا و نعم»؛ لأن المقصود[[٥]] بالسؤال أن أحدهما لا على التعيين جاءك أو لا.",
     "en": "for it is not correct [sic] to answer them with “no” and “yes”, because what is intended by the question is whether one of them, not specified, came to you or not."},
    # REVIEW: printed «فإنه لا يصح جوابهما بـ«لا و نعم»»; the argument and footnote ٥ require «يصح» (it is correct); transcribed as printed.

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «والمفرد أن بعدهما»; possibly for «والمراد»; transcribed as printed.
    {"type": "pair",
     "ar": "والآخر الهمزة ليكون أم مع الهمزة بتأويل أي: والمفرد أن بعدهما بتأويل المضاف إليه لأي",
     "en": "And the other [follows] the hamza, so that “am” together with the hamza stands for “ayy” (which?), and the single terms after them stand for what “ayy” is annexed to;"},
    {"type": "pair",
     "ar": "نحو: أزيد عندك أم عمرو؟ أي: أيهما عندك؟ وأفي الدار زيد أم في السوق؟ أي: في أي الموضعين.",
     "en": "as in “is Zayd with you or ʿAmr?”, that is, “which of the two is with you?”, and “is Zayd in the house or in the market?”, that is, “in which of the two places?”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نبه بقوله: عند المتكلم على أن المراد بالاستواء الاستواء في علم المتكلم،",
     "en": "By his words “in the mind of the speaker” he drew attention to the fact that what is meant by equivalence is equivalence in the speaker’s knowledge;"},
    # REVIEW: printed «وربما بما يتوهم»; «بما» appears superfluous; transcribed as printed.
    {"type": "pair",
     "ar": "وربما بما يتوهم أن الأقرب أن يراد الاستواء في الإعراب أو الإسناد ولا يستقيم؛ لأنه ينتقض بمثل: أقام زيد أم قام عمرو.",
     "en": "one may perhaps imagine that it is closer to mean equivalence in inflection or in predication, but that is not sound, since it is refuted by such [examples] as “did Zayd stand, or did ʿAmr stand?”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «ما في عدم عده»; likely for «إنما في عدم عده»; transcribed as printed.
    {"type": "pair",
     "ar": "لا كلام في عدم عده ضعيفا مطلقا ما في عدم عده ضعيفا بالإضافة إلى الأفصح فنظر.",
     "en": "There is no dispute about its not being counted weak absolutely; [but] as for its not being counted weak relative to the more eloquent, that is open to consideration."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن نعم لتقرير ما سبق، ولا لرده وما سبق ههنا ثبوت أحدهما غير معين، فلا يستفاد منه التعيين.",
     "en": "For “yes” is for confirming what preceded and “no” for rejecting it, and what preceded here is the establishment of one of them unspecified; so specification is not derived from it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فالسؤال عن أصل النسبة، فيصح الجواب بنعم ولا، لدلالتهما على ثبوت النسبة أو نفيها.",
     "en": "So the question is about the basic attribution (nisba), and the answer by “yes” and “no” is correct, since these indicate the affirmation or the negation of the attribution."},
]
