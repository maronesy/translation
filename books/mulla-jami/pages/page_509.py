# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 509 (printed ٥٠٨)."""

PAGE_NUMBER = 509
PRINTED_PAGE = "٥٠٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 508 ends with a complete sentence; this page opens a new one.
    {"type": "matn",
     "ar": "(وإن كان) أي: الفعل الذي أريد حذف فاعله، وإقامة المفعول مقامه (مضارعا ضم أوله) وهو حرف المضارعة نحو: «يضرب، ويكرم، ويلتزم، ويستخرج، ويتدحرج»",
     "en": "(And if it), that is, the verb whose agent is meant to be elided and its object put in its place, (is a muḍāriʿ, its first [letter] is given a ḍamma), namely the prefix of the muḍāriʿ, as in “yuḍrabu, wa-yukramu, wa-yultazamu, wa-yustakhraju, wa-yutadaḥraju”,"},
    {"type": "matn",
     "ar": "(وفتح ما قبل آخره) لخفة الفتحة وثقل المضارع بالزيادة",
     "en": "(and what precedes its last [letter] is given a fatḥa), because of the lightness of the fatḥa and the heaviness of the muḍāriʿ through the added letter."},
    {"type": "matn",
     "ar": "(ومعتل العين) المبني للمفعول (ينقلب) العين فيه (ألفا) ياء كانت أو واوا، نحو: «يقال، ويباع، ويختار، وينقاد، ويستجار، ويقام» لتحركها حقيقة أو حكما، وانفتاح ما قبلها.",
     "en": "(And in the verb with a weak ʿayn), constructed for the object, the ʿayn (is changed) in it (into an alif), whether it is a yāʾ or a wāw, as in “yuqālu, wa-yubāʿu, wa-yukhtāru, wa-yunqādu, wa-yustajāru, wa-yuqāmu”, because it is voweled, actually or virtually, and what precedes it has a fatḥa."},

    # REVIEW: the printed heading reads «المعتدي» (letters transposed), apparently a misprint for «المتعدي»; transcribed as printed.
    {"type": "section", "ar": "[المعتدي وغير المتعدي]",
     "en": "The Transitive and the Intransitive Verb"},

    {"type": "matn",
     "ar": "(المتعدي وغير المتعدي[[١]]).",
     "en": "(The transitive and the intransitive.)"},
    {"type": "matn",
     "ar": "(فالمتعدي) من الفعل[[٢]] (ما يتوقف فهمه على متعلق) أي: أمر غير الفاعل يتعلق الفعل به ويتوقف فهمه عليه،",
     "en": "(So the transitive) verb (is that whose understanding depends on something it is connected with (mutaʿallaq)), that is, a thing other than the agent with which the verb is connected and on which its understanding depends;"},
    {"type": "matn",
     "ar": "فإن كل فعل لا بد له من فاعل وفهمه موقوف على فهمه، لكن نسبة الفعل إلى الفاعل بطريق الصدور والقيام والإسناد،",
     "en": "for every verb must have an agent, and its understanding depends on the understanding of [the agent]; but the relation of the verb to the agent is by way of issuing, subsisting and attribution (isnād),"},
    {"type": "matn",
     "ar": "فيقال: هذا الفعل صادر عن الفاعل، وقائم به، ومسند إليه، ولا يقال في الاصطلاح: إنه متعلق به، فإن التعلق نسبة الفعل إلى غير الفاعل،",
     "en": "so one says: this verb issues from the agent, subsists in it and is attributed to it; and in technical usage it is not said to be “connected with” it, for connection (taʿalluq) is the relation of the verb to what is other than the agent."},
    {"type": "matn",
     "ar": "فالحاصل أن فهم الفعل إن كان موقوفا على فهم غير الفاعل فهو المتعدي (كـ«ضرب») فإن فهمه موقوف على تعقل المضروب؛ إذ لا يمكن تعقله إلا بعد تعقله،",
     "en": "The upshot is that if the understanding of the verb depends on the understanding of something other than the agent, it is the transitive, (like “ḍaraba” (he struck)); for its understanding depends on conceiving the one struck, since it cannot be conceived except after conceiving [the one struck];"},
    {"type": "matn",
     "ar": "بخلاف الزمان والمكان والغاية وهيئة الفاعل والمفعول[[٣]]، فإن فهم الفعل وتعقله بدون هذه الأمور ممكن.",
     "en": "unlike the time, the place, the purpose, and the state of the agent and the object; for understanding and conceiving the verb without these things is possible."},
    {"type": "matn",
     "ar": "(وغير المتعدي بخلافه) أي: بخلاف المتعدي، يعني: لا يتوقف فهمه على فهم أمر غير الفاعل (كـ«قعد») فإنه وإن كان له تعلق لكل واحد من الزمان والمكان والغاية",
     "en": "(And the intransitive is the opposite of it), that is, the opposite of the transitive; he means: its understanding does not depend on understanding a thing other than the agent, (like “qaʿada” (he sat)); for, even though it has a connection with each of the time, the place and the purpose…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذان قيدان لقسمي الفعل لا قسمان، فإن المتعدي أعم من الفعل وشبهه. وكذا غير المتعدي",
     "en": "These two are qualifications of the two divisions of the verb, not [themselves] two divisions, for the transitive is more general than the verb and what resembles it; and likewise the intransitive."},
    {"type": "pair",
     "ar": "إلا أن المتعدي مطلقا لا يمكن تعريفه بما يتوقف فهمه على متعلق، فإن المصدر لا يتوقف على شيء فضلا عن المفعول.",
     "en": "However, the transitive in the absolute sense cannot be defined as “that whose understanding depends on something it is connected with”, for the maṣdar does not depend on anything, let alone on the object."},
    {"type": "pair",
     "ar": "ولذا جاز حذف فاعله والسر في ذلك أن النسبة إلى الفاعل والتعلق بالمفعول به جزآن من معنى الفعل، وما سوى المصدر مما يشبهه",
     "en": "For this reason the elision of its agent is permitted. The secret of this is that the relation to the agent and the connection with the direct object (mafʿūl bihi) are two parts of the meaning of the verb, and of what resembles it other than the maṣdar."},
    {"type": "pair",
     "ar": "فنقول: المصدر المتعدي ما اشتق منه الفعل المتعدي، فالمتعدي المطلق ما يتوقف فهمه على متعلق، أو يتوقف فهم ما يشتق هو منه عليه،",
     "en": "So we say: the transitive maṣdar is that from which the transitive verb is derived; and the transitive in the absolute sense is that whose understanding depends on something it is connected with, or [that on which] depends the understanding of what is derived from it."},
    {"type": "pair",
     "ar": "وكأنه لذلك قال: المتعدي من الفعل.",
     "en": "It is as though it was for this reason that he said “the transitive verb”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "دون اسم الفاعل والمفعول والمصدر، فإنها غير متعدية بهذا المعنى لعدم توقف فهمها عليه.",
     "en": "Not the active participle, the passive participle and the maṣdar, for these are not transitive in this sense, since their understanding does not depend on it."},
    {"type": "pair",
     "ar": "ولذا جاز ترك مفعولها.",
     "en": "For this reason it is permitted to leave out their object."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يريد به معنى الحال.",
     "en": "By it he means the sense of the circumstantial (ḥāl)."},
]
