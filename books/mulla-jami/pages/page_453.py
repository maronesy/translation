# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 453 (printed ٤٥٢)."""

PAGE_NUMBER = 453
PRINTED_PAGE = "٤٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… والصفة المشبهة لا يلزم فيها» at the foot of PDF p. 452 (mid-sentence).
    {"type": "matn",
     "ar": "محذور، بخلاف المصدر، فإن له في نفسه تثنية وجمعا،",
     "en": "…any objectionable consequence; unlike the verbal noun, for it has a dual and a plural in itself."},
    {"type": "matn",
     "ar": "ولا شبهة أن الإضمار فيه يستلزم الاستتار، فإنه إذا كان بارزا لم يكن مضمرا فيه، بل مضمرا مطلقا، فلا حاجة إلى اعتبار قيد الاستتار على حدته، ليخرج مثل: «ضربي زيدا حاصل».",
     "en": "There is no doubt that concealment in it entails being hidden (istitār); for if [the pronoun] is visible, it is not concealed in it but is a pronoun without qualification; so there is no need to take the restriction of being hidden into account separately in order to exclude the like of “ḍarbī Zaydan ḥāṣilun” (my striking Zayd is taking place)."},
    {"type": "matn",
     "ar": "(ولا يلزم ذكر الفاعل) أي: فاعل المصدر لا مظهرا ولا مضمرا، نحو: «أعجبني ضرب زيدا»؛",
     "en": "(And mention of the agent is not required), that is, the agent of the verbal noun, neither overt nor concealed, as in “aʿjabanī ḍarbun Zaydan” (a striking of Zayd pleased me);"},
    {"type": "matn",
     "ar": "لأن النسبة إلى فاعل ما[[١]] غير مأخوذة في مفهومه، فلا يتوقف تصور مفهومه عليه، بخلاف الفعل واسمي الفاعل والمفعول والصفة المشبهة.",
     "en": "for the relation to some agent is not included in its concept, so conceiving its concept does not depend on it; unlike the verb, the active and passive participles and the resembling adjective."},
    {"type": "matn",
     "ar": "(ويجوز إضافته إلى الفاعل) مع أن إعماله[[٢]] منونا أولى[[٣]]؛ لأنه حينئذ أقوى مشابهة للفعل لكونه نكرة،",
     "en": "(And its annexation to the agent is permitted), although its being made to govern with nunation is preferable; for then it resembles the verb more strongly, being indefinite;"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿ولولا دفع الله الناس﴾[[٤]].",
     "en": "as in His words, the Exalted: “And were it not for Allah’s repelling people”."},
    {"type": "matn",
     "ar": "(وقد يضاف) أي: المصدر (إلى المفعول[[٥]]) سواء كان مفعولا به، أو ظرفا، أو مفعولا له على قلة بالنسبة إلى الفاعل،",
     "en": "(And it is sometimes annexed), that is, the verbal noun, (to the object), whether it be a direct object, an adverbial, or an object of purpose, less frequently compared with the agent,"},
    {"type": "matn",
     "ar": "نحو: «ضرب اللص الجلاد، وضرب يوم الجمعة، وضرب التأديب».",
     "en": "as in “the executioner’s striking of the thief”, “the striking of Friday” and “the striking of discipline”."},
    {"type": "matn",
     "ar": "(وإعماله) أي: إعمال المصدر متلبسا (باللام) أي: بلام التعريف (قليل)؛",
     "en": "(And making it govern), that is, making the verbal noun govern while it is joined (with the lām), that is, with the lām of definiteness, (is rare);"},
    {"type": "matn",
     "ar": "لأنه عند عمله مقدر بـ«أن» مع الفعل، فكما لا يدخل لام التعريف على «أن» مع الفعل ينبغي",
     "en": "for when it governs it is construed as “an” with the verb; so just as the lām of definiteness does not enter upon “an” with the verb, it ought…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: مطلقا معينا كان أو مبهما غير مأخوذة في مفهومه، بخلاف الفعل، فإن النسبة إلى الفاعل المعين الغير المأخوذة في مفهومه مأخوذة في مفهومه.",
     "en": "That is, [the relation to an agent] absolutely, whether specified or indeterminate, is not included in its concept; unlike the verb, for the relation to the specified agent, which is not itself included in its concept, is included in its concept."},
    {"type": "pair",
     "ar": "ولذا كان معناه المطابقي غير مستقل بالمفهومية،",
     "en": "For this reason its complete-correspondence meaning (al-maʿnā al-muṭābiqī) is not independently intelligible;"},
    {"type": "pair",
     "ar": "بخلاف اسم الفاعل والمفعول والصفة المشبهة، فإن النسبة إلى ذات ما مأخوذة في مفهومها مع تلك الذات، فكانت مستقلة بالمفهومية.",
     "en": "unlike the active and passive participles and the resembling adjective, for the relation to some essence is included in their concept together with that essence, so they are independently intelligible."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى دفع ما يرد من أن الإضافة إلى الفاعل أكثر من الإضافة إلى المفعول، كما يدل عليه قوله: وقد يضاف إلى آخره،",
     "en": "This points to the rebuttal of the objection that annexation to the agent is more frequent than annexation to the object, as his words “and it is sometimes annexed…” indicate,"},
    {"type": "pair",
     "ar": "فاللائق أن يقول: وإضافته إلى الفاعل أكثر.",
     "en": "so the fitting thing would be to say: “and its annexation to the agent is more frequent”."},
    {"type": "pair",
     "ar": "ووجه الدفع: أن الجواز ههنا بالنسبة إلى إعماله منونا، فإنه أولى.",
     "en": "The rebuttal is that “permitted” here is relative to making it govern with nunation, for that is preferable."},
    {"type": "pair",
     "ar": "ويفهم من الرضي أنه بالنسبة إلى عدم جوازها في اسم الفاعل.",
     "en": "From al-Raḍī it is understood that it is relative to its not being permitted in the active participle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإليه ذهب البعض.",
     "en": "Some have held this."},
    {"type": "pair",
     "ar": "وفي الرضي: وليس أقوى أقسام المصدر في العمل المنون كما قيل: بل الأقوى ما أضيف إلى الفاعل لكونه إذا كالجزء من المصدر، كما يكون من الفعل، فيكون عند ذلك أشد شبها بالفعل.",
     "en": "In al-Raḍī: the strongest kind of verbal noun in governing is not the nunated one, as has been said; rather, the strongest is the one annexed to the agent, since [the agent] is then like a part of the verbal noun, as it is of the verb, so that it then resembles the verb more closely."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: المصدر المضاف أقوى في العمل فيما عدا الفاعل المضاف إليه، كما يدل عليه تعليل الرضي.",
     "en": "It may be said: the annexed verbal noun is stronger in governing what is other than the agent to which it is annexed, as al-Raḍī’s reasoning indicates;"},
    {"type": "pair",
     "ar": "والمصدر المنون أولى بالعمل في الفاعل من المضاف إليه، كما يدل عليه تعليل الشارح.",
     "en": "and the nunated verbal noun is more entitled to govern the agent than the annexed one, as the commentator’s reasoning indicates."},
    {"type": "pair",
     "ar": "ولذا عمل المنون في لفظه والمضاف في محله.",
     "en": "For this reason the nunated one governs [the agent] in its wording, and the annexed one in its position."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢٥١، سورة الحج: ٤٠.",
     "en": "Qurʾān, Sūrat al-Baqara 2:251; Sūrat al-Ḥajj 22:40."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إذا قامت قرينة على كونه مفعولا. وتلك الإضافة أكثر عند حذف الفاعل.",
     "en": "When there is contextual evidence that it is the object. That annexation is more frequent when the agent is omitted."},
    {"type": "pair",
     "ar": "وتجيء على قلة مع ذكره حتى ذهب البعض إلى عدم جوازها، لكن نص سيبويه على جوازها.",
     "en": "It occurs rarely when [the agent] is mentioned, so that some held it impermissible; but Sībawayh stated explicitly that it is permissible."},
    # REVIEW: the verse is printed vocalized as dhikru raḥmati rabbika ʿabdahu Zakariyyā (fatḥa on the dāl of «عبده», no hamza on «زكريا»), yet the note says the reading has «بضم الدال والهمزة»; the vowelling as printed does not show the reading described. Diacritics removed per the no-diacritics rule; translated as printed.
    {"type": "pair",
     "ar": "ولم يجيء في القرآن إلا ما روي عن ابن عامر أنه قرأ ﴿ذكر رحمت ربك عبده زكريا﴾ (مريم: ٢) بضم الدال والهمزة.",
     "en": "It does not occur in the Qurʾān except in what is reported of Ibn ʿĀmir, that he read “dhikru raḥmati rabbika ʿabdahu Zakariyyā” (Qurʾān, Sūrat Maryam 19:2) with a ḍamma on the dāl and the hamza."},
]
