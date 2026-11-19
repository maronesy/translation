# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 309 (printed ٣٠٨)."""

PAGE_NUMBER = 309
PRINTED_PAGE = "٣٠٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… بل لا يمكن أو» at the foot of PDF p. 308.
    {"type": "matn",
     "ar": "المراد بالتجريد تجرده وخلوه من التعريف عند الإضافة، سواء كان نكرة في نفسه من غير تجريد أو كان معرفة جردت عن التعريف،",
     "en": "…what is meant by stripping is its being bare and free of definiteness at the time of annexation, whether it is indefinite in itself without any stripping, or it is a definite noun that has been stripped of definiteness."},
    # REVIEW: print reads «للأدني» with the two dots of yāʾ (expected «للأدنى»); transcribed as printed.
    {"type": "matn",
     "ar": "وإنما يجب التجريد؛ لأن المعرفة لو أضيفت إلى النكرة لكان طلبا للأدني[[١]] -وهو التخصيص- مع حصول الأعلى -وهو التعريف-",
     "en": "Stripping is required only because, if a definite noun were annexed to an indefinite one, it would be seeking the lower, which is specification, while the higher, which is definiteness, is already present;"},
    {"type": "matn",
     "ar": "ولو أضيفت إلى المعرفة لكان تحصيل الحاصل[[٢]]، فتضيع الإضافة حيث لا تفيد تعريفا ولا تخصيصا.",
     "en": "and if it were annexed to a definite noun, it would be producing what is already produced (taḥṣīl al-ḥāṣil); so the annexation would be wasted, since it would convey neither definiteness nor specification."},
    {"type": "matn",
     "ar": "فإن قيل: لا فرق بين إضافة المعرفة وبين جعلها علما[[٣]] في نحو: «النجم، والثريا والصعق، وابن عباس» في لزوم تعريف المعرف، فما بالهم جوزوا هذا دون ذلك؟",
     "en": "If it is said: there is no difference between annexing a definite noun and making it a proper name, in such as “al-Najm” (the Pleiades), “al-Thurayyā” (the Pleiades), “al-Ṣaʿiq” and “Ibn ʿAbbās,” as regards entailing the defining of what is already defined; so why did they permit the latter but not the former?"},
    # REVIEW: print reads «لا نسلم إن في» with hamza below (expected «أن»); transcribed as printed.
    {"type": "matn",
     "ar": "قيل: لا نسلم إن في هذه الأمثلة تعريف المعرف، بل فيها زوال التعريف[[٤]] -وهو التعريف الحاصل باللام أو الإضافة- وحصول تعريف آخر، وهو التعريف بالعلمية،",
     "en": "It is said [in reply]: we do not grant that in these examples there is a defining of what is already defined; rather, in them there is the removal of a definiteness, namely the definiteness produced by the article or by annexation, and the arising of another definiteness, namely definiteness by being a proper name (ʿalamiyya);"},
    {"type": "matn",
     "ar": "فإنها حين صارت أعلاما لم يبق فيها الإشارة إلى معلوميتها باللام أو الإضافة، فلا يلزم فيها تعريف المعرف، بل تبديل تعريف بتعريف آخر.",
     "en": "for when they became proper names, there no longer remained in them any indication of their being known through the article or annexation; so no defining of the defined follows in them, but rather the replacement of one definiteness by another."},
    {"type": "matn",
     "ar": "(وما أجازه الكوفيون من) تركيب («الثلاثة الأثواب» وشبهه من العدد) المعرف باللام المضاف إلى معدوده، نحو: «الخمسة الدراهم، والمائة الدينار» (ضعيف) قياسا واستعمالا.",
     "en": "(What the Kūfans permitted), namely the construction (“al-thalāthat al-athwāb” [the three garments] and similar numerals), the numeral bearing the article and annexed to what it counts, as in “al-khamsat al-darāhim” (the five dirhams) and “al-miʾat al-dīnār” (the hundred dinars), (is weak), by analogy (qiyās) and in usage."},
    {"type": "matn",
     "ar": "أما قياسا: فلما ذكر من لزوم تحصيل الحاصل.",
     "en": "By analogy, because of what was mentioned: that it entails producing what is already produced."},
    {"type": "matn",
     "ar": "وأما استعمالا: فلما ثبت من الفصحاء من ترك اللام، قال ذو الرمة:",
     "en": "In usage, because of the established practice of the eloquent of omitting the article. Dhū al-Rumma said:"},
    {"type": "verse",
     "ar": "وهل يرجع التسليم أو يكشف العمى          ثلاث الأثافي والديار البلاقع؟",
     "en": "Do the three hearthstones and the desolate abodes return a greeting, or dispel blindness?"},
    {"type": "matn",
     "ar": "وأما ما جاء في الحديث من قوله صلى الله تعالى عليه وسلم بـ«الألف الدينار»، فعلى البدل دون الإضافة.",
     "en": "As for what came in the ḥadīth, his words (may Allah the Exalted bless him and grant him peace) “al-alf al-dīnār” (the thousand, the dinars), it is by way of substitution (badal), not annexation."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهو مستنكر في بادئ النظر.",
     "en": "And that is objectionable at first sight."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن المقصود من الإضافة إلى المعرفة حصول أصل التعريف، وقد حصل للمعرفة،",
     "en": "He means that the purpose of annexation to a definite noun is the attainment of basic definiteness, and the definite noun already has it;"},
    {"type": "pair",
     "ar": "فلو أضيف إلى المعرفة لكان تحصيلا لما هو الحاصل فيها، يعني: أصل التعريف.",
     "en": "so if it were annexed to a definite noun, it would be producing what is already present in it, namely basic definiteness."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أن المعرفة في الأمثلة المذكورة هي الاسم لا المركب، والعلم هو المركب، فلم يكن المعرفة علما.",
     "en": "Against this: the definite noun in the examples mentioned is the noun alone, not the compound, while the proper name is the compound; so the definite noun has not become a proper name."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حاصله: أن العلمية لما كانت وضعا ثانيا أزالت مقتضى الوضع الأول بخلاف الإضافة،",
     "en": "Its upshot: since being a proper name is a second coinage, it removed what the first coinage required, unlike annexation;"},
    {"type": "pair",
     "ar": "فإنها لما لم تكن وضعا ثانيا لم تزل مقتضى الوضع الأول، فلو أضيفت المعرفة إلى المعرفة لأدت إلى اجتماع التعريفين في الإرادة.",
     "en": "for since annexation is not a second coinage, it does not remove what the first coinage required; so if a definite noun were annexed to a definite noun, it would lead to two kinds of definiteness combining in what is intended."},
]
