# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 599 (printed ٥٩٨)."""

PAGE_NUMBER = 599
PRINTED_PAGE = "٥٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(و) النون (المخففة تحذف للساكن) أي: لالتقائها الساكن المذكور بعدها.",
     "en": "(And the light) nūn (is elided for a quiescent), that is, because of its meeting the quiescent mentioned after it."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «للساكنين» أي: لالتقاء الساكنين، كقول الشاعر:",
     "en": "In some copies: “for two quiescents”, that is, because of the meeting of two quiescents; as in the poet's words:"},
    {"type": "verse",
     "ar": "لا تهين الفقير علك أن          تركع يوما والدهر قد رفعه",
     "en": "Do not despise the poor man; it may be that you will bow one day, when fate has raised him up."},
    {"type": "matn",
     "ar": "أي: لا تهينن، حذفت النون الخفيفة لالتقائها اللام الساكنة، التي بعدها، وأبقيت فتحة ما قبلها، لتدل عليها،",
     "en": "That is, “lā tuhīnan”: the light nūn was elided because of its meeting the quiescent lām after it, and the fatḥa of what precedes it was kept to point to it;"},
    {"type": "matn",
     "ar": "وإلا لكان الواجب أن يقال: «لا تهن الفقير»، ولم يحركوها كما يحرك التنوين فرقا بينهما.",
     "en": "otherwise one would have had to say “lā tuhini l-faqīra”. They did not give it a vowel as the tanwīn is given a vowel, to distinguish between the two."},
    {"type": "matn",
     "ar": "وإنما لم يعكس حطا لمرتبة ما يدخل الفعل عن مرتبة ما يدخل الاسم، لكون الاسم أصلا والفعل فرعا.",
     "en": "It was not done the other way round only so as to lower the rank of what enters the verb below the rank of what enters the noun, since the noun is primary and the verb secondary."},
    {"type": "matn",
     "ar": "(و) تحذف أيضا المخففة (في) حال (الوقف) على ما ألحقت به تخفيفا إذا ضم أو كسر ما قبلها كما يحذف التنوين لذلك.",
     "en": "(And) the light [nūn] is also elided (in) the state of (pause (waqf)) upon what it was attached to, for lightness, when what precedes it has a ḍamma or a kasra, just as the tanwīn is elided for that reason."},
    {"type": "matn",
     "ar": "(فيرد ما حذف[[١]]) لأجل المخففة كما إذا ألحقت المخففة بـ«اغزوا، واغزي» وقلت: «اغزن، واغزن» بحذف الواو والياء.",
     "en": "(So what was elided is restored) because of the light [nūn]; as when you attach the light [nūn] to “ughzū” and “ughzī” and say “ughzun” and “ughzin”, eliding the wāw and the yāʾ."},
    {"type": "matn",
     "ar": "فإذا وقفت عليهما وجب أن ترد المحذوف وقلت: «اغزوا، واغزي» بخلاف التنوين،",
     "en": "When you pause on them, you must restore what was elided and say “ughzū” and “ughzī”; unlike the tanwīn,"},
    {"type": "matn",
     "ar": "فإنه لا يرد ما حذف لأجله؛ لأن التنوين لازم في الأصل، والمخففة ليست بلازمة، فجعل للازم مزية بإبقاء أثره على ما ليس بلازم.",
     "en": "for what was elided on its account is not restored, because the tanwīn is necessary in principle while the light [nūn] is not necessary; so the necessary was given a distinction over what is not necessary by keeping its effect."},
    {"type": "matn",
     "ar": "(و) المخففة (المفتوح ما قبلها تقلب ألفا[[٢]]) كقولك في «اضربن»: «اضربا» تشبيها لها بالتنوين.",
     "en": "(And) the light [nūn] (preceded by a fatḥa is changed into an alif), as when you say “iḍribā” for “iḍriban”, likening it to the tanwīn."},
    {"type": "matn",
     "ar": "فإن التنوين إذا انفتح ما قبلها تقلب ألفا، وإذا انضم أو انكسر تحذف، نحو: «أصبت خيرا، وأصابني خير، واختم لي بخير».",
     "en": "For the tanwīn, when what precedes it has a fatḥa, is changed into an alif, and when it has a ḍamma or a kasra it is elided, as in “aṣabtu khayrā” (I obtained good), “aṣābanī khayr” (good befell me), and “ikhtim lī bi-khayr” (seal [my life] for me with good)."},
    {"type": "matn",
     "ar": "اللهم اجعل خاتمة أمورنا خيرا، ولا تلحق بنا من تبعة شرورنا ضيرا،",
     "en": "O Allah, make the end of our affairs good, and let no harm overtake us from the consequences of our evils;"},
    {"type": "matn",
     "ar": "واجعل نونات نقائصنا -خفيفة كانت أو ثقيلة- في مواقف الندامة منقلبة بألف آداب عبوديتك على نهج الاستقامة،",
     "en": "make the nūns of our failings — light or heavy — in the stations of remorse, changed by the alif of the proprieties of servanthood to You onto the path of uprightness;"},
    {"type": "matn",
     "ar": "وصل على كلمة شفاعته في محو أرقام الضلالات كافية، وعن",
     "en": "and bless the one whose word of intercession suffices to erase the records of errors, and from…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "متفرع على الحذف في حال الوقف؛ إذ لا مجال للرد في الحذف للساكنين إلا أن يجعل الرد أعم من الرد في الكتابة أيضا.",
     "en": "This is a consequence of the elision in the state of pause, since there is no room for restoration in the elision for two quiescents — unless restoration is made more general, [including] restoration in writing as well."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «على الوقت», where «على الوقف» (on the pausal form) is expected; transcribed as printed, translated by the sense.
    {"type": "pair",
     "ar": "بناء الكتابة في الآخر على الوقت، وفي الأول على الابتداء",
     "en": "Writing is based, at the end [of a word], on the pausal form, and at the beginning on the initial form;"},
    {"type": "pair",
     "ar": "كما تقرر في محله يوجب ألا يكتب الخفيفة التي لم يفتح ما قبلها ويكتب ألفا إذا انفتح ما قبلها، فكتابتها على خلاف القياس.",
     "en": "this, as established in its place, requires that the light [nūn] not preceded by a fatḥa not be written, and that it be written as an alif when what precedes it has a fatḥa; so writing it [as nūn] is contrary to analogy (qiyās)."},
]
