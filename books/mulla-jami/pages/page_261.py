# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 261 (printed ٢٦٠)."""

PAGE_NUMBER = 261
PRINTED_PAGE = "٢٦٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «محتملة للصدق والكذب؛» from the foot of PDF p. 260.
    {"type": "matn",
     "ar": "لأن الحال بمنزلة الخبر[[١]] عن ذي الحال، وإجراؤها عليه في قوة الحكم بها عليه،",
     "en": "…because the ḥāl is in the position of a predicate about the dhū al-ḥāl, and applying it to it has the force of predicating it of it;"},
    {"type": "matn",
     "ar": "والجمل الإنشائية لا تصلح أن يحكم بها على شيء،",
     "en": "and non-declarative (inshāʾī) clauses are not fit to be predicated of anything."},
    {"type": "matn",
     "ar": "ولما كانت الجملة مستقلة في الإفادة لا تقتضي ارتباطها بغيرها، والحال مرتبطة بغيرها، فإذا وقعت الجملة حالا لا بد لها من رابطة تربطها إلى صاحبها، وهي: «الضمير والواو»[[٢]].",
     "en": "Since a clause is self-sufficient in conveying information and does not call for connection to anything else, while the ḥāl is connected to something else, when a clause occurs as a ḥāl it must have a link (rābiṭa) binding it to its owner, namely “the pronoun and the wāw.”"},
    {"type": "matn",
     "ar": "والجملة الخبرية: إما اسمية أو فعلية.",
     "en": "The declarative clause is either nominal or verbal."},
    {"type": "matn",
     "ar": "والفعلية إما يكون فعلها مضارعا مثبتا، أو مضارعا منفيا، أو ماضيا مثبتا، أو ماضيا منفيا، فهذه خمس جمل.",
     "en": "In the verbal clause the verb is either an affirmative imperfect, a negated imperfect, an affirmative perfect, or a negated perfect; so these are five kinds of clause."},
    {"type": "matn",
     "ar": "(فالاسمية[[٣]]) أي: الجملة الاسمية الحالية متلبسة:",
     "en": "(The nominal), that is, the nominal circumstantial clause, is joined:"},
    {"type": "matn",
     "ar": "(بالواو والضمير معا)؛ لقوة الاسمية في الاستقلال، فناسب أن تكون الرابطة فيها في غاية القوة،",
     "en": "(with the wāw and the pronoun together), because of the strength of the nominal clause in self-sufficiency, so it is fitting that its link be as strong as possible,"},
    {"type": "matn",
     "ar": "نحو: «جئت وأنا راكب»، و«جئت وأنت راكب»، و«جاء زيد وهو راكب».",
     "en": "as in “I came while I was riding,” “I came while you were riding,” and “Zayd came while he was riding.”"},
    {"type": "matn",
     "ar": "(أو بالواو وحدها)؛ لأنها تدل على الربط في أول الأمر[[٤]]، فاكتفى بها",
     "en": "(Or with the wāw alone), because it signals the link at the very outset, so it suffices,"},
    {"type": "matn",
     "ar": "مثل قوله صلى الله تعالى عليه وسلم: «كنت نبيا وآدم بين الماء والطين»،",
     "en": "as in his words, may Allah the Exalted bless him and grant him peace: “I was a prophet while Adam was between water and clay.”"},
    {"type": "matn",
     "ar": "وهذا أي: الربط بالواو وحدها، أو بها مع الضمير إنما يكون في الحال المنتقلة.",
     "en": "This, that is, linking with the wāw alone or with it together with the pronoun, occurs only in the transient ḥāl (al-ḥāl al-muntaqila)."},
    {"type": "matn",
     "ar": "وأما في الحال المؤكدة فلا يجوز الواو، تقول: هو الحق لا شك فيه،",
     "en": "In the corroborative ḥāl (al-ḥāl al-muʾakkida) the wāw is not permitted; you say: “It is the truth, there is no doubt in it.”"},
    {"type": "matn",
     "ar": "وذلك لأن الواو لا تدخل بين المؤكد والمؤكد؛ لشدة الاتصال بينهما.",
     "en": "That is because the wāw does not come between the corroborated and the corroborating, owing to the close connection between them."},
    {"type": "matn",
     "ar": "(أو بالضمير وحده على ضعف)؛ لأن الضمير لا يجب أن يقع في الابتداء، فلا يدل على الربط في أول الأمر،",
     "en": "(Or with the pronoun alone, weakly), because the pronoun need not occur at the beginning, so it does not signal the link at the outset,"},
    {"type": "matn",
     "ar": "نحو: «كلمته فوه إلى في»، فلا بد من الواو على الصحيح.",
     "en": "as in “I spoke to him, his mouth to my mouth”; so the wāw is required, on the correct view."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولأن الحال تفيد تعلق الفعل بالفاعل أو المفعول بوقت وقوع مضمونها، ولا يقصد من الإنشاء وقوع مضمونه.",
     "en": "And because the ḥāl conveys that the action is connected with the fāʿil or the mafʿūl at the time its content occurs, whereas the occurrence of its content is not what is intended by a non-declarative utterance."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لما كانت الجملة الحالية فضلة احتاجت إلى زيادة ربط.",
     "en": "Since the circumstantial clause is an adjunct (faḍla), it needs additional linkage."},
    {"type": "pair",
     "ar": "ولهذا لا يكون الواو رابطة في الجملة الواقعة خبرا أو وصفا إلا إذا حصل لهما أدنى انفصال.",
     "en": "Hence the wāw is not a link in a clause occurring as a predicate or as an adjective unless some slight separation arises for them."},
    {"type": "pair",
     "ar": "وذلك بوقوعهما بعد «إلا» نحو: ما جئتك إلا وأنت بخيل، وما جاءني إلا وهو فقير.",
     "en": "That happens when they occur after “illā,” as in “I did not come to you but you were miserly” and “he did not come to me but he was poor.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وفي حكمها الجملة المصدرة بـ«ليس»؛ لأنها لمجرد النفي على الأصح، ولا تدل على الزمان، فهو كحرف نفي داخل على الاسمية.",
     "en": "Under the same rule is the clause beginning with “laysa,” because on the soundest view it is for bare negation and does not denote time; so it is like a negative particle prefixed to a nominal clause."},
    {"type": "pair",
     "ar": "وقد تخلو الاسمية من الرابطتين عند ظهور الملابسة نحو: خرجت زيد على الباب، وهو قليل.",
     "en": "The nominal clause is sometimes free of both links when the connection is evident, as in “I went out, Zayd at the door”; this is rare."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأنها في الأصل للجمع مع السابق، فهي داعية إلى النظر إلى السابق.",
     "en": "Because it is originally for joining with what precedes, so it prompts attention to what precedes."},
]
