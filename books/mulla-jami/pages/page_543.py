# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 543 (printed ٥٤٢)."""

PAGE_NUMBER = 543
PRINTED_PAGE = "٥٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فلا يقال: «حتاه» كما» at the foot of PDF p. 542 (mid-sentence).
    {"type": "matn",
     "ar": "يقال: «إليه»[[١]]؛ لأنها لو دخلت على المضمر لالتبس الضمير المجرور بالمنصوب لجواز وقوعهما بعدها، أي: بعد «حتى».",
     "en": "…one says “ilayhi”; because if it entered upon a pronoun, the genitive pronoun would be confused with the accusative one, since both may occur after it, that is, after “ḥattā”."},
    {"type": "matn",
     "ar": "(خلافا للمبرد) فإنه جوز دخوله على المضمر مستدلا بما وقع في بعض أشعار العرب على سبيل الندرة[[٢]].",
     "en": "(Contrary to al-Mubarrad), for he allowed its entry upon a pronoun, adducing as evidence what occurs in some poems of the Arabs by way of rarity."},
    {"type": "matn",
     "ar": "والجمهور يحكمون بشذوذه[[٣]]، فلا يجوزونه قياسا.",
     "en": "The majority judge it anomalous (shādhdh), and so do not allow it by analogy (qiyās)."},

    {"type": "section", "ar": "[في]",
     "en": "Fī"},

    {"type": "matn",
     "ar": "(وفي):",
     "en": "(And fī [is]):"},
    {"type": "matn",
     "ar": "١-(للظرفية) أي: لظرفية مدخوله لشيء حقيقة، نحو: «الماء في الكوز»، أو مجازا، نحو: «النجاة في الصدق».",
     "en": "1. (for containment (ẓarfiyya)), that is, for what it enters upon being a container of something, literally, as in “the water is in the jug”, or figuratively, as in “salvation is in truthfulness”."},
    {"type": "matn",
     "ar": "٢-(وبمعنى «على» قليلا) كقوله تعالى: ﴿ولأصلبنكم في جذوع[[٤]] النخل﴾[[٥]]، أي: على جذوع النخل.",
     "en": "2. (And in the sense of “ʿalā” (on), rarely), as in His words, the Exalted: “and I will surely crucify you in (fī) the trunks of the palm trees”, that is, on the trunks of the palm trees."},

    {"type": "section", "ar": "[الباء]",
     "en": "Al-Bāʾ"},

    {"type": "matn",
     "ar": "(والباء):",
     "en": "(And the bāʾ [is]):"},
    {"type": "matn",
     "ar": "١-(للإلصاق) أي: لإفادة لصوق أمر إلى مجرور الباء، هذه كما ترى في: «مررت بزيد»، فإن الباء فيه يفيد لصوق مرورك بزيد، أي: بمكان يقرب منه.",
     "en": "1. (for adhesion (ilṣāq)), that is, for conveying the adhesion of a thing to the noun governed in the genitive by the bāʾ, as you see in “I passed by Zayd”, for the bāʾ there conveys the adhesion of your passing to Zayd, that is, to a place near him."},
    {"type": "matn",
     "ar": "٢-(والاستعانة) أي: استعانة الفاعل في صدور الفعل عنه بمجروره، نحو: «كتبت بالقلم».",
     "en": "2. (And for seeking aid (istiʿāna)), that is, the agent’s seeking the aid of its governed noun in the issuing of the action from him, as in “I wrote with the pen”."},
    {"type": "matn",
     "ar": "٣-(والمصاحبة[[٦]]) نحو: «اشتريت الفرس بسرجه» أي: مع سرجه، فمعناه: مصاحبة السرج واشتراكه مع الفرس في الاشتراء، ولا يلزم أن يكون السرج حال",
     "en": "3. (And for accompaniment (muṣāḥaba)), as in “I bought the horse with (bi-) its saddle”, that is, together with its saddle; its meaning is the saddle’s accompanying the horse and sharing with it in being bought. It is not necessary that the saddle be, at the time…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: footnote 1 opens «ومعه وليس …» as printed; the sense of «ومعه» here is unclear (possibly «و"مع"» meant). Transcribed as printed.
    {"type": "pair",
     "ar": "ومعه وليس اختصاصه بالظاهر في مجرد كونه بمعنى «إلى».",
     "en": "And with it; its restriction to the explicit noun does not lie merely in its being in the sense of “ilā”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: القلة، فيه إشارة إلى ضعف استدلاله، فإن القليل في حكم العدم فلا يقاس.",
     "en": "That is, rarity. In this there is an indication of the weakness of his argument, for what is rare counts as non-existent, so no analogy is drawn from it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بكونه على خلاف الاستعمال الفصيح للضرورة.",
     "en": "That is, by its being contrary to eloquent usage, owing to [poetic] necessity (ḍarūra)."},
    {"type": "pair",
     "ar": "فهذا جواب غير ما يستفاد من قوله: على سبيل الندرة.",
     "en": "This is therefore an answer other than what is understood from his words “by way of rarity”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الجذع: الساق.",
     "en": "Al-jidhʿ: the trunk."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة طه: ٧١.",
     "en": "Qurʾān, Sūrat Ṭāhā 20:71."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قد تفنن في التعبير عن المصاحبة تارة بمعنى «مع»، وتارة بالمصاحبة.",
     "en": "He has varied the expression for accompaniment, at one time [saying] “in the sense of maʿa”, at another “accompaniment”."},
]
