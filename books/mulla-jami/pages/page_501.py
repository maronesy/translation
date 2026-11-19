# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 501 (printed ٥٠٠)."""

PAGE_NUMBER = 501
PRINTED_PAGE = "٥٠٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 500 ends with a complete sentence («أفاد استمرار ذلك إلى وقت التكلم بها.»); a new lemma begins here.
    {"type": "matn",
     "ar": "(وجواز حذف الفعل) أي: وتختص أيضا «لما» بجواز حذف الفعل المنفي بها إن دل عليه دليل نحو: «شارفت المدينة ولما» أي: ولما أدخلها.",
     "en": "(And the permissibility of omitting the verb), that is, “lammā” is also distinguished by the permissibility of omitting the verb negated by it, if some indication points to it, as in “shāraftu al-madīnata wa-lammā” (I drew near the city, and not yet), that is, “and I have not yet entered it”."},
    {"type": "matn",
     "ar": "وتختص أيضا بعدم دخول أدوات الشرط عليها، فلا تقول: «إن لما يضرب، ومن لما يضرب» كما تقول: «إن لم يضرب، ومن لم يضرب»،",
     "en": "It is also distinguished by the particles of condition not entering upon it: you do not say “in lammā yaḍrib” and “man lammā yaḍrib” as you say “in lam yaḍrib” (if he does not strike) and “man lam yaḍrib” (whoever does not strike);"},
    {"type": "matn",
     "ar": "وكان ذلك لكونها فاصلة قوية بين العامل ومعموله[[١]].",
     "en": "and that is because it is a strong separator between the governing word and what it governs."},
    {"type": "matn",
     "ar": "وتختص أيضا باستعمالها غالبا في المتوقع أي: ينفي بها فعل مترقب متوقع، تقول لمن يتوقع ركوب الأمير: «لما يركب الأمير».",
     "en": "It is also distinguished by being used mostly for what is expected, that is, by it an awaited, expected act is negated: you say to one who expects the emir to ride out, “lammā yarkab al-amīr” (the emir has not yet ridden out)."},
    {"type": "matn",
     "ar": "وقد تستعمل في غير المتوقع أيضا نحو: «ندم زيد ولما ينفعه الندم».",
     "en": "It is sometimes used for what is not expected as well, as in “nadima Zaydun wa-lammā yanfaʿhu al-nadamu” (Zayd repented, and the repentance has not yet benefited him)."},
    {"type": "matn",
     "ar": "(و«لام الأمر») هي اللام (المطلوب بها الفعل) وتدخل فيها لام الدعاء نحو: «ليغفر لنا الله» وهي مكسورة، وفتحها لغة،",
     "en": "(And “the lām of command”) is the lām (by which the act is requested); the lām of supplication is included in it, as in “li-yaghfir lanā Allāh” (may Allah forgive us). It takes a kasra, and giving it a fatḥa is a dialectal variant;"},
    {"type": "matn",
     "ar": "وقد تسكن بعد الواو والفاء وثم نحو: ﴿ولتأت طائفة أخرى لم يصلوا فليصلوا﴾[[٢]] ﴿ثم ليقضوا﴾[[٣]].",
     "en": "and it is sometimes made quiescent after wāw, fāʾ and thumma, as in “And let another party that has not prayed come and let them pray” (Qurʾān, Sūrat al-Nisāʾ 4:102) and “Then let them complete” (Qurʾān, Sūrat al-Ḥajj 22:29)."},
    {"type": "matn",
     "ar": "(و«لا» للنهي[[٤]]) هي «لا» (المطلوب بها الترك) أي: ترك الفعل.",
     "en": "(And “lā” of prohibition) is the “lā” (by which abstention is requested), that is, abstention from the act."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «ولا النهي ضدها»، أي: «لا» النهي التي هي ضد لام الأمر، وهي التي يطلب بها ترك الفعل،",
     "en": "In some copies: “and lā of prohibition is its opposite”, that is, the “lā” of prohibition, which is the opposite of the lām of command; it is that by which abstention from the act is requested,"},
    {"type": "matn",
     "ar": "وهي تدخل على جميع أنواع المضارع المبني للفاعل والمفعول، مخاطبا أو غائبا أو متكلما.",
     "en": "and it enters upon all kinds of muḍāriʿ, active and passive, whether second person, third person or first person."},
    {"type": "matn",
     "ar": "(وكلم المجازاة) المذكورة من قبل (تدخل على الفعلين لسببية) الفعل[[٥]] (الأول ومسببية) الفعل (الثاني) أي: لجعل الفعل الأول سببا والثاني مسببا.",
     "en": "(And the words of requital (kalim al-mujāzāt)), mentioned before, (enter upon two verbs for the causality of) the (first) verb (and the causedness of the second) verb, that is, to make the first verb a cause and the second an effect."},
    {"type": "matn",
     "ar": "وفي شرح المصنف: وكلم المجازاة ما تدخل على شيئين لتجعل الأول سببا للثاني.",
     "en": "In the author’s own commentary: “The words of requital are what enter upon two things to make the first a cause of the second.”"},
    {"type": "matn",
     "ar": "ولا شك أن كلم المجازاة لا تجعل الشيء سببا لشيء، فالمراد بجعلها الشيء",
     "en": "There is no doubt that the words of requital do not make a thing the cause of a thing; so what is meant by their making a thing…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأن «إن» في «إن لم أضرب» ليس عاملا في «أضرب»؛ لأنه مدخول «لم» ومعموله، وإنما مدخول «إن لم أضرب».",
     "en": "This is open to discussion: for “in” in “in lam aḍrib” (if I do not strike) does not govern “aḍrib”, since that is what “lam” enters upon and governs; what [“in”] enters upon is only “lam aḍrib” as a whole."},
    # REVIEW: footnote ١ prints «وإنما مدخول «إن لم أضرب»» (the quoted phrase includes «إن», which the sense suggests should be «لم أضرب»); transcribed as printed.

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النساء: ١٠٢.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:102."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الحج: ٢٩",
     "en": "Qurʾān, Sūrat al-Ḥajj 22:29."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يصح إضافة العلم، وكأنه نكرها، أو جعل النهي مرفوعا صفة لكلمة «لا» بمعنى لا الناهية.",
     "en": "Annexing a proper name [as in “lā al-nahy”] is not valid; it is as though he made it indefinite, or he made “al-nahy” nominative, as an attribute of the word “lā” in the sense of “the prohibiting lā”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يخفى أن السببية بمعنى كون الشيء سببا لا بمعنى جعله سببا،",
     "en": "It is not hidden that causality means a thing’s being a cause, not its being made a cause;"},
    {"type": "pair",
     "ar": "فاللائق أن يفسر الكلام بإفادة سببية الأول ومسببية الثاني،",
     "en": "so it is fitting to interpret the statement as conveying the causality of the first and the causedness of the second."},
    # REVIEW: footnote ٥ prints «فكان المصنف» and «وكان الشارح» (read in the sense of «فكأن»/«وكأن»); transcribed as printed.
    {"type": "pair",
     "ar": "فكان المصنف أراد بجعله سببا جعله سببا في نظر المخاطب، وذلك ليس إلا بالإفادة،",
     "en": "It is as though the author meant by its being made a cause its being made a cause in the view of the addressee, and that is only through conveying [it];"},
    {"type": "pair",
     "ar": "فمآله أن المراد لإفادة سببية الأول،",
     "en": "so its upshot is that what is meant is “for conveying the causality of the first”;"},
    {"type": "pair",
     "ar": "وكان الشارح أيضا أراد هذا المعنى إلا أنه بعد عن التنقيح.",
     "en": "and it is as though the commentator too meant this sense, except that he fell short of precision."},
]
