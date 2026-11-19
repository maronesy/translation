# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 359 (printed ٣٥٨)."""

PAGE_NUMBER = 359
PRINTED_PAGE = "٣٥٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فكأنه متقدم من» from the foot of PDF p. 358.
    {"type": "matn",
     "ar": "حيث المعنى[[١]] أو من سياق الكلام كقوله تعالى: ﴿ولأبويه﴾[[٢]]؛",
     "en": "…respect of meaning; or [the meaning is understood] from the context of speech, as in His words, the Exalted: “And for his parents”,"},
    {"type": "matn",
     "ar": "لأنه لما تقدم ذكر الميراث دل على أن ثمة موروثا فكأنه تقدم ذكره معنى.",
     "en": "for since mention of inheritance has preceded, it indicates that there is someone inherited from, so it is as though mention of him preceded in meaning."},
    {"type": "matn",
     "ar": "وأما التقدم الحكمي، فإنما جاء في ضمير الشأن[[٣]] والقصة؛",
     "en": "As for precedence by legal status (al-taqaddum al-ḥukmī), it occurs only in the pronoun of the matter (ḍamīr al-shaʾn) and of the story (al-qiṣṣa),"},
    {"type": "matn",
     "ar": "لأنه إنما جيء به من غير أن يتقدم ذكره، قصدا لتعظيم القصة بذكرها مبهمة، ليعظم وقوعها في النفس ثم يفسرها،",
     "en": "because it is brought without its mention having preceded, with the aim of magnifying the story by mentioning it vaguely, so that its impact on the soul is greater, and then it is explained;"},
    {"type": "matn",
     "ar": "فيكون ذلك أبلغ من ذكره أولا مفسرا وصار كأنه في حكم العائد إلى الحديث المتقدم المعهود بينك وبين مخاطبك،",
     "en": "this is more eloquent than mentioning it explained from the outset, and it becomes as though it had the status of referring back to a preceding matter familiar between you and your addressee."},
    {"type": "matn",
     "ar": "وكذا الحال في ضمير «نعم رجلا[[٤]] زيد، وربه رجلا».",
     "en": "The same holds of the pronoun in “niʿma rajulan Zaydun” (what a man Zayd is) and “rubbahu rajulan” (many a man)."},
    {"type": "matn",
     "ar": "(وهو) أي: المضمر بالنظر إلى ما قبله قسمان: (متصل ومنفصل).",
     "en": "(It), that is, the pronoun, with regard to what precedes it, is of two kinds: (attached (muttaṣil) and detached (munfaṣil))."},
    {"type": "matn",
     "ar": "(فالمنفصل[[٥]]: المستقل بنفسه[[٦]]) غير محتاج إلى كلمة أخرى قبله ليكون كالجزء منها، بل هو كالاسم الظاهر",
     "en": "(The detached is the one that stands by itself), not needing another word before it so as to be like a part of it; rather, it is like the overt noun,"},
    {"type": "matn",
     "ar": "سواء كان مجاورا لعامله نحو: «ما أنت منطلقا» عند الحجازية، أو غير مجاور له نحو: «ما ضربت إلا إياك».",
     "en": "whether it is adjacent to its governor, as in “mā anta munṭaliqan” (you are not departing) according to the Ḥijāzī usage, or not adjacent to it, as in “mā ḍarabtu illā iyyāka” (I struck none but you)."},
    {"type": "matn",
     "ar": "(والمتصل: غير المستقل بنفسه) المحتاج إلى عامله الذي قبله، ليتصل به ويكون كالجزء منه.",
     "en": "(The attached is the one that does not stand by itself), needing its governor that precedes it, so as to be joined to it and be like a part of it."},
    {"type": "matn",
     "ar": "(وهو) أي: المضمر باعتبار الإعراب ثلاثة أقسام: («مرفوع، ومنصوب، ومجرور»[[٧]]) لقيامه مقام الظاهر[[٨]]، وانقسام الظاهر إليها.",
     "en": "(It), that is, the pronoun, with respect to inflection, is of three kinds: (nominative, accusative and genitive), because it stands in place of the overt noun and the overt noun divides into these."},
    {"type": "matn",
     "ar": "(فالأولان) أي: المرفوع والمنصوب، كل واحد منهما قسمان: (متصل)؛ لأنه الأصل (ومنفصل) لمانع من الاتصال",
     "en": "(The first two), that is, the nominative and the accusative, are each of two kinds: (attached), since that is the default, (and detached), owing to something that prevents attachment;"},
    {"type": "matn",
     "ar": "(والثالث) أي: الضمير المجرور (متصل) فقط؛",
     "en": "(and the third), that is, the genitive pronoun, is (attached) only,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «متقدم» printed where the syntax after «كان» calls for «متقدما»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: كان لفظ العدل متقدم من أجل المعنى وتقدمه، فضمير كأنه للفظ العدل،",
     "en": "That is: the word “justice” has preceded on account of the meaning and its precedence; the pronoun in “ka-annahu” is for the word “justice”,"},
    {"type": "pair",
     "ar": "وقوله: من حيث المعنى تعليل، وإلا فينبغي أن يقول: فكأنه متقدم من حيث اللفظ.",
     "en": "and his words “in respect of meaning” give the reason; otherwise he ought to say: “so it is as though it preceded in respect of wording”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النساء: ١١.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:11."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يصح الحصر كما لا يخفى.",
     "en": "The restriction is not sound, as is evident."},
    {"type": "pair",
     "ar": "ولو كان راجعا إلى علة المجيء كان قوله: لأنه إنما جيء به من غير أن يتقدم ذكره مستدركا وكان العبارة المحررة.",
     "en": "Were it to bear on the reason for its being brought, his words “because it is brought without its mention having preceded” would be redundant, and the precise wording would have been:"},
    {"type": "pair",
     "ar": "وإنما جاء في ضمير الشأن قصدا إلى آخره،",
     "en": "“it occurs in the pronoun of the matter only with the aim…” to the end."},
    {"type": "pair",
     "ar": "والضمير الراجع إلى المتقدم الحكمي قد لا يكون للتعظيم بل للاحتراز عن الضمير قبل الذكر أو حذف الفاعل كما في تنازع الفعلين.",
     "en": "A pronoun referring to what precedes by legal status may not be for magnification but to avoid a pronoun before mention, or the elision of the agent, as in the contention of two verbs (tanāzuʿ al-fiʿlayn)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وأما الضمير في باب التنازع، فللتحرز عن التكرار، وحذف الفاعل.",
     "en": "As for the pronoun in the chapter of contention (tanāzuʿ), it is to avoid repetition and the elision of the agent."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الفاء للتفسير.",
     "en": "The fāʾ is explicative."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "في التلفظ بلسان التخاطب.",
     "en": "In being uttered in the language of mutual address."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الأخصر الأوضح، والأول مرفوع ومنصوب ومجرور، والثاني مرفوع ومنصوب.",
     "en": "The briefer and clearer [wording would be]: the first is nominative, accusative and genitive, and the second nominative and accusative."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "مع إعرابه للاختصار.",
     "en": "Together with its inflection, for brevity."},
]
