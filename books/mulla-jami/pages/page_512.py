# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 512 (printed ٥١١)."""

PAGE_NUMBER = 512
PRINTED_PAGE = "٥١١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 511 ends with a complete sentence («فقد ورد ذلك مع القرينة على قلة»); this page illustrates it.
    {"type": "matn",
     "ar": "أما حذف المفعول الأول، فكما في قوله تعالى: ﴿ولا يحسبن الذين يبخلون بما آتاهم الله من فضله هو خيرا لهم﴾[[١]]",
     "en": "As for the elision of the first object, it is as in His words, the Exalted: “And let not those who are niggardly with what Allah has given them of His bounty suppose it is better for them”,"},
    {"type": "matn",
     "ar": "على قراءة «ولا يحسبن» بالياء المنقوطة من تحت بنقطتين أي: لا يحسبن هؤلاء بخلهم هو خيرا لهم، فحذف «بخلهم» الذي هو المفعول الأول.",
     "en": "on the reading “wa-lā yaḥsabanna” with the yāʾ dotted below with two dots, that is, “let not these suppose their niggardliness to be better for them”; so “bukhlahum” (their niggardliness), which is the first object, has been elided."},
    {"type": "matn",
     "ar": "وأما حذف الثاني، فكما في قول الشاعر:",
     "en": "As for the elision of the second, it is as in the poet’s words:"},
    {"type": "verse",
     "ar": "لا تخلنا على غراتك إنا          طال ما قد وشى بنا الأعداء",
     "en": "Do not think us, at your deceits, [anxious]; for long have enemies slandered us [to you]."},
    {"type": "matn",
     "ar": "أي: لا تخلنا جازعين، فحذف «جازعين» الذي هو المفعول الثاني",
     "en": "That is, “do not think us anxious (jāziʿīna)”; so “jāziʿīna”, which is the second object, has been elided."},
    # REVIEW: printed «يعطى» (alif maqṣūra) in «يعطى الفقراء», where the active «يعطي» is apparently intended; transcribed as printed, translated as active.
    {"type": "matn",
     "ar": "(بخلاف باب «أعطيت»)، فإنه يجوز فيه الاقتصار على أحدهما مطلقا يقال: «فلان يعطي الدنانير» من غير ذكر المعطى له، أو «يعطى الفقراء» من غير ذكر المعطى.",
     "en": "(Unlike the class of “aʿṭaytu”), for in it restriction to one of the two is permitted absolutely: one says “so-and-so gives dinars”, without mentioning the one to whom it is given, or “he gives the poor”, without mentioning what is given."},
    {"type": "matn",
     "ar": "وقد يحذفان معا كقولك: «فلان يعطي ويكسو»؛ إذ يستفاد من مثله فائدة بدون المفعولين،",
     "en": "Both may be elided together, as in your saying “so-and-so gives and clothes”, since from the like of this a meaningful statement is obtained without the two objects;"},
    {"type": "matn",
     "ar": "بخلاف مفعولي باب «علمت» فإنك لا تحذفهما نسيا منسيا، فلا تقول: «علمت وظننت» لعدم الفائدة؛ إذ من المعلوم أن الإنسان لا يخلو من علم وظن.",
     "en": "unlike the two objects of the class of “ʿalimtu”: you do not elide them so that they are wholly forgotten. So you do not say “I knew” and “I supposed” [alone], for lack of informativeness, since it is known that a human being is never without knowledge and supposition."},
    {"type": "matn",
     "ar": "وأما مع قيام القرينة، فلا بأس بحذفهما نحو: «من يسمع يخل» أي: يخل مسموعة صادقا.",
     "en": "But where there is a contextual indication, there is no harm in eliding them, as in “man yasmaʿ yakhal” (whoever hears supposes), that is, supposes what he hears to be true."},
    {"type": "matn",
     "ar": "(ومنها) أي: ومن خصائص أفعال القلوب (جواز الإلغاء) أي: إبطال عملها[[٢]] (إذا توسطت) بين مفعوليها نحو: «زيد ظننت قائم» (أو تأخرت) عنهما نحو: «زيد قائم ظننت»،",
     "en": "(And among them), that is, among the particular properties of the verbs of the heart, (is the permissibility of cancellation (ilghāʾ)), that is, annulling their government, (when they are placed in the middle) between their two objects, as in “Zaydun ẓanantu qāʾimun” (Zayd, I supposed, is standing), (or are placed after) them, as in “Zaydun qāʾimun ẓanantu” (Zayd is standing, I supposed)."},
    {"type": "matn",
     "ar": "وإنما يجوز الإلغاء على التقديرين (لاستقلال الجزأين[[٣]]) الصالحين لأن يكونا مبتدأ وخبرا أو مفعولين[[٤]] لها (كلاما[[٥]] تاما[[٦]]) على تقدير الإلغاء[[٧]]، وجعلهما",
     "en": "Cancellation is permitted in both cases only (because the two parts), which are fit to be a subject and predicate or two objects of them, (are independent as a complete utterance (kalām)) on the supposition of cancellation; and making them…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة آل عمران: ١٨٠.",
     "en": "(Qurʾān, Sūrat Āl ʿImrān 3:180)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لفظا ومعنى.",
     "en": "In wording and in meaning."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بخلاف باب «أعطيت»؛ لأن مفعوليه ليسا بمستقلين لعدم صحة الحمل، فلا يجوز الإلغاء إذا توسطت أو تأخرت.",
     "en": "Unlike the class of “aʿṭaytu”, because its two objects are not independent, since predication [of one of the other] is not valid; so cancellation is not permitted when it is placed in the middle or after."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر الواو إلا أنه اختار، أو للتنبيه على أن صلاحيتهما للأمرين المذكورين على البدلية.",
     "en": "The apparent [choice] would be “and” (wāw), but he chose “or” to draw attention to the fact that their fitness for the two things mentioned is by way of alternation."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "حال أو تمييز.",
     "en": "A circumstantial (ḥāl) or a specifier (tamyīz)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "من غير ضم الفعل إليه، فيمتنعان عن التأثر عند ضعف العامل بالتأخير عن كليهما أو عن أحدهما.",
     "en": "Without adding the verb to it; so they resist being affected when the governing word (ʿāmil) is weakened by being placed after both of them or after one of them."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لكونهما حينئذ في معنى الظرف بخلاف تقدير العمل، فإنهما ليسا كلاما تاما؛ إذ المقصود نسبة الفعل إليهما بطريق الوقوع عليهما.",
     "en": "Because [the verb] is then in the sense of an adverbial; unlike the supposition of government, for then the two are not a complete utterance, since what is intended is the relation of the verb to them by way of its falling upon them."},
]
