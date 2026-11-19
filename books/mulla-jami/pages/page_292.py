# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 292 (printed ٢٩١)."""

PAGE_NUMBER = 292
PRINTED_PAGE = "٢٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «وهذا على تقدير فتح الهمزة.» at the foot of PDF p. 291 (new sentence).
    {"type": "matn",
     "ar": "وأما على تقدير كسرها فالتقدير: «إن كنت منطلقا انطلقت»، فعمل به ما عمل بالأول من غير فرق إلا حذف اللام؛ إذ لا لام فيه،",
     "en": "On the supposition that it takes kasra, the underlying form is “in kunta munṭaliqan inṭalaqtu” (if you were departing, I departed), and the same was done with it as with the first, with no difference except the elision of the lām, since there is no lām in it."},
    {"type": "matn",
     "ar": "واقتصر المصنف على الأول[[١]]؛ لأنه أشهر.",
     "en": "The author confined himself to the first because it is better known."},

    {"type": "section", "ar": "[اسم إن وأخواتها]",
     "en": "The Noun of Inna and Its Sisters"},

    {"type": "matn",
     "ar": "(اسم إن وأخواتها) وستعرفها[[٢]] في قسم الحرف -إن شاء الله تعالى- (هو المسند إليه بعد دخولها) أي: بعد دخول «إن» أو إحدى أخواتها (مثل: «إن زيدا قائم»)",
     "en": "(The noun of inna and its sisters)—you will come to know them in the section on the particle, if Allah the Exalted wills—(is that to which [something] is predicated after their entry), that is, after the entry of “inna” or one of its sisters, (as in “Indeed Zayd is standing”)."},
    {"type": "matn",
     "ar": "وبما عرفت من معنى البعدية والدخول فيما سبق اندفع انتقاض هذا التعريف ههنا أيضا بمثل: «أبوه» في مثل: «إن زيدا أبوه قائم».",
     "en": "By what you have learned above of the meaning of “after” and “entry,” the objection to this definition here too is removed—from such as “abūhu” in “Indeed Zayd, his father is standing.”"},

    {"type": "section", "ar": "[لا التي لنفي الجنس]",
     "en": "The Lā That Negates the Genus"},

    {"type": "matn",
     "ar": "(المنصوب[[٣]] بـ«لا» التي لنفي الجنس[[٤]]) أي: لنفي صفة الجنس[[٥]] وحكمه،",
     "en": "(The noun put in the accusative by the “lā” that negates the genus), that is, that negates an attribute of the genus and its predicate."},
    {"type": "matn",
     "ar": "وإنما لم يقل: «اسم لا»؛ لأنه ليس كله ولا أكثره من المنصوبات، فلا يصح جعله مطلقا من المنصوبات لا حقيقة ولا مجازا،",
     "en": "He did not say “the noun of lā” only because it is neither wholly nor mostly among the accusatives, so it cannot be classed absolutely among the accusatives, either literally or figuratively;"},
    {"type": "matn",
     "ar": "بل المنصوب منه أقل مما عداه، فلا بد من التعبير عنه بالمنصوب بها،",
     "en": "rather, the accusative part of it is less than the rest; so it had to be expressed as “that which is put in the accusative by it,”"},
    {"type": "matn",
     "ar": "بخلاف ما عداه من المنصوبات، فإن بعضها وإن لم يكن كله من المنصوبات، لكن أكثره منها، فأعطي للأكثر حكم الكل، فعد الكل منها تجوزا،",
     "en": "unlike the other accusatives: for some of them, though not wholly accusative, are mostly so; so the majority was given the rule of the whole, and the whole was counted among them by extension (tajawwuz)."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقال[[٦]]: اسم «لا» هو المنصوب بها لفظا -كالمضاف وشبهه- أو محلا كما هو مبني منه على الفتح،",
     "en": "It would not be far-fetched to say: the noun of “lā” is what is put in the accusative by it, overtly—like the annexed noun and what resembles it—or in place, as with the part of it that is indeclinable on the fatḥa;"},
    {"type": "matn",
     "ar": "وأما ما هو مرفوع فليس اسما لها، لعدم عملها فيه.",
     "en": "as for what is nominative, it is not its noun, since it does not govern it."},
    {"type": "matn",
     "ar": "(هو المسند إليه بعد دخولها) خرج به مثل: «أبوه» في «لا غلام رجل أبوه قائم» لما",
     "en": "(It is that to which [something] is predicated after its entry). By this is excluded such as “abūhu” in “There is no slave of a man whose father is standing,” since…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أنكر الشيخ الرضي مجيء إما بالكسر في هذا المقام حيث قال: إن حذف شرط «إن» مع «كان» وجوبا بلا تفسير وجب تغيير صورتها،",
     "en": "Shaykh al-Raḍī rejected the occurrence of “immā” with kasra in this context, saying: if the condition of “in” is obligatorily elided along with “kāna” without an explanatory [verb], its form must be changed;"},
    {"type": "pair",
     "ar": "فلذا قيل: أما أنت منطلقا انطلقت بالفتح مع أن الأصل إن كنت؛ لأنه لو ثبت إما أنت منطلقا بالكسر لم يتأت منه هذا القول.",
     "en": "this is why “ammā anta munṭaliqan inṭalaqtu” is said with fatḥa, although the origin is “in kunta”; for had “immā anta munṭaliqan” with kasra been established, he could not have made this statement."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: أخوات «إن»، وهو الظاهر، أو «إن» وأخواتها،",
     "en": "That is, the sisters of “inna,” which is the evident reading; or “inna” and its sisters;"},
    {"type": "pair",
     "ar": "فإن «إن» قد يكون من حروف الإيجاب ولا اسم لها، فلا بد من بيان «إن» هذه، فترك بيانها لإتيانها في قسم الحروف.",
     "en": "for “inna” is sometimes one of the particles of affirmation (ḥurūf al-ījāb, “yes”) and has no noun; so this “inna” had to be explained, and its explanation was left because it comes in the section on particles."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يريد المنصوب لفظا أو تقديرا، وإلا لم يكن التعريف جامعا مانعا.",
     "en": "He means what is accusative overtly or by supposition; otherwise the definition would not be comprehensive and exclusive (jāmiʿ māniʿ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "من غير تبعية، فلا يرد نحو: لا غلام رجل غلاما حسنا من أنه منصوب بلا.",
     "en": "Without being a dependent (tābiʿ); so no objection arises from such as “There is no slave of a man, a fine slave [ghulāman ḥasanan],” on the ground that it is put in the accusative by lā."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لنفي ما أجرى عليه.",
     "en": "That is, to negate what is predicated of it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: print reads «غير المنصوب منها أقل», whereas the matn says the accusative part is the lesser («المنصوب منه أقل مما عداه»); transcribed as printed.
    {"type": "pair",
     "ar": "تزييف لما سبق من أن غير المنصوب منها أقل.",
     "en": "A rejection of what preceded, namely that the non-accusative part of it is less."},
]
