# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 467 (printed ٤٦٦)."""

PAGE_NUMBER = 467
PRINTED_PAGE = "٤٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… (مجرد)» at the foot of PDF p. 466 (mid-sentence).
    {"type": "matn",
     "ar": "لا مزيد فيه (ليمكن بناء «أفعل» و«فعلى» منه)؛",
     "en": "…not augmented, (so that forming “afʿal” and “fuʿlā” from it is possible);"},
    {"type": "matn",
     "ar": "إذ البناء من الرباعي والثلاثي المزيد فيه من المحافظة على تمام حروفه متعذر؛ لأن هذه الصيغة لا تتسع الزيادة على ثلاثة أحرف،",
     "en": "for forming it from the quadriliteral and the augmented triliteral while preserving all their letters is impossible, because this form does not accommodate more than three letters;"},
    {"type": "matn",
     "ar": "ومع إسقاط بعضها يلزم الالتباس، فإنه لا يعلم أنه مشتق من الرباعي، أو الثلاثي المجرد، أو المزيد فيه،",
     "en": "and if some of them are dropped, confusion follows, for it would not be known whether it is derived from the quadriliteral, the bare triliteral, or the augmented;"},
    {"type": "matn",
     "ar": "فإن هذه الحروف الثلاثة تحتمل أن تكون تمام حروف ثلاثي مجرد، أو بعض حروف رباعي مجرد كلها أصول، أو تكون من حروف المزيد فيه إما من أصوله، أو من زوائده، أو ممتزجا منهما،",
     "en": "for these three letters may be all the letters of a bare triliteral, or some of the letters of a bare quadriliteral, all of them radical, or they may be among the letters of the augmented verb, either from its radicals, or from its augments, or a mixture of the two;"},
    {"type": "matn",
     "ar": "فلا يتبين ما هو المشتق منه، فلا يتعين المعنى",
     "en": "so what it is derived from would not be clear, and the meaning would not be determined;"},
    {"type": "matn",
     "ar": "(ليس بلون) أي: من ثلاثي مجرد ليس بلون (ولا عيب[[١]]) ظاهري",
     "en": "(not a colour), that is, from a bare triliteral that is not a colour, (nor a defect), an outward one,"},
    {"type": "matn",
     "ar": "(لأن منهما) اشتق («أفعل» لغيره) أي: لغير اسم التفضيل كـ«أحمر وأعور»،",
     "en": "(because from these two) is derived (“afʿal” for something else), that is, for other than the elative, as in “aḥmar” (red) and “aʿwar” (one-eyed);"},
    {"type": "matn",
     "ar": "فلو اشتق اسم التفضيل أيضا منهما لالتبس أن المراد: ذو حمرة وعور[[٢]] أو زائدة الحمرة أو العور،",
     "en": "so if the elative were also derived from them, it would be unclear whether what is meant is “possessing redness” or “one-eyedness”, or “exceeding in redness” or “one-eyedness”."},
    {"type": "matn",
     "ar": "وهذا التعليل إنما يتم إذا بين أن «أفعل الصفة» مقدم بناؤه على «أفعل التفضيل»، وهو كذلك؛",
     "en": "This reasoning is complete only if it is shown that the formation of “afʿal” of the adjective precedes “afʿal” of the elative; and it is so,"},
    {"type": "matn",
     "ar": "لأن ما يدل على ثبوت مطلق الصفة مقدم بالطبع على ما يدل على زيادة على الآخر في الصفة، والأولى موافقة الوضع الطبع",
     "en": "because what signifies the mere presence of a quality is by nature prior to what signifies excess over another in the quality, and it is more fitting that coinage accord with nature;"},
    {"type": "matn",
     "ar": "(مثل: «زيد أفضل الناس»)، فإن الأفضل اشتق من ثلاثي مجرد ليس بلون ولا عيب، وهو الفضل.",
     "en": "(as in “Zaydun afḍalu l-nās” (Zayd is the most excellent of people)), for “afḍal” is derived from a bare triliteral that is neither a colour nor a defect, namely “faḍl” (excellence)."},
    {"type": "matn",
     "ar": "(فإن قصد غيره) أي: غير الثلاثي المجرد[[٣]] بأن يراد أن يدل على أن لأحد زيادة فيه على غيره",
     "en": "(If another is intended), that is, other than the bare triliteral, in that it is meant to signify that someone has an excess in it over another,"},
    {"type": "matn",
     "ar": "(توصل إليه) أي: إلى غير الثلاثي المجرد (بـ«أشد» ونحوه، مثل: «هو أشد منه استخراجا») مثال للثلاثي المزيد فيه",
     "en": "(it is reached), that is, other than the bare triliteral, (by means of “ashadd” (more intense) and the like, as in “huwa ashaddu minhu istikhrājan” (he is more intense than him in extracting)), an example of the augmented triliteral,"},
    {"type": "matn",
     "ar": "(و«بياضا») مثال للون (وعمى) مثال للعيب،",
     "en": "(and “bayāḍan” (in whiteness)), an example of colour, (and “ʿaman” (in blindness)), an example of defect."},
    {"type": "matn",
     "ar": "وحيث قيدنا العيب بالظاهري لا يرد نحو: «أجهل وأبلد»،",
     "en": "Since we restricted the defect to the outward, the like of “ajhal” (more ignorant) and “ablad” (duller) does not count against it;"},
    {"type": "matn",
     "ar": "ولكن يرد أنه صح على هذا التقدير اشتقاق «أحمق» على معنى التفضيل، فإنه لا فرق بين الجهل والبلادة",
     "en": "but it may be objected that on this assumption deriving “aḥmaq” (more foolish) in the elative sense would be valid, for there is no difference between ignorance and dullness…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 466 (printed ٤٦٥), note ٨ ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "والنقصان، فلا يقال: الشمس أغرب وأطلع اليوم فمستغنى عنه بقوله: بزيادة على غيره، فإن الزيادة إنما تتصور فيما يقبلها.",
     "en": "…and deficiency, so that one does not say “the sun sets more” or “rises more today”, this is dispensed with by his words “by way of excess over another”, for excess is conceivable only in what admits it."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ينبغي أن يقول: ولا حلية؛ لأنه لا يشتق من البلج بمعنى كون الحاجبين غير متصلين أبلج للتفضيل بل للصفة.",
     "en": "He ought to say “nor a physical feature (ḥilya)”, because from “balaj”, meaning the eyebrows’ not being joined, “ablaj” is derived not as an elative but as an adjective."},
    {"type": "pair",
     "ar": "قال الكوفيون: يجيء من البياض والسواد اللذين هما أصل الألوان. وقال البصريون: ما جاء منهما شاذ.",
     "en": "The Kūfans said: it comes from whiteness and blackness, which are the root of colours. The Baṣrans said: what comes from them is anomalous."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «ذهاب حسن إحدى العينين»; one would expect «حس» (sense, sight). Transcribed as printed.
    {"type": "pair",
     "ar": "في القاموس: العور: كالفرس ذهاب حسن إحدى العينين.",
     "en": "In al-Qāmūs: “al-ʿawar”, on the pattern of al-faras, is the loss of the soundness of one of the two eyes."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اللام للعهد أي: غير الثلاثي المجرد المعهود أي: الموصوف بما ليس بلون ولا عيب،",
     "en": "The article denotes prior reference, that is, other than the aforementioned bare triliteral, that is, the one described as being neither colour nor defect;"},
    {"type": "pair",
     "ar": "فلا يرد أن مرجع الضمير ليس مجرد الثلاثي المجرد بل أخص منه.",
     "en": "so it cannot be objected that the referent of the pronoun is not the bare triliteral as such but something more specific than it."},
]
