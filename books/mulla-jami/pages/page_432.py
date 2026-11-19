# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 432 (printed ٤٣١)."""

PAGE_NUMBER = 432
PRINTED_PAGE = "٤٣١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «بل يذكرون ما» at the foot of PDF p. 431.
    {"type": "matn",
     "ar": "يصلح أن يكون تمييزا لهما على تقدير ذكر التمييز معهما، ويطرحون الواحد والاثنين",
     "en": "…would be fit to be a specifier for them, supposing the specifier were mentioned with them, and they drop wāḥid and ithnān,"},
    {"type": "matn",
     "ar": "(استغناء بلفظ التمييز) أي: الصالح لأن يكون تمييزا على تقدير ذكره معهما، الدال بجوهره على الجنس، وبصيغته على الوحدة أو الاثنينية",
     "en": "(dispensing with them by the word of the specifier), that is, the word fit to be a specifier, supposing it were mentioned with them, which indicates by its substance the genus, and by its form oneness or twoness,"},
    {"type": "matn",
     "ar": "(عنهما) أي: عن الواحد إذا كان التمييز مفردا، وعن الاثنين إذا كان مثنى (مثل: «رجل ورجلان»)",
     "en": "(from them), that is, from wāḥid when the specifier is singular and from ithnān when it is dual, (as in “rajul” and “rajulān”);"},
    {"type": "matn",
     "ar": "فإن من صيغة[[١]] «رجل» يفهم الجنس والوحدة، ومن صيغة «رجلان» يفهم الجنس والاثنينية، فبذكرهما استغني عن المميز.",
     "en": "for from the form “rajul” the genus and oneness are understood, and from the form “rajulān” the genus and twoness are understood; so by mentioning them the [number that would be] specified is dispensed with."},
    {"type": "matn",
     "ar": "فإن قلت: هب[[٢]] أن مميز الواحد مغن عنه[[٣]]، لكن لا نسلم أن مميز الاثنين كذلك،",
     "en": "If you say: grant that the specifier of wāḥid makes it unnecessary; but we do not concede that the specifier of ithnān is likewise;"},
    {"type": "matn",
     "ar": "نعم إذا كان مميزه مثنى يغني عنه لم لا يجوز أن يكون مفردا كما يقال: اثنا رجل؟[[٤]]",
     "en": "yes, when its specifier is dual it makes it unnecessary; [but] why may it not be singular, as one might say “ithnā rajul”?"},
    {"type": "matn",
     "ar": "قلت: لما التزموا الجمعية في مميز سائر الآحاد[[٥]]، ينبغي أن يعتبر[[٦]] فيما لم تيسر الجمعية فيه ما هو أقرب إليها، وهو الاثنينية،",
     "en": "I say: since they made plurality binding in the specifier of the rest of the units, what is nearest to plurality, namely twoness, should be taken into account where plurality is not feasible."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقال: معنى الكلام[[٧]] أنه لا يميز واحد ولا اثنان استغناء بلفظ التمييز،",
     "en": "It is not far-fetched to say: the meaning of the statement is that wāḥid and ithnān are not specified, it being enough to use the word of the specifier,"},
    {"type": "matn",
     "ar": "أي: بجواهر حروفه المصورة بهيئة خاصة، القابلة للحوق علامة الإفرادية، أعني: التنوين أو علامة الاثنينية، أعني: حرفي التثنية،",
     "en": "that is, by the substance of its letters shaped in a particular form, receptive to the attachment of the mark of singularity, I mean the tanwīn, or the mark of twoness, I mean the two letters of the dual;"},
    {"type": "matn",
     "ar": "فإذا اعتبر مع علامة الإفراد، استغني به عن ذكر الواحد على حدة، وإذا اعتبر مع علامة",
     "en": "so when it is taken with the mark of singularity, mention of wāḥid separately is dispensed with by it, and when it is taken with the mark…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أعني: الجوهر مع الهيئة كما هو المعنى الحقيقي، فلا ينافي السابق.",
     "en": "I mean: the substance together with the form, as is the proper meaning; so it does not conflict with what preceded."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "حاصله: أن المدعى عام كما مر. والدليل خاص؛ لأنه لا ينتهض فيما إذا أورد مميز الاثنين مفردا،",
     "en": "Its upshot: the claim is general, as has passed, while the proof is particular, for it does not hold in the case where the specifier of ithnān is brought in the singular;"},
    {"type": "pair",
     "ar": "فإنه صالح لتمييزه لكونه مبنيا للجنس. ولذا جاء في قول الشاعر: ثنتا حنظل، والاستغناء بلفظه لعدم فهم الاثنينية منه.",
     "en": "for it is fit to specify it, since it expresses the genus; hence there occurs in the poet’s words “thintā ḥanẓal” (two colocynths); and [there is no] dispensing with [the number] by its word, since twoness is not understood from it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه إشارة إلى منع الإغناء لجواز إفادته التأكيد كما في إله واحد وإلهين اثنين.",
     "en": "In this is an indication that [its] making [the number] unnecessary may be disputed, since it may convey emphasis, as in “ilāh wāḥid” (one god) and “ilāhayn ithnayn” (two gods)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     # REVIEW: the verse is usually cited «ثنتا حنظل» (without «رجل»); transcribed as printed.
     "ar": "وقد جاء في الشعر ثنتا رجل حنظل، ومن أسانيد المنع الذي ذكره الرضي نحو: واحد رجال، واثنا رجال، فاعرفه.",
     "en": "There occurs in poetry “thintā … ḥanẓal”; and among the supports of the objection mentioned by al-Raḍī are [expressions] such as “wāḥid rijāl” and “ithnā rijāl”. So know it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأولى أن يقال: لما التزموا الموافقة بين المميز والعدد في سائر الآحاد في الدلالة على المتعدد ينبغي أن يعتبر في الاثنين أيضا، فافهم.",
     "en": "It is better to say: since they made agreement between the specifier and the number binding in the rest of the units, in indicating multiplicity, it should be taken into account for ithnān too. So understand."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن اللائق بالقياس أن يعتبر في الاثنين المثنى رعاية للموافقة بمميز سائر الآحاد بقدر الإمكان،",
     "en": "He means: what befits analogy is that the dual be taken into account for ithnān, observing agreement with the specifier of the rest of the units as far as possible;"},
    {"type": "pair",
     "ar": "فالمفرد ليس بصالح لتمييز الاثنين قياسا، وما وقع في الشعر شاذ للضرورة.",
     "en": "so the singular is not fit, by analogy, to specify ithnān, and what occurs in poetry is anomalous, due to metrical necessity."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "خلاصته: أن معنى الكلام أنه لا يجمع بينهما، وبين تمييزهما استغناء بلفظ التمييز،",
     "en": "Its gist: the meaning of the statement is that they [wāḥid and ithnān] are not combined with their specifier, it being enough to use the word of the specifier,"},
    {"type": "pair",
     "ar": "أعني: الصيغة من غير اعتبار علامة الإفراد والتثنية عنهما؛",
     "en": "I mean the form, without regard to the mark of singular or dual, [in place of] them;"},
    {"type": "pair",
     "ar": "لأنه بإلحاق علامة الإفراد يفيد الوحدة، وبإلحاق علامة التثنية يفيد الاثنينية، فلا حاجة إلى ذكر الواحد والاثنين.",
     "en": "because by attaching the mark of the singular it conveys oneness, and by attaching the mark of the dual it conveys twoness; so there is no need to mention wāḥid and ithnān."},
    {"type": "pair",
     "ar": "وإنما قال: ولا يبعد؛ لأن فيه حمل اللفظ على خلاف الظاهر السابق إلى الفهم.",
     "en": "He said “it is not far-fetched” only because it involves taking the wording contrary to the apparent sense that first comes to mind."},
]
