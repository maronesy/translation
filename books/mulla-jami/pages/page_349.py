# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 349 (printed ٣٤٨)."""

PAGE_NUMBER = 349
PRINTED_PAGE = "٣٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… و«مررت بزيد أخيك».» at the foot of PDF p. 348 (new paragraph).
    {"type": "matn",
     # REVIEW: «إلي» printed with a dotted yāʾ (as on PDF p. 348); transcribed as printed.
     "ar": "واحترز بقوله: «مقصود بما نسب إلي المتبوع» عن النعت والتأكيد وعطف البيان؛ لأنها ليست مقصودة بما نسب إليه، بل المتبوع مقصود به.",
     "en": "By his words “intended by what is attributed to the word followed” he excluded the qualifier (naʿt), the corroborative and the explicative apposition, since they are not intended by what is attributed to it; rather, the word followed is what is intended by it."},
    {"type": "matn",
     "ar": "وبقوله: «دونه» احتراز عن العطف بحرف، فإن المتبوع فيه مقصود بما نسب إليه مع التابع،",
     "en": "His words “not it” exclude conjunction by a particle, for there the word followed is intended by what is attributed to it together with the appositive."},
    {"type": "matn",
     "ar": "ولا يصدق الحد على المعطوف بـ«بل»؛ لأن متبوعه مقصود ابتداء ثم بدا له فأعرض عنه وقصد المعطوف، فكلاهما مقصودان بهذا المعنى.",
     "en": "Nor does the definition apply to what is conjoined by “bal”, because the word it follows is intended at first; then [the speaker] changed his mind, turned away from it and intended the conjoined word; so both are intended in this sense."},
    {"type": "matn",
     "ar": "فإن قيل: هذا الحد لا يتناول البدل الذي بعد «إلا» مثل: «ما قام أحد إلا زيد»، فإن «زيدا» بدل من «أحد»،",
     "en": "If it is said: this definition does not cover the substitute that comes after “illā”, as in “mā qāma aḥadun illā Zaydun” (no one stood except Zayd), for “Zayd” is a substitute for “aḥad”,"},
    {"type": "matn",
     "ar": "وليس نسبة ما نسب إليه من عدم القيام مقصودة بالنسبة إلى «زيد»، بل النسبة المقصودة بنسبة ما نسب إلى «أحد» نسبة القيام إلى زيد؟",
     "en": "and the attribution of what is attributed to it, namely not standing, is not intended with respect to “Zayd”; rather, the attribution intended by the attribution of what is attributed to “aḥad” is the attribution of standing to Zayd?"},
    {"type": "matn",
     "ar": "قلنا: ما نسب إلى المتبوع ههنا القيام، فإنه نسب إليه نفيا ونسبة القيام بعينه إلى التابع مقصودة، ولكن إثباتا،",
     "en": "We say: what is attributed to the word followed here is standing; it is attributed to it negatively, and the attribution of that very standing to the appositive is intended, but affirmatively."},
    {"type": "matn",
     "ar": "فيصدق على «زيد» أنه تابع مقصود نسبته بنسبة ما نسب إلى المتبوع، فإن النسبة المأخوذة في الحد أعم من أن يكون بطريق الإثبات أو النفي،",
     "en": "So it holds of “Zayd” that it is an appositive whose attribution is intended by the attribution of what is attributed to the word followed, for the attribution taken in the definition is more general than being by way of affirmation or of negation."},
    {"type": "matn",
     "ar": "ويمكن أن يقصد بنسبته إلى شيء نفيا نسبته إلى شيء آخر إثباتا، ويكون الأول توطئة للثاني.",
     "en": "By attributing it negatively to one thing, its attribution affirmatively to another thing may be intended, the first being a preparation for the second."},
    {"type": "matn",
     "ar": "(وهو) أي: البدل أنواع أربعة:",
     "en": "(It), that is, the substitute, is of four kinds:"},
    {"type": "matn",
     "ar": "١-(بدل الكل) أي: بدل هو كل المبدل منه.",
     "en": "1. (The whole-for-whole substitute [badal al-kull]), that is, a substitute that is the whole of the word substituted for."},
    {"type": "matn",
     "ar": "٢-(و) بدل (البعض) أي: بدل هو بعض المبدل منه، فالإضافة فيهما مثلها في «خاتم فضة».",
     "en": "2. (And) the substitute of (the part [badal al-baʿḍ]), that is, a substitute that is part of the word substituted for. The annexation in both is like that in “khātamu fiḍḍatin” (a ring of silver)."},
    {"type": "matn",
     "ar": "٣-(و) بدل (الاشتمال) أي: بدل مسبب غالبا عن اشتمال أحد المبدلين على الآخر.",
     "en": "3. (And) the substitute of (inclusion [badal al-ishtimāl]), that is, a substitute that usually results from one of the two terms including the other:"},
    {"type": "matn",
     "ar": "أما اشتمال البدل على المبدل منه نحو: «سلب زيد ثوبه»، أو بالعكس نحو: ﴿يسألونك عن الشهر الحرام قتال فيه﴾[[١]].",
     "en": "either the substitute including the word substituted for, as in “suliba Zaydun thawbuhu” (Zayd was robbed, his garment), or the reverse, as in “They ask you about the sacred month, fighting in it”."},
    {"type": "matn",
     "ar": "٤-(و) بدل (الغلط) أي: بدل مسبب عن الغلط، فالإضافة في الأخيرين من قبيل إضافة المسبب إلى السبب لأدنى ملابسة.",
     "en": "4. (And) the substitute of (error [badal al-ghalaṭ]), that is, a substitute resulting from error. The annexation in the last two is of the type of annexing the effect to the cause, on account of the slightest connection."},
    {"type": "matn",
     "ar": "(فالأول) أي: بدل الكل (مدلوله مدلول الأول[[٢]]) يعني: متحدان ذاتا، لا أن يتحد مفهوماهما ليكونا مترادفين نحو: «جاءني زيد أخوك»، فـ«زيد وأخوك» وإن اختلفا",
     "en": "(The first), that is, the whole-for-whole substitute, (signifies what the first [term] signifies): that is, the two are one in referent, not that their concepts are one so that they would be synonyms; as in “jāʾanī Zaydun akhūka” (Zayd, your brother, came to me), for “Zayd” and “your brother”, although they differ …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢١٧.",
     "en": "(Qurʾān, Sūrat al-Baqara 2:217)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     # REVIEW: «يؤتيى» printed (one would expect «يؤتى»); transcribed as printed.
     "ar": "ولم يقل: مدلوله؛ لأنه أريد بالأول الثاني غير الأول، وفي مثل هذا المقام يؤتيى بالظاهر إظهارا للمغايرة.",
     "en": "He did not say “its signification” [with a pronoun], because by the second “al-awwal” something other than the first “al-awwal” is meant; in such a context the explicit noun is used to make the difference evident."},
]
