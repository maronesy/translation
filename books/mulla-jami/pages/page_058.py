# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 58 (printed ٥٧)."""

PAGE_NUMBER = 58
PRINTED_PAGE = "٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "…بين الحال والاستقبال يدل على زمانين معينين[[١]] من الأزمنة الثلاثة، فيدل على واحد معين أيضا في ضمنهما[[٢]]؛ إذ لا يقدح في الدلالة على معين الدلالة على ما سواه، نعم يقدح في إرادة المعين إرادة ما سواه، وأين الدلالة من الإرادة؟",
     "en": "…[being shared] between the present and the future, it indicates two specific times out of the three times, and so it also indicates one specific [time] included within them; for the signification of a specific [time] is not impaired by the signification of what is other than it. Indeed, [what is impaired is] the intending of a specific one by the intending of what is other than it — and what has signification to do with intention?"},

    {"type": "section", "ar": "[ خواص الاسم ]",
     "en": "The Distinctive Properties of the Noun"},

    {"type": "matn",
     "ar": "ولما فرغ[[٣]] من بيان حد الاسم، أراد أن يذكر خواصه[[٤]]، ليفيد[[٥]] زيادة معرفة به[[٦]]، فقال: (ومن خواصه[[٧]]) منبها بصيغة جمع الكثرة على كثرتها[[٨]]، و«من» التبعيضية[[٩]] على أن ما ذكره بعض منها.",
     "en": "And when he had finished expounding the definition of the ism, he wished to mention its distinctive properties (khawāṣṣ), so that it might impart a further knowledge of it; and so he said: “(and among its distinctive properties),” alerting, by the form of the plural of multiplicity (jamʿ al-kathra), to their being many, and by the partitive “min”, to [the fact] that what he mentions is [only] a portion of them."},
    {"type": "matn",
     "ar": "وهي جمع خاصة[[١٠]]، وخاصة الشيء: ما يختص به[[١١]]، ولا يوجد في غيره، وهي[[١٢]]:",
     "en": "It (khawāṣṣ) is the plural of khāṣṣa; and the distinctive property (khāṣṣa) of a thing is that which is proper to it and is not found in anything else; and they [the properties] are:"},
    {"type": "matn",
     "ar": "- إما شاملة لجميع أفراد ما هي خاصة له، كالكاتب بالقوة للإنسان.",
     "en": "- either all-encompassing of every individual of that of which it is a property — like [the property of] being potentially a writer (al-kātib bi-l-quwwa) for the human being;"},
    {"type": "matn",
     "ar": "- أو غير شاملة، كالكاتب بالفعل[[١٣]].",
     "en": "- or not all-encompassing — like [the property of] being actually a writer (al-kātib bi-l-fiʿl) [for the human being]."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهما الحال والاستقبال.",
     "en": "The two being the present and the future (al-ḥāl and al-istiqbāl)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قد عرفت أن اللفظ المشترك لا يدل إلا بالقرينة، فلا يدل إلا على زمان واحد.",
     "en": "You have already learned that a homonymous expression (al-lafẓ al-mushtarak) signifies only by means of a contextual indicator (qarīna), so it signifies only one time [at a time]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "المصنف من بيان حد الاسم.",
     "en": "[The subject is] the author — [when he had finished] with the exposition of the definition of the ism."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "من اللفظ والمعنى.",
     "en": "[Its distinctive properties] with respect to both wording and meaning."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: ليعلم المصنف بذكر بعض الخواص.",
     "en": "That is: so that the author might make [it] known by mentioning some of the distinctive properties."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: بالاسم.",
     "en": "That is: of the ism (noun)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "خبر قدم للاهتمام به، أو للقصر، أو مبتدأ كما قال صاحب الكشاف في قوله تعالى: ﴿ومن الناس من يقول آمنا﴾ (سورة البقرة: ٨). ولا يبعد أن يقال: يفهم حينئذ أن المذكور أقل من المتروك.",
     "en": "[It is] a predicate advanced [for emphasis], out of concern for it, or for [the sake of] restriction (qaṣr); or [it is] a subject (mubtadaʾ), as the author of al-Kashshāf said regarding His words, the Exalted: “(And among the people is he who says: We believe)” (Qurʾān, Sūrat al-Baqara 2:8). It is not unlikely that one should say: it is then understood that what is mentioned is less than what is left [unmentioned]."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "التي تتجاوز العشرة، قالوا: إنها تبلغ قريبا من ثلاثين.",
     "en": "Those [plural patterns] which exceed ten; they said: they amount to close to thirty."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "بقرينة دخولها على الجمع، فلو دخلت على مفرد لكانت ابتدائية اتصالية يشهد عليه قولك: هذا من الناس، أو من الإنسان. لا يقال: يفهم منه أنه لو لم يأت بـ«من» لكان الحكم صحيحا لكنه عار عن التنبيه مع أنه لا يصح؛ لأن أقل مرتبة جميع الكثرة عشرة. لأنا نقول: لا نسلم لزوم ذلك. ولئن سلم فلا نسلم أن أقل مرتبته العشرة؛ إذ لا فرق بينه وبين جمع القلة في جانب القلة. ولئن سلم فكثيرا ما يقوم كل منها مقام الآخر، فذلك مجاز غير عزيز.",
     "en": "By the indication of its entering upon a plural; for had it entered upon a singular it would be inceptive-connective (ibtidāʾiyya ittiṣāliyya), as attested by your saying “this is one of the people (min al-nās)” or “of mankind (min al-insān).” It is not to be objected: it is understood from this that, had he not brought “min,” the ruling would [still] be sound, only devoid of the alerting [function] — whereas [in fact] it would not be sound, because the least rank of every plural of multiplicity is ten. For we say: we do not concede that this is necessitated; and even if it be conceded, we do not concede that its least rank is ten, for there is no difference between it and the plural of paucity on the side of paucity; and even if it be conceded, [still] frequently each of them stands in the place of the other, and that is a figurative usage that is not rare."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: جمع كثرة للخاصة، اسم فاعل أو خاص، فإنهما بمعنى واحد، وتأنيثها لكونها حالة الشيء، أو التاء للمبالغة أو النقل. وقيل: هي مصدر بوزن العافية.",
     "en": "That is: [it is] a plural of multiplicity of “al-khāṣṣa”; [and khāṣṣa] is an active participle (ism fāʿil), or [the same as] “khāṣṣ,” for the two are of one meaning; and its feminine form is because it is [taken as] the state of the thing (ḥālat al-shayʾ), or the tāʾ is for hyperbole (mubālagha) or for transference (naql). It has [also] been said: it is a verbal noun (maṣdar) on the pattern of “al-ʿāfiya.”"},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: بالشيء.",
     "en": "That is: to the thing (bi-l-shayʾ)."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: الخواص.",
     "en": "That is: the distinctive properties (al-khawāṣṣ)."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: للإنسان.",
     "en": "That is: for the human being (li-l-insān)."},
]
