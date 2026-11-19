# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 412 (printed ٤١١)."""

PAGE_NUMBER = 412
PRINTED_PAGE = "٤١١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «وقد تجيء للمستقبل كقوله تعالى: ﴿فسوف يعلمون. إذ الأغلال في أعناقهم﴾.» at the foot of PDF p. 411 (new sentence).
    {"type": "matn",
     "ar": "(ويقع بعدها الجملتان) الاسمية والفعلية[[١]] لعدم اشتمالها على معنى الشرط المقتضي اختصاصها بالفعلية، مثل: «كان ذلك إذ زيد قائم، وإذ قام زيد».",
     "en": "(And both kinds of sentence occur after it), the nominal and the verbal, because it does not contain the meaning of condition, which would require it to be restricted to the verbal; as in “kāna dhālika idh Zaydun qāʾimun” (that was when Zayd was standing) and “idh qāma Zaydun” (when Zayd stood)."},
    {"type": "matn",
     "ar": "وقد يجيء للمفاجأة، نحو: «خرجت فإذ زيد قائم»[[٢]]، ولقلة مجيئها لم يذكرها المصنف.",
     "en": "It sometimes comes for surprise, as in “kharajtu fa-idh Zaydun qāʾimun” (I went out, and there was Zayd standing); because this occurs rarely, the author did not mention it."},
    {"type": "matn",
     "ar": "(ومنها: «أين» و«أنى») فهما (للمكان[[٣]] استفهاما وشرطا) أي: حال كونهما للاستفهام والشرط[[٤]]،",
     "en": "(And among them are “ayna” and “annā”); they are (for place, interrogatively and conditionally), that is, when they are for interrogation and condition."},
    {"type": "matn",
     "ar": "وبناؤهما لتضمنهما حرف الاستفهام أو الشرط، نحو: «أين زيد؟ وأين تكن أكن، وأنى زيد؟ وأنى تجلس أجلس».",
     "en": "Their indeclinability is because they contain [the meaning of] the interrogative or conditional particle, as in “ayna Zaydun?” (where is Zayd?), “ayna takun akun” (wherever you are, I shall be), “annā Zaydun?” (where is Zayd?) and “annā tajlis ajlis” (wherever you sit, I shall sit)."},
    # REVIEW: the first example is printed «أني زيد؟» (with dotted yāʾ), beside «أنى القتال؟»; transcribed as printed.
    {"type": "matn",
     "ar": "وقد جاء «أني زيد؟» بمعنى: كيف، و«أنى القتال؟» بمعنى: متى[[٥]].",
     "en": "“Annā Zaydun?” has occurred in the sense of “kayfa” (how is Zayd?), and “annā al-qitālu?” in the sense of “matā” (when is the fighting?)."},
    {"type": "matn",
     "ar": "(و) منها: («متى» للزمان فيهما) أي: في الاستفهام والشرط، نحو: «متى القتال، ومتى تخرج أخرج».",
     "en": "(And) among them is (“matā”, for time in both), that is, in interrogation and condition, as in “matā al-qitālu?” (when is the fighting?) and “matā takhruj akhruj” (whenever you go out, I shall go out)."},
    {"type": "matn",
     "ar": "(و) منها: («أيان» للزمان استفهاما[[٦]]) مثل: «متى» نحو: ﴿أيان يوم الدين﴾[[٧]]،",
     "en": "(And) among them is (“ayyāna”, for time, interrogatively), like “matā”, as in: “When is the Day of Judgement?”"},
    {"type": "matn",
     "ar": "والفرق بينهما أن «أيان» مختص بالأمور العظام وبالمستقبل، فلا يقال: «أيان يوم قيام زيد؟» و«أيان قدم الحاج؟» بخلاف «متى» فإنه غير مختص بهما، والمشهور فتح",
     "en": "The difference between them is that “ayyāna” is restricted to momentous matters and to the future; so one does not say “ayyāna yawmu qiyāmi Zaydin?” (when is the day of Zayd’s standing?) or “ayyāna qadima al-ḥājju?” (when did the pilgrim arrive?); unlike “matā”, which is not restricted to them. The well-known [reading] is with fatḥa…"},

    {"type": "rule"},

    # ---------------- Footnote continued from the previous page ----------------
    # Continuation of the unnumbered paragraph after fn. ٦ of PDF p. 411 («...كأنه قيل: فسوف يعلمون زمان الأغلال»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "في أعناقهم، فهم كونه مستقبلا بقرينة فسوف يعلمون.",
     "en": "…on their necks”; its being future is understood from the indication of “they will come to know”."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "التي فعلها ماض لفظا ومعنى أو معنى فقط.",
     "en": "[The verbal sentence] whose verb is past in form and meaning, or in meaning only."},
    {"type": "pair",
     "ar": "وقد اجتمعت الثلاثة في قوله تعالى: ﴿إلا تنصروه فقد نصره الله إذ أخرجه الذين كفروا ثاني اثنين إذ هما في الغار إذ يقول لصاحبه﴾ (التوبة: ٤٠).",
     "en": "All three come together in His words, the Exalted: “If you do not help him, Allah has already helped him when those who disbelieved drove him out, the second of two, when the two were in the cave, when he said to his companion” (Qurʾān, Sūrat al-Tawba 9:40)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "في الرضي: والأغلب مجيء «إذ» في جواب «بينما»، و«إذا» في جواب «بيننا»،",
     "en": "In al-Raḍī: “idh” mostly comes in the answer to “baynamā”, and “idhā” in the answer to “baynanā”."},
    # REVIEW: printed «في جواب «بيننا»» (for «بينا»?); transcribed as printed.
    {"type": "pair",
     "ar": "ولا يجيء بعد «إذ» المفاجأة إلا الفعل الماضي وبعد «إذا» المفاجأة إلا الاسمية.",
     "en": "After “idh” of surprise only the past verb comes, and after “idhā” of surprise only the nominal sentence."},
    {"type": "pair",
     "ar": "وقد يجيء «إذ» للمفاجأة في غير جواب «بينما وبيننا» نحو قولك: كنت واقفا إذ جاءني عمرو",
     "en": "“Idh” sometimes comes for surprise outside the answer to “baynamā” and “baynanā”, as in your saying: “I was standing when ʿAmr came to me.”"},
    # REVIEW: «وفي الباب وهما يعني» printed as such; the sense is elliptical.
    {"type": "pair",
     "ar": "وفي الباب وهما يعني: «إذ وإذا» كائنتين للمفاجأة، ويختص الأولى بالفعلية والثانية بالاسمية إيقاعا للمخالفة بينهما أو بين الزمانية.",
     "en": "And in the chapter, the two—meaning “idh” and “idhā”—being for surprise, the first is restricted to the verbal sentence and the second to the nominal, to establish a difference between them, or between [them and] the temporal ones."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قدر المبتدأ بالفاء بقرينة اشتمال الحكم على التفصيل، أعني: استفهاما وشرطا وجعله صفة وإن كان صحيحا، لكن جعله حكما مستقلا ألصق بالقلب.",
     "en": "He supposed the subject with “fa” on the evidence that the ruling contains a breakdown, namely “interrogatively and conditionally”; making it a qualifier is correct, but making it an independent ruling sits closer to the heart."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كأنه جعل استفهاما حالا منهما مسامحة بتقدير ذاتي استفهام؛ لأن الاستفهام معناهما.",
     "en": "It is as if he made “interrogatively” a ḥāl from them, loosely, by supposing “possessing interrogation”, since interrogation is their meaning."},
    {"type": "pair",
     "ar": "والأظهر أن المصنف جعله ظرفا يدل عليه.",
     "en": "The more evident view is that the author made it an adverb indicating it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولا يجيء بمعنى «متى وكيف» إلا وبعده فعل.",
     "en": "It comes in the sense of “matā” and “kayfa” only when a verb follows it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وكتب الجمهور ساكتة عن كونها للشرط. وأجاز ذلك بعض المتأخرين وهو غير مسموع،",
     "en": "The books of the majority are silent about its being conditional. Some later [grammarians] allowed it, but it is unattested."},
    # REVIEW: this sentence on «كيف» is printed under fn. ٦ (on «أيان»); its link to the note is unclear; transcribed as printed.
    {"type": "pair",
     "ar": "والاستفهام بـ«كيف» عن النكرة، فلا يكون جوابه إلا نكرة، فلا يجوز بالتركيب الصحيح في جواب «كيف زيد؟».",
     "en": "Interrogation with “kayfa” is about an indefinite, so its answer can only be indefinite; so [the definite] is not permitted, in correct construction, in the answer to “kayfa Zaydun?” (how is Zayd?)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة الذريات: ١٢.",
     "en": "Qurʾān, Sūrat al-Dhāriyāt 51:12."},
]
