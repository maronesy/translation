# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 529 (printed ٥٢٨)."""

PAGE_NUMBER = 529
PRINTED_PAGE = "٥٢٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وههنا احتمال آخر، وهو أن يكون «زيد» مرفوعا بأنه اسم «عسى»، وفي «يخرج»[[١]] ضمير يعود إلى «زيد»، و«أن يخرج» في محل النصب بأنه خبر «عسى».",
     "en": "There is another possibility here: that “Zayd” is nominative as the noun of “ʿasā”, that in “yakhruja” there is a pronoun referring back to “Zayd”, and that “an yakhruja” is in the position of the accusative as the predicate of “ʿasā”."},
    {"type": "matn",
     "ar": "وآخر: وهو أن يجعل[[٢]] ذلك من باب التنازع بين «عسى» و«يخرج» في «زيد»،",
     "en": "And another: that this be treated as a case of contention (tanāzuʿ) between “ʿasā” and “yakhruja” over “Zayd”."},
    {"type": "matn",
     "ar": "فإن أعمل الأول كان «زيد» اسم «عسى»، و«أن يخرج» خبرا له مقدما عليه،",
     "en": "If the first is given government, “Zayd” is the noun of “ʿasā”, and “an yakhruja” is its predicate placed before it;"},
    {"type": "matn",
     "ar": "وإن أعمل الثاني[[٣]] كان اسم «عسى» ما استكن فيه من ضمير «زيد»، وخبره «أن يخرج زيد»، فهي على هذين الاحتمالين ناقصة أيضا.",
     "en": "and if the second is given government, the noun of “ʿasā” is the pronoun of “Zayd” latent in it, and its predicate is “an yakhruja Zaydun”. So on these two possibilities too it is incomplete."},
    {"type": "matn",
     "ar": "(وقد يحذف «أن») عن الفعل المضارع[[٤]] في الاستعمال الأول تشبيها لها بـ«كاد»،",
     "en": "(And “an” is sometimes omitted) from the muḍāriʿ verb in the first usage, likening it to “kāda”:"},
    {"type": "matn",
     "ar": "فكما أن «كاد زيد يخرج» لم يذكر فيه «أن» كذلك «عسى زيد يخرج» لا يذكر فيه «أن» كقولهم:",
     "en": "just as “an” is not mentioned in “kāda Zaydun yakhruju” (Zayd was about to go out), so “an” is not mentioned in “ʿasā Zaydun yakhruju”, as in their saying:"},
    {"type": "verse",
     "ar": "عسى الهم الذي أمسيت فيه          يكون وراءه فرج قريب",
     "en": "Perhaps the care in which I find myself this evening / will have, behind it, a relief that is near."},
    {"type": "matn",
     "ar": "كان الأصل: «أن يكون وراءه»، فحذف «أن» دون الاستعمال الثاني؛ لعدم مشابهة قولك[[٥]]: «عسى أن يخرج زيد» بقولك: «كاد زيد يخرج».",
     "en": "The original was “an yakūna warāʾahu”, and “an” was omitted; [this is] not [done] in the second usage, because your saying “ʿasā an yakhruja Zaydun” does not resemble your saying “kāda Zaydun yakhruju”."},
    {"type": "matn",
     "ar": "(والثاني) أي: ما وضع لدنو الخبر دنو حصول («كاد»، تقول: «كاد زيد يجيء») فتخبر عن دنو الخبر؛ لعلمك بإشرافه على الحصول للفاعل في الحال،",
     "en": "(And the second), that is, what was coined for the nearness of the predicate as a nearness of occurrence, (is “kāda”; you say “kāda Zaydun yajīʾu” (Zayd was about to come)), so you report the nearness of the predicate, because you know that it is on the verge of occurring for the agent at the present time."},
    {"type": "matn",
     "ar": "ففاعله اسم محض[[٦]] -كما هو الأصل- وخبره فعل مضارع؛ ليدل على قرب حصول الخبر من الحال باعتبار أحد معنييه",
     "en": "So its agent is a pure noun, as is the norm, and its predicate is a muḍāriʿ verb, so as to indicate the nearness of the predicate’s occurrence to the present, by virtue of one of its two meanings,"},
    {"type": "matn",
     "ar": "من غير «أن» لدلالته على الاستقبال[[٧]] المنافي للحال.",
     "en": "without “an”, because it indicates the future, which is incompatible with the present."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وحينئذ يكون بعينه الاستعمال الأول معنى إلا أنه قدم الخبر على الاسم، فلا التباس لاتحاد المعنى، بل هو تعدد وجوه الاستعمال",
     "en": "In that case it is in meaning exactly the first usage, except that the predicate has been placed before the noun; so there is no ambiguity, since the meaning is one; rather it is a multiplicity of ways of usage,"},
    {"type": "pair",
     "ar": "بخلاف \"زيد قام\"، فإنه لو قدم قام يفوت التقوي ففيه الالتباس.",
     "en": "unlike “Zaydun qāma” (Zayd stood), for if “qāma” were placed first the strengthening (taqawwī) would be lost; so there is ambiguity in it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يتوقف صحة هذا التوجيه على أن يثبت في الاستعمال عسيا أن يخرج الزيدان،",
     "en": "The soundness of this explanation depends on “ʿasayā an yakhruja al-Zaydāni” being attested in usage;"},
    {"type": "pair",
     "ar": "ولو كان الاستعمال عسى أن يخرج الزيدان، فلا شيء على مذهب البصريين من اختيار إعمال الثاني.",
     "en": "and if the usage is “ʿasā an yakhruja al-Zaydāni”, then there is nothing [to support it] on the position of the Baṣrans, who choose to give government to the second."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فتقول في اختيار البصريين: عسى أن يخرج الزيدان، وعلى اختيار الكوفيين: عسى أن يخرجا الزيدان، وعلى هذا القياس الجمع والمؤنث.",
     "en": "So you say, on the Baṣrans’ choice, “ʿasā an yakhruja al-Zaydāni”, and on the Kūfans’ choice, “ʿasā an yakhrujā al-Zaydāni”; and the plural and the feminine follow this analogy."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فالأولى أن يقول المصنف: تقول: عسى زيد أن يخرج. وقد يحذف «أن» وعسى أن يخرج زيد.",
     "en": "So it would have been better for the author to say: “You say ‘ʿasā Zaydun an yakhruja’ (and ‘an’ is sometimes omitted) and ‘ʿasā an yakhruja Zaydun’.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا واضح على تقدير أن يكون «زيد» فاعل «يخرج» إما لو كان اسم «عسى» وأن يخرج خبره، أو يكون اسم «عسى» ضمير «زيد» كما جوزه، فالمشابهة متحققة كما كانت في الاستعمال الأول.",
     "en": "This is clear on the supposition that “Zayd” is the agent of “yakhruja”; but if it were the noun of “ʿasā” and “an yakhruja” its predicate, or if the noun of “ʿasā” were the pronoun of “Zayd”, as he allowed, then the resemblance is realized, as it was in the first usage."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا ما دل عليه كما في الاستعمال الثاني لـ«عسى».",
     "en": "Not something that indicates it, as in the second usage of “ʿasā”."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: لدلالة أن على زمان الاستقبال المنافي للحال، فلا يناسب ذكره مع «كاد» الذي مدلوله الإشراف على الحصول وقربه منه غاية القرب.",
     "en": "That is, because “an” indicates future time, which is incompatible with the present; so mentioning it does not suit “kāda”, whose signification is being on the verge of occurring and its utmost nearness to it."},
]
