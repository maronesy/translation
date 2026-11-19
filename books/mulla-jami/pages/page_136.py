# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 136 (printed ١٣٥)."""

PAGE_NUMBER = 136
PRINTED_PAGE = "١٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "أما في صورة انتفاء الإعراب والقرينة فيهما: فللتحرز عن الالتباس[[١]].",
     "en": "As for the case in which both inflection and indicator are absent in the two [nouns]: [the fronting of the agent is required] in order to guard against ambiguity."},
    {"type": "matn",
     "ar": "وأما في صورة كون الفاعل ضميرا متصلا: فلمنافاة الاتصال الانفصال[[٢]].",
     "en": "And as for the case in which the agent is an attached pronoun: it is because attachment is incompatible with separation."},
    {"type": "matn",
     "ar": "وأما في صورة وقوع المفعول بعد «إلا»، لكن بشرط توسطها بينهما في صورتي التقديم والتأخير، فلئلا ينقلب الحصر المطلوب،",
     "en": "And as for the case in which the object falls after “illā” — but on the condition of its (illā’s) coming between the two, in both cases of fronting and postposing — it is so that the intended restriction (ḥaṣr) not be inverted;"},
    {"type": "matn",
     "ar": "فإن المفهوم من قوله: «ما ضرب زيد إلا عمرا» انحصار ضاربية «زيد» في «عمرو» مع جواز أن يكون «عمرو» مضروبا لشخص آخر[[٣]]،",
     "en": "for what is understood from his saying mā ḍaraba Zaydun illā ʿAmran (“Zayd struck none but ʿAmr”) is the confinement of Zayd’s being-a-striker to ʿAmr, together with the admissibility that ʿAmr be one struck by another person;"},
    {"type": "matn",
     "ar": "والمفهوم من قوله: «ما ضرب عمرا إلا زيد» انحصار مضروبية «عمرو» في «زيد» مع جواز أن يكون «زيد» ضاربا لشخص آخر، فلو انقلب أحدهما[[٤]] بالآخر بينهما لانقلب الحصر المطلوب.",
     "en": "and what is understood from his saying mā ḍaraba ʿAmran illā Zaydun (“none struck ʿAmr but Zayd”) is the confinement of ʿAmr’s being-struck to Zayd, together with the admissibility that Zayd be one who strikes another person; so were one of the two [constructions] to be inverted into the other between them, the intended restriction would be inverted."},
    {"type": "matn",
     "ar": "وإنما قلنا: «بشرط توسطها[[٥]] بينهما في صورتي التقديم والتأخير»؛ لأنه لو قدم المفعول على الفاعل مع «إلا»[[٦]] فيقال: «ما ضرب إلا عمرا زيد»، فالظاهر أن معناه انحصار ضاربية «زيد» في «عمرو»؛ إذ الحصر إنما هو فيما يلي «إلا»، فلا ينقلب",
     "en": "We said only “on the condition of its coming between the two, in both cases of fronting and postposing,” because were the object placed before the agent together with “illā” — so that one says mā ḍaraba illā ʿAmran Zaydun — then apparently its meaning is the confinement of Zayd’s being-a-striker to ʿAmr, since the restriction pertains only to what follows “illā”; so [the meaning] is not inverted"},

    {"type": "rule"},

    # ---------------- Footnote 7 (continued from previous page) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "مقصوده تحرير المدعى ليستدل على كل منها بقوله: أما في صورة انتفاء الإعراب إلى آخره.",
     "en": "His aim is the precise formulation of the claim, so that each of these [cases] may be argued for by his words: “As for the case in which the inflection is absent …,” to the end [of the passage]."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "المخل بالمقصود مع رعاية النظم الطبيعي. لقائل أن يقول: التحرز عن الالتباس المخل يقتضي امتناع تقديم المفعول على الفعل في نحو: «موسى ضرب عيسى» لالتباسه بالاسمية التي تخل بالمقصود.",
     "en": "[The ambiguity] that impairs the intended sense while [otherwise] observing the natural order. Someone might say: guarding against the impairing ambiguity requires the impermissibility of placing the object before the verb, as in Mūsā ḍaraba ʿĪsā (“Mūsā struck ʿĪsā”), because of its being confused with a nominal sentence, which impairs the intended sense."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: لو قدم المفعول المذكور بعد الفعل على الفاعل المتصل به يلزم انفصال الفاعل.",
     "en": "Meaning: were the said object [which comes] after the verb placed before the agent attached to it, the detachment of the agent would follow."},
    {"type": "pair",
     "ar": "فإن قلت: إنما يلزم انفصال الفاعل لو كان المفعول منفصلا. وأما إذا كان المفعول أيضا متصلا فلا، أي: لا يلزم الانفصال، نحو: «ضربتك» كما لا يلزم الانفصال في «ضربتك»؟",
     "en": "If you say: the detachment of the agent follows only if the object were detached; but if the object too is attached, then it does not — that is: detachment is not entailed, as in ḍarabtuka (“I struck you”), just as detachment is not entailed in ḍarabtuka?"},
    {"type": "pair",
     "ar": "قلت: على هذا يلزم تقديم الأضعف على الأقوى فيما هو كالكلمة الواحدة، والفاعل المضمر المتصل بالفعل كالجزء للفعل لفظا ومعنى.",
     "en": "I say: on this [supposition] there would follow the placing of the weaker before the stronger within what is like a single word; for the latent agent-pronoun attached to the verb is like a part of the verb, both in wording and in meaning."},
    {"type": "pair",
     "ar": "فلو دخل المفعول بينه وبين الفعل يلزم وقوع كلمة بين أجزاء كلمة، وذا لا يجوز.",
     "en": "So were the object to enter between it and the verb, there would follow the occurrence of a word amid the parts of [another] word, and that is impermissible."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا ظاهر في المثال المذكور ونظائره مما كان الفاعل خاصا. أما إذا كان عاما فلا، كقولك: «ما ضرب أحد إلا زيدا»، وذلك لأنه لم يبق أحد حتى يصح أن يكون «زيد» مضروبا له.",
     "en": "This is evident in the said example and its likes, where the agent is particular. But if it is general, then not [so], as in your saying mā ḍaraba aḥadun illā Zaydan (“no one struck anyone but Zayd”); [and that is] because no one remains for it to be sound that Zayd be someone struck by him."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: أحد هذين التركيبين بالآخر بأن يقدم المفعول، ويؤخر الفاعل، ويقع إلا بينهما.",
     "en": "That is: [the inversion of] one of these two constructions into the other, by placing the object first, postposing the agent, and letting “illā” fall between them."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يجب عند أكثر النحاة تقديم الفاعل إذا كان المفعول بعد «إلا»، ولا يجوز تقديم المفعول لا مع «إلا» ولا بدونها، ويجوز تقديم المفعول مع «إلا» عند السكاكي وجماعة من النحويين.",
     "en": "According to most grammarians, it is obligatory to place the agent first when the object comes after “illā,” and it is impermissible to front the object, neither with “illā” nor without it; whereas fronting the object together with “illā” is permitted according to al-Sakkākī and a group of grammarians."},
    {"type": "pair",
     "ar": "فالظاهر في حل عبارة المتن أن يكون على مذهب أكثر النحويين. وكأنه دعا الشارح إلى حل عبارة المتن على مذهب السكاكي أن المصنف علل وجوب التقديم بانقلاب المعنى.",
     "en": "So the apparent [course] in resolving the wording of the base text is that it be according to the doctrine of most grammarians. It is as though what drove the Commentator to resolve the wording of the base text according to al-Sakkākī’s doctrine is that the author justified the obligation of fronting by the inversion of the meaning."},
    {"type": "pair",
     "ar": "ولك أن تتكلف في التعلل، فتقول: المراد أنه يلزم الانقلاب في بعض الصور، وحمل الباقي عليه طردا للباب.",
     "en": "You may [instead] take on the burden in the justification and say: what is meant is that inversion is entailed in some of the cases, the rest being assimilated to it for the sake of uniformity of the chapter’s rule."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كما ذهب إليه السكاكي وجماعة من النحويين. وأما عند أكثرهم فلا يجوز؛ لأنهم لم يجوزوا أن يعمل ما قبل «إلا» فيما بعد المستثنى بها إلا أن يكون تابعا له أو معمولا لغير عامله أو مستثنى منه،",
     "en": "As al-Sakkākī and a group of grammarians held. But according to most of them it is impermissible, because they did not permit that what precedes “illā” govern what comes after the term excepted by it, unless it be a follower (tābiʿ) of it, or governed by something other than its own governor, or the term from which the exception is made (mustathnā minhu);"},
    {"type": "pair",
     "ar": "فكأنه قدس سره حمل كلامه على ما هو المتفق عليه، أو مال إلى ما ذهب إليه الجماعة.",
     "en": "so it is as though he — may his secret be sanctified — construed his own words upon that which is agreed upon, or [else] inclined toward what that group held."},
]
