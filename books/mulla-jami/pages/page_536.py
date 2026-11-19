# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 536 (printed ٥٣٥)."""

PAGE_NUMBER = 536
PRINTED_PAGE = "٥٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نحو: «نعم الرجل زيد» (أو)» at the foot of PDF p. 535 (mid-sentence).
    {"type": "matn",
     "ar": "يكون (مضافا إلى المعرف بها) أي: باللام، إما بغير واسطة نحو: «نعم صاحب الرجل زيد»،",
     "en": "…be (annexed to what is made definite by it), that is, by the lām, either without an intermediary, as in “niʿma ṣāḥibu al-rajuli Zaydun”,"},
    {"type": "matn",
     "ar": "أو بواسطة نحو: «نعم فرس غلام الرجل» أو «نعم وجه فرس غلام الرجل»، وهلم جرا",
     "en": "or with an intermediary, as in “niʿma farasu ghulāmi al-rajuli” or “niʿma wajhu farasi ghulāmi al-rajuli”, and so on;"},
    {"type": "matn",
     "ar": "(أو) يكون (مضمرا مميزا بنكرة منصوبة مفردة[[١]]) أو مضافة إلى نكرة أو معرفة إضافة لفظية",
     "en": "(or) it is (a concealed pronoun specified by an indefinite noun in the accusative, singular), or annexed to an indefinite, or to a definite in a verbal (non-defining) annexation (iḍāfa lafẓiyya),"},
    {"type": "matn",
     "ar": "نحو: «نعم رجلا، أو ضارب رجل أو زيد أو حسن الوجه أنت»",
     "en": "as in “niʿma rajulan”, or “ḍāriba rajulin”, or “Zaydin”, or “ḥasana al-wajhi anta”;"},
    {"type": "matn",
     "ar": "(أو) مميزا (بما) بمعنى: شيء؛ منصوب المحل على التمييز (مثل «فنعما هي») أي: «نعم شيئا هي».",
     "en": "(or) specified (by mā) in the sense of “a thing”, in the accusative position as a specification (tamyīz), (as in “fa-niʿimmā hiya”), that is, “niʿma shayʾan hiya” (an excellent thing it is)."},
    {"type": "matn",
     "ar": "وقال الفراء وأبو علي: هي موصولة بمعنى «الذي»، فاعل لـ«نعم»، ويكون[[٢]] الصلة بأجمعها في «فنعما هي» محذوفة؛",
     "en": "Al-Farrāʾ and Abū ʿAlī said: it is a relative in the sense of “alladhī”, agent of “niʿma”, and the relative clause in its entirety is omitted in “fa-niʿimmā hiya”,"},
    {"type": "matn",
     "ar": "لأن «هي» مخصوصة أي: نعم الذي فعله هي أي: الصدقات.",
     "en": "because “hiya” is the specified term; that is, “excellent is that which he does: it”, that is, the alms."},
    {"type": "matn",
     "ar": "وقال سيبويه والكسائي: «ما» معرفة تامة بمعنى الشيء، فمعنى: ﴿فنعما هي﴾[[٣]] «نعم الشيء هي»،",
     "en": "Sībawayh and al-Kisāʾī said: “mā” is a complete definite in the sense of “the thing”; so the meaning of “fa-niʿimmā hiya” is “niʿma al-shayʾu hiya” (an excellent thing it is);"},
    {"type": "matn",
     "ar": "فـ«ما» هو الفاعل؛ لكونه بمعنى ذي اللام، وهي مخصوصة.",
     "en": "so “mā” is the agent, because it is in the sense of [a noun] bearing the lām, and “hiya” is the specified term."},
    {"type": "matn",
     "ar": "(وبعد ذلك) الفاعل (المخصوص) بالمدح أو الذم، وبعديته إنما هي بحسب الغالب؛",
     "en": "(And after that) agent comes (the term specified) for praise or blame; its coming after is only according to the prevailing usage,"},
    {"type": "matn",
     "ar": "لأنه قد يقدم المخصوص فيقال: «زيد نعم الرجل» صرح به في المفتاح.",
     "en": "because the specified term is sometimes put first, so that one says “Zaydun niʿma al-rajulu”; this is stated explicitly in al-Miftāḥ."},
    {"type": "matn",
     "ar": "(وهو) أي: المخصوص (مبتدأ، ما قبله) أي: الجملة الواقعة قبله غالبا (خبره)",
     "en": "(And it), that is, the specified term, (is a subject (mubtadaʾ), and what precedes it), that is, the sentence that usually occurs before it, (is its predicate);"},
    {"type": "matn",
     "ar": "ولم تحتج هذه الجملة الواقعة خبرا إلى ضمير المبتدأ؛ لقيام لام التعريف العهدي[[٤]] مقامه",
     "en": "and this sentence occurring as predicate does not need a pronoun referring to the subject, because the lām of referential definiteness stands in its place;"},
    {"type": "matn",
     "ar": "(أو خبر مبتدأ محذوف) وهو (مثل: «نعم الرجل زيد») فـ«زيد» في هذا المثال: إما",
     "en": "(or it is the predicate of an omitted subject); and this is (as in “niʿma al-rajulu Zaydun”), for “Zayd” in this example is either…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الرضي: ذهب الجزولي ومن تبعه إلى لزوم إفراد تمييز هذا الضمير، والظاهر أنه وهم منه،",
     "en": "In al-Raḍī: al-Jazūlī and those who followed him held that the specification of this pronoun must be singular; apparently this is a mistake on his part;"},
    # REVIEW: printed «أهل المصريين»; one would expect «أهل المصرين» (the people of the two cities, Baṣra and Kūfa). Transcribed as printed.
    {"type": "pair",
     "ar": "بل يجب مطابقته لما قصد عند أهل المصريين. وقد صرح المصنف وابن مالك بمطابقته لما قصد، وهو الحق.",
     "en": "rather, according to the people of the two cities [Baṣra and Kūfa], it must agree with what is intended. The author and Ibn Mālik stated explicitly that it agrees with what is intended, and this is correct."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه إشارة إلى تضعيفه؛ لأن حذف الصلة بأجمعها قليل، وكذا يضعفه قلة وقوع الذي مصرحا به فاعلا لـ«نعم وبئس».",
     "en": "In it is an indication that he regards it as weak, because omitting the relative clause in its entirety is rare; likewise it is weakened by the rarity of “alladhī” occurring explicitly as the agent of “niʿma and biʾsa”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة البقرة:٢٧١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:271."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: العهد الذهني ليلائم ما سبق.",
     "en": "That is, mental reference, so as to accord with what preceded."},
    {"type": "pair",
     "ar": "ولا يخفى أنه إذا كان زيد مبتدأ يبعد أن يكون اللام للعهد الذهني؛ لأنه عبارة عن زيد.",
     "en": "It is not hidden that when “Zayd” is the subject, it is unlikely that the lām is for mental reference, because it [the agent] denotes Zayd."},
    {"type": "pair",
     "ar": "وكذا لا يظهر على هذا التقدير كون الضمير في «نعم رجلا زيد» مبهما، بل الظاهر أنه راجع إلى زيد، ورجلا تمييز عن النسبة",
     "en": "Likewise, on this construal it is not apparent that the pronoun in “niʿma rajulan Zaydun” is vague; rather, apparently it refers back to Zayd, and “rajulan” is a specification of the attribution (tamyīz ʿan al-nisba);"},
    {"type": "pair",
     "ar": "إلا أنهم حكموا بأنه ضمير مبهم للزوم إفراده، فالعائد في «نعم رجلا زيد» ليس الضمير بل الضمير مع تمييزه صار بمنزلة نعم الرجل وصار الخبر مرتبطا بالمبتدأ بهذا الاعتبار،",
     "en": "except that they judged it to be a vague pronoun because it must be singular; so the referring element in “niʿma rajulan Zaydun” is not the pronoun; rather, the pronoun together with its specification has become equivalent to “niʿma al-rajulu”, and in this respect the predicate has become linked to the subject."},
    {"type": "pair",
     "ar": "ولولا أن المخصوص قد تقدم على الجملة لكان الأنسب جعله عطف بيان، وهذا هو المرجح لكونه مبتدأ؛ لأنه لا يحسن تقديم التفسير على الإبهام.",
     "en": "Were it not that the specified term is sometimes put before the sentence, it would be more fitting to make it an explicative apposition (ʿaṭf bayān); and this is what favours its being a subject, because it is not good to put the explanation before the vagueness."},
]
