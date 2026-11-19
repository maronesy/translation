# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 30 (printed ٢٩)."""

PAGE_NUMBER = 30          # PDF page
PRINTED_PAGE = "٢٩"       # page number printed in the book

BLOCKS = [
    {"type": "section", "ar": "[الكلمة]",
     "en": "The Word (al-Kalima)"},

    # ---------------- The main text (matn) ----------------
    {"type": "matn",
     "ar": "وبدأ[[١]] بتعريف الكلمة والكلام؛ لأنه[[٢]] يبحث في هذا الكتاب[[٣]] عن أحوالهما[[٤]]،",
     "en": "He began with the definition of the word (kalima) and speech (kalām), because in this book he investigates their states (aḥwāl);"},
    {"type": "matn",
     "ar": "فمتى لم يعرف[[٥]]، كيف يبحث عن أحوالهما؟",
     "en": "for if [a thing] is not defined, how can their states be investigated?"},
    {"type": "matn",
     "ar": "وقدم[[٦]] الكلمة على الكلام لكون أفرادها[[٧]] جزءا من أفراد الكلام، ومفهومها جزءا من مفهومه[[٨]]،",
     "en": "And he gave the word (kalima) precedence over speech (kalām) because its individual instances (afrād) are a part of the individual instances of speech, and its concept (mafhūm) is a part of its [speech’s] concept."},
    {"type": "matn",
     "ar": "فقال: (الكلمة[[٩]])",
     "en": "So he said: “al-kalima” (the word)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عطف على «لم يصدر».",
     "en": "Coordinated (ʿaṭf) upon “he did not prefix (lam yuṣaddir).”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: المصنف.",
     "en": "That is: the author (al-muṣannif)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إشارة إلى أن موضوع علم النحو: الكلمة والكلام، فيبحث فيه تارة عن أحوال الكلمة، وتارة عن أحوال الكلام.",
     "en": "An indication that the subject matter of the science of grammar (naḥw) is the word and speech; so within it one investigates at times the states of the word, and at times the states of speech."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الكلمة والكلام.",
     "en": "That is: the word and speech."},
    {"type": "pair",
     "ar": "قوله: «لأنه يبحث في هذا الكتاب عن أحوالهما» أي: من أحوال منسوبة إليهما من حيث إنها منسوبة إليهما، سواء أثبتت لأنفسهما أو لأقسامهما أو لأقسامهما من حيث إنها أقسامهما.",
     "en": "His words “because he investigates in this book their states” mean: [states] attributed to the two, inasmuch as they are attributed to them, whether they are affirmed of the two themselves, or of their divisions, or of their divisions inasmuch as they are their divisions."},
    {"type": "pair",
     "ar": "وفيه إشارة إلى أنهما موضوعا النحو، ردا على من قال: موضوعه الكلمة أو الكلام؛ لعدم اختصاص البحث بواحد منهما، وجعل البحث عن أحدهما راجعا إلى الآخر تكلف.",
     "en": "And in it is an indication that the two are the subject matter of grammar (al-naḥw), in refutation of the one who said: its subject matter is [only] the word or [only] speech — because investigation is not confined to [only] one of the two, and to make the investigation of one of them revert to the other is a contrived interpretation (takalluf)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الفاء للتفريع. وقوله: «لم يعرف» إما بتشديد الراء من التعريف، أو بتخفيفها من المعرفة.",
     "en": "The fāʾ [in “fa-matā”] is for [drawing] a subordinate conclusion (tafrīʿ). His words “lam yuʿarraf” are either with doubling (shadda) of the rāʾ, from “definition” (taʿrīf), or with lightening of it, from “knowledge” (maʿrifa)."},
    {"type": "pair",
     "ar": "وعلى كلا التقديرين مبني هذا الكلام على أن معرفتها السابقة التي يستدعيها بيان الأحوال يتوقف على التعريف، إن تم تم، وإلا فلا.",
     "en": "On both estimations, this statement is built upon [the premise] that the prior knowledge [of them] which the exposition of the states requires depends upon the definition: if it is complete, [that knowledge] is complete; and if not, then not."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: قدم الكلمة على الكلام كما هو المناسب بالسابق، أعني قوله: «وبدأ بتعريف الكلمة والكلام»،",
     "en": "That is: he gave the word precedence over speech, as is suited to what precedes — I mean his words “and he began with the definition of the word and speech”;"},
    {"type": "pair",
     "ar": "أو قدم الكلمة باعتبار التعريف والتقسيم كما هو المناسب باللاحق؛ إذ يجعل قوله: «لكون أفرادها جزءا من أفراد الكلام» علة لتقديم تقسيم الكلمة على تقسيم الكلام.",
     "en": "or he gave the word precedence with respect to definition and division (taqsīm), as is suited to what follows; since he makes his words “because its individuals are a part of the individuals of speech” the cause for giving precedence to the division of the word over the division of speech."},
    {"type": "pair",
     "ar": "وقوله: «ومفهومها جزءا من مفهومه» علة لتقديم تعريفها على تعريف الكلام بطريق اللف والنشر المشوش.",
     "en": "And his words “and its concept is a part of its concept” [are] the cause for giving precedence to its definition over the definition of speech — by way of disordered/interwoven distribution (al-laff wa-l-nashr al-mushawwash)."},
    {"type": "pair",
     "ar": "فإن قلت: كون أفراد الكلمة جزءا من أفراد الكلام لا يكون باعثا لتقديم تقسيم الكلمة على تقسيم الكلام؛ إذ التقسيم يكون للمفهوم لا للأفراد؟",
     "en": "If you say: the individuals of the word being a part of the individuals of speech cannot be the motive for giving precedence to the division of the word over the division of speech, since division pertains to the concept, not to the individuals?"},
    {"type": "pair",
     "ar": "قلت: التقسيم وإن كان للمفهوم، لكن الأفراد ملحوظة ومنظورة فيه، والغرض منه تمييز بعض الأفراد من بعض آخر.",
     "en": "I say: even though division pertains to the concept, the individuals are regarded and taken into account within it, and its aim is to distinguish some individuals from others."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: أفراد الكلمة. قوله: «وقدم الكلمة على الكلام لكون أفرادها» هذه وجوه أربعة للتقديم:",
     "en": "That is: the individuals of the word. His words “and he gave the word precedence over speech because its individuals…” — these are four grounds for the precedence:"},
    {"type": "pair",
     "ar": "الأول: توقف تحقق مفهوم الكلام على مفهوم الكلمة. والثاني: توقف تحقق معرفة مفهوم الكلام على معرفة مفهوم الكلمة.",
     "en": "The first: that the realization of the concept of speech depends upon the concept of the word. The second: that the realization of the knowledge of the concept of speech depends upon the knowledge of the concept of the word."},
    {"type": "pair",
     "ar": "والثالث: توقف تحقق الكلام على فرد الكلمة. والرابع: توقف تحقق معرفة فرد الكلام على معرفة مفهوم فرد الكلمة، فتدبر.",
     "en": "The third: that the realization of speech depends upon the individual [instance] of the word. The fourth: that the realization of the knowledge of the individual of speech depends upon the knowledge of the concept of the individual of the word — so ponder (fa-tadabbar)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الكلام.",
     "en": "That is: speech."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الفاء للتعقيب، ومدخولها معطوف على «بدأ»، فالمعنى: لما أراد الابتداء بتعريف الكلمة والكلام، فقال: الكلمة كذا، والكلام كذا،",
     "en": "The fāʾ [in “fa-qāla”] is for immediate sequence (taʿqīb), and what it governs is coordinated upon “he began”; so the meaning is: when he intended to begin with the definition of the word and speech, he said: “the word is such,” and “speech is such”;"},
    {"type": "pair",
     "ar": "أو معطوف على «قدم»، فمعناه: لما أراد تقديم تعريف الكلمة، فقال: الكلمة لفظ كذا إلى آخره.",
     "en": "or it is coordinated upon “he gave precedence,” so its meaning is: when he intended to give precedence to the definition of the word, he said: “the word is an utterance (lafẓ) of such [a kind],” to the end [of the definition]."},
    {"type": "pair",
     "ar": "وإنما قدرنا الإرادة بالتعريف، أو تقديم التعريف؛ لأن الابتداء بتعريف في نظم الكلام، أو تقديم التعريف",
     "en": "We only estimated the intention as pertaining to the definition, or to the giving of precedence to the definition, because beginning with a definition in the ordering of the discourse, or giving precedence to the definition …"},
]
