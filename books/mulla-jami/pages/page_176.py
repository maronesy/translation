# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 176 (printed ١٧٥)."""

PAGE_NUMBER = 176
PRINTED_PAGE = "١٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "ضيعته»[[١]]، فهذا الخبر واجب حذفه[[٢]]؛ لأن الواو تدل على الخبر الذي هو مقرون، وأقيم المعطوف في موضعه[[٣]].",
     "en": "…his craft.” This predicate must be elided, because the wāw indicates the predicate, which is “joined,” and the conjoined element has been put in its place."},
    {"type": "matn",
     "ar": "ورابعا: كل مبتدأ يكون مقسما به[[٤]] وخبره القسم",
     "en": "Fourth: every subject that is something sworn by, whose predicate is the oath (qasam);"},
    {"type": "matn",
     "ar": "(و) ذلك مثل: («لعمرك لأفعلن كذا»[[٥]]) أي: «لعمرك وبقاؤك[[٦]] قسمي» أي: ما أقسم به،",
     "en": "(and) that is as in: (“By your life, I shall certainly do such-and-such”—la-ʿamruka la-afʿalanna kadhā), that is: “Your life and your continuance are my oath,” that is: what I swear by."},
    {"type": "matn",
     "ar": "فلا شك أن «لعمرك» يدل على القسم المحذوف، وجواب القسم قائم مقامه، فيجب حذفه.",
     "en": "There is no doubt that “la-ʿamruka” indicates the elided oath, and the response to the oath (jawāb al-qasam) stands in its place; so its elision is obligatory."},
    {"type": "matn",
     "ar": "و«العمر والعمر» بمعنى واحد، ولا يستعمل مع اللام[[٧]] إلا المفتوحة[[٨]]؛ لأن القسم موضع التخفيف، لكثرة استعماله.",
     "en": "“Al-ʿumr” and “al-ʿamr” have one meaning, and with the lām only the form with fatḥa is used, because the oath is a place for lightening [the word], owing to how frequently it is used."},

    {"type": "rule"},

    # ---------------- Footnote 8 (continued from previous page) ----------------
    # Unnumbered continuation of footnote ٨ of PDF p.175; it has no marker on this
    # page, so the note count (9) exceeds the marker count (8) by one.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "إلى رجل؛ لأنه ليس مقصودا؟",
     "en": "…to “rajul,” because it is not what is intended?"},
    {"type": "pair",
     "ar": "قلنا: المقصود واضح، فإن المعنى أن كل رجل مع ضيعة ذلك الرجل.",
     "en": "We say: the intent is clear, for the meaning is that every man is with the craft of that man."},
    {"type": "pair",
     "ar": "قيل في توجيهه: التقدير: كل رجل مقرون هو وضيعته على أن يكون ضيعته معطوفة على ضمير الخبر، فيجوز سدها مسد الخبر.",
     "en": "It has been said in explaining it: the implied form is “Every man is joined, he and his craft,” with “his craft” conjoined to the pronoun of the predicate; so it may fill the place of the predicate."},
    {"type": "pair",
     "ar": "وفيه أنه يلزم ثلاثة أمور: حذف المؤكد، وجواز الرفع، والنصب في ضيعته، كما في «جئت أنا وزيدا»،",
     "en": "Against this: it entails three things: eliding the corroborated element (al-muʾakkad); permitting the nominative and the accusative in “his craft,” as in “I came, I and Zayd (wa-Zaydan)”;"},
    {"type": "pair",
     "ar": "وعدم الاندراج في القاعدة المذكورة؛ لأن ضيعته ليست معطوفة على المبتدأ.",
     "en": "and its not falling under the stated rule, because “his craft” is not conjoined to the subject."},
    {"type": "pair",
     "ar": "ويمكن أن يجاب: أما عن الأول: فبأن حذف المؤكد مع المؤكد جائز.",
     "en": "It can be answered: as to the first, that eliding the corroborated element together with the corroborative is permissible."},
    {"type": "pair",
     "ar": "وأما عن الثاني: فبأن المفعول معه لا بد له من فعل غير المدلول عليه بالواو.",
     "en": "As to the second: the concomitant object (al-mafʿūl maʿahu) requires a verb other than that indicated by the wāw."},
    {"type": "pair",
     "ar": "وأما عن الثالث: فبأن المراد العطف على المبتدأ نظرا إلى الصورة.",
     "en": "As to the third: what is meant is conjunction to the subject in view of the outward form."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كما تقول: زيد قائم وعمرو.",
     "en": "As you say: “Zayd is standing, and ʿAmr.”"},
    {"type": "pair",
     "ar": "وإنما لم يقل: كل رجل وضيعته مقرونان كما هو الظاهر؛ لأن الخبر إذا كان مثنى، فمحله بعد المعطوف، وليس بعد المعطوف لفظ يسد مسد الخبر.",
     "en": "He did not say “Every man and his craft are joined (maqrūnān),” as would be the apparent [form], only because, when the predicate is dual, its place is after the conjoined element, and after the conjoined element there is no word to fill the place of the predicate."},
    {"type": "pair",
     "ar": "ولا يجوز أن يجعل المعطوف سادا مسد الخبر؛ لأنه من تتمة المبتدأ.",
     "en": "Nor may the conjoined element be taken as filling the place of the predicate, because it belongs to the completion of the subject."},
    {"type": "pair",
     "ar": "قيل: لهذا الخبر حيثيتان: حيثية كونه خبرا عن زيد، وحيثية كونه خبرا عن ضيعته،",
     "en": "It has been said: this predicate has two aspects: the aspect of its being a predicate of Zayd, and the aspect of its being a predicate of his craft;"},
    {"type": "pair",
     "ar": "فهو من حيث إنه خبر عن «زيد» جاز أن يقال: وضيعته ساد مسد الخبر، ويكفي في النيابة حيثية واحدة.",
     "en": "so insofar as it is a predicate of “Zayd,” it may be said that “and his craft” fills the place of the predicate; one aspect suffices for the substitution."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وجعل الشيخ الرضي حذف الخبر ههنا غالبا لا واجبا.",
     "en": "Shaykh al-Raḍī held the elision of the predicate here to be predominant, not obligatory."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن المعطوف على المبتدأ وإن كان من تتمته، لكنه يذكر بعد الخبر، فيصح أن ينوب عن الخبر، ويشغل مكانه.",
     "en": "Because what is conjoined to the subject, though it belongs to its completion, is mentioned after the predicate; so it may validly stand in for the predicate and occupy its place."},
    {"type": "pair",
     "ar": "ومن أشكل عليه هذا قال: هو معطوف على ضمير، وهو فاعل الخبر أي: كل رجل مقرون هو وضيعته، فحذف المؤكد مع المؤكد وهو جائز.",
     "en": "Whoever found this problematic said: it is conjoined to a pronoun, which is the agent of the predicate, that is: “Every man is joined, he and his craft”; so it is an elision of the corroborated element together with the corroborative, which is permissible."},
    {"type": "pair",
     "ar": "ومعنى كلامهم: كل مبتدأ عطف عليه بالواو وبمعنى «مع» أنه عطف عليه صورة لا حقيقة.",
     "en": "The meaning of their statement “every subject to which something is conjoined by the wāw meaning ‘with’” is that it is conjoined to it in form, not in reality."},
    {"type": "pair",
     "ar": "ولا يخفى أنه يستغنى عنه لما ذكرنا.",
     "en": "It is not hidden that this is unnecessary, given what we have mentioned."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ومتعينا للقسم، فإن تعينه له يدل على تعين الخبر،",
     "en": "And determinately [used] for the oath; for its being determined for it indicates the determination of the predicate."},
    {"type": "pair",
     "ar": "فنحو: «أمانة الله لأفعلن كذا» لا يجب حذف خبره.",
     "en": "So in such as “The trust of Allah—I shall certainly do such-and-such,” the elision of its predicate is not obligatory."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قد يستعمل «لعمرك» في قسم السؤال نحو: لعمرك لأفعلن.",
     "en": "“La-ʿamruka” is sometimes used in the oath of request (qasam al-suʾāl), as in: “By your life, I shall certainly do [it].”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أشار بهذا العطف التفسير إلى أن العمر بالضم الحياة والبقاء.",
     "en": "By this explicative conjunction (ʿaṭf al-tafsīr) he indicated that ʿumr, with ḍamma, means life and continuance."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "في القاموس: العمر بالضم والفتح البقاء، وبالفتح الدين. قيل: ومنه لعمري.",
     "en": "In al-Qāmūs: ʿumr and ʿamr, with ḍamma and fatḥa, mean continuance, and with fatḥa [also] religion (dīn). It has been said: from this is “la-ʿamrī.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: يستعمل مع اللام الموطئة للقسم في مقام وقع مقسما به إلا المفتوحة.",
     "en": "That is: with the lām that prepares for the oath (al-lām al-muwaṭṭiʾa li-l-qasam), in a context where it occurs as what is sworn by, only the form with fatḥa is used."},
]
