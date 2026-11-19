# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 367 (printed ٣٦٦)."""

PAGE_NUMBER = 367
PRINTED_PAGE = "٣٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «…ولك الفصل نحو: «ضربي إياك» للاعتداد بالفصل.» at the foot of PDF p. 366 (new sentence).
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن أحدهما أعرف، أو يكون ولكن ما قدمته (فهو) أي: الضمير الثاني على كل من التقديرين (منفصل) لا غير.",
     "en": "(Otherwise), that is, if neither of them is more definite, or one is but you have not placed it first, (it), that is, the second pronoun, on either supposition, (is separate) and nothing else."},
    # REVIEW: «الأخر» is printed with hamza (expected «الآخر»); transcribed as printed.
    {"type": "matn",
     "ar": "أما على التقدير الأول، فلئلا يلزم الترجيح في تقديم أحد المثلين على الأخر فيما هو كالكلمة الواحدة بلا مرجح.",
     "en": "On the first supposition, this is so that there is no preferring, without a preponderating factor, in placing one of two like things before the other within what is like a single word."},
    {"type": "matn",
     "ar": "وأما على التقدير الثاني لكراهتهم تقديم الأنقص على الأقوى فيما هو كالكلمة الواحدة",
     "en": "On the second supposition, it is because of their dislike of placing the weaker before the stronger within what is like a single word."},
    {"type": "matn",
     "ar": "(نحو: «أعطيته إياه») مثال لما لم يكن أحدهما أعرف، لكونهما ضميرين غائبين",
     "en": "(Such as “aʿṭaytuhu iyyāhu”) (I gave him it) is an example of where neither is more definite, both being third-person pronouns;"},
    # REVIEW: «المخاطبن» printed (for «المخاطب»); transcribed as printed.
    {"type": "matn",
     "ar": "(أو) «أعطيته» («إياك») مثال لما يكون أحدهما أعرف، وهو ضمير المخاطبن ولكن ما قدمته.",
     "en": "(or) “aʿṭaytuhu” (“iyyāka”) (I gave him to you) is an example of where one of them is more definite — the second-person pronoun — but you have not placed it first."},
    {"type": "matn",
     "ar": "(والمختار في خبر باب «كان») أي: خبر كان وأخواتها، إذا كان ضميرا (الانفصال) كما تقول: «كان زيد قائما، وكنت إياه»؛",
     "en": "(What is preferred in the predicate of the category of “kāna”), that is, the predicate of kāna and its sisters, when it is a pronoun, (is separation), as you say: “kāna Zaydun qāʾiman, wa-kuntu iyyāhu” (Zayd was standing, and I was it),"},
    {"type": "matn",
     "ar": "لأنه كان في الأصل خبر المبتدأ[[١]]، ويجب أن يكون خبر المبتدأ ضميرا منفصلا؛ لأن عامله معنوي.",
     "en": "because it was originally the predicate of a subject, and the predicate of a subject must be a separate pronoun, since its governor is abstract."},
    {"type": "matn",
     "ar": "ويجوز أن يكون ضميرا متصلا أيضا نحو: «كان زيد قائما وكنته»؛ لأنه شبيه بالمفعول، وضمير المفعول في مثل: «ضربته» واجب الاتصال،",
     "en": "It may also be a connected pronoun, as in “kāna Zaydun qāʾiman wa-kuntuhu”, because it resembles the object, and the object pronoun in such as “ḍarabtuhu” must be connected."},
    {"type": "matn",
     "ar": "ففي شبه المفعول إن لم يكن واجب الاتصال، فلا أقل من أن يكون جائز الاتصال، لكن الانفصال مختار؛ لأن رعاية الأصل أولى من رعاية المشابهة بالمفعول[[٢]].",
     "en": "So in what resembles the object, if connection is not obligatory, it is at least permitted; but separation is preferred, because regard for the original state takes priority over regard for resemblance to the object."},
    {"type": "matn",
     "ar": "(والأكثر) في الاستعمال انفصال الضمير المرفوع بعد «لولا» لكون ما بعد «لولا» مبتدأ[[٣]] محذوف الخبر",
     "en": "(The more common) in usage is separation of the nominative pronoun after “lawlā”, because what follows “lawlā” is a subject whose predicate is elided."},
    {"type": "matn",
     "ar": "تقول: («لولا أنت»[[٤]] إلى آخرها) يعني: «لولا أنت، لولا أنتما، لولا أنتم، لولا أنت، لولا أنتما، لولا أنتن، لولا هو، لولا هما، لولا هم، لولا هي، لولا هما، لولا هن، لولا أنا، لولا نحن»،",
     "en": "You say: (“lawlā anta” (were it not for you) to the end of them), meaning: “lawlā anta, lawlā antumā, lawlā antum, lawlā anti, lawlā antumā, lawlā antunna, lawlā huwa, lawlā humā, lawlā hum, lawlā hiya, lawlā humā, lawlā hunna, lawlā anā, lawlā naḥnu”."},
    {"type": "matn",
     "ar": "وكان الأوفق بما سبق أن يقول: «لولا",
     "en": "It would have been more consistent with what preceded for him to say: “lawlā…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قيل: انفصال خبر المبتدأ باعتبار أن عامله معنوي، وقد انتفى بوجود الناسخ، فكيف يصح إبقاء أثره؟",
     "en": "If it is said: the separation of the subject’s predicate is on account of its governor being abstract, and that has ceased with the presence of the abrogating word (al-nāsikh); so how can its effect validly remain?"},
    {"type": "pair",
     "ar": "قلنا: هو معدوم صورة ثابت معنى، والناسخ عكس ذلك؛ لأن الناسخ في الحقيقة قيد للخبر،",
     "en": "We say: it is absent in form but present in meaning, and the abrogating word is the reverse of that, because the abrogating word is in reality a qualification of the predicate;"},
    {"type": "pair",
     "ar": "فإن قولك: «كان زيد قائما» في معنى زيد قائم في الزمان الماضي.",
     "en": "for your saying “kāna Zaydun qāʾiman” means “Zayd is standing in past time”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يقل: من رعاية العارض إشارة إلى جهتي أولوية أحدهما الإشارة بذكر الأصل إلى الترجيح بالأصالة.",
     "en": "He did not say “than regard for the accidental”, to point to the two grounds of the priority: the first is pointing, by mentioning the original, to preference by originality;"},
    {"type": "pair",
     "ar": "وثانيهما بذكر المشابهة بالمفعول إلى ترجيح الخبرية؛ لأن الخبرية حقيقية والمفعولية تشبيهية.",
     "en": "the second is [pointing], by mentioning resemblance to the object, to the preference of predicate-status, since predicate-status is real while object-status is by resemblance."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "عند الجمهور أو فاعل فعل محذوف أو مرفوعا بـ«لولا»، والوجوه الثلاثة تقتضي الانفصال.",
     "en": "According to the majority; or [it is] the agent of an elided verb, or made nominative by “lawlā”; and all three views require separation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يقل: لولا أنت وعسيت إلى آخرهما، فيكون أخصر لئلا يتوهم أنه يجب استعمالهما معا.",
     "en": "He did not say “lawlā anta and ʿasayta to the end of them”, which would be shorter, lest it be imagined that the two must be used together."},
    {"type": "pair",
     "ar": "ولما رفع هذا الوهم جمعهما في قوله: وجاء لولاك وعساك إلى آخرهما لعدم خوف التباس المقصود بغيره.",
     "en": "Having removed this misconception, he combined them in his words “and there occurs lawlāka and ʿasāka to the end of them”, since there was no fear of the intended meaning being confused with another."},
]
