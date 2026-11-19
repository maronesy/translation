# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 75 (printed ٧٤)."""

PAGE_NUMBER = 75
PRINTED_PAGE = "٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn + sharḥ) ----------------
    {"type": "matn",
     "ar": "(جمع المؤنث السالم[[١]]) وهو ما يكون بالألف والتاء[[٢]].",
     "en": "(The sound feminine plural [jamʿ al-muʾannath al-sālim]) — it is that which is formed with the [augmented] alif and tāʾ."},
    {"type": "matn",
     "ar": "واحترز به[[٣]] عن المكسر[[٤]]، فإنه قد علم[[٥]] (بالضمة) رفعا (والكسرة) نصبا وجرا،",
     "en": "By it [the word “sound”] he guards against the broken [plural] (al-mukassar), for that has already been made known. [It is inflected] (with the ḍamma) in the nominative (rafʿ) and (with the kasra) in the accusative (naṣb) and genitive (jarr),"},
    {"type": "matn",
     "ar": "فإن النصب فيه[[٦]] تابع للجر إجراء للفرع على وتيرة[[٧]] الأصل[[٨]] الذي هو جمع المذكر السالم،",
     "en": "for the naṣb in it follows the jarr, carrying the branch (farʿ) upon the pattern of the root (aṣl), which is the sound masculine plural;"},
    {"type": "matn",
     "ar": "فإن النصب فيه[[٩]] تابع للجر -كما سيجيء ذكره- مثل: «جاءتني مسلمات»، و«رأيت مسلمات»، و«مررت بمسلمات».",
     "en": "for the naṣb in it [the root] too follows the jarr — as will be mentioned — as in: “Muslim women came to me” (jāʾatnī muslimātun), “I saw Muslim women” (raʾaytu muslimātin), and “I passed by Muslim women” (marartu bi-muslimātin)."},
    {"type": "matn",
     "ar": "(غير المنصرف بالضمة) رفعا (والفتحة) نصبا وجرا، فالجر فيه تابع للنصب، -كما سنذكره-",
     "en": "(The diptote [ghayr al-munṣarif] — with the ḍamma) in the nominative, (and with the fatḥa) in the accusative and genitive, so the jarr in it follows the naṣb — as we shall mention —"},
    {"type": "matn",
     "ar": "نحو: «جاءني أحمد»، و«رأيت أحمد»، و«مررت بأحمد».",
     "en": "as in: “Aḥmad came to me” (jāʾanī Aḥmadu), “I saw Aḥmad” (raʾaytu Aḥmada), and “I passed by Aḥmad” (marartu bi-Aḥmada)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قدمه على غير المنصرف لانحطاطه عن أقسام الاسم المعرب لشبهه بالفعل؛ وهو بصدد بيان أقسام المعرب وإعرابها، ولأنه أكثر خلافا للأصل من جمع المؤنث حيث ترك فيه إحدى الحركات مع التنوين، بخلاف جمع المؤنث،",
     "en": "He gave it precedence over the diptote (ghayr al-munṣarif) because of the latter’s being lower than the [other] categories of the declinable noun, owing to its resemblance to the verb — and he is here engaged in expounding the categories of the declinable and their declension; and because it [the diptote] is more contrary to the norm than the feminine plural, since it forgoes one of the vowels along with tanwīn, unlike the feminine plural;"},
    {"type": "pair",
     "ar": "ولأن جمع المؤنث السالم أكثر ارتباطا بالقسمين الأولين؛ لأنه مقابل للأول، ومناسب للثاني باعتبار الجزء الأول، ومقابل للثاني باعتبار الجزء الثاني، وليكون ذكرهما مع ترتيب ذكر مقابليهما.",
     "en": "and because the sound feminine plural is more closely connected to the first two categories, for it is the counterpart of the first and suited to the second with respect to its first component, and the counterpart of the second with respect to its second component; and so that the two may be mentioned together, following the ordering of the mention of their counterparts."},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: قوله: «السالم» مرفوع على أنه صفة للجمع انتهى، مجرور على أنه صفة للمؤنث الذي يكون سالما عن التغيير إذا جمع.",
     "en": "He (may his secret be sanctified) said in the gloss: “His word ‘al-sālim’ is in the nominative, as an adjective of ‘the plural’ (al-jamʿ)” — end [of quote]; [but it may also be] in the genitive, as an adjective of “the feminine” (al-muʾannath), which is “sound” [i.e., unaltered] from change when pluralized."},
    {"type": "pair",
     "ar": "وجاز توصيف المضاف بذي اللام عند الجمهور؛ لأنهما في درجة من التعريف عندهم. وأما عند المبرد فتعريف المضاف المكتسب من المضاف إليه أنقص، ومثله بدل عنده.",
     "en": "Qualifying the first term of annexation (al-muḍāf) by a word bearing the definite article is permissible according to the majority, because the two are of [equal] rank in definiteness in their view; but according to al-Mubarrad, the definiteness of the muḍāf, acquired from the muḍāf ilayhi, is deficient, and such [an adjective] is, in his view, an appositive substitute (badal)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سواء كان واحده مؤنثا كمسلمات جمع مسلمة، أو مذكرا كسجلات جمع سجل، ومرفوعات جمع مرفوع، وسواء كان جمعا بحسب الحال أو بحسب الأصل، فدخل عرفات فيه.",
     "en": "Whether its singular is feminine — like muslimāt, the plural of muslima — or masculine — like sijillāt, the plural of sijill, and marfūʿāt, the plural of marfūʿ; and whether it is a plural with respect to its [present] state or with respect to its origin — so that ʿArafāt is included in it."},
    {"type": "pair",
     "ar": "لا يخفى أن تفسيره بما ذكر سواء كان بحسب العرف أو بعموم المجاز كما يدخل مثل سجلات يخرج نحو ثبين جمع ثبة، وكما لا حاجة في إدخال الأول إلى تقدير مضاف، وهو صيغة أو معطوف، وهو ما على صيغته لم يحتج في إخراج الثاني إلى تقدير المضاف.",
     "en": "It is not hidden that his defining it by what has been mentioned — whether by [linguistic] convention or by the generality of figurative usage — just as it admits the likes of sijillāt, [so] it excludes the likes of thubīn, the plural of thuba; and just as there was no need, in admitting the first, to posit an implied muḍāf — namely a [certain] pattern (ṣīgha) or a conjoined element (maʿṭūf), that is, what is of that pattern — so too there was no need, in excluding the second, to posit the muḍāf."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بالسالم.",
     "en": "That is: by [the word] “sound” (al-sālim)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "عن جمع المذكر السالم، فإنه سيعلم. ولقائل أن يقول: الاحتراز ليس عن علم أو سيعلم، بل لأنه لا يشاركه في هذا الحكم على أنه لم يعلم المكسر مطلقا، بل المنصرف.",
     "en": "[Guarding also] against the sound masculine plural, for it will be treated [later]. Yet one might object: the guarding is not [warranted merely] because [something] is known or will be known; rather, [it is because] it does not share [the feminine plural] in this ruling — granting that the broken [plural] is not [what is here] known at all, but rather the triptote (al-munṣarif)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني أنه قد علم أن إعراب المكسر ليس كذلك، وإلا فمجرد العلم لا يوجب الاحتراز عنه.",
     "en": "It means that it has already become known that the declension of the broken plural is not so; otherwise, mere knowledge [of it] would not necessitate guarding against it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: في جمع المؤنث السالم.",
     "en": "That is: in the sound feminine plural."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: على طريقة.",
     "en": "That is: “upon the manner of.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وإنما جعل إعرابه على وتيرة الأصل؛ لأنه ليس في آخره حرف صالح لأن يجعل إعرابا، بخلاف جمع المذكر السالم، لكن يلزم بسبب جعل إعرابه بالحركة مزية الفرع على الأصل.",
     "en": "Its declension was made to follow the pattern of the root only because there is not, at its end, a letter fit to be made an inflectional marker — unlike the sound masculine plural; yet, because its declension is made by a vowel, it follows that the branch [here] holds a superiority over the root."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: في الجمع المذكر السالم.",
     "en": "That is: in the sound masculine plural."},
]
