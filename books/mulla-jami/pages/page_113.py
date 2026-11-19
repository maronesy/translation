# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 113 (printed ١١٢)."""

PAGE_NUMBER = 113
PRINTED_PAGE = "١١٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "على أن الأصل في الاسم هو الصرف، فبني الإعلال على ما هو الأصل، ثم سقطت الضمة للثقل، والياء لالتقاء الساكنين، فصار «جوار» على وزن «سلام وكلام»[[١]]،",
     "en": "…that the default in the noun is declension; so the iʿlāl was built upon what is the default. Then the ḍamma dropped on account of heaviness, and the yāʾ [dropped] on account of the meeting of two quiescents, so that “jawār” came to be of the measure of “salām” and “kalām”;"},

    {"type": "matn",
     "ar": "فلم يبق على صيغة منتهى الجموع، فهو بعد الإعلال أيضا منصرف، والتنوين فيه للصرف، كما كان قبل الإعلال كذلك.",
     "en": "so it no longer remained of the pattern of the utmost plurals (ṣīghat muntahā al-jumūʿ). Thus, even after the iʿlāl, it is declinable, and the nunation in it is [the nunation] of declension, just as it was so before the iʿlāl."},

    {"type": "matn",
     "ar": "وذهب بعضهم: إلى أنه بعد الإعلال غير منصرف[[٢]]؛ لأن فيه الجمعية مع صيغة منتهى الجموع؛ لأن المحذوف بمنزلة المقدر[[٣]]، ولهذا لا يجري الإعراب على الراء،",
     "en": "But others held that, after the iʿlāl, it is non-declinable — because plurality is present in it together with the pattern of the utmost plurals; for the elided [letter] stands in the place of what is [merely] posited, and for this reason the inflection does not run upon the rāʾ."},

    {"type": "matn",
     "ar": "والتنوين فيه تنوين العوض، فإنه لما سقط تنوين الصرف عوض عن الياء المحذوفة، أو عن حركتها هذا التنوين. وعلى هذا القياس حالة الجر بلا تفاوت.",
     "en": "And the nunation in it is the nunation of compensation (tanwīn al-ʿiwaḍ); for when the nunation of declension fell away, this nunation was made a substitute for the elided yāʾ, or for its vowel. On this same analogy is the genitive state, with no difference."},

    {"type": "matn",
     "ar": "وفي لغة بعض العرب: إثبات الياء في حالة الجر، كما في حالة النصب، تقول: «مررت بجواري» كما تقول: «رأيت جواري»،",
     "en": "In the dialect of some of the Arabs, the yāʾ is retained in the genitive state, just as in the accusative state; you say “marartu bi-jawārī” just as you say “raʾaytu jawārī.”"},

    {"type": "matn",
     "ar": "وبناء هذه اللغة[[٤]] على تقديم منع الصرف على الإعلال، فإنه حينئذ[[٥]] تكون الياء مفتوحة في حالة الجر، والفتحة خفيفة، فما وقع فيه الإعلال.",
     "en": "This dialect is based upon making the withholding of declension precede the iʿlāl; for in that case the yāʾ is vowelled with fatḥa in the genitive state, and the fatḥa is light, so that no iʿlāl occurs in it."},

    {"type": "matn",
     "ar": "وأما في حالة الرفع، فأصل «جوار»: «جواري» بالضم بلا تنوين، حذفت الضمة للثقل، وعوض عنها التنوين[[٦]]، فسقطت الياء لالتقاء الساكنين، فصار «جوار»،",
     "en": "As for the nominative state, the original of “jawār” is “jawārī” with ḍamma and without nunation; the ḍamma was dropped on account of heaviness, and the nunation was made a substitute for it, so the yāʾ fell away on account of the meeting of two quiescents, and it became “jawār.”"},

    {"type": "matn",
     "ar": "وعلى هذه اللغة لا إعلال إلا في حالة واحدة، بخلاف اللغة المشهورة، فإن فيها الإعلال في حالتين، كما عرفت.",
     "en": "According to this dialect, there is no iʿlāl except in a single state — unlike the well-known dialect, in which the iʿlāl occurs in two states, as you have come to know."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: لم يبق فيه صيغة منتهى الجموع، ويكون على وزن المفردات مثل فرازنة.",
     "en": "He means: the pattern of the utmost plurals no longer remains in it, and it comes to be on the measure of the singulars, like farāzina."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يفهم منه أن من جعله غير منصرف يجعل الإعلال مقدما على منع الصرف، سواء كان التنوين عوضا عن الياء، أو عن الحركة.",
     "en": "It is understood from this that whoever makes it non-declinable makes the iʿlāl precede the withholding of declension, whether the nunation is a substitute for the yāʾ or for the vowel."},
    {"type": "pair",
     "ar": "وينبغي أن يكون كذلك لأن منع الصرف لو كان مقدما على الإعلال لوجب الفتح حالة الجر.",
     "en": "And it ought to be so, because if the withholding of declension were prior to the iʿlāl, then fatḥa would be obligatory in the genitive state."},
    {"type": "pair",
     "ar": "والقول بأن الفتح في حكم الكسر؛ لأنه بمعناه بعيد، لكن من قال: إن التنوين عوض عن الحركة، هو المبرد.",
     "en": "The claim that the fatḥa has the ruling of the kasra — because it is equivalent to it in sense — is far-fetched; but the one who said that the nunation is a substitute for the vowel is al-Mubarrad."},
    {"type": "pair",
     "ar": "والمفهوم من كلام الرضي: إن منع الصرف مقدم على الإعلال عنده، وأصل جوار جواري بالتنوين؛ لأن أصل الاسم الصرف.",
     "en": "What is understood from the words of al-Raḍī is that, in his view, the withholding of declension is prior to the iʿlāl, and the origin of “jawār” is “jawārī” with nunation — because the origin of the noun is declension."},
    {"type": "pair",
     "ar": "ثم جواري بحذفها وإثبات الحركة، ثم جواري بحذف الحركة للاستثقال، ثم جوار بتعويض التنوين عن الحركة ليخف الثقل بحذف الياء للساكنين.",
     "en": "Then “jawārī” by dropping it (the nunation) and retaining the vowel; then “jawārī” by dropping the vowel on account of heaviness; then “jawār” by making the nunation a substitute for the vowel, so that the heaviness is lightened through the dropping of the yāʾ owing to the two quiescents."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يفهم منه أن صاحب هذا المذهب يجعل الإعلال مقدما على منع الصرف.",
     "en": "It is understood from this that the proponent of this school makes the iʿlāl precede the withholding of declension."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مبتدأ خبره قوله: على تقديم أي: بناء لغة بعض العرب كائن على تقديم منع الصرف على الإعلال.",
     "en": "[It is] a subject (mubtadaʾ) whose predicate is his statement “upon making [it] precede”; that is: the basing of the dialect of some of the Arabs is [founded] upon making the withholding of declension precede the iʿlāl."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "علة لكون بناء هذه اللغة على تقديم المذكور. وقوله: مفتوحة أي: بدون تنوين.",
     "en": "[It is] a cause for this dialect’s being based upon the aforementioned precedence. And his statement “vowelled with fatḥa” means: without nunation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: عوضت عن الضمة كما قال به المبرد حتى التقى ساكنان، فسقطت إلى آخره.",
     "en": "That is: it was made a substitute for the ḍamma — as al-Mubarrad held — such that two quiescents met, so it (the yāʾ) fell away, and so on."},
]
