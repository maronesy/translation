# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 312 (printed ٣١١)."""

PAGE_NUMBER = 312
PRINTED_PAGE = "٣١١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the list of three things begun at the foot of PDF p. 311.
    {"type": "matn",
     "ar": "٢- وانتفاء التعريف.",
     "en": "2. The absence of definiteness."},
    {"type": "matn",
     "ar": "٣- وانتفاء التخصيص يستلزم جواز التركيب الأول وامتناع الثاني،",
     "en": "3. And the absence of specification; [this sum] entails the permissibility of the first construction and the impossibility of the second."},
    {"type": "matn",
     "ar": "ولا يلزم من ذلك أن يكون لكل واحد من تلك الأمور دخل في ذلك الاستلزام، بل يجوز أن يكون باعتبار بعضها،",
     "en": "It does not follow from that that each one of those things has a part in that entailment; rather, it may be by virtue of some of them;"},
    {"type": "matn",
     "ar": "فلا يرد أنه لا دخل في ذلك الاستلزام لانتفاء التخصيص[[١]].",
     "en": "so the objection does not arise that the absence of specification has no part in that entailment."},
    {"type": "matn",
     "ar": "(و) من جهة أنها تفيد تخفيفا[[٢]] (جاز) تركيب («الضاربا زيد»، و«الضاربو زيد») لحصول التخفيف بحذف النون",
     "en": "(And) because it conveys lightening, (it was permissible) to construct (“al-ḍāribā Zaydin” [the two beating Zayd] and “al-ḍāribū Zaydin” [those beating Zayd]), since lightening is obtained by dropping the nūn;"},
    {"type": "matn",
     "ar": "(وامتنع «الضارب زيد») لعدم التخفيف؛ لأن تنوين «الضارب» إنما سقط للألف واللام لا للإضافة،",
     "en": "(and “al-ḍārib Zaydin” was impossible), for lack of lightening, because the tanwīn of “al-ḍārib” dropped only because of the alif and lām [of the article], not because of the annexation."},
    {"type": "matn",
     "ar": "ولا شك أنه لا دخل في هذا التفريع لانتفاء التعريف ولا لانتفاء التخصيص، بل يكفي فيه وجوب التخفيف فقط،",
     "en": "There is no doubt that neither the absence of definiteness nor the absence of specification has any part in this derived rule; rather, the requirement of lightening alone suffices for it;"},
    {"type": "matn",
     "ar": "وعلى هذا كان الأنسب تقديم هذا الفرع[[٣]]، لكنه أخره لكثرة لواحقه",
     "en": "on this basis it would have been more fitting to put this derived rule first, but he put it later because of the many matters attached to it."},
    {"type": "matn",
     "ar": "(خلافا للفراء[[٤]]) فإنه يجوز تركيب «الضارب زيد»:",
     "en": "(Contrary to al-Farrāʾ), for he permits the construction “al-ḍārib Zaydin”:"},
    {"type": "matn",
     "ar": "إما لأنه توهم أن دخول لام التعريف إنما هو بعد الإضافة، فحصل التخفيف بحذف التنوين بسبب الإضافة، ثم عرف باللام.",
     "en": "either because he supposed that the definite article enters only after the annexation, so that lightening was obtained by dropping the tanwīn on account of the annexation, and then it was made definite by the article."},
    {"type": "matn",
     "ar": "وأجاب المصنف[[٥]] عنه في شرحه: بأنه غير مستقيم؛ لأن القول بتأخر اللام المتقدمة حسا على الإضافة مجردا وادعاء مخالف للظاهر.",
     "en": "The author answered this in his commentary: it is not sound, because to hold that the article, which perceptibly comes first, comes after the annexation is a bare claim contrary to the apparent."},
    # REVIEW: the matn prints «الأعشي» with the dots of yāʾ, while footnote ٦ has «الأعشى»; transcribed as printed.
    {"type": "matn",
     "ar": "وإما لما وقع في شعر الأعشي[[٦]] من قوله: «الواهب المائة الهجان وعبدها»",
     "en": "Or because of what occurs in the poetry of al-Aʿshā, in his words: “al-wāhibu l-miʾati l-hijāni wa-ʿabdihā” (the giver of the hundred white camels and their herdsman);"},
    {"type": "matn",
     "ar": "فإن قوله: «وعبدها» بالجر معطوف على «المائة»، فصار المعنى باعتبار العطف «الواهب",
     "en": "for his word “wa-ʿabdihā,” in the genitive, is coordinated with “al-miʾa,” so that the sense, taking the coordination into account, became “al-wāhib…"},

    {"type": "rule"},

    # ---------------- Footnote ٢ of PDF p. 311, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "إفادة التخصيص؛ لأن معنى واحدا في الإضافة يوجب التعريف والتخصيص،",
     "en": "…of conveying specification, because a single meaning in annexation necessitates both definiteness and specification;"},
    {"type": "pair",
     "ar": "وإنما تفاوت الإيجاب بتفاوت المضاف إليه في التعريف والنكارة.",
     "en": "the necessitating differs only as the annexing term differs in definiteness and indefiniteness."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قد عرفت دفعه بما هو الأحق بالاختيار.",
     "en": "You have already learned its rebuttal by what is most deserving of being chosen."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى أن يقال: من جهة أنها لا تفيد تعريفا وتفيد تخفيفا افترق «الضاربا زيد» و«الضارب زيد» في الجواز والامتناع؛",
     "en": "It would be better to say: because it does not convey definiteness and does convey lightening, “al-ḍāribā Zaydin” and “al-ḍārib Zaydin” differed in permissibility and impossibility;"},
    {"type": "pair",
     "ar": "إذ لو أفادت التعريف لتساويا في الامتناع، ولو لم تفد التخفيف لتساويا في الجواز.",
     "en": "for had it conveyed definiteness, the two would have been equal in impossibility; and had it not conveyed lightening, they would have been equal in permissibility."},
    # REVIEW: «لتساويا في الجواز» as printed; the argument seems to require equality in impossibility when lightening is absent; transcribed as printed.

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: لأن إفادة التخفيف مذكورة صريحا بخلاف انتفاء إفادة التعريف والتخصيص،",
     "en": "It has been said: because the conveying of lightening is stated explicitly, unlike the absence of conveying definiteness and specification;"},
    {"type": "pair",
     "ar": "وتقديم المتفرع على مصرح أولى من تقديم المتفرع على المذكور ضمنا.",
     "en": "and putting first what derives from something explicit is better than putting first what derives from something mentioned implicitly."},
    {"type": "pair",
     "ar": "ويعارضه أن النفي مقدم على الإثبات، فالترتيب الذكري في الاستدلال مرعي فيما فعله المصنف.",
     "en": "Against this stands [the principle] that negation precedes affirmation; so the order of mention in the argument is observed in what the author did."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: يخالف هذا القول خلافا للفراء.",
     "en": "That is, this statement differs, in disagreement with al-Farrāʾ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وأجاب بعضهم بأن الإضافة ضائعة بقاء وإن كانت مفيدة ابتداء،",
     "en": "Some answered that the annexation is wasted in its continuance, even if it was beneficial at the outset;"},
    {"type": "pair",
     "ar": "فيلزم بعد إدخال اللام عدم بقائها، والرجوع إلى النصب الذي هو الأصل لزوال ما عرضت الإضافة لأجله.",
     "en": "so after the article is introduced it must not remain, and there must be a return to the accusative, which is the original, since that for whose sake the annexation occurred has gone."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأعشى اسم لخمسة عشر شاعرا بخمسة عشر قبائل، وتفصيله في القاموس.",
     "en": "Al-Aʿshā is the name of fifteen poets from fifteen tribes; the details are in al-Qāmūs."},
]
