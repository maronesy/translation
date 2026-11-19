# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 90 (printed ٨٩).

Poetic examples of declining the diptote for necessity: the breaking of meter,
the metrical deviation (ziḥāf), and the observance of rhyme.
"""

PAGE_NUMBER = 90
PRINTED_PAGE = "٨٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "في الشعر، فكثيرا ما يقع من منع صرفه انكسار يخرجه عن الوزن، أو انزحاف يخرجه عن السلاسة.",
     "en": "…in poetry, then frequently there arises, from withholding its declension, a breakage that takes it out of the meter, or a metrical deviation (inziḥāf) that takes it out of smoothness (salāsa)."},
    {"type": "matn",
     "ar": "أما الأول: فكقوله:",
     "en": "As for the first [the breaking of meter], it is as in his saying:"},
    {"type": "verse",
     "ar": "صبت[[١]] علي مصائب لو أنها          صبت على الأيام صرن لياليا",
     "en": "Calamities have been poured upon me such that, had they // been poured upon the days, they would have turned to nights."},
    {"type": "matn",
     "ar": "وأما الثاني فكقوله:",
     "en": "As for the second [the metrical deviation], it is as in his saying:"},
    {"type": "verse",
     "ar": "أعد ذكر نعمان لنا إن ذكره[[٢]]          هو المسك ما كررته يتضوع",
     "en": "Repeat for us the mention of Nuʿmān, for its mention // is [as] musk: the more you repeat it, the more it diffuses its fragrance."},
    {"type": "matn",
     "ar": "فإنه لو فتح نون «نعمان» من غير تنوين يستقيم الوزن، ولكن يقع فيه زحاف يخرجه عن السلاسة، كما يحكم به سلامة الطبع.",
     "en": "For if the nūn of “Nuʿmān” were given a fatḥa without tanwīn, the meter would be sound; but there would occur in it a metrical deviation (ziḥāf) that takes it out of smoothness, as soundness of [poetic] taste (salāmat al-ṭabʿ) judges."},
    {"type": "matn",
     "ar": "فإن قلت: الاحتراز[[٣]] عن الزحاف ليس بضروري[[٤]]، فكيف يشمله قوله: «للضرورة»؟",
     "en": "If you say: guarding against metrical deviation is not obligatory (ḍarūrī), then how does his statement “for necessity (li-l-ḍarūra)” include it?"},
    {"type": "matn",
     "ar": "قلنا: الاحتراز عن بعض الزحافات إذا أمكن الاحتراز عنه ضروري عند الشعراء.",
     "en": "We say: guarding against certain metrical deviations, when it is possible to guard against them, is [reckoned] obligatory among the poets."},
    {"type": "matn",
     "ar": "وأما الضرورة الواقعة لرعاية القافية، فكما في قوله:",
     "en": "As for the necessity occurring for the sake of observing the rhyme, it is as in his saying:"},
    {"type": "verse",
     "ar": "سلام على خير الأنام وسيد          حبيب إله العالمين محمد",
     "en": "Peace be upon the best of mankind and the master, // the beloved of the God of all the worlds, Muḥammad,"},
    {"type": "verse",
     "ar": "بشير نذير هاشمي مكرم          عطوف رؤوف من يسمى بأحمد",
     "en": "a bearer of glad tidings, a warner, a Hāshimite, ennobled, // tender and compassionate — he who is named Aḥmad."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الحاشية: هذا البيت مما قالته فاطمة رضي الله عنها في مرثية النبي صلى الله عليه وسلم، وأوله:",
     "en": "In the margin [it is noted]: this verse is among what Fāṭima, may Allah be pleased with her, said in her elegy for the Prophet, may Allah bless him and grant him peace; and its opening is:"},
    {"type": "verse",
     "ar": "ماذا على من شم تربة أحمد          أن لا يشم مدى الزمان غواليا",
     "en": "What [harm] is there upon one who has smelled the dust of Aḥmad’s [grave] // that he should not, for all time, smell [any] costly perfumes (ghawālī)?"},
    {"type": "pair",
     "ar": "مرثية بالتخفيف.",
     "en": "“Marthiya” (elegy) is [pronounced] with lightening (takhfīf) [of the yāʾ]."},
    {"type": "pair",
     "ar": "والمعنى: ما الذي أو أي شيء وقع على من شم تربة أحمد في أن لا يشم مدى الزمان وامتداده أنواع الغالية، والاستفهام للإنكار.",
     "en": "The meaning: What thing, or what matter, has befallen one who has smelled the dust of Aḥmad, that he should not smell — for the whole span and extent of time — the [various] kinds of costly perfume (ghāliya)? The interrogative is for denial (inkār)."},
    {"type": "pair",
     "ar": "والمعنى: لم يقع عليه شيء؛ لأنه استغنى بشمه عن شم الغوالي.",
     "en": "The meaning [is]: nothing has befallen him, because by that smelling he has been rendered independent of smelling the costly perfumes."},
    {"type": "pair",
     "ar": "أو المعنى: ماذا أوجب على من شم تربة أحمد ألا يشم إلى آخره، والاستفهام للتعجب من عظم الموجب، وهو كمال الاستغناء عن شم الغوالي.",
     "en": "Or the meaning [is]: What has made it incumbent upon one who has smelled the dust of Aḥmad that he should not smell — and so on [to the end of the verse] — the interrogative here being for wonder (taʿajjub) at the greatness of the necessitating factor, namely the perfect sufficiency that dispenses with smelling the costly perfumes."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يجوز الكسر في «إن»؛ وحينئذ تكون الجملة استئنافية، والفتح؛ وحينئذ يكون منصوبا بنزع الخافض، وهو اللام.",
     "en": "The kasra is permissible in “inna” [reading “inna ḏikrahu”], in which case the sentence is a resumptive one (istiʾnāfiyya); and the fatḥa [reading “anna”] is [also permissible], in which case [“ḏikrahu”] is accusative through the removal of the governing preposition (nazʿ al-khāfiḍ), namely the lām."},
    {"type": "pair",
     "ar": "وإنما لم يمثل للضرورة لظهور أمرها.",
     "en": "He gave no example for the [rhyme-related] necessity only because its matter is evident."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إلى قوله: ضروري، فالمراد بالضرورة ما عده الشعراء ضرورة.",
     "en": "[This extends] up to his words “ḍarūrī”; so what is meant by “necessity” (ḍarūra) is whatever the poets have counted as a necessity."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: فلا يجب الصرف لأجله، بل يجوز كما في حال التناسب، ولا يخفى وجه تفريع هذا السؤال على ما قبله.",
     "en": "That is: declension is not obligatory on its account; rather it is [merely] permissible, as in the case of [phonetic] correspondence (tanāsub). And the manner in which this question branches off from what precedes it is not hidden."},
]
