# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 363 (printed ٣٦٢)."""

PAGE_NUMBER = 363
PRINTED_PAGE = "٣٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… إذا لم يكونا مسندين إلى الظاهر نحو: «زيد» from the foot of PDF p. 362.
    {"type": "matn",
     "ar": "يضرب، وهند تضرب» (وفي الصفة مطلقا[[١]]) سواء كانت اسم فاعل أو مفعول أو صفة مشبهة أو أفعل التفضيل،",
     "en": "…yaḍribu, wa-Hindun taḍribu” (Zayd strikes, and Hind strikes); (and in the adjective, without qualification), whether it is an active participle, a passive participle, a resembling adjective (ṣifa mushabbaha) or an elative (afʿal al-tafḍīl),"},
    {"type": "matn",
     "ar": "وسواء كان مفردا أو مثنى أو مجموعا، أو مذكرا أو مؤنثا إذا لم تكن مسندا إلى الظاهر[[٢]] نحو: «أقائم الزيدان»،",
     "en": "and whether singular, dual or plural, masculine or feminine — when it is not attributed to an overt noun, as [opposed to] “a-qāʾimun al-Zaydāni” (are the two Zayds standing?) —"},
    # REVIEW: «والزيدان ضاربتان» printed (the masculine dual would be «ضاربان», as the next sentence has); transcribed as printed.
    {"type": "matn",
     "ar": "كقولك: «زيد ضارب، وهند ضاربة، والزيدان ضاربتان، والزيدون ضاربون، والهندات ضاربات»،",
     "en": "as when you say: “Zaydun ḍāribun, wa-Hindun ḍāribatun, wa-l-Zaydāni ḍāribatāni, wa-l-Zaydūna ḍāribūna, wa-l-Hindātu ḍāribātun”."},
    {"type": "matn",
     "ar": "وليست الألف في «ضاربان»، والواو في «ضاربون» بضميرين؛ لأنهما تقلبان «ياء» في النصب والجر،",
     "en": "The alif in “ḍāribāni” and the wāw in “ḍāribūna” are not pronouns, because they change to “yāʾ” in the accusative and genitive,"},
    {"type": "matn",
     "ar": "والضمائر لا تتغير عن حالها إلا أن يتغير عاملها، والعامل هنا ليس عاملا في الضمير،",
     "en": "whereas pronouns do not change from their state unless their governor changes; and the governor here does not govern the pronoun:"},
    {"type": "matn",
     "ar": "وإنما هو عامل في اسم الفاعل، والضمير فاعل له، والضمير باق على ما كان عليه في الرفع،",
     "en": "it governs only the active participle, the pronoun is its agent, and the pronoun remains as it was in the nominative."},
    {"type": "matn",
     "ar": "فلو كانت ضمائر لا تتغير[[٣]]، ألا ترى أن الياء في «تضربين»، والنون في «يضربن»، والواو في «يضربون»، والألف في «يضربان» لا تتغير",
     "en": "So if they were pronouns, they would not change. Do you not see that the yāʾ in “taḍribīna”, the nūn in “yaḍribna”, the wāw in “yaḍribūna” and the alif in “yaḍribāni” do not change?"},
    {"type": "matn",
     "ar": "فيهما أي: الألف والواو في الصفة حرف التثنية والجمع[[٤]]، وليستا بضميرين.",
     "en": "In the two of them, that is, the alif and the wāw in the adjective, are the particle of the dual and the plural, and they are not pronouns."},
    {"type": "matn",
     "ar": "(ولا يسوغ) أي: لا يجوز الضمير (المنفصل[[٥]]) مرفوعا كان أو منصوبا لأجل شيء[[٦]] (إلا لتعذر المتصل[[٧]]) أي: لأجل تعذره؛",
     "en": "(The detached) pronoun (is not admissible), that is, is not permitted, whether nominative or accusative, for any reason (except when the attached is impossible), that is, on account of its impossibility,"},
    {"type": "matn",
     "ar": "لأن وضع الضمائر للاختصار، والمتصل أخصر، فمتى أمكن الاتصال لا يسوغ الانفصال.",
     "en": "because pronouns are coined for brevity, and the attached is briefer; so whenever attachment is possible, detachment is not admissible."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ليس حالا من الصفة كما يشعر به قوله: سواء كانت اسم الفاعل، وإلا لوجب أن يقال: مطلقة",
     "en": "It is not a circumstantial qualifier of “the adjective”, as his words “whether it is the active participle” suggest; otherwise one would have to say “muṭlaqatan”;"},
    {"type": "pair",
     "ar": "ولا من الضمير المرفوع كما يشعر به قوله: وسواء كان أي الضمير مفردا إلى آخره لا سواء كان الصفة،",
     "en": "nor of the nominative pronoun, as his words “and whether it — that is, the pronoun — is singular…” to the end suggest, not “whether the adjective is”;"},
    {"type": "pair",
     "ar": "وإلا لوجب أن يقال: سواء كانت مفردة أو مثناة أو مجموعة مذكرة أو مؤنثة؛ لأنه لا يصح حينئذ قوله: سواء كانت اسم الفاعل",
     "en": "otherwise one would have to say “whether it is singular, dual or plural, masculine or feminine” [in the feminine], because then his words “whether it is the active participle” would not be sound;"},
    {"type": "pair",
     "ar": "بل ظرفا أي: زمانا مطلقا سواء كان زمان كون الصفة اسم فاعل أو غيره، وسواء كان زمان كون المرفوع المتصل مفردا أو غيره،",
     "en": "rather, it is an adverb, that is, “at any time”, whether the time when the adjective is an active participle or something else, and whether the time when the attached nominative is singular or otherwise."},
    {"type": "pair",
     "ar": "فقوله: سواء كانت إلى آخره بيان المطلق بمعنى زمانا مطلقا بحسب المعنى.",
     "en": "So his words “whether it is…” to the end explain “muṭlaqan” in the sense of “at any time”, according to the meaning."},
    {"type": "pair",
     "ar": "قال عبد الغفور: تذكير قوله «مطلقا» باعتبار أن الصفة هو الوصف.",
     "en": "ʿAbd al-Ghafūr said: the masculine of his word “muṭlaqan” is because al-ṣifa is [taken as] al-waṣf."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا حاجة إلى هذا القيد؛ لأن الكلام في بيان استتار المرفوع المتصل حيثما كان، ولا يكون في المسند إلى الظاهر",
     "en": "There is no need for this qualification, because the discussion concerns the concealment of the attached nominative wherever it occurs, and it does not occur in what is attributed to an overt noun;"},
    {"type": "pair",
     "ar": "لا في بيان وجود المرفوع المتصل حتى يحتاج إلى تقييد الماضي الغائب بهذا القيد، وقس عليه نظائره.",
     "en": "it is not about the existence of the attached nominative, such that the third-person past would need to be restricted by this qualification. Judge its parallels by analogy with it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الصواب: لما تغيرت، وكأنه سهو من الناسخ.",
     "en": "The correct [reading] is “they would not have changed” (lamā taghayyarat); it seems to be a slip of the copyist."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر: حرفا التثنية والجمع.",
     "en": "The apparent [reading] is “the two particles of the dual and the plural” (ḥarfā)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا ينحصر صور الانفصال فيما ذكره؛ لأن الصفة الواقعة بعد حرف النفي أو حرف الاستفهام إذا كانت عاملة في الضمير الفاعل يجب انفصاله نحو: «أقائم أنتم»،",
     "en": "The cases of detachment are not confined to what he mentioned, because when an adjective occurring after a particle of negation or interrogation governs the agent pronoun, that pronoun must be detached, as in “a-qāʾimun antum” (are you standing?)."},
    {"type": "pair",
     "ar": "وذلك لأن عامله أحد جزئي الجملة، فاعتنى بإبرازه، وكذا فاعل المصدر.",
     "en": "That is because its governor is one of the two parts of the sentence, so care was taken to make it visible; the same holds of the agent of the verbal noun."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "نبه على أن اللام قوله: إلا لتعذر المتصل للتعليل لا للوقت؛ لأنه علم في التعليل،",
     "en": "He indicated that the lām in his words “illā li-taʿadhdhuri al-muttaṣil” is causal, not temporal, because it is well established in causation."},
    {"type": "pair",
     "ar": "فمتى أمكن لا يعدل عنه، وفيه تعريض لمن جوزهما هنا على السواء.",
     "en": "So whenever [that reading] is possible it is not abandoned; and in this there is an allusion against whoever permitted both here equally."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "اللام للوقت أو للأجل.",
     "en": "The lām is temporal or causal."},
]
