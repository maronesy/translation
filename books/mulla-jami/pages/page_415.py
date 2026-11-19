# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 415 (printed ٤١٤)."""

PAGE_NUMBER = 415
PRINTED_PAGE = "٤١٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقد يقع[[١]]) بعدهما (المصدر) نحو: «ما خرجت مذ ذهابك» (أو الفعل[[٢]]) نحو: «ما خرجت مذ ذهبت»",
     "en": "(And there may occur) after them (the maṣdar), as in “mā kharajtu mudh dhahābuka” (I have not gone out since your departure), (or the verb), as in “mā kharajtu mudh dhahabta” (I have not gone out since you left),"},
    {"type": "matn",
     "ar": "(أو «أن») أي: ما كتب في هذه الصورة مثقلة كانت أو مخففة نحو: «ما خرجت مذ أنك ذاهب» أو «ما خرجت مذ أن ذهبت»",
     "en": "(or “an”), that is, what is written in this form, whether doubled or lightened, as in “mā kharajtu mudh annaka dhāhibun” (I have not gone out since you were leaving) or “mā kharajtu mudh an dhahabta” (I have not gone out since you left),"},
    {"type": "matn",
     "ar": "أو الجملة الاسمية نحو: «ما خرجت مذ زيد مسافر» ولم يذكره لقلته",
     "en": "or the nominal sentence, as in “mā kharajtu mudh zaydun musāfirun” (I have not gone out since Zayd has been travelling), which he did not mention because it is rare;"},
    {"type": "matn",
     "ar": "(فيقدر) بعدهما (زمان مضاف[[٣]]) إلى أحد هذه الأمور ليصح حمل ما بعدهما عليهما،",
     "en": "(so there is supposed) after them (a time annexed) to one of these things, so that what follows them may validly be predicated of them;"},
    {"type": "matn",
     "ar": "فكان التقدير في «ما خرجت مذ ذهابك»: مذ زمان ذهابك، وعلى هذا القياس فيما بقي.",
     "en": "thus the supposed form in “mā kharajtu mudh dhahābuka” is “mudh zamānu dhahābika” (since the time of your departure), and the rest follow the same analogy."},
    {"type": "matn",
     "ar": "(وهو) أي: كل واحد من «مذ ومنذ» اسمين (مبتدأ) وهما معرفتان لكونهما في تأويل الإضافة؛ لأنهما إما بمعنى: «أول المدة»، أو «جميع المدة»",
     "en": "(And it), that is, each of “mudh” and “mundhu” when they are nouns, (is an inchoative (mubtadaʾ)); they are definite because they are to be construed as annexed, since they mean either “the beginning of the period” or “the whole period”;"},
    {"type": "matn",
     "ar": "(وخبره ما بعده) أي: خبر كل منهما ما يقع بعده (خلافا للزجاج)، فإنهما عنده خبر المبتدأ، والمبتدأ ما بعدهما.",
     "en": "(and its predicate is what comes after it), that is, the predicate of each of them is what occurs after it, (contrary to al-Zajjāj), for according to him they are the predicate of the inchoative, and the inchoative is what comes after them."},
    {"type": "matn",
     "ar": "ويرد عليه[[٤]] أنه يلزم أن يكون المبتدأ في مثل قولك: «مذ يومان» نكرة، والخبر",
     "en": "Against him it is objected that the inchoative in such a saying as “mudh yawmāni” would then have to be indefinite, and the predicate…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "معطوف على ما يستفاد من سابق كلامه أي: يقع بعدهما على المعنيين اسم زمان، وقد يقع بعدهما المصدر.",
     "en": "It is coordinated with what is understood from his preceding words, that is: in both senses a noun of time occurs after them, and the maṣdar may occur after them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى: أو الجملة ليعلم أن الزمان المقدر مضاف إلى الجملة لا إلى مجرد الفعل كما يوهمه عبارته.",
     "en": "It would have been better [to say] “or the sentence”, so that it is known that the supposed time is annexed to the sentence, not to the bare verb, as his wording suggests."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هو زمان أو ساعة أو وقت أو يوم أو ليلة لو ساعدهما القرينة، فلهذا أنكر الزمان لم يقل: فيقدر الزمان المضاف.",
     "en": "It is “time”, “hour”, “moment”, “day” or “night”, if the context supports them; for this reason he made “time” indefinite and did not say “so the annexed time is supposed”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: «رحمه الله عليه» printed so (expected رحمة الله عليه); transcribed as printed.
    {"type": "pair",
     "ar": "قال المصنف رحمه الله عليه: وهذا المذهب وهم لا يساعده المعنى واللفظ.",
     "en": "The author, may Allah have mercy on him, said: this doctrine is a mistake that neither the meaning nor the wording supports."},
    {"type": "pair",
     "ar": "أما المعنى فلأنك تخبر عن أول المدة أو جميع المدة بأنها يوم الجمعة أو يومان لا العكس.",
     "en": "As for the meaning, it is because you report of the beginning of the period or the whole period that it is Friday or two days, not the reverse."},
    {"type": "pair",
     "ar": "وأما اللفظ فلما ذكره الشارح رحمه الله.",
     "en": "As for the wording, it is because of what the commentator, may Allah have mercy on him, mentioned."},
    {"type": "pair",
     "ar": "وتقديم الظرف إنما يكون مصححا إذا كان الظرف المقدم ظرفا للمبتدأ، كقولك: «في الدار رجل»، وفيما نحن فيه ليس كذلك.",
     "en": "Fronting the adverbial validates [an indefinite inchoative] only when the fronted adverbial is an adverbial of the inchoative, as in your saying “fī l-dāri rajulun” (in the house is a man); in our case it is not so."},
    {"type": "pair",
     "ar": "وتفصيل المقام أن لـ«مذ ومنذ» ثلاث حالات:",
     "en": "The details of the matter are that “mudh” and “mundhu” have three states."},
    {"type": "pair",
     "ar": "إحداها: أن يليهما اسم مجرور فهما حرفا جر بمعنى «من» إن كان الزمان ماضيا، وبمعنى «في» إن كان الزمان حاضرا، وبمعنى «من وإلى» جميعا إن كان معدودا.",
     "en": "The first: a genitive noun follows them; they are then prepositions in the sense of “min” (from) if the time is past, in the sense of “fī” (in) if the time is present, and in the sense of “min” and “ilā” (from … to) together if it is counted."},
    {"type": "pair",
     "ar": "وثانيتها: أن يليهما اسم مرفوع نحو: «مذ يوم الخميس ومنذ يومان ذهابك».",
     "en": "The second: a nominative noun follows them, as in “mudh yawmu l-khamīsi” (since Thursday) and “mundhu yawmāni dhahābuka” (for two days [has been] your absence)."},
    {"type": "pair",
     "ar": "وثالثها: أن يليهما جملة فعلية واسمية.",
     "en": "The third: a verbal or nominal sentence follows them."},
    {"type": "pair",
     "ar": "فقال البصريون: إنهما مبتدآن وما بعدهما خبرهما بدون التقدير فيما إذا كان ما بعدهما اسم زمان، نحو: «مذ يوم الجمعة»، وتقدير زمان فيما إذا كان ما بعدهما مصدرا أو جملة",
     "en": "The Baṣrans said: they are inchoatives and what follows them is their predicate, without any supposed element when what follows them is a noun of time, as in “mudh yawmu l-jumuʿa”, and with “time” supposed when what follows them is a maṣdar or a sentence."},
    {"type": "pair",
     "ar": "فقولنا: «ما رأيته مذ يوم الجمعة أو يومان» جملتان، والثانية مفسرة للأولى، فلذا لم يعطف عليه",
     "en": "So our saying “mā raʾaytuhu mudh yawmu l-jumuʿa” or “… yawmāni” is two sentences, the second explaining the first; that is why it is not coordinated with it,"},
    {"type": "pair",
     "ar": "وإن جاز العطف فيما هو بمعناه نحو: «ما رأيته» وأول مدة عدم رؤيتي يوم الجمعة.",
     "en": "although coordination is permissible in what has its meaning, as in “mā raʾaytuhu, wa-awwalu muddati ʿadami ruʾyatī yawmu l-jumuʿa” (I have not seen him, and the beginning of the period of my not seeing [him] is Friday)."},
    # REVIEW: «فإن لما قبلهما» printed so (فإن followed by لما); transcribed as printed.
    {"type": "pair",
     "ar": "وقال الكوفيون: إنهما ظرفان، فإن لما قبلهما مضافان إلى جملة مصرح بجزأيها إذا كان بعدهما جملة، ومحذوف أحد جزأيها إذا كان بعدهما مفرد",
     "en": "The Kūfans said: they are adverbials belonging to what precedes them, annexed to a sentence whose two parts are explicit when a sentence follows them, and one of whose two parts is omitted when a single word follows them,"},
    {"type": "pair",
     "ar": "نحو: «ما رأيته مذ يوم الجمعة»، ومنذ ذهابك أي: مذ كان يوم الجمعة، ومنذ كان ذهابك،",
     "en": "as in “mā raʾaytuhu mudh yawmu l-jumuʿa” and “mundhu dhahābuka”, that is, “since Friday was” and “since your departure was”."},
    {"type": "pair",
     "ar": "فقولنا: «ما رأيته مذ يوم الجمعة» جملة واحدة، قال صاحب",
     "en": "So our saying “mā raʾaytuhu mudh yawmu l-jumuʿa” is a single sentence. The author of…"},
]
