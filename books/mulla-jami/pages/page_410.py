# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 410 (printed ٤٠٩)."""

PAGE_NUMBER = 410
PRINTED_PAGE = "٤٠٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وفيها) أي: في «إذا» (معنى الشرط) وهو ترتب مضمون جملة على أخرى،» at the foot of PDF p. 409.
    {"type": "matn",
     "ar": "فتضمنت حرف الشرط، فهذا علة أخرى لبنائها",
     "en": "…so it contains [the meaning of] the conditional particle; and this is another cause of its indeclinability."},
    {"type": "matn",
     "ar": "(فلذلك) أي: لكون معنى الشرط فيها[[١]] (اختير) أي: جعل مختارا (بعدها الفعل) لمناسبة الفعل الشرط،",
     "en": "(For this reason), that is, because the meaning of condition is in it, (the verb is preferred after it), that is, made the preferred option, because the verb suits the condition;"},
    {"type": "matn",
     "ar": "وجوز الاسم أيضا على الوجه الغير المختار، لعدم تأصلها في الشرط، مثل: «إن ولو».",
     "en": "and the noun too is allowed, as the non-preferred option, because it is not rooted in condition as “in” and “law” are."},
    {"type": "matn",
     "ar": "(وقد تكون) أي: إذا (للمفاجأة[[٢]]) مجردة عن الشرط،",
     "en": "(And it is sometimes), that is, “idhā”, (for surprise (mufājaʾa)), stripped of condition."},
    {"type": "matn",
     "ar": "يقال: فاجأه الأمر مفاجأة من قولهم: فجئته فجاءة -بالضم والمد[[٣]]- إذا لقيته وأنت لا تشعر به",
     "en": "One says “fājaʾahu al-amru mufājaʾatan” (the matter came upon him by surprise), from their saying “fajiʾtuhu fujāʾatan”, with ḍamma and lengthening, when you meet him without being aware of him."},
    {"type": "matn",
     "ar": "(فيلزم[[٤]] المبتدأ بعدها) فرقا بين «إذا» هذه، وبين «إذا» الشرطية،",
     "en": "(So the mubtadaʾ necessarily follows it), to distinguish this “idhā” from conditional “idhā”."},
    {"type": "matn",
     "ar": "والمراد بلزوم المبتدأ غلبة وقوعه بعدها[[٥]]، فلا ينافي ما سبق من عدم وجوب الرفع بعدها في باب الإضمار على شريطة التفسير",
     "en": "What is meant by the mubtadaʾ’s being necessary is that it predominantly occurs after it; so this does not contradict what preceded, that the nominative is not obligatory after it in the chapter of suppression subject to explication (al-iḍmār ʿalā sharīṭat al-tafsīr)."},
    {"type": "matn",
     "ar": "نحو: «خرجت فإذا السبع» أي: «فإذا السبع واقف أو حاضر» على حذف الخبر،",
     "en": "Example: “kharajtu fa-idhā al-sabuʿu” (I went out, and there was the beast of prey), that is, “and there the beast of prey was standing” or “present”, with the khabar omitted."},
    {"type": "matn",
     "ar": "والعامل في «إذا» هذه[[٦]] معنى المفاجاة، وهو عامل لا يظهر قد استغنوا",
     "en": "The governor in this “idhā” is the meaning of surprise, which is a governor that is never expressed; they have dispensed…"},

    {"type": "rule"},

    # ---------------- Footnote continued from the previous page ----------------
    # Continuation of fn. ٨ of PDF p. 409 («...كقوله تعالى: ﴿وإذا ما غضبوا هم»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "يغفرون﴾ (الشورى: ٣٧)، وقوله تعالى: ﴿والذين إذا أصابهم البغي هم ينتصرون﴾ (الشورى: ٣٩).",
     "en": "…forgive” (Qurʾān, Sūrat al-Shūrā 42:37), and His words, the Exalted: “And those who, when tyranny befalls them, defend themselves” (Qurʾān, Sūrat al-Shūrā 42:39)."},
    # REVIEW: the hemistich is printed «إذ الخصم أبزى مائل الرأس أنكب» (with «إذ», not «إذا», though the note is about «إذا»); transcribed as printed.
    {"type": "pair",
     "ar": "ويجيء جملتها الشرطية اسمية على سبيل الشذوذ، نحو قوله: إذ الخصم أبزى مائل الرأس أنكب،",
     "en": "Its condition clause comes as a nominal sentence by way of anomaly, as in the poet’s words: “when the adversary is haughty, with head tilted, turning aside”."},
    {"type": "pair",
     "ar": "ولا يعمل في المضارع الواقع بعدها، والمصنف أشار إلى ضعف معنى الشرط فيها بقوله: وفيها معنى الشرط، تأمل.",
     "en": "It does not govern the imperfect that follows it; and the author indicated the weakness of the meaning of condition in it by his words “and in it is the meaning of condition”. Reflect."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأولى أن يراد بقوله: ولذلك ولكون معنى الشرط فيها غير قوية كما نبه عليه بقوله: «وفيها معنى الشرط» قوله: اختير بعدها الفعل، ولم يجب كما في «متى» وأخواتها،",
     "en": "It is better that by his words “for this reason” be meant: and because the meaning of condition in it is not strong, as he indicated by his words “and in it is the meaning of condition”, [he said] “the verb is preferred after it”, and it is not obligatory as with “matā” and its sisters."},
    {"type": "pair",
     "ar": "والذي يستفاد من الرضي أن مجيء الاسم بعدها شاذ.",
     "en": "What is gathered from al-Raḍī is that a noun’s coming after it is anomalous."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولا يحتاج إلى جواب، ولا يقع في الابتداء، ومعناها الحال لا الاستقبال، والأكثر توافقه بحال أنت فيها،",
     "en": "It needs no answering clause and does not occur at the beginning [of speech]; its meaning is the present, not the future, and mostly it coincides with a state you are in."},
    {"type": "pair",
     "ar": "قال: وقد تراخى كقوله تعالى: ﴿ومن آياته أن خلقكم من تراب ثم إذا أنتم بشر تنتشرون﴾ (الروم: ٢٠)،",
     "en": "He said: and it may be delayed, as in His words, the Exalted: “And among His signs is that He created you from dust; then, lo, you are human beings spreading out” (Qurʾān, Sūrat al-Rūm 30:20)."},
    {"type": "pair",
     "ar": "وهو حرف عند الكوفيين والأخفش. ولا محل لها من الإعراب، وظرف عند غيرهم مكان أو زمان كما سيجيء.",
     "en": "It is a particle according to the Kūfans and al-Akhfash, and has no place in inflection; according to others it is an adverb of place or time, as will come."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: من حد سمع ومنع، وإنما قيد الفجأة بالضم والمد؛ لأن الفجاءة كالضرة مصدر فجأه من الحدين بمعنى أخذه بغتة.",
     "en": "He means: of the pattern of samiʿa and manaʿa. He specified fujāʾa with ḍamma and lengthening only because fajʾa, like ḍarba, is the maṣdar of fajaʾahu in both patterns, in the sense of “took him suddenly”."},
    # REVIEW: printed «قيد الفجأة» and «لأن الفجاءة كالضرة»; the two spellings appear reversed relative to the argument (ḍamma and madd belong to «الفجاءة»); transcribed as printed.

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: على أحد الأقوال، فإن فيه ثلاثة أقوال: الأول: اختصاصها بالاسمية. والثاني: جواز دخولها على الاسمية والفعلية.",
     "en": "That is, on one of the views; for there are three views on it. The first: it is restricted to the nominal sentence. The second: it may enter both the nominal and the verbal sentence."},
    {"type": "pair",
     "ar": "والثالث: إذا قرنت بـ«قد» يجوز دخولها عليه، وإن لم تقترن فيمتنع، كذا في التحفة.",
     "en": "The third: when [the verb] is joined with “qad”, it may enter it, and if it is not so joined it may not; so in al-Tuḥfa."},
    {"type": "pair",
     "ar": "فحينئذ لا تنافي بين هذا وبين ما سبق في شريطة التفسير، ولا حاجة إلى تكلف حمل اللزوم على الغلبة كما ذكره الشارح، ولا إلى تخصيص اللزوم بغير باب شريطة التفسير.",
     "en": "Then there is no contradiction between this and what preceded on explication, and no need for the strained interpretation of “necessity” as “predominance”, as the commentator stated, nor for restricting the necessity to what is outside the chapter of explication."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا بعيد. وقيل: لزوم المبتدأ في غير باب الإضمار على شريطة التفسير.",
     "en": "This is far-fetched. It has been said: the mubtadaʾ is necessary outside the chapter of suppression subject to explication."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: ذهب إليه الزمخشري وابن الحاجب، وعند غيرهم الخبر المذكور في نحو: «خرجت فإذا زيد جالس» أو المقدر في نحو: «فإذا السبع» أي: حاضر،",
     "en": "That is, al-Zamakhsharī and Ibn al-Ḥājib held this; according to others [the governor] is the khabar, expressed as in “kharajtu fa-idhā Zaydun jālisun” (I went out, and there was Zayd sitting), or supposed as in “fa-idhā al-sabuʿu”, that is, “present”."},
    # Footnote ٦ runs on to PDF p. 411.
    {"type": "pair",
     "ar": "وإن قدرت أنها الخبر فعاملها مستقر، كذا في",
     "en": "If you suppose that it is the khabar, its governor is [the omitted] mustaqirr (being settled); so in…"},
]
