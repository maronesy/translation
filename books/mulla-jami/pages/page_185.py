# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 185 (printed ١٨٤)."""

PAGE_NUMBER = 185
PRINTED_PAGE = "١٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "على الجزء، فخرج به مثل: «تأديبا» في قولك: «ضربته تأديبا»[[١]]،",
     "en": "…upon the part. Thereby is excluded such as “taʾdīban” (for discipline) in your saying: “I struck him for discipline” (ḍarabtuhu taʾdīban);"},
    {"type": "matn",
     "ar": "فإنه وإن كان مما فعله فاعل فعل مذكور، لكنه ليس مما يشتمل عليه معنى الفعل،",
     "en": "for although it is among the things that the agent of a mentioned verb did, it is not among the things that the meaning of the verb contains;"},
    {"type": "matn",
     "ar": "وكذلك خرج به مثل: «كراهتي» في نحو: «كرهت كراهتي»، فإن للكراهة اعتبارين[[٢]]:",
     "en": "and likewise thereby is excluded such as “karāhatī” (my aversion) in an example like: “I disliked my aversion” (karihtu karāhatī); for aversion (karāha) has two considerations:"},
    {"type": "matn",
     "ar": "أحدهما: كونها بحيث قامت بفاعل الفعل المذكور، واشتق منها فعل أسند إليه.",
     "en": "the first of them: its being such that it subsists in the agent of the mentioned verb, and a verb has been derived from it that is predicated of him."},
    {"type": "matn",
     "ar": "ولا شك أن معنى الفعل مشتمل عليها حينئذ.",
     "en": "There is no doubt that the meaning of the verb contains it in that case."},
    {"type": "matn",
     "ar": "وثانيهما: كونها بحيث وقع عليها فعل الكراهة،",
     "en": "The second of them: its being such that the act of disliking falls upon it."},
    {"type": "matn",
     "ar": "فإذا ذكرت بعد الفعل بالاعتبار الأول كما في قولك: «كرهت كراهة» فهو مفعول مطلق.",
     "en": "So when it is mentioned after the verb under the first consideration, as in your saying: “I disliked [with] a dislike” (karihtu karāhatan), it is an absolute object (mafʿūl muṭlaq)."},
    {"type": "matn",
     "ar": "وإذا ذكرت بعده بالاعتبار الثاني كما في قولك: «كرهت كراهتي» فهو مفعول به لا مفعول مطلق؛",
     "en": "And when it is mentioned after it under the second consideration, as in your saying: “I disliked my aversion” (karihtu karāhatī), it is a direct object (mafʿūl bihi), not an absolute object;"},
    {"type": "matn",
     "ar": "إذ ليس ذلك الفعل مشتملا عليه بهذا الاعتبار، بل هو واقع عليه وقوع الفعل على المفعول به.",
     "en": "for that verb does not contain it under this consideration; rather, it falls upon it as the verb falls upon the direct object."},
    {"type": "matn",
     "ar": "فخرج بهذا الاعتبار عن الحد، وانطبق الحد على المحدود جامعا ومانعا[[٣]].",
     "en": "So by this consideration it is excluded from the definition, and the definition fits the thing defined, being comprehensive and exclusive (jāmiʿan wa-māniʿan)."},
    {"type": "matn",
     "ar": "(ويكون) أي: المفعول المطلق:",
     "en": "(And it is—wa-yakūnu), that is, the absolute object:"},
    {"type": "matn",
     "ar": "١-(للتأكيد[[٤]]) إن لم يكن في مفهومه زيادة على ما يفهم من الفعل[[٥]].",
     "en": "1. (for emphasis—li-l-taʾkīd), if there is in its sense no addition to what is understood from the verb;"},
    {"type": "matn",
     "ar": "٢-(والنوع) إن دل على بعض أنواعه[[٦]].",
     "en": "2. (and [for] kind—wa-l-nawʿ), if it indicates one of its kinds."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا إذا لم يقصد من التأديب الضرب. وأما إذا قصد ذلك فلا، كما هو مذهب الزجاج.",
     "en": "This is when striking is not intended by “discipline” (taʾdīb). But if that is intended, then not [so], as is the doctrine of al-Zajjāj."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى أن يقال: فإن ههنا كراهتين: إحداهما ما وجد من فعل، وعبر عنها بكراهتي.",
     "en": "It would be better to say: for here there are two aversions: one of them is what came into existence from an act, and it is expressed by “karāhatī” (my aversion)."},
    {"type": "pair",
     "ar": "والأخرى: ما وجد بعدها، وتعلقت بتلك الكراهة الأولى تعلق الفعل بالمفعول به، فعبر عنها بقولك: كرهت، فهما متغايران بحسب الوجود.",
     "en": "The other: what came into existence after it and attached to that first aversion as the verb attaches to the direct object; it is expressed by your saying “karihtu” (I disliked). So the two are distinct in respect of existence."},
    {"type": "pair",
     "ar": "ويجوز أن يراد بكراهتي معنى مصدر كرهت لا ما وقعت سابقة عليها،",
     "en": "It is also possible that by “karāhatī” the meaning of the maṣdar of “karihtu” is intended, not what occurred prior to it;"},
    {"type": "pair",
     "ar": "فحينئذ يكون مفعولا مطلقا، والفعل مشتمل على ما قصد منه مثل ما ذكر في \"كرهت\".",
     "en": "in that case it is an absolute object, and the verb contains what is intended by it, like what was mentioned regarding “karihtu.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حالان من الحد.",
     "en": "[Jāmiʿan and māniʿan are] two circumstantial qualifiers (ḥālān) of “the definition.”"},
    {"type": "pair",
     "ar": "ولا يرد جوامد تقام مقام المفعول المطلق مثل: تربا وجندلا؛ لأنهما ليسا مفعولا مطلقا، بل جاريتان مجراه.",
     "en": "No objection arises from non-derived nouns (jawāmid) put in place of the absolute object, such as “turban” (dust) and “jandalan” (stones), because the two are not absolute objects but are treated as such (jāriyatān majrāhu)."},
    {"type": "pair",
     "ar": "وبعض النحاة زاد في التعريف أو جار مجراه، فحينئذ تحتاج إلى أن تريد بالاسم المذكور ما يعم الجاري مجراه.",
     "en": "Some grammarians added to the definition “or what is treated as such”; in that case you need to intend by the mentioned noun (ism) what includes that which is treated as such."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: لتأكيد ما هو المسند حقيقة، نحو: «ضربت ضربا»، فإنه لتأكيد الضرب المدلول عليه بـ«ضربت» لا تأكيد الإسناد والزمان أيضا.",
     "en": "That is: for emphasizing what is in reality the predicated element (al-musnad), as in: “I struck a striking” (ḍarabtu ḍarban); for it emphasizes the striking indicated by “ḍarabtu,” not the predication (isnād) and the time as well."},
    {"type": "pair",
     "ar": "فلو قيل: إنه لتأكيد الفعل كان مسامحة.",
     "en": "So if it were said that it is for emphasizing the verb, that would be loose expression (musāmaḥa)."},
    {"type": "pair",
     "ar": "وفائدته: دفع توهم السهو أو دفع توهم التجوز.",
     "en": "Its benefit is removing the suspicion of inadvertence, or removing the suspicion of figurative usage (tajawwuz)."},
    {"type": "pair",
     "ar": "وعليه حمل قوله تعالى: ﴿وكلم الله موسى تكليما﴾، أي: كلمه بذاته لا بترجمان بأن أمره بالتكلم لموسى عليه السلام.",
     "en": "On this is interpreted His saying, the Exalted: “And Allah spoke to Moses with [direct] speech” (Qurʾān, Sūrat al-Nisāʾ 4:164), that is: He spoke to him Himself, not through an interpreter, [that is, not] by commanding one to speak to Moses, peace be upon him."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "المصدر المعرف بلام الجنس إن كان للتأكيد وجب تخصيص الزيادة بما يفيد النوع والعدد،",
     "en": "The maṣdar made definite by the generic lām, if it is for emphasis, requires that “addition” be restricted to what conveys kind and number;"},
    {"type": "pair",
     "ar": "وإن كان للنوع وجب أن يقال بدل قوله على بعض أنواعه: على الزيادة غير العدد.",
     "en": "and if it is for kind, then instead of his words “one of its kinds” it should be said: “an addition other than number.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يريد الدلالة على بعض أنواعه فقط، أو في ضمن الدلالة على جميع أنواعه، لئلا يخرج نحو: «ضربت جميع أنواع الضرب».",
     "en": "He means indicating one of its kinds only, or [doing so] within indicating all its kinds, so that an example such as “I struck all kinds of striking” is not excluded."},
]
