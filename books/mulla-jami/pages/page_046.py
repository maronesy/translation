# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 46 (printed ٤٥)."""

PAGE_NUMBER = 46
PRINTED_PAGE = "٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فعلم لكل واحد منها معرف جامع لأفراده، ومانع عن دخول غيرها فيه.",
     "en": "So there has come to be known, for each one of them, a definer (muʿarrif) inclusive of its instances and preventive of the entry of others into it."},
    {"type": "matn",
     "ar": "وليس المراد بالحد ههنا[[١]] إلا المعرف الجامع المانع.",
     "en": "And nothing is intended by “definition” (ḥadd) here except the inclusive, exclusive definer (al-jāmiʿ al-māniʿ)."},
    {"type": "matn",
     "ar": "ولله در المصنف[[٢]]، حيث أشار إلى حدودها في ضمن دليل الحصر، ثم نبه عليها بقوله: «وقد علم بذلك»، ثم صرح بها فيما بعد[[٣]] بناء على تفاوت مراتب الطبائع[[٤]].",
     "en": "How excellent is the author! — for he pointed to their definitions within the proof of restriction, then drew attention to them by his words “and by that it has been known,” then stated them explicitly afterwards, on the basis of the disparity of the ranks of natural dispositions (ṭabāʾiʿ)."},

    {"type": "section", "ar": "[الكلام]", "en": "Speech (al-Kalām)"},

    {"type": "matn",
     "ar": "(الكلام)[[٥]] في اللغة: ما يتكلم به[[٦]] قليلا كان أو كثيرا[[٧]].",
     "en": "(Speech, al-kalām), in the language, is: that which is uttered, be it little or much."},
    {"type": "matn",
     "ar": "وفي اصطلاح النحاة: (ما تضمن) أي: لفظ تضمن[[٨]] (كلمتين) حقيقة أو حكما، أي: يكون كل واحدة منهما في ضمنه[[٩]].",
     "en": "And in the technical usage of the grammarians: (that which comprises) — that is, an utterance (lafẓ) that comprises — (two words), whether in reality or in ruling (ḥukman); that is: such that each of the two is contained within it."},
    {"type": "matn",
     "ar": "فالمتضمن: -اسم فاعل- هو المجموع، والمتضمن: -اسم مفعول- هو",
     "en": "So “that which comprises” (al-mutaḍammin) — an active participle — is the totality; and “that which is comprised” (al-mutaḍamman) — a passive participle — is…"},  # continues on the next page

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: في هذا الفن، فإن الحد عند الأدباء هو المعرف الجامع المانع، أو في هذا المقام؛ لأن المركب مما فيه الاشتراك، وما به الامتياز لا يستلزم أن يكون حدا مقابلا للرسم.",
     "en": "That is: in this discipline — for “definition” among the litterateurs (udabāʾ) is the inclusive, exclusive definer — or in this particular context; because that which is composed of that in which there is commonality and that by which distinction [is effected] does not necessarily constitute a “definition” (ḥadd) as opposed to a “description” (rasm)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الدر في اللغة: اللبن، وفيه خير كثير عند العرب، فأريد به الخير مجازا. فيقال في الذم: «لا در دره»، أي: لا كثر خيره، وفي المدح: «لله دره».",
     "en": "“Al-darr” in the language means milk, and in it there is much good (khayr) in the view of the Arabs; so by it “good” is intended figuratively. Thus it is said, in dispraise: “lā darra darruhu” — that is, may his good not increase — and, in praise: “li-Llāhi darruhu.”"},
    {"type": "pair",
     "ar": "وذلك لأن العرب إذا عظموا شيئا نسبوه إلى الله سبحانه قصدا إلى أن غيره لا يقدر عليه. وقد يقال: اللام للتعجب، والدر اللبن، والمعنى: تعجبوا من لبن أم ربت به كاملا في العلم أو القدر إلى غير ذلك من الصفات الكمالية.",
     "en": "That is because the Arabs, when they magnified something, would ascribe it to Allah, Glorified is He, intending [thereby] that none other than He is capable of it. It may also be said: the lām is for wonderment (taʿajjub), and “al-darr” is milk — the meaning being: they marvel at the milk of a mother that nurtured, by it, one perfect in knowledge, or in worth, and other than that of the perfective attributes."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا التصريح في حد الحرف غير ظاهر، فإن ما فهم في ضمن دليل الحصر هو ما لا يدل على معنى في نفسها، وما صرح به بعد هو ما دل على معنى في غيره، فهما متغايران وإن كانا متلازمين.",
     "en": "This explicit statement, in the case of the definition of the particle, is not evident; for what was understood within the proof of restriction is “that which does not signify a meaning in itself,” whereas what was explicitly stated afterwards is “that which signifies a meaning in another” — the two being distinct, even if mutually entailing."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: العقول.",
     "en": "That is: the intellects (al-ʿuqūl)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يعطف على السابق؛ لأنه فصل آخر من الكلام.",
     "en": "He did not conjoin it to what precedes, because it is another section of the discourse."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ثم استعمل استعمال المصدر، فقيل: «كلمته كلاما» كـ«أعطى عطاء»، مع أنه في الأصل لما يعطى.",
     "en": "Then it was used with the usage of a verbal noun (maṣdar), so one says “kallamtuhu kalāman” (I spoke to him a speaking), like “aʿṭā ʿaṭāʾan” (he gave a giving) — even though [“ʿaṭāʾ”] is, in origin, [a name] for that which is given (li-mā yuʿṭā)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا يظهر داع إلى ترك بيان المعنى اللغوي للكلمة، وهو اللفظة، وتخصيص المعنى اللغوي للكلام بالبيان.",
     "en": "No motive appears for omitting the clarification of the lexical meaning of “the word” (kalima) — which is “the utterance” (al-lafẓa) — while singling out the lexical meaning of “speech” (kalām) for clarification."},
    {"type": "pair",
     "ar": "ولا يخفى أن الكلمة أنسب بمعناه الاصطلاحي من الكلام لشمول الكلام الكثير دون الكلمة، وأن الكلمة لا يناسب المعنى الاصطلاحي للكلام، فتخصيص كل من اللفظين بما خصا به اصطلاحا ليس لمجرد التمييز بينهما في الاسم.",
     "en": "It is not hidden that “the word” (kalima) is more fitting for its technical meaning than “speech” (kalām) is — because “speech” [lexically] embraces the much/abundant, not the single word — and that “the word” does not suit the technical meaning of “speech”; so the singling out of each of the two terms by what each was assigned technically is not merely for distinguishing between them in name."},
    {"type": "pair",
     "ar": "ومن المعاني اللغوية للكلام ما يكون مكتفيا به في أداء المرام على ما في القاموس. ولا يخفى أنه أشد مناسبة بما اصطلح عليه، فالأولى أن يجعل النقل عنه إليه.",
     "en": "And among the lexical meanings of “speech” there is that which suffices, by itself, for conveying the aim, as in al-Qāmūs. It is not hidden that it [that lexical sense] is more strongly suited to what was technically agreed upon; so it would be more fitting that the [technical] transfer be made from it to it [the technical sense]."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "تضمن الكل لجزأيه.",
     "en": "The comprising of the whole for its two parts."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فإن التثنية اختصار العطف، فكأنه قال: كلمة وكلمة. قيل: لو جعلت الباء للاستعانة لم يحتج إلى هذا التأويل؛ لأن المتضمن بالكسر مجموع الكلمتين والإسناد، والمتضمن بالفتح مجموع الكلمتين،",
     "en": "For the dual is an abbreviation of conjunction, so it is as though he said “a word and a word.” It has been said: had the bāʾ been taken for instrumentality (istiʿāna), there would be no need for this construal (taʾwīl); because “that which comprises” (al-mutaḍammin, with kasra) is the totality of the two words together with predication (isnād), while “that which is comprised” (al-mutaḍamman, with fatḥa) is the totality of the two words;"},
    {"type": "pair",
     "ar": "ولو جعلت بمعنى «مع» احتيج إلى أن يؤول بأن يقال: المتضمن بالكسر الأجزاء الثلاثة: الكلمتان والهيئة، والمتضمن بالفتح كل واحد من الأجزاء الثلاثة.",
     "en": "and were it [the bāʾ] taken in the sense of “with” (maʿa), it would need to be construed by saying: “that which comprises,” with kasra, is the three parts — the two words and the form (hayʾa) — while “that which is comprised,” with fatḥa, is each one of the three parts."},
    {"type": "pair",
     "ar": "ولا يخفى أن هذا القول مبني على جعل الهيئة جزءا للكلام، ويلزم حينئذ ألا يكون الكلام لفظا حقيقة، بل مسامحة. ولو لم يجعل جزءا له كما في الشرح احتيج إلى التأويل.",
     "en": "It is not hidden that this statement is built upon making the form (hayʾa) a part of “speech,” from which it then follows that speech would not be an utterance (lafẓ) in reality, but only by loose usage; and were it not made a part of it — as [is the case] in the Sharḥ — recourse to construal (taʾwīl) would [still] be needed."},
]
