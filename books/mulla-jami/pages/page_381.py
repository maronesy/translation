# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 381 (printed ٣٨٠)."""

PAGE_NUMBER = 381
PRINTED_PAGE = "٣٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «(له) أي: للموصول لا لغيره.» at the foot of PDF p. 380 (new sentence).
    {"type": "matn",
     "ar": "(وصلة الألف واللام اسم فاعل أو مفعول[[١]])؛ لأن اللام الموصول تشبه اللام الحرفية[[٢]]،",
     "en": "(The relative clause of alif-lām is an active or passive participle), because the relative lām resembles the particle lām,"},
    {"type": "matn",
     "ar": "فجعلت صلتها ما كانت جملة معنى[[٣]] مفردا صورة؛ عملا بالحقيقة والشبه جميعا.",
     "en": "so its relative clause was made something that is a sentence in meaning and a single word in form, acting on both the reality and the resemblance together."},
    {"type": "matn",
     "ar": "(وهي) أي: الموصولات[[٤]] (الذي[[٥]]) للمفرد المذكر (والتي[[٦]]) للمفرد المؤنث",
     "en": "(They are), that is, the relative nouns: (alladhī) for the masculine singular, (allatī) for the feminine singular,"},
    {"type": "matn",
     "ar": "(واللذان) للمثنى المذكر (واللتان[[٧]]) لمثنى المؤنث، ويكونان (بالألف) في حال الرفع (والياء) في حال النصب والجر.",
     "en": "(alladhāni) for the masculine dual, (allatāni) for the feminine dual; and they are (with alif) in the nominative (and with yāʾ) in the accusative and genitive."},
    {"type": "matn",
     "ar": "(والألى) على وزن «العلى» لجمع المذكر والمؤنث، إلا أنه في جمع المذكر أشهر",
     "en": "(Al-ulā), on the pattern of “al-ʿulā”, for the masculine and feminine plural, though it is more common in the masculine plural;"},
    {"type": "matn",
     "ar": "(والذين) كـ«اللائين» لجمع المذكر",
     "en": "(alladhīna), like “al-lāʾīna”, for the masculine plural;"},
    {"type": "matn",
     "ar": "(واللائي) بالهمزة والياء (واللاء) بالهمزة المكسورة فقط (واللاي) بالياء فقط مكسورة أو ساكنة إجراء للوصل مجرى الوقف لجمع المذكر والمؤنث، إلا أنها في جمع المؤنث أشهر",
     "en": "(al-lāʾī), with hamza and yāʾ, (al-lāʾi), with the hamza bearing a kasra only, (and al-lāy), with the yāʾ only, bearing a kasra or quiescent, treating the connected state like the pause, for the masculine and feminine plural, though they are more common in the feminine plural;"},
    {"type": "matn",
     "ar": "(واللاتي واللواتي) لجمع المؤنث.",
     "en": "(and allātī and allawātī) for the feminine plural."},
    {"type": "matn",
     "ar": "وجاء في اللاتي «اللات» بحذف الياء وإبقاء الكسرة على التاء، وفي اللواتي «اللوا» بحذف التاء والياء معا.",
     "en": "For allātī, “allāti” also occurs, with the yāʾ dropped and the kasra kept on the tāʾ; and for allawātī, “allawā”, with the tāʾ and yāʾ both dropped."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: اسم فاعل مع ما يتعلق به من الفاعل والمفعول وغيرهما، وكذا اسم المفعول",
     "en": "That is, an active participle together with what is connected with it, such as the agent, the object and other things, and likewise the passive participle."},
    {"type": "pair",
     "ar": "يريد أن صلة الألف واللام من بين الجمل هذه الجملة،",
     "en": "He means that the relative clause of alif-lām, among sentences, is this sentence."},
    {"type": "pair",
     "ar": "فالتعرض لها ليس لأنها لم يدخل في تعريف الصلة، وأن الصلة المعرفة ما عداها، بل لاختصاص الألف واللام ببعض الجمل، وهو اسم الفاعل مع فاعله، واسم المفعول مع مرفوعه.",
     "en": "So treating it is not because it did not enter the definition of the relative clause, and that the defined relative clause is what is other than it; rather, it is because alif-lām is restricted to certain sentences, namely the active participle with its agent and the passive participle with its nominative."},
    {"type": "pair",
     "ar": "والأولى أن يقول: وصلة الألف واللام فقط اسم فاعل أو مفعول لا غير.",
     "en": "It would have been better to say: “the relative clause of alif-lām is only an active or passive participle, and nothing else.”"},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون صلتها صفة مشبهة ولا اسم تفضيل؛ لأنهما لبعدهما عن الفعل لعدم الدلالة على الحدوث لا يتأولان بالفعل، فلا يصيران بمعنى الجملة.",
     "en": "Its relative clause may not be an assimilated adjective (ṣifa mushabbaha) or an elative (ism tafḍīl), because these two, being remote from the verb since they do not signify occurrence in time (ḥudūth), are not interpreted as a verb, and so do not come to have the meaning of a sentence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وليست بالحقيقة لاما حرفية كما زعم بعضهم لعود الضمير إليه.",
     "en": "In reality it is not a particle lām, as some have claimed, because the pronoun refers back to it."},
    # REVIEW: printed «موضوف» (with ḍād), evidently for «موصوف»; transcribed as printed.
    {"type": "pair",
     "ar": "والقول بأن الضمير راجع إلى موضوف مقدر بعيد.",
     "en": "The view that the pronoun refers to an implied qualified noun is far-fetched."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولهذا يعمل حينئذ ولو كان بمعنى الماضي.",
     "en": "Hence it governs in that case, even if it has a past meaning."},
    {"type": "pair",
     "ar": "وأيضا لا يكون صلته مصدرا؛ لأنه لا يقدر بالفعل إلا مع ضميمة «أن»، وهو معها بتقدير المفرد، والصلة لا تكون إلا جملة.",
     "en": "Also, its relative clause is not a verbal noun, because that is construed as a verb only with “an” added, and with it, it is construed as a single word, while a relative clause is only ever a sentence."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: المرجع مأخوذ من السياق.",
     "en": "He means: the referent is taken from the context."},
    {"type": "pair",
     "ar": "قال عبد الغفور: لاحظ معنى الجمعية باعتبار الخبر كما أن تأنيث الضمير باعتبار أن خبره جماعة، فيكون المرجع مفهوما من السياق، والضمير واقع فيه.",
     "en": "ʿAbd al-Ghafūr said: he took account of the plural sense with regard to the predicate, just as the pronoun is feminine because its predicate is a group; so the referent is understood from the context, and the pronoun occurs in it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أصله «لذي» عند البصرية زيدت اللام عليها بحسب اللفظ، حتى لا يتوهم أن الجملة التي بعدها صفة لها، فإن الجملة لا تكون صفة للمعرفة.",
     "en": "Its origin, according to the Baṣrans, is “ladhī”; the lām was added to it in form, so that it should not be imagined that the sentence after it is an adjective qualifying it, for a sentence cannot qualify a definite noun."},
    {"type": "pair",
     "ar": "ولما كان وزنه وزن الصفات جاز أن يكون صفة كما أن \"ذو\" الطائية لما شاكل \"ذو\" بمعنى صاحب جاز أن يكون صفة بخلاف سائر الموصولات.",
     "en": "Since its pattern is the pattern of adjectives, it may be an adjective, just as the Ṭayyiʾ “dhū”, since it resembles “dhū” meaning “possessor”, may be an adjective, unlike the other relative nouns."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بقلب الذال تاء.",
     "en": "By changing the dhāl into tāʾ."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وقد يشدد النون فيهما بدلا من الياء في المفرد.",
     "en": "The nūn in both is sometimes doubled, in compensation for the yāʾ of the singular."},
]
