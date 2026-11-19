# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 411 (printed ٤١٠)."""

PAGE_NUMBER = 411
PRINTED_PAGE = "٤١٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والعامل في «إذا» هذه معنى المفاجاة، وهو عامل لا يظهر قد استغنوا» at the foot of PDF p. 410.
    {"type": "matn",
     "ar": "عن إظهاره، لقوة ما فيه من الدلالة عليه، وأما الفاء، فهي للسببية[[١]]، فإن مفاجاة السبع مسببة عن الخروج.",
     "en": "…with expressing it, because of the strength of the indication of it contained [in the word]. As for the “fa”, it is causal, for coming upon the beast of prey is caused by the going out."},
    {"type": "matn",
     "ar": "قيل[[٢]]: والأقرب إلى التحقيق أنها للعطف من جهة المعنى، أي: «خرجت ففاجأت»، وحاصل المعنى: «خرجت ففاجأت زمان وقوف السبع»،",
     "en": "It has been said: closer to verification is that it is conjunctive in respect of meaning, that is, “kharajtu fa-fājaʾtu” (I went out and came upon); the upshot of the meaning is “I went out and came upon the time of the beast’s standing”,"},
    {"type": "matn",
     "ar": "كما هو مذهب الزجاج من أن «إذا» هذه زمانية، أو مكان وقوف السبع، كما ذهب إليه المبرد، فإنها عنده مكانية،",
     "en": "according to the doctrine of al-Zajjāj that this “idhā” is temporal; or “the place of the beast’s standing”, as al-Mubarrad held, for with him it is spatial."},
    {"type": "matn",
     "ar": "وقوله: «زمان وقوف السبع أو مكانه» مفعول فيه لـ«فاجأت» لا مفعول به، وإلا لم يبق «إذا» ظرفية[[٣]]، بل تصير اسمية،",
     "en": "His words “the time of the beast’s standing, or its place” are an adverbial object (mafʿūl fīhi) of “fājaʾtu”, not a direct object; otherwise “idhā” would not remain adverbial but would become a noun."},
    {"type": "matn",
     "ar": "بل المفعول به محذوف أي: فاجأت في زمان وقوف السبع أو مكانه إياه؛ أي: السبع.",
     "en": "Rather, the direct object is omitted, that is, “I came upon it, in the time of the beast’s standing or its place”; that is, [came upon] the beast."},
    {"type": "matn",
     "ar": "وقد يكون لمجرد الزمان، نحو: «أتيتك إذا احمر البسر» أي: وقت احمرار البسر.",
     "en": "It is sometimes for mere time, as in “ataytuka idhā iḥmarra al-busru” (I came to you when the unripe dates reddened), that is, at the time of the dates’ reddening."},
    {"type": "matn",
     "ar": "وقد يستعمل اسما مجردا عن معنى الظرفية في نحو: «إذا يقوم زيد إذا يقعد عمرو»، وقد سبقت إليه إشارة.",
     "en": "It is sometimes used as a noun stripped of the meaning of adverbiality, as in “idhā yaqūmu Zaydun idhā yaqʿudu ʿAmrun” (when Zayd stands is when ʿAmr sits); this has already been alluded to."},
    {"type": "matn",
     "ar": "(ومنها) أي: من الظروف المبنية («إذ») الكائنة (للماضي[[٤]]) وبناؤها لما مر في «حيث»، أو لكون وضعها وضع الحروف،",
     "en": "(And among them), that is, among the indeclinable adverbs, is (“idh”), which is (for the past). Its indeclinability is for the reason given for “ḥaythu”, or because its coinage is that of the particles."},
    {"type": "matn",
     "ar": "وقد تجيء للمستقبل[[٥]] كقوله تعالى: ﴿فسوف يعلمون. إذ الأغلال في أعناقهم﴾[[٦]].",
     "en": "It sometimes comes for the future, as in His words, the Exalted: “They will come to know, when the fetters are on their necks”."},

    {"type": "rule"},

    # ---------------- Footnote continued from the previous page ----------------
    # Continuation of fn. ٦ of PDF p. 410 («...وإن قدرت أنها الخبر فعاملها مستقر، كذا في»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "المغني. وعلى جميع التقادير «إذا» مقطوعة عن الإضافة،",
     "en": "…al-Mughnī. On all suppositions “idhā” is cut off from annexation;"},
    {"type": "pair",
     "ar": "وعلى تقدير كونه ظرف زمان يحتاج إلى تقدير المضاف إذا كان خبرا عن الجثة نحو: «خرجت فإذا السبع» أي: إذا حضور السبع.",
     "en": "and on the supposition that it is an adverb of time, an annexed word must be supposed when it is the khabar of a concrete entity, as in “kharajtu fa-idhā al-sabuʿu”, that is, “and then [was] the presence of the beast”."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "حذرا من لزوم عطف الاسمية على الفعلية.",
     "en": "To avoid having to conjoin a nominal sentence to a verbal one."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قائله الشيخ الرضي. ويؤيده وقوع «ثم» موقع الفاء في قوله تعالى: ﴿ثم إذا أنتم بشر تنتشرون﴾ (الروم: ٢٠).",
     "en": "The one who said it is Shaykh al-Raḍī. It is supported by “thumma” occurring in the place of “fa” in His words, the Exalted: “then, lo, you are human beings spreading out” (Qurʾān, Sūrat al-Rūm 30:20)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وقد سبق أنه قال الرضي: أنا لم أعثر على «إذا» مجردة عن معنى الظرفية،",
     "en": "It has preceded that al-Raḍī said: “I have not come across ‘idhā’ stripped of the meaning of adverbiality.”"},
    # REVIEW: printed «عدم بنائها ظرفية» (checked at 700 dpi); the context (matn «لم يبق «إذا» ظرفية») suggests «بقائها»; transcribed as printed.
    {"type": "pair",
     "ar": "ولا ينبغي أن يتوهم أنه أراد أن عدم بنائها ظرفية لا تصح في المقام؛ لأنها عدت من الظروف المبنية، فلا بد له من الظرفية؛",
     "en": "One should not imagine that he meant that its not remaining (lit. “not being built as”) adverbial is not valid here because it is counted among the indeclinable adverbs, so that it must be adverbial;"},
    {"type": "pair",
     "ar": "لأن «مذ ومنذ» قد عدا منه مع أنهما مبتدآن عند الجمهور.",
     "en": "for “mudh” and “mundhu” are counted among them, although according to the majority they are subjects (mubtadaʾ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قدر المتعلق معرفا باللام على أنه صفة رعاية لجزالة المعنى بخلاف النكرة، فإنها تكون حالا قيدا للعامل.",
     "en": "He supposed the governing word as definite with the article, as a qualifier, for the sake of the soundness of the meaning; unlike the indefinite, which would be a ḥāl restricting the governor."},
    {"type": "pair",
     "ar": "وأما تقدير المبتدأ وإن كان صحيحا، لكن غير ممدوح.",
     "en": "As for supposing a subject, though it is correct, it is not commendable."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بتجرده عن الماضي، واستعمال المطلق في المقيد.",
     "en": "By its being stripped of the past, and by the use of the unrestricted for the restricted."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة غافر: ٧٠-٧١.",
     "en": "Qurʾān, Sūrat Ghāfir 40:70–71."},
    # The following paragraph is printed flush, without a number, after fn. ٦; it continues the discussion of «إذ» for the future and runs on to PDF p. 412.
    # REVIEW: printed «لتنزيل المستقل» (sic, for «المستقبل»); transcribed as printed.
    {"type": "pair",
     "ar": "وذلك لتنزيل المستقل منزلة الماضي لكونه من أخبار من عنده المستقبل كالماضي، فتأمل.",
     "en": "That is because the future is treated as the past, since it is among the reports of One with whom the future is like the past. Reflect."},
    {"type": "pair",
     "ar": "ويمكن منع كونه في الآية للمستقبل لجواز أن يكون لمطلق الوقت كأنه قيل: فسوف يعلمون زمان الأغلال",
     "en": "One may deny that it is for the future in the verse, since it may be for time in general, as though it were said: “they will come to know the time of the fetters…"},
]
