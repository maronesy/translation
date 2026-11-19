# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 569 (printed ٥٦٨)."""

PAGE_NUMBER = 569
PRINTED_PAGE = "٥٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وأنشد السيرافي في ذلك:» at the foot of PDF p. 568.
    {"type": "verse",
     "ar": "وداع دعا يا من يجيب إلى الندى          فلم يستجبه عند ذاك مجيب",
     "en": "…“And many a caller has called: ‘O who will answer the call to generosity?’, and no answerer responded to him then.”"},
    {"type": "verse",
     "ar": "فقلت أدع أخرى وارفع الصوت دعوة          لعل أبي المغوار منك قريب",
     "en": "“So I said: ‘Call once more and raise your voice in a call; perhaps Abū l-Mighwār (laʿalla Abī l-Mighwāri) is near you.’”"},
    {"type": "matn",
     "ar": "وأجيب عنه: بأنه يحتمل أن يكون على سبيل الحكاية، كذا قال المصنف في شرحه،",
     "en": "This has been answered by saying that it may be by way of quotation (ḥikāya); so the author said in his commentary."},
    {"type": "matn",
     "ar": "يعني: أنه وقع مجرورا في موضع آخر، فالشاعر حكاه على ما كان عليه، أو كان اشتهر ذلك الرجل بأبي المغوار بالياء.",
     "en": "He means that it occurred in the genitive in another place and the poet quoted it as it was; or that man had become known as “Abī l-Mighwār”, with the yāʾ."},
    {"type": "matn",
     "ar": "فيجب أن يحكى في الأحوال الثلاث بالياء.",
     "en": "So it must be quoted with the yāʾ in all three cases."},
    {"type": "matn",
     "ar": "ولعل مراد المصنف بما ذكر من التأويل: أن هذا البيت يحتمل ألا يكون من قبيل هذه اللغة الشاذة،",
     "en": "Perhaps what the author means by the interpretation he gave is that this verse may not belong to this anomalous dialect;"},
    {"type": "matn",
     "ar": "وإلا فلا حاجة إلى التأويل بعد ما جزم فيه بوجود الجر بهما[[١]]، وحكم بشذوذه.",
     "en": "otherwise there would be no need for interpretation after he had affirmed that the genitive with these two [i.e., laʿalla] occurs and had judged it anomalous."},

    {"type": "section", "ar": "[الحروف العاطفة]",
     "en": "The Coordinating Particles"},

    {"type": "matn",
     "ar": "(الحروف العاطفة) العطف في اللغة: الإمالة.",
     "en": "(The coordinating particles (al-ḥurūf al-ʿāṭifa)). Lexically, ʿaṭf means inclining [something towards something]."},
    {"type": "matn",
     "ar": "ولما كانت هذه الحروف تميل المعطوف إلى المعطوف عليه سميت عاطفة.",
     "en": "Since these particles incline the coordinated term (al-maʿṭūf) towards that upon which it is coordinated (al-maʿṭūf ʿalayhi), they are called coordinating."},
    {"type": "matn",
     "ar": "(وهي: «الواو، والفاء، وثم، وحتى، وأو، وإما») بكسر الهمزة (و«أم، ولا، وبل، ولكن»).",
     "en": "(They are “wa, fa, thumma, ḥattā, aw, immā”), with kasra on the hamza, (and “am, lā, bal and lākin”)."},
    {"type": "matn",
     "ar": "وعد بعضهم «أي» المفسرة منها.",
     "en": "Some have counted the explicative “ay” among them."},
    {"type": "matn",
     "ar": "وعند الأكثرين: أن ما بعدها عطف بيان لما قبلها،",
     "en": "According to the majority, what follows it is an explicative apposition (ʿaṭf bayān) to what precedes it;"},
    {"type": "matn",
     "ar": "كما ذهب بعض آخر إلى أن «بل»[[٢]] التي بعدها مفرد، نحو: «جاءني زيد بل عمرو وما جاءني زيد بل عمرو» ليست منها؛ لأن ما بعدها بدل غلط مما قبلها.",
     "en": "just as some others held that the “bal” followed by a single word, as in “Zayd came to me — no, ʿAmr” and “Zayd did not come to me — rather ʿAmr”, is not among them, because what follows it is a substitute of error (badal ghalaṭ) for what precedes it."},
    {"type": "matn",
     "ar": "وبدل الغلط بدونها غير فصيح. وأما معها، ففصيح مطرد في كلامهم؛ لأنها موضوعة لتدارك مثل هذا الغلط.",
     "en": "The substitute of error without it is not eloquent; with it, however, it is eloquent and regular in their speech, because it is coined for correcting such an error."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الجزم بوجود الجر لبعد هذا التأويل، والحاجة إلى التأويل لئلا يقال: بجر «لعل» للإشكال فيه مع أنه لا سند له إلا هذا البيت الواقع من عقيلي.",
     "en": "The affirmation that the genitive occurs is because this interpretation is far-fetched; and the need for interpretation is so that it not be asserted that “laʿalla” governs the genitive, given the difficulty in that and given that it has no support except this verse, which comes from a man of ʿUqayl."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «أما أنهم بعض آخر» is printed so (the sense seems to be «أما أنه بعض آخر»); transcribed as printed.
    {"type": "pair",
     "ar": "قال العصام: ما هو المثبت في الكتب أن بعض النحاة ذهب إليه أما أنهم بعض آخر فلم نعثر عليه.",
     "en": "ʿIṣām [al-Dīn] said: what is recorded in the books is that some grammarians held this; as for their being “some others”, we have not come across it."},
]
