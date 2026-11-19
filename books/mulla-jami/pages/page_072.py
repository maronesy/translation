# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 72 (printed ٧١)."""

PAGE_NUMBER = 72
PRINTED_PAGE = "٧١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "حقيقة أو حكما[[١]]، ليشمل الملحقات به.",
     "en": "…either in reality or by status — so as to include what is annexed to it."},
    {"type": "matn",
     "ar": "(والجر) حركة كان أو حرفا (علم الإضافة) أي: علامة كون الشيء مضافا إليه[[٢]].",
     "en": "“And jarr” — whether a vowel or a letter — “is the mark of annexation (ʿalam al-iḍāfa),” that is, the sign that the thing is that to which annexation is made (muḍāf ilayhi)."},
    {"type": "matn",
     "ar": "وإذا كانت الإضافة نفسها مصدرا لم يحتج إلى إلحاق الياء المصدرية[[٣]] إليها، كما في الفاعلية والمفعولية.",
     "en": "Since annexation (iḍāfa) is itself a verbal noun (maṣdar), there is no need to append the maṣdar-forming yāʾ to it, as [is done] in fāʿiliyya and mafʿūliyya."},
    {"type": "matn",
     "ar": "وإنما اختص الرفع بالفاعل[[٤]]، والنصب بالمفعول؛ لأن الرفع ثقيل، والفاعل قليل؛ لأنه واحد، فأعطي الثقيل للقليل[[٥]]،",
     "en": "Rafʿ was assigned specifically to the agent, and naṣb to the object, only because rafʿ is heavy while the agent is few — since it is single — so the heavy was given to the few;"},
    {"type": "matn",
     "ar": "والنصب خفيف، والمفاعيل كثيرة[[٦]]؛ لأنها خمسة، فأعطي الخفيف للكثير، ولما لم يبق للمضاف إليه علامة غير الجر جعل علامة له.",
     "en": "and naṣb is light while the objects are many — for they are five — so the light was given to the many; and since no mark remained for the muḍāf ilayhi other than jarr, it was made its mark."},

    {"type": "section", "ar": "[ العامل ]",
     "en": "The Governing Agent (al-ʿĀmil)"},

    {"type": "matn",
     "ar": "(والعامل) لفظيا كان أو معنويا (ما به[[٧]] يتقوم[[٨]]) أي: يحصل (المعنى المقتضي)",
     "en": "“And the governing agent (al-ʿāmil),” whether verbal (lafẓī) or semantic (maʿnawī), “is that by which is constituted” — that is, brought about — “the necessitating meaning (al-maʿnā al-muqtaḍī),”"},
    {"type": "matn",
     "ar": "أي: معنى من المعاني[[٩]] المعتورة على المعرب المقتضية (للإعراب).",
     "en": "that is, one of the meanings that successively befall the declinable word, [the meanings] that necessitate iʿrāb."},
    {"type": "matn",
     "ar": "ففي: «جاءني زيد»[[١٠]]، «جاء» عامل؛ إذ به[[١١]] حصل معنى الفاعلية[[١٢]] في",
     "en": "For in “Zayd came to me” (jāʾanī Zaydun), “came” (jāʾa) is the governing agent, since through it the meaning of agenthood came about in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وذلك فيما إذا كان الاسم فضلة.",
     "en": "And that is in the case where the noun is a surplus element (faḍla)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بقرينة المقابلة للفاعلية والمفعولية، فإنه مقابل لهما لا يكون مضافا. وإنما لم يقل: حقيقة أو حكما؛ لأن الجر لا وجود له في غير المضاف إليه.",
     "en": "This is by the indication of [its] contrast with fāʿiliyya and mafʿūliyya, for what stands opposite them is not made muḍāf. He did not say “in reality or by status” because jarr has no existence except in the muḍāf ilayhi."},
    {"type": "pair",
     "ar": "وأما نحو: بحسبك زيد، فلما كان الجار زائدا فيه لم يعتدوا به، أو كان الجر زائدا كالجار، فكأنه ليس علامة.",
     "en": "As for [expressions] like “Zayd suffices you” (bi-ḥasbika Zaydun), since the preposition (jārr) in it is redundant they did not reckon with it; or the jarr [itself] is redundant like the preposition, so that it is as though it were not a mark."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى لم يصح إلحاق الياء المصدرية؛ لأن الياء المصدرية لا تلحق المصدرية.",
     "en": "The better [wording]: it would not be valid to append the maṣdar-forming yāʾ, because the maṣdar-forming yāʾ is not appended to that which already carries maṣdar-ness (al-maṣdariyya)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الاختصاص إضافي بالنسبة إلى المفاعيل والمضاف إليه، وإلا فالرفع غير مختص بالفاعل، بل هو موجود في الملحقات بالفاعل أيضا.",
     "en": "The specification is relative — in relation to the objects and the muḍāf ilayhi — for otherwise rafʿ is not specific to the agent, but is found also in what is annexed to the agent."},
    {"type": "pair",
     "ar": "وإنما بين الاختصاص في الفاعل لكونه أصلا في الإعراب من حيث إنه معمول ما هو أصل في العمل.",
     "en": "He clarified the specification with respect to the agent only because it is the original locus in iʿrāb, inasmuch as it is the operand of that which is original in governance (ʿamal)."},
    {"type": "pair",
     "ar": "فإن قلت: المضاف إليه أيضا قليل فلم لم يعط الرفع إياه؟ قلت: الاهتمام بشأن الفاعل أكثر لكونه معمول ما هو أصل في العمل، أو المراد أن الفاعل لا يوجد في الكلام الواحد إلا واحدا، بخلاف المضاف إليه والمفعول، فيكون الفاعل قليلا في الكلام، فأعطي الثقيل إياه.",
     "en": "If you say: the muḍāf ilayhi is also few, so why was rafʿ not given to it? — I say: the concern with the affair of the agent is greater, because it is the operand of that which is original in governance; or what is meant is that the agent occurs only once in a single utterance, unlike the muḍāf ilayhi and the object, so the agent is “few” in the utterance, and thus the heavy was given to it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأولى ترك اللام، لأنه المفعول الثاني لـ«أعطى»، ودخول لام التقوية في المعمول المتأخر لا يجوز.",
     "en": "The better [course] is to omit the lām, because it is the second object of “aʿṭā” (to give), and the introduction of the strengthening lām (lām al-taqwiya) upon a postposed operand is not permissible."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أو ضعيف، والفضلة ضعيفة، فجعل الضعيف للضعيف.",
     "en": "Or [naṣb is] weak, and the surplus element (faḍla) is weak, so the weak was assigned to the weak."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الباء للسببية.",
     "en": "The bāʾ [in bihi] denotes causality (sababiyya)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فسر بالنكرة للاهتمام لا للحصر؛ إذ لا دخل له في التعريف.",
     "en": "It was interpreted as indefinite (nakira) for the sake of emphasis, not restriction, since [indefiniteness] has no bearing on definition."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فسر بالنكرة إشارة إلى أن اللام في المعنى للعهد الذهني الذي هو في حكم النكرة؛ إذ المتقوم بالعامل هو معنى من المعاني المعتورة.",
     "en": "It was interpreted as indefinite to indicate that the lām in “al-maʿnā” denotes mental determination (al-ʿahd al-dhihnī), which has the ruling of the indefinite, since what is constituted by the governing agent is one of the meanings that successively befall [the word]."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "الفاء للتفسير والإيضاح.",
     "en": "The fāʾ [in fa-fī] is for explanation and clarification."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: بسببه.",
     "en": "That is: by reason of it."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "لأن له استدعاء الإسناد إليه.",
     "en": "Because it entails the requirement of predication being made to it."},
]
