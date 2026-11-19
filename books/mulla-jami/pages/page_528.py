# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 528 (printed ٥٢٧)."""

PAGE_NUMBER = 528
PRINTED_PAGE = "٥٢٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… تقوية لمعنى الترجي الذي هو توقع وجود الفعل» at the foot of PDF p. 527 (mid-sentence).
    {"type": "matn",
     "ar": "في الاستقبال، فـ«زيد» اسم «عسى»، و«أن يخرج» في محل النصب بالخبرية أي: عسى زيد الخروج، بتقدير مضاف[[١]]:",
     "en": "…in the future. So “Zayd” is the noun (ism) of “ʿasā”, and “an yakhruja” is in the position of the accusative as its predicate, that is, “ʿasā Zaydun al-khurūja” (Zayd may [be] the going out), with a supposed governing noun of annexation (muḍāf) supplied:"},
    {"type": "matn",
     "ar": "إما في جانب الاسم[[٢]] نحو: «عسى حال زيد الخروج»، أو في جانب الخبر أي: «عسى زيد ذا الخروج»؛",
     "en": "either on the side of the noun, as in “ʿasā ḥālu Zaydin al-khurūja” (Zayd’s state may be the going out), or on the side of the predicate, that is, “ʿasā Zaydun dhā al-khurūji” (Zayd may be one who goes out);"},
    {"type": "matn",
     "ar": "لوجوب[[٣]] صدق الخبر على الاسم، وعلى هذا «عسى» ناقصة[[٤]].",
     "en": "because the predicate must be truly predicable of the noun. On this [view] “ʿasā” is incomplete (nāqiṣa)."},
    {"type": "matn",
     "ar": "وقيل: المضارع مع «أن» مشبه بالمفعول وليس بخبر؛ لعدم صدقه على الاسم، وتقدير المضاف تكلف،",
     "en": "It has been said: the muḍāriʿ with “an” is likened to the object (mushabbah bi-l-mafʿūl) and is not a predicate, because it is not predicable of the noun, and supplying the muḍāf is strained;"},
    {"type": "matn",
     "ar": "وذلك لأن المعنى الأصلي[[٥]]: «قارب زيد أن يخرج» أي: الخروج، ثم نقل إلى إنشاء الطمع،",
     "en": "that is because the original meaning is “qāraba Zaydun an yakhruja” (Zayd came near to going out), that is, the going out; then it was transferred to the performative expression (inshāʾ) of hope."},
    {"type": "matn",
     "ar": "فالمضارع مع «أن» وإن لم يبق على المفعولية في صورة الإنشاء[[٦]]، فهو مشبه بالمفعول الذي كان في صورة الخبر، فانتصب لشبهه بالمفعول،",
     "en": "So the muḍāriʿ with “an”, even if it did not remain an object in the performative form, is likened to the object that it was in the declarative (khabar) form, and so it was put in the accusative for its resemblance to the object;"},
    {"type": "matn",
     "ar": "و«عسى» على هذا تامة.",
     "en": "and on this [view] “ʿasā” is complete (tāmma)."},
    {"type": "matn",
     "ar": "وقال الكوفيون: «أن يفعل» في محل الرفع بدلا مما قبله بدل الاشتمال؛",
     "en": "The Kūfans said: “an yafʿala” is in the position of the nominative, as a substitute (badal) for what precedes it, a substitute of inclusion (badal al-ishtimāl);"},
    {"type": "matn",
     "ar": "لأن فيه إجمالا ثم تفصيلا، وفي إبهام الشيء ثم تفسيره وقع عظيم لذلك الشيء في النفس.",
     "en": "because there is in it a summary followed by a detailing, and in making a thing vague and then explaining it there is a great impact of that thing upon the soul."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: والذي أرى أن هذا وجه قريب.",
     "en": "The commentator al-Raḍī said: “What I hold is that this is a plausible view.”"},
    {"type": "matn",
     "ar": "(و) تقول على الاستعمال الآخر: («عسى أن يخرج زيد») بأن يذكر مرفوع فقط -وهو ما كان منصوبا في الاستعمال الأول- فاستغنى عن الخبر؛",
     "en": "(And) you say, on the other usage, (“ʿasā an yakhruja Zaydun”), with only a nominative being mentioned (which is what was in the accusative in the first usage), so that it dispenses with the predicate,"},
    {"type": "matn",
     "ar": "لاشتمال الاسم على المنسوب والمنسوب إليه، كما استغنى في: «علمت أن زيدا قائم» عن المفعول الآخر، فأقيم مقامهما، فهي في هذا الاستعمال ناقصة.",
     "en": "because the noun comprises both the attributed and that to which it is attributed, just as in “ʿalimtu anna Zaydan qāʾimun” (I knew that Zayd is standing) it dispenses with the other object; so it was put in the place of both, and in this usage it is incomplete."},
    {"type": "matn",
     "ar": "وإن اقتصر على المرفوع من غير قصد إقامته مقام المرفوع والمنصوب بمعنى: «قرب خروج زيد»، فهي تامة.",
     "en": "But if one confines oneself to the nominative without intending to put it in the place of the nominative and the accusative, in the sense of “qaruba khurūju Zaydin” (Zayd’s going out drew near), then it is complete."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «إن زائدة» with hamza below the alif; the particle in question is «أن». Transcribed as printed.
    {"type": "pair",
     "ar": "وقيل: إنه من قبيل رجل عدل. وقيل: إن زائدة.",
     "en": "It has been said that it is of the type of “rajulun ʿadlun” (a man [who is] justice). And it has been said that “an” is redundant."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يزيغه ما جاء في كلامهم من قولهم: عسيت صائما، ويرجح تأويل الخبر باسم الفاعل.",
     "en": "What occurs in their speech, their saying “ʿasaytu ṣāʾiman” (I may be fasting), makes it deviate, and favours interpreting the predicate as an active participle (ism al-fāʿil)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "متعلق بتقدير مضاف أي: لوجوب صدق الخبر على الاسم لكونهما في الأصل مبتدأ وخبرا، والحدث لا يصدق على الجثة.",
     "en": "Connected with “supplying a muḍāf”; that is, because the predicate must be predicable of the noun, since the two are originally subject and predicate, and an event (ḥadath) is not predicable of a body (juththa)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بمعنى أنها لا تتم بالمرفوع لا بمعنى تقرير الفاعل على صفة.",
     "en": "In the sense that it is not complete with the nominative alone, not in the sense of establishing the agent in a quality."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: الوضعي إلى آخره.",
     "en": "That is, [the meaning] by original coinage (al-waḍʿī), to the end [of the passage]."},
    {"type": "pair",
     "ar": "في المغني: أنها فعل متعد بمنزلة قارب عملا ومعنى أو قاصر بمنزلة قرب من أن يفعل حذف الجار توسعا، وهذا مذهب سيبويه والمبرد.",
     "en": "In al-Mughnī: that it is a transitive verb equivalent to “qāraba” in government and meaning, or an intransitive one equivalent to “qaruba min an yafʿala”, with the preposition omitted by extension of usage; this is the position of Sībawayh and al-Mubarrad."},
    {"type": "pair",
     "ar": "في الرضي: فيه بحث؛ إذ لم يثبت في \"عسى\" معنى المقاربة لا وضعا ولا استعمالا.",
     "en": "In al-Raḍī: there is a point of discussion in this, since the meaning of nearness (muqāraba) is not established for “ʿasā”, neither by coinage nor by usage."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى أن يجعل منصوبا على المفعولية باعتبار الأصل. ويرده أيضا عسيت صائما.",
     "en": "It would be better to make it accusative as an object in respect of the original. “ʿAsaytu ṣāʾiman” also refutes it."},
]
