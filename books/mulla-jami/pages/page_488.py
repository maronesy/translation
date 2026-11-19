# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 488 (printed ٤٨٧)."""

PAGE_NUMBER = 488
PRINTED_PAGE = "٤٨٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وذلك في خمسة» at the foot of PDF p. 487 (mid-sentence).
    {"type": "matn",
     "ar": "مواضع: (بالنون) حالة الرفع (وحذفها) أي: بحذف النون حالتي الجزم والنصب، فإن النصب فيه تابع للجزم، كما في الأسماء تابع للجر.",
     "en": "…places: (with the nūn) in the state of the nominative, (and its omission), that is, with omission of the nūn in the two states of the jussive and the accusative; for the accusative in it follows the jussive, as in nouns it follows the genitive."},
    {"type": "matn",
     "ar": "(مثل: «يضربان، وتضربان ويضربون، وتضربون، وتضربين») و«لم يضربا، ولن يضربا» إلى آخره.",
     "en": "(As in “yaḍribāni”, “taḍribāni”, “yaḍribūna”, “taḍribūna” and “taḍribīna”), and “lam yaḍribā” and “lan yaḍribā”, to the end."},
    {"type": "matn",
     "ar": "(و) المضارع (المعتل) الآخر (بالواو والياء بالضمة تقديرا) في حال الرفع؛ لأن الضمة على الواو والياء ثقيلة، تقول: «يدعو ويرمي»",
     "en": "(And) the muḍāriʿ (weak) in its final letter (with the wāw and the yāʾ [is inflected] with the ḍamma by supposition) in the state of the nominative, because the ḍamma on the wāw and the yāʾ is heavy; you say “yadʿū” and “yarmī”;"},
    {"type": "matn",
     "ar": "(والفتحة لفظا) في حال النصب لخفة الفتحة نحو: «لن يدعو ولن يرمي»",
     "en": "(and with the fatḥa overtly) in the state of the accusative, owing to the lightness of the fatḥa, as in “lan yadʿuwa” and “lan yarmiya”;"},
    {"type": "matn",
     "ar": "(والحذف) أي: بحذف الواو والياء في حال الجزم؛ لأن الجازم لما لم يجد حركة، أسقط الحرف المناسب[[١]] لها، نحو: «لم يغز ولم يرم».",
     "en": "(and with omission), that is, with omission of the wāw and the yāʾ in the state of the jussive; because the jussive particle, finding no vowel, dropped the letter akin to it, as in “lam yaghzu” and “lam yarmi”."},
    {"type": "matn",
     "ar": "(و) المضارع (المعتل) الآخر[[٢]] (بالألف بالضمة والفتحة تقديرا)؛ لأن الألف لا تقبل الحركة، تقول: «يرضى ولن يرضى»",
     "en": "(And) the muḍāriʿ (weak) in its final letter (with the alif [is inflected] with the ḍamma and the fatḥa by supposition), because the alif does not admit a vowel; you say “yarḍā” and “lan yarḍā”;"},
    {"type": "matn",
     "ar": "(والحذف) أي: بحذف الألف في حال الجزم تقول: «لم يرض».",
     "en": "(and with omission), that is, with omission of the alif in the state of the jussive; you say “lam yarḍa”."},
    {"type": "matn",
     "ar": "(ويرتفع) المضارع (إذا تجرد عن الناصب والجازم، نحو: «يقوم زيد») سواء كان العامل فيه هذا التجرد، كما هو المتبادر من عبارته، وذلك مذهب الكوفيين،",
     "en": "(And) the muḍāriʿ (is put in the nominative when it is free of the accusative-governing and the jussive-governing particle, as in “yaqūmu Zaydun”), whether what governs it is this freedom, as first appears from his wording, and that is the doctrine of the Kūfans;"},
    {"type": "matn",
     "ar": "وسواء كان العامل فيه وقوعه موقع الاسم، كما في «زيد يضرب»[[٣]] أي: ضارب، أو «مررت برجل يضرب»، أو «رأيت رجلا يضرب».",
     "en": "or what governs it is its occurring in the position of the noun, as in “Zaydun yaḍribu”, that is, ḍāribun (striking), or “I passed by a man who strikes”, or “I saw a man who strikes”."},
    {"type": "matn",
     "ar": "وإنما ارتفع لوقوعه موقع الاسم؛ لأنه إذن يكون كالاسم، فأعطي أسبق إعراب الاسم[[٤]] وأقواه، وهو الرفع، وذلك مذهب البصريين.",
     "en": "It is put in the nominative because of its occurring in the position of the noun only because it is then like the noun, so it was given the noun’s first and strongest inflection, namely the nominative; and that is the doctrine of the Baṣrans."},
    {"type": "matn",
     "ar": "وأورد عليه: أنه يرتفع في مواضع لا يقع فيها موقع الاسم، كما في الصلة، نحو: «الذي يضرب»[[٥]] وفي نحو: «سيقوم، وسوف يقوم»، وفي خبر كاد نحو: «كاد زيد",
     "en": "It has been objected against this that it is put in the nominative in places where it does not occur in the position of the noun: as in the relative clause (ṣila), as in “alladhī yaḍribu” (he who strikes); in a case like “sa-yaqūmu” and “sawfa yaqūmu”; and in the predicate of kāda, as in “kāda Zaydun…"},

    {"type": "rule"},

    # ---------------- Continuation of footnote ٧ from PDF p. 487 ----------------
    # Unnumbered: runs on from footnote ٧ of printed p. ٤٨٦ («… فنبه الشارح»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "عليه بقوله: والمضارع المتصل،",
     "en": "…to this by his words “and the joined muḍāriʿ”."},
    {"type": "pair",
     "ar": "ولو مثل المصنف بقولنا: «يدعوان وتدعوان» إلى آخره بدل «يضربان» لكان واضحا.",
     "en": "Had the author given the example with our saying “yadʿuwāni” and “tadʿuwāni”, to the end, in place of “yaḍribāni”, it would have been clear."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن حرف العلة مناسب للحركة في كونهما قابلين للسقوط.",
     "en": "Because the weak letter is akin to the vowel in that both are liable to being dropped."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المعتل عندهم: ما يقابل الصحيح، وهو ما كان آخره حرف علة،",
     "en": "The weak [verb] among them is what is set against the sound, namely that whose final letter is a weak letter;"},
    {"type": "pair",
     "ar": "لكن المتبادر من كلام الشارح أن المعتل عام أريد به الخاص.",
     "en": "but what first appears from the Commentator’s words is that “weak” is a general term by which the specific is meant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: يقع موقع الاسم المرفوع المجرور والمنصوب.",
     "en": "That is, it occurs in the position of the noun in the nominative, the genitive and the accusative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لكونه إعراب أسبق المعمولات وأقواه لكونه إعراب العمد.",
     "en": "Because it is the inflection of the first of the governed terms, and the strongest because it is the inflection of the pillars [of the sentence] (ʿumad)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فإنه لا يقع اسم الفاعل موقعه لوجوب كون الصلة جملة، ولا يدخل السين وسوف على الاسم، وخبر «كاد» يجب أن يكون فعلا،",
     "en": "For the active participle does not occur in its position, since the relative clause must be a sentence; sa- and sawfa do not enter upon the noun; and the predicate of “kāda” must be a verb;"},
    {"type": "pair",
     "ar": "وفي يقوم الزيدان يلزم عمل اسم الفاعل بدون الاعتماد.",
     "en": "and in “yaqūmu al-Zaydāni” the active participle’s governing without support (iʿtimād) would follow."},
]
