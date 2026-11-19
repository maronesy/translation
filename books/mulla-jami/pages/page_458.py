# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 458 (printed ٤٥٧)."""

PAGE_NUMBER = 458
PRINTED_PAGE = "٤٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… لأنها عنده من قبيل إضافة الصفة» at the foot of PDF p. 457.
    # REVIEW: the page prints a stray dot after the colon («تعالى:.»); the dot is omitted here.
    {"type": "matn",
     "ar": "إلى معمولها، وتمسك الكسائي بقوله تعالى: ﴿وكلبهم باسط ذراعيه بالوصيد﴾[[١]]، وقد مر الجواب عنه.",
     "en": "…to its governed term. Al-Kisāʾī adduced as proof the words of the Exalted: “and their dog stretching out its forelegs at the threshold”; the answer to this has already been given."},
    {"type": "matn",
     "ar": "(فإن كان له) أي: لاسم الفاعل (معمول آخر) غير ما أضيف اسم الفاعل إليه (فبفعل مقدر) أي: فانتصابه بفعل مقدر، لا باسم الفاعل",
     "en": "(If it has), that is, the active participle, (another governed term) besides that to which the active participle is annexed, (then [it is] by an implied verb), that is, its accusative is by an implied verb, not by the active participle,"},
    {"type": "matn",
     "ar": "(نحو: «زيد معطي عمرو درهما أمس») فـ«درهما» منصوب بـ«أعطى» المقدر،",
     "en": "(as in “Zayd was the giver of ʿAmr a dirham yesterday”); “dirhaman” is in the accusative by an implied “aʿṭā” (he gave);"},
    {"type": "matn",
     "ar": "فأنه لما قيل: «معطي عمرو» قيل: ما أعطاه؟ فقيل: «درهما» أي: أعطاه درهما.",
     "en": "for when “the giver of ʿAmr” was said, it was asked: “What did he give him?” and it was answered: “a dirham”, that is, “he gave him a dirham”."},
    {"type": "matn",
     "ar": "(فإن دخلت اللام) الموصولة على اسم الفاعل (استوى الجميع) أي: جميع الأزمنة،",
     "en": "(If the lām), the relative one, (enters) upon the active participle, (all are equal), that is, all times;"},
    {"type": "matn",
     "ar": "فتقول: «مررت بالضارب أبوه زيدا أمس» كما تقول: «مررت بالضارب أبوه زيدا الآن أو غدا»؛",
     "en": "so you say “I passed by the one whose father struck Zayd yesterday” just as you say “I passed by the one whose father is striking Zayd now or tomorrow”;"},
    {"type": "matn",
     "ar": "لأنه فعل بالحقيقة حينئذ، عدل عن صيغة الفعل إلى صيغة الاسم لكراهتهم إدخال اللام عليه.",
     "en": "because it is then in reality a verb, turned from the form of the verb to the form of the noun because of their aversion to putting the lām on it [the verb]."},
    {"type": "matn",
     "ar": "(وما وضع منه) أي: من اسم الفاعل بتغيير صيغته إلى أخرى بحيث يخرج عن حد اسم الفاعل (للمبالغة) في الفعل المشتق منه",
     "en": "(And what is formed from it), that is, from the active participle, by changing its form into another such that it leaves the definition of the active participle, (for intensiveness) (mubālagha) in the verb from which it is derived,"},
    {"type": "matn",
     "ar": "(كـ«ضراب، وضروب ومضراب») بمعنى: كثير الضرب (و«عليم») بمعنى: كثير العلم (و«حذر») بمعنى: كثير الحذر",
     "en": "(such as “ḍarrāb”, “ḍarūb” and “miḍrāb”), meaning “much given to striking”, (and “ʿalīm”), meaning “of much knowledge”, (and “ḥadhir”), meaning “very wary”,"},
    {"type": "matn",
     "ar": "(مثله) أي: مثل اسم الفاعل في العمل، واشتراط ما يشترط به عمله.",
     "en": "(is like it), that is, like the active participle in governing and in the stipulation of what its governing is conditioned on."},
    {"type": "matn",
     "ar": "هذا على تقدير أن يكون صيغ المبالغة خارجة عن حد اسم الفاعل،",
     "en": "This is on the supposition that the intensive forms fall outside the definition of the active participle."},
    {"type": "matn",
     "ar": "وأما إذا كانت داخلة فيه فمعنى هذه العبارة أن صيغ اسم الفاعل إذا كانت للمبالغة[[٢]] مثله، أي: مثل اسم الفاعل إذا لم يكن للمبالغة",
     "en": "But if they are included in it, then the meaning of this phrase is that the forms of the active participle, when they are for intensiveness, are like it, that is, like the active participle when it is not for intensiveness,"},
    {"type": "matn",
     "ar": "نحو: «زيد ضراب أبوه عمرا الآن أو غدا»، و«مررت بزيد الضراب عمرا الآن، أو غدا، أو أمس»،",
     "en": "as in “Zayd, his father is a frequent striker of ʿAmr now or tomorrow”, and “I passed by Zayd, the frequent striker of ʿAmr now, or tomorrow, or yesterday”;"},
    {"type": "matn",
     "ar": "وما فيه من معنى المبالغة[[٣]] ناب مناب ما فات من المشابهة اللفظية.",
     "en": "and the sense of intensiveness in it stands in place of the verbal resemblance it has lost."},
    {"type": "matn",
     "ar": "(والمثنى) من اسم الفاعل ومما وضع منه للمبالغة (و) كذلك (المجموع) منهما مصححا كان أو مكسرا (مثله) أي: مثل اسم الفاعل إذا كان مفردا في العمل. وشروطه:",
     "en": "(And the dual) of the active participle and of what is formed from it for intensiveness, (and) likewise (the plural) of both, whether sound or broken, (is like it), that is, like the active participle when singular, in governing. And its conditions:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الكهف: ١٨.",
     "en": "Qurʾān, Sūrat al-Kahf 18:18."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا بد من هذا التقييد على هذا التوجيه بخلاف التوجيه الأول لما أن فيه صرف كلمة «من» عن معناها المتبادر أعني: التبيين والتوجيهان مطلوبان.",
     "en": "This restriction is necessary on this interpretation, unlike the first interpretation, since it involves turning the word “min” away from its obvious sense, namely explication (tabyīn); and both interpretations are sought."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن المبالغة وصول الشيء إلى كماله، ففيها قوة معنى الحدث الذي يعمل لأجله",
     "en": "Because intensiveness is a thing’s reaching its perfection, so in it there is a strength of the sense of the event (ḥadath) on account of which it governs;"},
    {"type": "pair",
     "ar": "بخلاف اسم التفضيل، فإن فيه اعتبار زيادة معه. وبضمها لا يبقى معنى الفعل على حاله، فلذا لم يعمل اسم التفضيل.",
     "en": "unlike the elative (ism al-tafḍīl), for in it an increase is considered along with it, and with its addition the sense of the verb does not remain as it was; for this reason the elative does not govern."},
]
