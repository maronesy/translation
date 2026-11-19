# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 170 (printed ١٦٩)."""

PAGE_NUMBER = 170
PRINTED_PAGE = "١٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(أو) كل رجل (في الدار) هذا مثال للاسم الموصوف بظرف (فله درهم).",
     "en": "“Or” every man [who is] “in the house”—this is an example of the noun qualified by an adverbial phrase—“shall have a dirham.”"},
    {"type": "matn",
     "ar": "وأما مثال للاسم المضاف إلى النكرة الموصوفة بأحدهما، فقولك: «كل غلام رجل يأتيني أو في الدار فله درهم».",
     "en": "As for an example of the noun annexed to an indefinite qualified by one of the two, it is your saying: “Every slave of a man who comes to me, or [who is] in the house, shall have a dirham” (kullu ghulāmi rajulin yaʾtīnī aw fī al-dāri fa-lahu dirhamun)."},
    {"type": "matn",
     "ar": "(وليت ولعل) من الحروف المشبهة بالفعل إذا دخلا على المبتدأ الذي يصح دخول الفاء على خبره (مانعان) عن دخوله عليه؛",
     "en": "“And layta and laʿalla”—among the particles resembling the verb (al-ḥurūf al-mushabbaha bi-l-fiʿl)—when they enter upon a mubtadaʾ on whose khabar the fāʾ may validly enter, “prevent” its entering upon it;"},
    {"type": "matn",
     "ar": "لأن صحة دخول الفاء عليه[[١]] إنما كانت لمشابهة المبتدأ والخبر للشرط والجزاء، و«ليت ولعل» يزيلان تلك المشابهة[[٢]]؛",
     "en": "because the validity of the fāʾ's entering upon it was only due to the resemblance of the mubtadaʾ and khabar to the condition and apodosis, and “layta” and “laʿalla” remove that resemblance;"},
    {"type": "matn",
     "ar": "لأنهما يخرجان الكلام من الخبرية إلى الإنشائية، والشرط والجزاء[[٣]] من قبيل الأخبار،",
     "en": "for they take the utterance out of the declarative (khabariyya) into the performative (inshāʾiyya), whereas the condition and the apodosis belong to the class of declaratives."},
    {"type": "matn",
     "ar": "وذلك المنع إنما هو (بالاتفاق) من النحاة، فلا يقال: «ليت ولعل الذي يأتيني أو في الدار فله درهم».",
     "en": "That prevention is “by the agreement” of the grammarians; so one does not say: “Would that, and perhaps, he who comes to me or [is] in the house—so he shall have a dirham.”"},
    {"type": "matn",
     "ar": "فإن قيل: باب «كان»[[٤]] وباب «علمت» أيضا مانعان بالاتفاق، فما وجه تخصيص «ليت ولعل»؟",
     "en": "If it is said: the class of “kāna” and the class of “ʿalimtu” also prevent [it] by agreement, so what is the reason for singling out “layta” and “laʿalla”?"},
    {"type": "matn",
     "ar": "قيل: تخصيصهما ببيان الاتفاق إنما هو من بين الحروف المشبهة بالفعل لا مطلقا[[٥]]. ووجه ذلك التخصيص الاهتمام ببيان الاختلاف الواقع فيها[[٦]].",
     "en": "It is said: singling them out by stating the agreement is only among the particles resembling the verb, not absolutely. The reason for that singling out is concern to state the disagreement that occurs over them."},
    {"type": "matn",
     "ar": "(وألحق بعضهم) قيل: هو سيبويه («إن») المكسورة (بهما) أي: بـ«ليت ولعل» في المنع عن دخول الفاء على الخبر،",
     "en": "“And some added”—it is said: this is Sībawayh—“inna” with kasra “to the two,” that is, to “layta” and “laʿalla,” in preventing the fāʾ from entering upon the khabar;"},
    {"type": "matn",
     "ar": "والأصح أنها لا تمنع عنه؛ لأنها لا تخرج الكلام عن الخبرية",
     "en": "but the sounder view is that it does not prevent it, because it does not take the utterance out of the declarative…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولأن دخول الفاء بملاحظة مشابهة المبتدأ بكلمات الشرط ومقتضاها التصدر، ومقتضاه امتناع دخول النواسخ مطلقا عليه.",
     "en": "And because the entry of the fāʾ is in view of the mubtadaʾ's resemblance to the conditional words, whose requirement is to stand at the head; and that requires that the abrogating governors (nawāsikh) can in no case enter upon it."},
    {"type": "pair",
     "ar": "وإنما جاز دخول «إن» لأنها لا تغير معنى الكلام.",
     "en": "The entry of “inna” is permitted only because it does not alter the meaning of the utterance."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وذلك لأن الشرط والجزاء يحتملان الصدق والكذب لكونهما خبرا، والكلام الذي فيه شيء من «ليت ولعل» لا يحتملهما لكونه إنشاء.",
     "en": "That is because the condition and the apodosis admit truth and falsehood, being declarative, whereas an utterance containing either of “layta” and “laʿalla” does not admit them, being performative (inshāʾ)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: الجملة الشرطية لا تكون إلا خبرية، فلا يرد أن الجزاء قد يكون إنشاء.",
     "en": "That is: the conditional sentence can only be declarative; so the objection that the apodosis is sometimes performative does not arise."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في التسهيل: أن المنع من حيث التتبع والاستعمال إنما يتحقق في «ليت» و«لعل». وكذا الاختلاف على هذا الوجه إنما وقع في «إن» المكسورة.",
     "en": "In al-Tashīl: prevention, as established by survey and usage, obtains only with “layta” and “laʿalla”; likewise, disagreement in this respect has arisen only over “inna” with kasra."},
    {"type": "pair",
     "ar": "وأما المنع والاختلاف في غيرها، فمن باب القياس. هذا. فظهر وجه كل تخصيص وقع من المصنف في هذا المقام.",
     "en": "As for prevention and disagreement in other [particles], they belong to analogy. Note this. Thus the reason for every singling out made by the author in this place has become clear."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لا مطلق النواسخ حتى يرد ما ذكر.",
     "en": "That is: not among the abrogating governors without restriction, such that what was mentioned would count against it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أو ذلك التخصيص لذكر أخبار الحروف المشبهة في المرفوعات، والتصريح بأن أمره كأمر خبر المبتدأ.",
     "en": "Or that singling out is because the khabars of the particles resembling [the verb] are mentioned among the nominatives (al-marfūʿāt), and because it is stated explicitly that its status is like the status of the khabar of the mubtadaʾ."},
]
