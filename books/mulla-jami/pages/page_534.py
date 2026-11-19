# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 534 (printed ٥٣٣)."""

PAGE_NUMBER = 534
PRINTED_PAGE = "٥٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وأجيب[[١]]: بأن ذكر التأخير إنما هو للتأكيد، لا للتأسيس على أن كل واحد منهما وإن لم ينفصل عن الآخر بالوجود، لكنه ينفصل عنه بالقصد، فكأنه اعتبر القصد.",
     "en": "It was answered that the mention of placing after is only for emphasis, not to add a new point (taʾsīs); besides, each of the two, even if it is not separable from the other in existence, is separable from it in intention; so it is as though he took intention into account."},
    {"type": "matn",
     "ar": "(ولا) يتصرف فيهما بإيقاع (فصل) بين العامل والمعمول[[٢]] نحو: «ما أحسن في الدار زيدا»، و«أكرم اليوم بزيد» لإجرائهما مجرى الأمثال، كما سبق.",
     "en": "(Nor) is there free handling of them by placing a (separation) between the governor and the governed, as in “mā aḥsana fī al-dāri Zaydan” and “akrim al-yawma bi-Zaydin”, because they are treated as proverbs, as has preceded."},
    {"type": "matn",
     "ar": "(وأجاز المازني الفصل بالظرف) لما سمع من العرب قولهم: «ما أحسن بالرجل أن يصدق»،",
     "en": "(Al-Māzinī permitted separation by an adverbial (ẓarf)), because of what was heard from the Arabs, their saying “mā aḥsana bi-l-rajuli an yaṣduqa” (how good it is in a man that he be truthful!)."},
    {"type": "matn",
     "ar": "وأجاز الأكثرون الفصل بكلمة «كان»[[٣]] مثل: «ما كان أحسن زيدا»، ومعناه: أنه كان له في الماضي حسن واقع دائم إلا أنه لم يتصل بزمان التكلم، بل كان دائما قبله.",
     "en": "Most permitted separation by the word “kāna”, as in “mā kāna aḥsana Zaydan” (how handsome Zayd was!), whose meaning is that he had in the past an actual, lasting beauty, except that it did not continue up to the time of speaking but was lasting before it."},
    {"type": "matn",
     "ar": "(و«ما» ابتداء) أي: مبتدأ على أن يكون المصدر بمعنى اسم المفعول، أو ذو ابتداء بتقدير المضاف.",
     "en": "(And “mā” is ibtidāʾ), that is, a subject (mubtadaʾ), taking the verbal noun in the sense of the passive participle; or [it means] “possessing ibtidāʾ”, by supplying the muḍāf."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «وما ابتدائية» ومعناه ظاهر",
     "en": "In some copies: “and mā is inceptive (ibtidāʾiyya)”, whose meaning is clear;"},
    {"type": "matn",
     "ar": "(نكرة) بمعنى: «شيء»؛ لأن النكارة تناسب التعجب؛ لأنه يكون فيما خفي سببه",
     "en": "(indefinite (nakira)), in the sense of “something”, because indefiniteness suits wonder, since [wonder] arises at that whose cause is hidden,"},
    {"type": "matn",
     "ar": "(عند سيبويه، وما بعدها) أي: ما بعد «ما» (الخبر) من باب: «شر أهر ذا ناب»",
     "en": "(according to Sībawayh; and what comes after it), that is, after “mā”, (is the predicate), of the type “sharrun aharra dhā nābin” (something evil has made the fanged one snarl)."},
    {"type": "matn",
     "ar": "(وموصولة) أي: «ما» موصولة (عند الأخفش، والخبر محذوف) أي: «الذي أحسن زيدا -أي: جعله ذا حسن- شيء عظيم».",
     "en": "(And it is relative (mawṣūla)), that is, “mā” is relative, (according to al-Akhfash, and the predicate is omitted), that is, “that which made Zayd handsome (that is, made him possessed of beauty) is something great”."},
    {"type": "matn",
     "ar": "وقال الفراء: «ما» استفهامية، ما بعدها خبرها.",
     "en": "Al-Farrāʾ said: “mā” is interrogative, and what follows it is its predicate."},
    # REVIEW: printed «لأنه كان جهل»; the sense suggests «لأنه كأنه جهل». Transcribed as printed; the translation follows the apparent sense.
    {"type": "matn",
     "ar": "قال الشارح الرضي: وهو قوي من حيث المعنى؛ لأنه كان جهل سبب حسنه فاستفهم عنه،",
     "en": "The commentator al-Raḍī said: it is strong in respect of meaning, for it is as though he did not know the cause of his beauty and so asked about it;"},
    {"type": "matn",
     "ar": "وقد يستفاد من الاستفهام معنى التعجب نحو: ﴿وما أدراك ما يوم الدين﴾[[٤]].",
     "en": "and the meaning of wonder is sometimes derived from the interrogative, as in “And what will make you know what the Day of Judgement is?”"},
    {"type": "matn",
     "ar": "وأما «أحسن بزيد»، فـ«أفعل» صورته أمر ومعناه الماضي، من «أفعل» بمعنى: «صار ذا فعل»، كـ«ألحم» أي: «صار ذا لحم».",
     "en": "As for “aḥsin bi-Zaydin”, “afʿil” is imperative in form and past in meaning, from “afʿala” in the sense of “he became possessed of fiʿl”, like “alḥama”, that is, “he became possessed of flesh”."},
    {"type": "matn",
     "ar": "(و«به») أي: مجروره[[٥]] (فاعل) لهذا الفعل (عند سيبويه) والباء زائدة لازمة إلا إذا",
     "en": "(And “bihi”), that is, what it governs in the genitive, (is the agent) of this verb (according to Sībawayh), and the bāʾ is redundant and obligatory, except when…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "نقل عن الشارح. وأجاب بعضهم: بأنه يجوز أن يكون المراد تقديمه على شيء، وتأخيره بالنسبة إلى شيء آخر.",
     "en": "Transmitted from the commentator. Some answered that what is meant may be placing it before one thing and placing it after in relation to another thing."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بقرينة قوله: بالظرف، وإنما قيد بذلك؛ لأنه أجاز الأكثرون الفصل بكلمة «كان» بين «ما» والفعل.",
     "en": "As indicated by his words “by an adverbial”. He qualified it so only because most permitted separation by the word “kāna” between “mā” and the verb."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فقط، وهي زائدة للدلالة على ثبوت الحكم في الزمان الماضي، وانقطاعه في الحال كما بينه الشارح.",
     "en": "Only; and it is redundant, to indicate that the judgement held in past time and has ceased in the present, as the commentator explained."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة الانفطار:١٧.",
     "en": "Qurʾān, Sūrat al-Infiṭār 82:17."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "التسامح شائع في كلامهم لشدة الاتصال بين الجار والمجرور.",
     "en": "Loose expression is common in their speech, because of the close connection between the preposition and its object."},
]
