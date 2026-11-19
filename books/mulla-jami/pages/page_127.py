# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 127 (printed ١٢٦)."""

PAGE_NUMBER = 127
PRINTED_PAGE = "١٢٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "مذكر لا يعقل[[١]]، ويجمع هذا الجمع مطردا صفة المذكر الذي لا يعقل؛ كـ«الصافنات» للذكور من الخيل[[٢]]، و«جمال سجلات» أي: ضخمات وكـ«الأيام الخاليات».",
     "en": "…masculine, non-rational; and by this [sound feminine] plural is regularly pluralized the adjective of the masculine non-rational, such as “al-ṣāfināt” for male horses, and “jimāl sijillāt” — that is, huge [camels] — and such as “al-ayyām al-khāliyāt” (the bygone days)."},
    {"type": "matn",
     "ar": "(هو) أي: المرفوع الدال عليه «المرفوعات»[[٣]]؛ لأن التعريف إنما يكون للماهية[[٤]] لا للأفراد[[٥]].",
     "en": "(it): that is, the nominative (al-marfūʿ) indicated by “the nominatives” (al-marfūʿāt); because a definition is only of the quiddity (māhiyya), not of the individuals (afrād)."},
    {"type": "matn",
     "ar": "(ما اشتمل) أي: اسم[[٦]] اشتمل (على علم الفاعلية[[٧]]) أي: علامة كون الاسم",
     "en": "(that which comprises): that is, a noun that comprises (the mark of agency, ʿalam al-fāʿiliyya) — that is, a sign that the noun is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: ويجوز أن يجمع بالألف والتاء صفة المذكر الذي لا يعقل من غير اشتراط شيء آخر، كما جاز أن يجمع المؤنث بهذا الجمع.",
     "en": "That is: the adjective of the masculine non-rational may be pluralized with alif and tāʾ [the sound feminine plural] without stipulating anything else, just as the feminine may be pluralized by this plural."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "كتب في الحاشية: الصافن من الخيل الذي يقوم على ثلاثة قوائم، وأقام الرابعة على طرف الحافر، هذا كلامه.",
     "en": "It was written in the gloss: the ṣāfin among horses is the one that stands upon three legs and raises the fourth upon the edge of the hoof — these are his words."},
    {"type": "pair",
     "ar": "والسبحل على وزن القمطر الضخم كالكتف للعظيم الجسد، والأيام الخاليات مجاز؛ لأن خلا المكان بمعنى مات، أو مضى على ما في القاموس، وتخلية المكان بالموت أو المضي ليس حال الأيام، بل حال ما فيها.",
     "en": "And al-sibaḥl, on the pattern of al-qimaṭr, is the huge one, like the shoulder-blade for one of great body. And “the bygone days” is a figurative usage, because “khalā” of a place means “it perished” or “it passed away,” as in al-Qāmūs; and the emptying of a place by death or passing is not the state of the days [themselves], but the state of what is in them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "دلالة الجمع على الجنس لا على فرده. فعلى هذا التفسير تكون جملة «هو ما اشتمل» منقطعة عن السابق،",
     "en": "The plural’s signification is of the genus, not of its individual. On this interpretation, the clause “it is that which comprises” is disconnected from what precedes,"},
    {"type": "pair",
     "ar": "وهو إما موقوف وقف الأسماء الغير المركبة مذكور للفصل، أو مرفوع على أنه مبتدأ محذوف الخبر، أو خبر محذوف المبتدأ، والتقدير: المرفوعات هذه، أو هذه المرفوعات.",
     "en": "and [the word “huwa”] is either suspended (mawqūf) in the manner of non-compound nouns, mentioned as a separator (faṣl); or in the nominative as a subject (mubtadaʾ) whose predicate is elided, or as a predicate whose subject is elided — the implied sense being: “these are the nominatives,” or “these nominatives.”"},
    {"type": "pair",
     "ar": "واللام لاستغراق الأنواع، ويحتمل على التقدير الأول العهد إلى ما يفهم من السابق حيث قال: وأنواعه: رفع ونصب وجر، وفيه تأمل.",
     "en": "The lām is for the all-inclusiveness of the kinds (istighrāq al-anwāʿ); and on the first estimation it may be for definite reference (ʿahd) to what is understood from the preceding, where he said: “and its kinds are: nominative, accusative, and genitive.” In this there is [room for] reflection."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فمن جعل الضمير راجعا إلى كل واحد من المرفوعات أول إلى المرفوعات. وقال: توحيده وتذكيره بالنظر إلى خبره، أعني: ما اشتمل فإن المبتدأ هو الخبر، فيجوز مطابقته له كما يجوز مطابقته للمرجع لم يأت بشيء؛",
     "en": "So whoever makes the pronoun refer to each one of the nominatives has [in effect] reduced it to “the nominatives.” And whoever said that its singularity and masculinity are by regard to its predicate — I mean “that which comprises,” for the subject is [identical with] the predicate, so its agreement with it is permissible just as its agreement with the antecedent is permissible — has brought nothing [conclusive];"},
    {"type": "pair",
     "ar": "إلا أن يقال: إن اللام أبطلت معنى الجمعية، وإقحام صيغة الجمع للإشارة إلى تعدد الأنواع، أو يقال: إن الكلام محمول على الطرد.",
     "en": "unless it be said that the lām nullified the sense of plurality, and that the insertion of the plural form is [only] to point to the multiplicity of the kinds; or it be said that the discourse is borne upon [general] currency (ṭard)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيلغو ذكر المفرد والإشعار به في مقام التعريف. ولك أن تقول: السنة فيما بين الأدباء تفسير المفرد المذكر لا فروعه.",
     "en": "So the mention of the individual, and the intimation of it, is of no account in the setting of a definition. And you may say: the custom among the litterateurs is to interpret [i.e. define via] the masculine singular, not its derivatives."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فسر بالاسم؛ لأن الكلام في مرفوعات الأسماء. وأيضا لو أبقى على عمومه لصدق تعريف المرفوع على الحروف الأواخر كدال «زيد» في «جاء زيد» مثلا مع أن المرفوع هو «زيد».",
     "en": "He interpreted [“mā”] as “noun,” because the discussion concerns the nominatives among nouns. Moreover, were it left in its generality, the definition of the nominative would hold true of final letters — such as the dāl of “Zayd” in “jāʾa Zaydun,” for example — even though the nominative is “Zayd” [itself]."},
    {"type": "pair",
     "ar": "فإن قيل: تفسير «ما» بالاسم في تعريف المرفوع يخرج الخبر الجملة عن التعريف مع أنه من جملة المرفوعات؟",
     "en": "If it be said: interpreting “mā” as “noun” in the definition of the nominative excludes the sentential predicate (al-khabar al-jumla) from the definition, even though it is among the nominatives?"},
    {"type": "pair",
     "ar": "أجيب: أن الاسم أعم من أن يكون حقيقة أو حكما، كما سيصرح بذلك في تعريف الفاعل والخبر الجملة اسم حكما.",
     "en": "The reply is: “noun” is more general than to be [only] a real noun or a noun by [legal/functional] status (ḥukman), as he will state explicitly in the definition of the agent; and the sentential predicate is a noun by status."},
    {"type": "pair",
     "ar": "وفيه أن هذا مخالف لما سيأتي في بحث المبتدأ والخبر، ولما هو المقرر عندهم من أن الجملة يكون خبرا مع بقاء كونها جملة من غير تأويلها بالمفرد،",
     "en": "Against this stands that it contradicts what will come in the discussion of subject and predicate, and what is established with them: that a sentence may be a predicate while remaining a sentence, without being construed as a single [noun];"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: إن المراد بالاسم الحكمي ما يصلح لأن يعبر عنه بالاسم المفرد مثل ما قاله المنطقيون في المفرد بالقوة. وبالجملة التي وقع خبر المبتدأ يصلح لأن يعبر عنها بالاسم المفرد كهذا أو ذاك كما بين في موضعه.",
     "en": "unless it be said that what is meant by the noun-by-status is that which is fit to be expressed by a single noun — like what the logicians said concerning the “potentially single”; and a sentence that has served as the predicate of a subject is fit to be expressed by a single noun, such as “this” or “that,” as has been clarified in its place."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يقل: «على الرفع»؛ لأن الخفاء في المرفوع ليس إلا باعتبار مأخذه، فإذا أخذ المأخذ في تعريفه صار من قبيل أخذ المعرف في تعريفه.",
     "en": "He did not say “[comprising] the nominative case (rafʿ)”; because the obscurity in the nominative [term] is only by regard to its derivational source, so if that source is taken into its definition, it becomes of the type of taking the defined into its own definition."},
    {"type": "pair",
     "ar": "ولئن تنزل عن ذلك فلا شبهة في إيهام الدور، ولأنه خال عن الإشارة إلى أصالة الرفع في الفاعل، وعن زيادة الإيضاح المناسبة لمقام التعريف.",
     "en": "And even if one concedes that point, there is no doubt about its suggesting circularity (dawr); and [also] because it would be devoid of the indication of the original belonging of the nominative case to the agent, and devoid of the added clarification befitting the setting of a definition."},
]
