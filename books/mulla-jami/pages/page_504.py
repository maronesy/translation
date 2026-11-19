# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 504 (printed ٥٠٣)."""

PAGE_NUMBER = 504
PRINTED_PAGE = "٥٠٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وإنما كانت مقدرة:» at the foot of PDF p. 503 (mid-sentence).
    {"type": "matn",
     "ar": "(بعد الأمر[[١]]) نحو: «زرني أكرمك» أي: إن تزرني أكرمك.",
     "en": "…(after a command), as in “zurnī ukrimka” (visit me and I will honour you), that is, “in tazurnī ukrimka” (if you visit me, I will honour you);"},
    {"type": "matn",
     "ar": "(والنهي) نحو: «لا تفعل الشر يكن خيرا لك» أي: إن لم تفعله يكن خيرا لك.",
     "en": "(and a prohibition), as in “lā tafʿal al-sharra yakun khayran laka” (do not do evil, and it will be better for you), that is, “if you do not do it, it will be better for you”;"},
    {"type": "matn",
     "ar": "(والاستفهام) نحو: «هل عندكم ماء أشربه»؛ لأن المعنى: إن يكن عندكم ماء أشربه.",
     "en": "(and a question), as in “hal ʿindakum māʾun ashrabhu” (have you water, that I may drink it?), because the meaning is “if you have water, I will drink it”;"},
    {"type": "matn",
     "ar": "(والتمني) نحو: «ليت لي مالا أنفقه»؛ لأن المعنى: إن يكن لي مال أنفقه.",
     "en": "(and a wish), as in “layta lī mālan unfiqhu” (would that I had wealth, that I might spend it), because the meaning is “if I have wealth, I will spend it”;"},
    {"type": "matn",
     "ar": "(والعرض) نحو: «ألا تنزل تصب خيرا» أي: إن تنزل تصب خيرا",
     "en": "(and a proposal), as in “a-lā tanzilu tuṣib khayran” (will you not alight, and you will meet with good?), that is, “if you alight, you will meet with good”,"},
    {"type": "matn",
     "ar": "(إذا) كان المضارع الواقع بعد هذه الأشياء الخمسة صالحا لأن يكون مسببا لما تقدم و(قصد السببية) أي: سببية ما تقدم له،",
     "en": "(when) the muḍāriʿ occurring after these five things is fit to be an effect of what precedes, and (causality is intended), that is, the causality of what precedes for it;"},
    {"type": "matn",
     "ar": "فحينئذ يقدر «إن» مع مضارع يؤخذ مما تقدم، ويجعل المضارع الواقع بعد هذه الأشياء مجزوما به،",
     "en": "for then “in” is supposed together with a muḍāriʿ taken from what precedes, and the muḍāriʿ occurring after these things is made jussive by it."},
    {"type": "matn",
     "ar": "وإنما اختص تقدير «إن» بما بعد هذه الأشياء؛ لأنها تدل على الطلب،",
     "en": "The supposing of “in” is restricted to what comes after these things only because they indicate a request,"},
    {"type": "matn",
     "ar": "والطلب غالبا يتعلق بمطلوب يترتب عليه فائدة يكون ذلك المطلوب سببا لها[[٢]] وهي مسببة له،",
     "en": "and a request is mostly connected with something requested upon which a benefit follows, that requested thing being its cause and the benefit its effect;"},
    {"type": "matn",
     "ar": "فإذا كان المضارع الواقع بعدها تلك الفائدة وقصد سببية الفعل المطلوب بتلك الأشياء لها قدر «إن» مع ذلك الفعل ويجعل المضارع الواقع بعدها جزاء فينجزم بها",
     "en": "so when the muḍāriʿ occurring after them is that benefit, and the causality for it of the act requested by those things is intended, “in” is supposed with that act, and the muḍāriʿ occurring after them is made a requital and is put in the jussive by it,"},
    {"type": "matn",
     "ar": "(نحو: «أسلم تدخل الجنة») فإن المطلوب ب«أسلم» هو الإسلام، وهو مطلوب فائدته دخول الجنة، فهو سبب لها،",
     "en": "(as in “aslim tadkhuli al-jannata” (embrace Islam and you will enter Paradise)): what is requested by “aslim” is embracing Islam, a requested thing whose benefit is entering Paradise, so it is its cause;"},
    {"type": "matn",
     "ar": "وقصد أداء تلك السببية، فقدر «إن» مع الفعل المأخوذ من «أسلم» وجعل «تدخل الجنة» جزاء له، فقيل: «إن تسلم تدخل الجنة»",
     "en": "and conveying that causality was intended; so “in” was supposed with the verb taken from “aslim”, and “tadkhul al-jannata” was made its requital, and it was said “in tuslim tadkhul al-jannata” (if you embrace Islam, you will enter Paradise)."},
    {"type": "matn",
     "ar": "(و) نحو: («لا تكفر تدخل الجنة») أي: «إن لا تكفر تدخل الجنة»؛ لأن النهي قرينة للفعل المنفي لا المثبت.",
     "en": "(And) as in (“lā takfur tadkhuli al-jannata” (do not disbelieve, and you will enter Paradise)), that is, “in lā takfur tadkhul al-jannata” (if you do not disbelieve, you will enter Paradise), because the prohibition is an indication of the negated verb, not the affirmed."},
    {"type": "matn",
     "ar": "(ولهذا امتنع «لا تكفر تدخل النار») عند الجمهور (خلافا للكسائي) فإنه لا يمتنع ذلك عنده،",
     "en": "(For this reason “lā takfur tadkhuli al-nāra” (do not disbelieve, and you will enter the Fire) is not allowed) according to the majority, (contrary to al-Kisāʾī), for according to him it is not disallowed."},
    # REVIEW: the opening guillemet before «إن لا تكفر تدخل النار» has no printed closing guillemet; transcribed as printed.
    {"type": "matn",
     "ar": "فامتناعه عند الجمهور (لأن التقدير) على ما عرفت[[٣]] («إن لا تكفر تدخل النار) وهو ظاهر الفساد،",
     "en": "Its disallowance according to the majority is (because the supposed form), as you have learned, (is “in lā takfur tadkhul al-nāra” (if you do not disbelieve, you will enter the Fire)), which is evidently corrupt."},
    {"type": "matn",
     "ar": "وأما عدم امتناعه عند الكسائي، فلأنه يقول: معناه بحسب العرف: «إن تكفر تدخل النار»،",
     "en": "As for its not being disallowed according to al-Kisāʾī, that is because he says: its meaning according to common usage (ʿurf) is “in takfur tadkhul al-nāra” (if you disbelieve, you will enter the Fire);"},
    {"type": "matn",
     "ar": "فالعرف في هذه المواضع قرينة الشرط المثبت، والعرف قرينة قوية.",
     "en": "so in these places common usage is an indication of the affirmed condition, and common usage is a strong indication."},
    {"type": "matn",
     "ar": "هذا إذا قصدت السببية. وأما إذا لم تقصد لم يجز الجزم قطعا، بل يجب أن يرفع",
     "en": "This is when causality is intended. When it is not intended, the jussive is not permitted at all; rather, it must be put in the nominative…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اعلم أن كل ما يجاب بالفاء، فينتصب المضارع بعدها يصح أن يجاب بمضارع مجزوم إلا النفي.",
     "en": "Know that everything that may be answered with the fāʾ, after which the muḍāriʿ is put in the accusative, may validly be answered with a jussive muḍāriʿ, except negation."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ليتحقق معنى الشرط.",
     "en": "So that the sense of condition is realized."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: يجب أن يكون المقدر مثل المظهر إثباتا ونفيا.",
     "en": "That is, what is supposed must be like what is expressed, in affirmation and negation."},
    {"type": "pair",
     "ar": "وأما قولهم في العرض: ألا تنزل بنا تصب خيرا أي: إن تنزل فلأن كلمة العرض همزة إنكارية دخلت على حرف النفي، فتفيد الإثبات.",
     "en": "As for their saying in a proposal “a-lā tanzilu binā tuṣib khayran” (will you not alight with us, and you will meet with good?), that is, “if you alight”: that is because the word of proposal is a hamza of denial entering upon the particle of negation, so it yields affirmation."},
]
