# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 151 (printed ١٥٠)."""

PAGE_NUMBER = 151
PRINTED_PAGE = "١٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "في توقف تعقل الفعل عليهما، فإن الضرب مثلا كما أنه لا يمكن تعقله بلا ضارب كذلك لا يمكن تعقله بلا مضروب،",
     "en": "…in that the conception of the verb depends on both of them; for striking, for example, just as it cannot be conceived without a striker, so it cannot be conceived without one struck;"},
    {"type": "matn",
     "ar": "بخلاف سائر المفاعيل، فإنها ليست بهذه الصفة.",
     "en": "unlike the other objects, for they are not of this character."},
    {"type": "matn",
     "ar": "(تقول: ضرب زيد) بإقامة المفعول به مقام الفاعل (يوم الجمعة) ظرف زمان (أمام الأمير) ظرف مكان (ضربا شديدا) مفعول مطلق للنوع باعتبار الصفة.",
     "en": "(You say: Zayd was struck—taqūlu: ḍuriba Zaydun), by setting the direct object in the place of the agent, (on Friday—yawma al-jumuʿati), an adverb of time, (in front of the emir—amāma al-amīri), an adverb of place, (a severe striking—ḍarban shadīdan), an absolute object (mafʿūl muṭlaq) of kind, by virtue of the adjective."},
    {"type": "matn",
     "ar": "وفائدة وصف الضرب[[١]] بالشدة التنبيه على أن المصدر لا يقوم مقام الفاعل بلا قيد مخصص؛ إذ لا فائدة فيه[[٢]] لدلالة الفعل عليه.",
     "en": "The benefit of qualifying the striking as severe is to draw attention to the fact that the verbal noun does not stand in the place of the agent without a specifying qualification; for there is no benefit in it, since the verb [already] indicates it."},
    {"type": "matn",
     "ar": "(في داره) جار ومجرور شبيه بالمفاعيل[[٣]] أقيم مقام الفاعل مثلها (فتعين «زيد»)،",
     "en": "(In his house—fī dārihi), a preposition and its genitive object, resembling the objects, which is set in the place of the agent like them; (so “Zayd” is singled out—fa-taʿayyana Zaydun);"},
    {"type": "matn",
     "ar": "(وإن لم يكن) أي: وإن لم يوجد في الكلام المفعول به (فالجميع) أي: جميع ما سوى المفعول به[[٤]] (سواء[[٥]]) في جواز وقوعها موقع الفاعل.",
     "en": "(And if there is none—wa-in lam yakun), that is: if there is no direct object in the utterance, (then all—fa-l-jamīʿ), that is: all that is other than the direct object, (are equal—sawāʾun) in the permissibility of their occurring in the position of the agent."},
    {"type": "matn",
     "ar": "(و) المفعول (الأول من باب «أعطيت») أي: الفعل المتعدي إلى المفعولين ثانيهما غير الأول (أولى) بأن يقوم مقام الفاعل (من) المفعول (الثاني)؛",
     "en": "(And the first—wa-l-awwal) object (of the category of “aʿṭaytu”—min bābi aʿṭaytu), that is: of the verb that is transitive to two objects, the second of which is other than the first, (is more entitled—awlā) to stand in the place of the agent (than—mina) the (second—al-thānī) object;"},
    {"type": "matn",
     "ar": "لأن فيه معنى الفاعلية[[٦]] بالنسبة إلى الثاني؛ لأنه عاط، أي: آخذ، نحو: «أعطي زيد درهما» مع جواز",
     "en": "because there is in it the sense of agency (fāʿiliyya) relative to the second, since it is a taker (ʿāṭin), that is: a receiver (ākhidh), as in: “Zayd was given a dirham” (uʿṭiya Zaydun dirhaman), while it is permissible…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وكذا فائدة الزمان المعين في التمثيل حيث قال: «يوم الجمعة» ولم يقل: «زمانا»،",
     "en": "Likewise the benefit of the specified time in the example, where he said “on Friday” and did not say “at a time”;"},
    {"type": "pair",
     "ar": "وفائدة المكان المعين حيث قال: «أمام الأمير»، ولم يقل: «مكانا»؛",
     "en": "and the benefit of the specified place, where he said “in front of the emir” and did not say “in a place”:"},
    {"type": "pair",
     "ar": "للتنبيه على أن الزمان المطلق والمكان المطلق لا يصلحان للقيام مقام الفاعل لعدم الفائدة لدلالة الفعل عليهما على ما قيل.",
     "en": "it is to draw attention to the fact that unqualified time and unqualified place are not fit to stand in the place of the agent, for lack of benefit, since the verb indicates them, according to what has been said."},
    {"type": "pair",
     "ar": "وعلى هذا ينبغي ألا يجوز قيام مفعول به مبهم غاية الإبهام مقام الفاعل بأن يقال: «ضرب شخص»،",
     "en": "On this basis, it ought not to be permissible for a direct object that is vague in the extreme to stand in the place of the agent, by saying: “A person was struck” (ḍuriba shakhṣun);"},
    {"type": "pair",
     "ar": "وكذا المفعول بواسطة إذا كان في غاية العموم، نحو: «ضرب في مكان».",
     "en": "and likewise the object [reached] through an intermediary (bi-wāsiṭa) when it is general in the extreme, as in: “There was striking in a place” (ḍuriba fī makānin)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والفاعل محل الفائدة، فيجب أن يكون ما يقوم مقامه محلا لها.",
     "en": "The agent is the locus of the information conveyed (fāʾida), so what stands in its place must be a locus for it."},
    {"type": "pair",
     "ar": "ولهذا لا يقع الزمان والمكان المبهمان مقام الفاعل لدلالة الفعل عليهما.",
     "en": "For this reason vague time and vague place do not occur in the place of the agent, since the verb indicates them."},
    {"type": "pair",
     "ar": "فعلى هذا وجب تقييد قوله: «فالجميع سواء» بما سيذكره.",
     "en": "On this basis his words “then all are equal” must be restricted by what he will mention."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بلا واسطة.",
     "en": "[That is, the objects reached] without an intermediary."},
    {"type": "pair",
     "ar": "وإنما قيدنا بذلك؛ لأن الظرف وإن كان معه «في» مفعول فيه عند المصنف، فلا يظهر حينئذ القول بالتشبيه.",
     "en": "We restricted [it] in this way only because the adverb, even when “fī” is with it, is an adverbial object (mafʿūl fīhi) according to the author; so the statement of resemblance would not then be evident."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وهو الزمان المعين، والمكان المعين، والمصدر المقيد، والمفعول بالواسطة.",
     "en": "That is: specified time, specified place, the qualified verbal noun, and the object [reached] through an intermediary."},
    {"type": "pair",
     "ar": "إن قلت: ينبغي أن يكون المفعول بالواسطة متعينا لأن يقع مقام الفاعل؛ لأنه مفعول به؟",
     "en": "If you say: the object [reached] through an intermediary ought to be singled out for occurring in the place of the agent, since it is a direct object?"},
    {"type": "pair",
     "ar": "قلنا: صورة الجر لما كانت منافية لحالة الفاعل، أعني: الرفع، منعت أن يكون في درجة المفعول بلا واسطة.",
     "en": "We say: since the form of the genitive (jarr) is incompatible with the state of the agent, I mean the nominative (rafʿ), it prevents it from being on the level of the object without an intermediary."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: لو قال: «والبواقي سواء» لكان أخصر وأظهر، يعني: أن البواقي سواء في جواز وقوعها موقع الفاعل، وامتناع وقوعها موقعه.",
     "en": "It has been said: had he said “and the remaining ones are equal,” it would have been more concise and clearer—meaning that the remaining ones are equal in the permissibility of their occurring in the position of the agent and in the impossibility of their occurring in its position."},
    # REVIEW: printed «عل تقدير» (sic) for «على تقدير»; transcribed as printed.
    {"type": "pair",
     "ar": "وفيه أن حال البواقي قد علمت عل تقدير وجود المفعول به، وإنما المجهول حالها على تقدير عدمه،",
     "en": "In this [there is a difficulty]: the state of the remaining ones has [already] been learned on the supposition that a direct object is present; what is unknown is only their state on the supposition of its absence;"},
    {"type": "pair",
     "ar": "فالتعرض لحالها على تقدير وجوده مستدرك،",
     "en": "so addressing their state on the supposition of its presence is superfluous;"},
    {"type": "pair",
     "ar": "مع أنه أراد التصريح برد من قال: إن البواقي على تقدير عدمه ليست سواء،",
     "en": "besides which he wished to state explicitly the rejection of whoever said that the remaining ones, on the supposition of its absence, are not equal;"},
    {"type": "pair",
     "ar": "كما أراد التصريح برد من قال: إن المفعول به إذا وجد مع المفاعيل لم يتعين، فقال: «وإذا وجد» إلى آخره.",
     "en": "just as he wished to state explicitly the rejection of whoever said that the direct object, when it is present with [other] objects, is not singled out; so he said: “And when [the direct object] is present…” to the end."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قيل: ينبغي أن يكون المفعول الأول من باب «أعلمت» أولى من الثاني؛ لأنه العالم، والثاني هو المعلوم.",
     "en": "It has been said: the first object of the category of “aʿlamtu” ought to be more entitled than the second, because it is the knower, while the second is the known."},
]
