# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 516 (printed ٥١٥)."""

PAGE_NUMBER = 516
PRINTED_PAGE = "٥١٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # The verse completes «كقول الشاعر:» at the foot of PDF p. 515.
    {"type": "verse",
     "ar": "ولقد أراني للرماح[[١]] دريئة[[٢]]     من عن يميني تارة وأمامي",
     "en": "…And I have seen myself a target for the spears, from my right side at one time and from in front of me."},
    {"type": "quran",
     "ar": "وكقوله تعالى: ﴿إني أراني أعصر خمرا﴾[[٣]].",
     "en": "And as in His words, the Exalted: “I saw myself pressing wine” (Qurʾān, Sūrat Yūsuf 12:36)."},
    {"type": "matn",
     "ar": "(ولبعضها) أي: لبعض أفعال القلوب ما عدا «حسبت[[٤]]، وخلت، وزعمت» (معنى آخر) قريب من معانيها الأول،",
     "en": "(And some of them), that is, some of the verbs of the heart other than “ḥasibtu, khiltu and zaʿamtu”, (have another meaning), close to their first meanings,"},
    {"type": "matn",
     "ar": "وهي: إما العلم أو الظن، بحيث يمكن أن يتوهم أنه بهذا المعنى أيضا متعد إلى مفعولين،",
     "en": "which are either knowledge or supposition, such that it may be imagined that in this meaning too it is transitive to two objects."},
    {"type": "matn",
     "ar": "وإنما قيدنا بذلك[[٥]] لئلا يقال: لا وجه للتخصيص بالبعض[[٦]]؛ لأن لكل واحد معنى آخر،",
     "en": "We added this qualification only so that it not be said: there is no reason for restricting [this] to some of them, since each one has another meaning;"},
    {"type": "matn",
     "ar": "فإن «خلت» جاء بمعنى: صرت ذا خال[[٧]]، و«حسبت» بمعنى: صرت ذا حسب، و«زعمت» بمعنى: كفلت",
     "en": "for “khiltu” has come in the sense of “I became possessed of khāl (pride)”, “ḥasibtu” in the sense of “I became possessed of ḥasab (reddish hair)”, and “zaʿamtu” in the sense of “I became surety”."},
    {"type": "matn",
     "ar": "(يتعدى به) أي: بذلك المعنى الآخر (إلى) مفعول (واحد) لا اثنين",
     "en": "(By it it is transitive), that is, by that other meaning, (to one) object, not two:"},
    {"type": "matn",
     "ar": "(فـ«ظننت» بمعنى «اتهمت») من الظنة[[٨]] بمعنى: التهمة، فـ«ظننت زيدا» بمعنى: اتهمته أي: أخذته مكانا لوهمي، والوهم نوع من العلم،",
     "en": "(so “ẓanantu” in the sense of “ittahamtu” (I suspected)), from al-ẓinna in the sense of “suspicion” (al-tuhma); so “ẓanantu zaydan” means “I suspected him”, that is, I took him as a locus for my surmise (wahm), and surmise is a kind of knowledge."},
    # REVIEW: the verse is printed «بضنين» (with ḍād), though it is cited as an instance of ظن «اتهم» and glossed «بمتهم» (the reading «بظنين»); transcribed as printed.
    {"type": "quran",
     "ar": "ومنه قوله تعالى: ﴿وما هو على الغيب بضنين﴾[[٩]] أي: بمتهم",
     "en": "From it is His words, the Exalted: “And he is not, concerning the Unseen, bi-ḍanīn” (Qurʾān, Sūrat al-Takwīr 81:24), that is, suspect;"},
    {"type": "matn",
     "ar": "(و«علمت» بمعنى: «عرفت») تقول: «علمت زيدا» بمعنى: «عرفت شخصه»، وهو العلم بنفس شيء من غير حكم عليه",
     "en": "(and “ʿalimtu” in the sense of “ʿaraftu” (I recognized)): you say “ʿalimtu zaydan” meaning “I recognized his person”; it is knowledge of the thing itself without a judgement about it;"},
    {"type": "matn",
     "ar": "(و«رأيت» بمعنى: «أبصرت») ومعنى «أبصرت» قريب من",
     "en": "(and “raʾaytu” in the sense of “abṣartu” (I saw)); the meaning of “abṣartu” is close to…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اللام للابتداء أو جواب القسم، وأراني أي: أبصر للرماح جمع رمح",
     "en": "The lām is that of the inchoative or of the response to an oath; “arānī” means “I see”; “li-l-rimāḥ” is the plural of rumḥ (spear)."},
    {"type": "pair",
     "ar": "دريئة على وزن فعيلة بالهمزة الحلقة التي يتعلم الطعن، والرمي عليها،",
     "en": "“Darīʾa”, on the pattern faʿīla with hamza, is the ring on which thrusting and shooting are learned."},
    {"type": "pair",
     "ar": "من عن يميني متعلق بـ«أراني»، وهو القرينة على أنه من الرؤية البصرية دون القلبية؛ إذ لا تعلق للعلم بالجهة،",
     "en": "“Min ʿan yamīnī” is connected with “arānī”, and it is the indication that it is from seeing with the eye, not with the heart, since knowledge has no connection with direction."},
    {"type": "pair",
     "ar": "وعن اسم بمعنى الجانب لدخول من عليه.",
     "en": "“ʿAn” is a noun meaning “side”, because “min” enters upon it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «حلقه» (with hāʾ), whereas footnote 1 has «الحلقة»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: أبصر نفسي حلقه، هي هدف الرماح،",
     "en": "That is, I see myself a ring, which is the target of the spears;"},
    {"type": "pair",
     "ar": "ولكون «أرى» بمعنى العلم مساغ، فيكون دريئة مفعوله الثاني، وعلى ما ذكره هي حال.",
     "en": "and there is room for “arā” being in the sense of knowledge, in which case “darīʾa” is its second object; on what he mentioned, it is a circumstantial (ḥāl)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة يوسف: ٣٦.",
     "en": "Sūrat Yūsuf 12:36."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بدل من البعض، فائدته تعيين ذلك البعض قبل البيان.",
     "en": "A substitute (badal) for “some”; its benefit is to specify those some before the explanation."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «معاينها», whereas the commentary text has «معانيها»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: بقوله: قريب من معاينها الأول.",
     "en": "That is, by his words “close to their first meanings”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولئلا يقال: لا وجه لتخصيص بيان هذا البعض من المعاني الأخر، فإن لكل منها معاني أخر.",
     "en": "And so that it not be said: there is no reason for restricting the explanation of other meanings to these some, since each of them has other meanings."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: أي: لتخصيص الذكر بالبعض، أو لتخصيص البعض بالحكم المذكور؛",
     "en": "ʿAbd al-Ḥakīm said: that is, for restricting the mention to some, or for restricting the stated ruling to some;"},
    {"type": "pair",
     "ar": "إذ كما أن لهذا البعض معنى يتعدى به إلى مفعول واحد كذلك للبعض الآخر، ولذلك البعض معاني لا يتعدى بها.",
     "en": "for just as these some have a meaning by which they are transitive to one object, so do the other some; and those some have meanings by which they are not transitive."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الخال والخيلاء التكبر، والأحسب من الناس الذي في شعر رأسه شقرة.",
     "en": "Al-khāl and al-khuyalāʾ are pride; and al-aḥsab among people is one in whose hair there is a reddish tinge."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بكسر الظاء: التهمة كهمزة أصله، وهمة قلبت الواو تاء كما في وكل.",
     "en": "With a kasra on the ẓāʾ. Al-tuhma, on the pattern of humaza: its origin is wuhama, the wāw having been changed to tāʾ, as in wukal [> tukal]."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "سورة التكوير: ٢٤.",
     "en": "Sūrat al-Takwīr 81:24."},
]
