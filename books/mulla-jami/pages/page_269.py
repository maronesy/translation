# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 269 (printed ٢٦٨)."""

PAGE_NUMBER = 269
PRINTED_PAGE = "٢٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "ويمكن أن يجاب عنه: بأن المراد بالأنواع حصص الجنس[[١]]؛ سواء كانت بالخصوصيات الكلية أو الشخصية.",
     "en": "One may answer this by [saying] that what is meant by “species” is the portions (ḥiṣaṣ) of the genus, whether [they are distinguished] by universal or by individual particularities."},
    {"type": "matn",
     "ar": "(ويجمع) أي: يورد التمييز على ما فوق الواحد[[٢]] جوازا حيث لم يقصد الواحد (في غيره) أي: في غير الجنس، نحو: «عندي عدل ثوبين أو أثوابا».",
     "en": "(And it is put in the plural), that is, the tamyīz may be given in a form for more than one, where one is not intended, (in other than it), that is, in other than a genus, as in “I have a load of two garments, or of garments.”"},
    {"type": "matn",
     "ar": "(ثم إن كان) أي: المفرد المقدار[[٣]] تاما (إما بتنوين أو بنون التثنية)",
     "en": "(Then if it is), that is, the single term that is a measure, complete (either by tanwīn or by the nūn of the dual);"},
    {"type": "matn",
     "ar": "أو المعنى: إن وجد التمييز[[٤]] متلبسا بتنوين المفرد أو بنونه التي للتثنية،",
     "en": "or the meaning is: if the tamyīz is found in conjunction with the tanwīn of the single term or with its nūn of the dual;"},
    {"type": "matn",
     "ar": "فإنه لما تم الاسم بهما اقتضى التمييز",
     "en": "for when the noun is completed by these two it calls for the tamyīz,"},
    {"type": "matn",
     "ar": "(جازت الإضافة) أي: إضافة المفرد المقدار إلى التمييز إضافة بيانية، بإسقاط التنوين ونون التثنية، جوازا شائعا كثيرا لحصول الغرض، وهو رفع الإبهام بذلك مع التخفيف",
     "en": "(the genitive construction is permitted), that is, putting the single term of measure into an explicative genitive construction (iḍāfa bayāniyya) with the tamyīz, dropping the tanwīn and the nūn of the dual; this is widely and frequently permitted because the purpose, namely the removal of vagueness, is achieved by it along with lightness,"},
    {"type": "matn",
     "ar": "نحو: «رطل زيت، ومنوا سمن» (وإلا) أي: وإن لم يكن بتنوين أو بنون التثنية",
     "en": "as in “a raṭl of oil” and “two manns of clarified butter” [in the genitive]. (Otherwise), that is, if it is not by tanwīn or by the nūn of the dual…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 268 (no. ٥ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "التمييز عن ذات مذكورة، فهو خارج عما نحن بصدده.",
     "en": "…the tamyīz from a mentioned entity, so it lies outside what we are dealing with."},
    {"type": "pair",
     "ar": "واعترض عليه بأن التاء أخرج الكلمة عن كونها جنسا، فهو خارج عما نحن فيه.",
     "en": "It has been objected that the tāʾ removed the word from being a genus, so it lies outside what we are concerned with."},
    {"type": "pair",
     "ar": "وفيه نظر: أما أولا: فلأن التاء فيها من أصل الكلمة سواء كانت صيغة المرة أو النوع، وليست الفارقة بين الجنس والوحدة،",
     "en": "This is open to question. First, because the tāʾ in it belongs to the base of the word, whether it is the form of a single instance or of a manner, and is not the tāʾ that distinguishes the genus from the unit;"},
    {"type": "pair",
     "ar": "فلا ينافي كون الكلمة اسم جنس شاملا للتقليل والكثير من أنواع الجلوس أو آحادها.",
     "en": "so it does not conflict with the word’s being a generic noun covering few and many of the kinds of sitting or of its single instances."},
    # REVIEW: «للتقليل والكثير» as printed (one would expect «للقليل»); transcribed as printed.
    {"type": "pair",
     "ar": "وأما ثانيا: فلأن المناقشة في المثال ليست من دأب المحصلين.",
     "en": "Second, because disputing an example is not the practice of accomplished scholars."},
    {"type": "pair",
     "ar": "والجواب: بأن الشارح أجاب على سبيل التنزيل ليس مما يستحسنه أرباب الترقي.",
     "en": "And the reply that the commentator answered by way of concession (tanzīl) is not something those who seek higher [answers] approve of."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا بعيد جدا. ومع ذلك الأولى أن يقال: أفراد الجنس بدل الحصص؛",
     "en": "This is very far-fetched. Even so, it would be better to say “the individuals of the genus” instead of “the portions,”"},
    {"type": "pair",
     "ar": "لأن الحصة لا تطلق على المتعارف إلا على الفرد الاعتباري الذي يحصله العقل من أخذ المفهوم الكلي مع الإضافة إلى معين، ولا يطلق على الفرد الحقيقي.",
     "en": "because in common usage “portion” (ḥiṣṣa) applies only to the notional individual that the intellect produces by taking the universal concept together with a relation to something determinate; it does not apply to the real individual."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قد جاوز حد التكلف كيف، والجمع إذا قوبل بالأفراد يراد به صيغة الجمع مع أنه لا حاجة إلى تكلف؛",
     "en": "He has gone beyond the bounds of strained interpretation, how so? For “plural,” when contrasted with “singular,” means the plural form; moreover, there is no need for strain,"},
    {"type": "pair",
     "ar": "لأن المصنف لم يجوز في قصد المتعدد إلا صيغة الجمع، فلا يجوز عنده إلا عدل أثوابا صرح به في إيضاح المفصل.",
     "en": "because the author permitted only the plural form when plurality is intended; so in his view only “a load of garments” is permitted, as he stated explicitly in Īḍāḥ al-Mufaṣṣal."},
    {"type": "pair",
     "ar": "ويؤيده أنه لولا المراد بقوله: ويجمع في غيره صيغة الجمع لكان مستغنى عنه.",
     "en": "This is supported by the fact that, were the plural form not what is meant by his words “and it is put in the plural in other than it,” they would be superfluous."},
    {"type": "pair",
     "ar": "اعلم أن سوق الكلام ناظر إلى أن المراد بغيره غير الجنس.",
     "en": "Know that the drift of the discourse indicates that what is meant by “other than it” is other than a genus."},
    {"type": "pair",
     "ar": "والتحقيق أن المراد غير الجنس، والجنس المقصود به الأنواع.",
     "en": "The precise view is that what is meant is what is not a genus, and the genus by which the species are intended."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الظاهر أن الضمير راجع إلى المفرد المقدار غير العدد، وإن كان الحكم المذكور شاملا للمفرد المقدار مطلقا.",
     "en": "Apparently the pronoun refers to the single term of measure other than number, even though the ruling mentioned covers the single term of measure without qualification."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا موجب لجعل كان في التوجيه الأول ناقصة، والثاني تامة.",
     "en": "There is no reason to take “kāna” in the first interpretation as incomplete (nāqiṣa) and in the second as complete (tāmma)."},
    {"type": "pair",
     "ar": "وكأنه أراد الإشارة إلى توجيهين لكان في التوجيهين.",
     "en": "It is as though he wished to point to two construals of “kāna” in the two interpretations."},
    {"type": "pair",
     "ar": "والتوجيه الثاني بعيد جدا؛ لأن جعل التمييز متلبسا بتنوين المبهم أو نونه ركيك جدا.",
     "en": "The second interpretation is very far-fetched, because making the tamyīz conjoined with the tanwīn or the nūn of the vague noun is very weak."},
    {"type": "pair",
     "ar": "والمتبادر من قوله: جاز الإضافة المتلبس بالتنوين لا إضافة الشيء إليه، ولا داعي إليه إلا مراعاة مشاركة ضمير مفرد، وإن كان في المرجع.",
     "en": "What first comes to mind from his words “the genitive construction is permitted” is [the iḍāfa of] what is conjoined with the tanwīn, not the annexing of something to it; and nothing calls for [the second interpretation] except keeping the singular pronoun shared, even if in its referent."},
    {"type": "pair",
     "ar": "والمصنف نبه على ذلك التفاوت بالعطف بـ«ثم»، فإنه ليس هنا للتراخي في الزمان، بل لتفاوت الحكمين، وإن أخذهما متعلق بالتمييز والآخر بالمميز.",
     "en": "The author drew attention to this difference by conjoining with “thumma,” for here it does not denote delay in time but the difference between the two rulings, in that one of them concerns the tamyīz and the other the specified term (mumayyaz)."},
    # REVIEW: «وإن أخذهما» as printed (sense requires «وأن أحدهما»); transcribed as printed.
]
